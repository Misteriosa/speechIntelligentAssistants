import pyaudio
from six.moves import queue #six is a package that helps in writing code that is compatible with both Python 2 and Python 3. 


class MicrophoneStream(object):
    """Opens a recording stream as a generator yielding the audio chunks."""
    def __init__(self, rate, chunk, device = 0):
        self._rate = rate
        self._chunk = chunk

        # Create a thread-safe buffer of audio data
        self._buff = queue.Queue()
        self.closed = True
        self.device = device

    def __enter__(self):   #__enter__ method is called at the start of 'with' block and __exit__ method is called at the end.
        self._audio_interface = pyaudio.PyAudio()
        
        self._audio_stream = self._audio_interface.open(
            format=pyaudio.paInt16,
            # The API currently only supports 1-channel (mono) audio
            # https://goo.gl/z757pE
            channels=1, rate=self._rate,
            input_device_index=self.device,
            input=True, frames_per_buffer=self._chunk,
            # Run the audio stream asynchronously to fill the buffer object.
            # This is necessary so that the input device's buffer doesn't
            # overflow while the calling thread makes network requests, etc.
            stream_callback=self._fill_buffer, 
            #stream_callback-Specifies a callback function for non-blocking (callback) operation. 
            #Default is None, which indicates blocking operation (i.e., Stream.read() and Stream.write()). 
        )
        self.closed = False
        return self
        
    def _fill_buffer(self, in_data, frame_count, time_info, status_flags):
        """Continuously collect data from the audio stream, into the buffer."""
        self._buff.put(in_data)
        #print ('antes pa.cnntinue')
        return None, pyaudio.paContinue #paContinue signals there is more audio data to come

    def __exit__(self, type, value, traceback):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        self._buff.put(None)
        self._audio_interface.terminate()

    def stop(self):
        self._audio_stream.stop_stream()
        self._audio_stream.close()
        self.closed = True
        # Signal the generator to terminate so that the client's
        # streaming_recognize method will not block the process termination.
        #self._buff.put(None)
        #self._audio_interface.terminate()

    def generator(self):
        while not self.closed:
            # Use a blocking get() to ensure there's at least one chunk of
            # data, and stop iteration if the chunk is None, indicating the
            # end of the audio stream.
            chunk = self._buff.get()
            if chunk is None:
                return
            data = [chunk]

            # Now consume whatever other data's still buffered.
            while True:
                try:
                    chunk = self._buff.get(block=False)
                    if chunk is None:
                        return
                    data.append(chunk)
                except queue.Empty:
                    break

            yield b''.join(data) #built-in method join of bytes object, maybe just  (Python 3.0)
                                 #example: my_list = ["Hello", "world"]  print("-".join(my_list))     Produce: "Hello-world"
            
            

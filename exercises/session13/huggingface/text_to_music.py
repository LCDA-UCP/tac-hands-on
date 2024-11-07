from transformers import pipeline
import scipy

synthesiser = pipeline("text-to-audio", "facebook/musicgen-small", device='cuda')

music = synthesiser("reggaeton beat with a summer vibe", forward_params={"do_sample": True})

scipy.io.wavfile.write("reggae_out.wav", rate=music["sampling_rate"], data=music["audio"])

# FastSpeech 2: English and Telugu TTS

## Implementation
Base implementation: ming024/FastSpeech2.
Training environment: Indiana University Big Red 200 HPC.

## English
The English model was trained for 5,000 steps.
A checkpoint was saved at step 5,000.

Final logged training losses:
- Total: 4.4300
- Mel: 1.1586
- Mel PostNet: 1.1664
- Pitch: 0.8302
- Energy: 1.0353
- Duration: 0.2395

Five test utterances were synthesized.
Audio samples and visualizations are in Results/English.
Six training loss plots are also included.

## Telugu
The Telugu audio and transcript dataset was prepared.
Configuration files were updated for Telugu.
Forced alignment, preprocessing, training, and inference
remain incomplete.

## Limitations
Audio quality has not yet been independently evaluated.
The Telugu model and its required evaluation outputs are pending.

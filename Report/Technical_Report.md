# FastSpeech 2: English and Telugu Text-to-Speech Implementation

## 1. Objective
Implement and evaluate FastSpeech 2 for English and Telugu text-to-speech synthesis, including acoustic preprocessing, model training, speech generation, and variance-adaptor analysis.

## 2. Implementation
- Base implementation: ming024/FastSpeech2.
- Computing environment: Indiana University Big Red 200 HPC.
- Language-specific preprocessing, model, and training configuration files were maintained separately.
- FastSpeech 2 models duration, pitch, and energy in addition to mel-spectrogram generation.
- A HiFi-GAN vocoder was used for speech synthesis.

## 3. English Experiments
The English model was trained for 5,000 steps.

### Final Logged Training Losses
| Component | Loss |
|---|---:|
| Total | 4.4300 |
| Mel | 1.1586 |
| Mel PostNet | 1.1664 |
| Pitch | 0.8302 |
| Energy | 1.0353 |
| Duration | 0.2395 |

A checkpoint was saved at step 5,000.

Five English test utterances were synthesized, covering pronunciation, homographs, spacing, dates, and code-switching.

Generated WAV files and associated visualizations are available in `Results/English/`.

Six training-loss plots are also included:
- Total loss
- Mel loss
- Mel PostNet loss
- Pitch loss
- Energy loss
- Duration loss

## 4. Telugu Experiments
The Telugu dataset contains 1,449 audio recordings and corresponding transcripts.

Preprocessing produced:
- 1,449 mel-spectrogram feature files
- 1,449 pitch feature files
- 1,449 duration feature files

Separate Telugu preprocessing, model, and training configurations were prepared.

The Telugu training configuration specifies 5,000 optimization steps, batch size 2, validation every 500 steps, and checkpoint saving every 500 steps.

A previous checkpoint in the Telugu directory was identified as a copy of an English checkpoint and was renamed to avoid presenting it as a Telugu-trained model.

A new Telugu training job (Slurm ID 8859291) was submitted on November 6, 2026. At the time of this report update, the job was waiting for GPU resources. Telugu-trained model results and synthesis outputs are therefore not yet available for evaluation.

## 5. Evaluation and Observations
English training-loss plots, generated speech files, and synthesis visualizations are provided for inspection.

The existence of generated audio files does not establish perceptual speech quality. No independent listening evaluation or objective speech-quality benchmark has been completed.

Telugu evaluation is pending successful training and inference.

## 6. Limitations
- Telugu training and inference remain incomplete at the reporting cutoff.
- Telugu test utterances, generated WAVs, and variance-adaptor plots remain pending.
- English speech quality has not been independently evaluated.
- Training-loss values are not equivalent to speech intelligibility or naturalness scores.
- The full requested English/Telugu comparative evaluation is not yet available.

## 7. Reproducibility
The repository contains language-specific configuration files, training and inference scripts, and available English results.

Base implementation: https://github.com/ming024/FastSpeech2

Project repository: https://github.com/aashi1511/FastSpeech2-IIITH

Large datasets and model checkpoints may be excluded from GitHub due to their size.

## 8. Conclusion
The English FastSpeech 2 pipeline produced a trained checkpoint, five synthesized utterances, and training-loss visualizations. Telugu data preparation and acoustic feature extraction were completed, and a separate training job was submitted. Full bilingual evaluation requires successful Telugu training and synthesis.

## 9. Telugu Training Status at Submission

The Telugu dataset preprocessing and acoustic feature extraction were completed, including 1,449 mel-spectrogram, pitch, and duration feature files.

A separate Telugu FastSpeech 2 training job (Slurm Job ID: 8859291) was submitted on Indiana University's Big Red 200 HPC cluster.

At the time of report preparation, the job status was PENDING (PD), meaning the job was waiting for GPU resources and had not started execution.

The following Telugu deliverables remain incomplete:
- Completed Telugu model training and verified final checkpoint.
- Five Telugu synthesized speech samples.
- Telugu duration, pitch, and energy evaluation plots.
- Telugu training-loss analysis and comparative English/Telugu evaluation.

These results are not presented as completed experiments. The submitted report documents the work completed so far and the outstanding experiments.

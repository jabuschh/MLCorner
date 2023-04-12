# MLCorner

Collection of scripts and tricks to make Machine Learning for UHH2-based analyses a bit easier.

## Workflow

- input: hadded root files after baseline selection (with analysis tree)
- convert the input to numpy arrays using the script `MLCorner/InputsPreparation/UHH2toNumpy/steer.py`
- use this output as input for the DNN training

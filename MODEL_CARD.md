# Model / system card

## Intended use

Align fictional transcript and protein measurements using a regularized canonical-correlation projection. Educational local experiment; no production deployment is implied.

## Data

Synthetic arrays, manually written documents or replayed JSON. No real user records. Seeds and sample inputs are recorded in app.py and sample_input.json.

## Method

Center paired modalities, whiten each regularized covariance matrix, then perform SVD on cross-covariance. Project both modalities into a shared low-dimensional space.

## Evaluation protocol

Fit on training pairs and retrieve the matching protein profile for held-out transcript profiles. Compare top-one retrieval with chance; paired test samples never fit the transform.

## Known limits

The pairing and shared factors are synthetic. This is linear CCA, not a multi-omics foundation model; matching scores are not biological interaction evidence.

## Verification status

Local tests and default experiment are executed during packaging. Live model generation is not exercised in the build. A successful validation result is limited to the checks implemented in code.

## Further work

Evaluate real paired modalities with donor-held-out splits, missing modalities, nonlinear encoders and batch-aware baselines.

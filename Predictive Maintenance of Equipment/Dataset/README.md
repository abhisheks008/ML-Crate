**Source**: [Predictive Maintenance Dataset](https://www.kaggle.com/datasets/stephanmatzka/predictive-maintenance-dataset-ai4i-2020/data)

**Description**:
This synthetic dataset is modeled after an existing milling machine and consists of 10,000 data points stored as rows with 14 columns.

	**Features**:
    1. UID: unique identifier ranging from 1 to 10000
    2. product ID: consisting of a letter L, M, or H for low, medium and high as product quality variants, and a variant-specific serial number
    3. type: just the product type L, M or H from column 2
    4. air temperature [K]
    5. process temperature [K]
    6. rotational speed [rpm]
    7. torque [Nm]
    8. tool wear [min]: The quality variants H/M/L add 5/3/2 minutes of tool wear to the used tool in the process.

    **Target**: 'machine failure' label that indicates, whether the machine has failed in this particular datapoint.
	
	The machine failure consists of five independent failure modes
	1. tool wear failure (TWF)
    2. heat dissipation failure (HDF)
    3. power failure (PWF)
    4. overstrain failure (OSF)
    5. random failures (RNF)
    
    If at least one of the above failure modes is true, the process fails and the 'machine failure' label is set to 1.

**Citation**:
S. Matzka, "Explainable Artificial Intelligence for Predictive Maintenance Applications," 2020 Third International Conference on Artificial Intelligence for Industries (AI4I), 2020, pp. 69-74, doi: 10.1109/AI4I49448.2020.00023.
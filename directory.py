import pickle

data = [
    {
        "guest": "promazine",
        "host": "beta-cyclodextrin",
        "energy (kJ/mol)": -20.83,
        "uncertainty": 0.1,
    },
    {
        "guest": "promazine",
        "host": "heptakis-6-methyl-beta-cyclodextrin",
        "energy (kJ/mol)": -18.01,
        "uncertainty": 0.45,
    },
    {
        "guest": "promazine",
        "host": "heptakis-2,6-dimethyl-betacyclodextrin",
        "energy (kJ/mol)": -21.15,
        "uncertainty": 0.08,
    },
    {
        "guest": "promethazine",
        "host": "beta-cyclodextrin",
        "energy (kJ/mol)": -18.72,
        "uncertainty": 0.2,
    },
    {
        "guest": "promethazine",
        "host": "heptakis-6-methyl-beta-cyclodextrin",
        "energy (kJ/mol)": -24.72,
        "uncertainty": 3.84,
    },
    {
        "guest": "promethazine",
        "host": "heptakis-2,6-dimethyl-betacyclodextrin",
        "energy (kJ/mol)": -22.40,
        "uncertainty": 0.05,
    },
    {
        "guest": "chloropromazine",
        "host": "beta-cyclodextrin",
        "energy (kJ/mol)": -22.74,
        "uncertainty": 0.09,
    },
    {
        "guest": "chloropromazine",
        "host": "heptakis-6-methyl-beta-cyclodextrin",
        "energy (kJ/mol)": -12.62,
        "uncertainty": 0.95,
    },
    {
        "guest": "chloropromazine",
        "host": "heptakis-2,6-dimethyl-betacyclodextrin",
        "energy (kJ/mol)": -22.60,
        "uncertainty": 0.14,
    },
    {
        "guest": "chloropromazine",
        "host": "beta-cyclodextrin",
        "energy (kJ/mol)": -22.74,
        "uncertainty": 0.09,
    },
    {
        "guest": "chloropromazine",
        "host": "heptakis-6-methyl-beta-cyclodextrin",
        "energy (kJ/mol)": -12.62,
        "uncertainty": 0.95,
    },
    {
        "guest": "chloropromazine",
        "host": "heptakis-2,6-dimethyl-betacyclodextrin",
        "energy (kJ/mol)": -22.60,
        "uncertainty": 0.14,
    },
    {
        "guest": "thioridazine",
        "host": "beta-cyclodextrin",
        "energy (kJ/mol)": -23.85,
        "uncertainty": 0.12,
    },
    {
        "guest": "thioridazine",
        "host": "heptakis-6-methyl-beta-cyclodextrin",
        "energy (kJ/mol)": -29.40,
        "uncertainty": 0.9,
    },
    {
        "guest": "thioridazine",
        "host": "heptakis-2,6-dimethyl-betacyclodextrin",
        "energy (kJ/mol)": -27.07,
        "uncertainty": 0.14,
    },
    {
        "guest": "trifluoperazine",
        "host": "beta-cyclodextrin",
        "energy (kJ/mol)": -21.16,
        "uncertainty": 0.24,
    },
    {
        "guest": "trifluoperazine",
        "host": "heptakis-6-methyl-beta-cyclodextrin",
        "energy (kJ/mol)": -22.76,
        "uncertainty": 2.15,
    },
    {
        "guest": "trifluoperazine",
        "host": "heptakis-2,6-dimethyl-betacyclodextrin",
        "energy (kJ/mol)": -23.19,
        "uncertainty": 0.16,
    },
]

with open("directory.p", "wb") as outfile:
    pickle.dump(data, outfile)

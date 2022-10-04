import pickle

data = [
    {
        "guest": "promazine",
        "host": "beta-cyclodextrin",
        "energy (kJ/mol)": -20.83,
        "uncertainty": 0.10,
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
        "uncertainty": 0.20,
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
        "uncertainty": 0.90,
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
    {
        "guest": "plus-borneol",
        "host": "6-O-4-chlorophenyl-beta-cyclodextrin",
        "energy (kJ/mol)": -29.26,
        "uncertainty": 0.05,
    },
    {
        "guest": "plus-borneol",
        "host": "6-O-4-bromophenyl-beta-cyclodextrin",
        "energy (kJ/mol)": -28.18,
        "uncertainty": 0.13,
    },
    {
        "guest": "plus-borneol",
        "host": "6-O-4-nitrophenyl-beta-cyclodextrin",
        "energy (kJ/mol)": -28.7,
        "uncertainty": 0.01,
    },
    {
        "guest": "plus-borneol",
        "host": "6-O-4-hydroxybenzoyl-beta-cyclodextrin",
        "energy (kJ/mol)": -28.09,
        "uncertainty": 0.08,
    {
        "guest": "minus-borneol",
        "host": "6-O-4-chlorophenyl-beta-cyclodextrin",
        "energy (kJ/mol)": -28.27,
        "uncertainty": 0.02,
    },
    {
        "guest": "minus-borneol",
        "host": "6-O-4-bromophenyl-beta-cyclodextrin",
        "energy (kJ/mol)": -28.35,
        "uncertainty": 0.00,
    },
    {
        "guest": "minus-borneol",
        "host": "6-O-4-nitrophenyl-beta-cyclodextrin",
        "energy (kJ/mol)": -26.77,
        "uncertainty": 0.28,
    },
    {
        "guest": "minus-borneol",
        "host": "6-O-4-hydroxybenzoyl-beta-cyclodextrin",
        "energy": -28.34,
        "uncertainty": 0.0,
]

with open("directory.p", "wb") as outfile:
    pickle.dump(data, outfile)

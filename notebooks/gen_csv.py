import pandas as pd
import os

def gen_csv():

    def display_dataframe_to_user(name, df):
        print(f"[INFO] Dataframe '{name}' preview:")
        print(df.head())

    data = [
        {
            "metric_id": "cmhc_prevalence_men_pct",
            "metric_label": "Common mental health conditions prevalence (men)",
            "value": 15.4,
            "units": "percent",
            "year": 2023,
            "population_scope": "England (APMS 2023/24)",
            "source": "NHS Digital — APMS 2023/24",
            "source_url": "https://digital.nhs.uk/data-and-information/publications/statistical/adult-psychiatric-morbidity-survey/survey-of-mental-health-and-wellbeing-england-2023-24/common-mental-health-conditions",
            "note": "APMS definition: anxiety, depression and other common mental disorders."
        },
        {
            "metric_id": "male_suicide_rate_per_100k",
            "metric_label": "Male suicide rate",
            "value": 17.4,
            "units": "per 100000 population",
            "year": 2023,
            "population_scope": "England (ONS registered deaths 2023)",
            "source": "ONS — Suicides in the UK (reference tables)",
            "source_url": "https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/suicidesintheunitedkingdomreferencetables",
            "note": "Age-standardised rate; check ONS tables for exact England-only vs England & Wales split."
        },
        {
            "metric_id": "men_never_spoken_pct",
            "metric_label": "Men who have never spoken to anyone about their mental health",
            "value": 40.0,
            "units": "percent",
            "year": 2023,
            "population_scope": "UK (Priory Group survey)",
            "source": "Priory Group — public survey",
            "source_url": "https://www.priorygroup.com/blog/40-of-men-wont-talk-to-anyone-about-their-mental-health",
            "note": "Commercial survey; sample details in source. Use as indicative."
        },
        {
            "metric_id": "men_would_talk_to_nobody_pct",
            "metric_label": "Men who would talk to nobody if experiencing mental health problems",
            "value": 14.0,
            "units": "percent",
            "year": 2021,
            "population_scope": "UK (Psychreg survey)",
            "source": "Psychreg (summary of survey)",
            "source_url": "https://www.psychreg.org/uk-men-would-not-talk-about-mental-health/",
            "note": "Snapshot survey; includes breakdown of who men would talk to if they did."
        },
        {
            "metric_id": "iapt_referrals_pct_men",
            "metric_label": "Proportion of IAPT (talking-therapies) referrals for men",
            "value": 32.6,
            "units": "percent",
            "year": 2023,
            "population_scope": "England (IAPT service data)",
            "source": "NHS / IAPT statistics (summary)",
            "source_url": "https://www.england.nhs.uk/mental-health/",
            "note": "Percent of referrals that were male; proxy for help-seeking via NHS talking-therapies."
        }
    ]

    df = pd.DataFrame(data)

    csv_path = "../data/mens_mental_health_compact_metrics.csv"
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)

    df.to_csv(csv_path, index=False)

    display_dataframe_to_user("Men's mental health — compact metrics", df)

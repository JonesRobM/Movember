# Men's Mental Health Metrics

A compact dataset exploring key indicators of men's mental health in the UK - from prevalence rates to the gap between those struggling and those seeking help.

## What's Inside

This project consolidates data from NHS surveys, ONS statistics, and public research into a single CSV file and visualizations that highlight a critical story: many men experience mental health challenges, but far fewer reach out for support.

**Dataset:** `data/mens_mental_health_compact_metrics.csv`

**Visualizations:** `figures/mh_gap_chart.png` and `figures/mh_metrics_bar_chart.png`

**Analysis:** Jupyter notebook at `notebooks/metrics.ipynb`

### Dataset Structure

Each metric includes:
- `metric_id` - stable identifier for programmatic use
- `metric_label` - human-readable description
- `value` - numeric estimate
- `units` - measurement units
- `year` - year of estimate
- `population_scope` - geography and demographics
- `source` - publisher or statistical body
- `source_url` - link to original data
- `note` - methodology notes

## Data Sources

The metrics in this dataset come from official NHS statistics, ONS data, and public surveys. All sources are properly cited with URLs to the original publications.

**When using this dataset, please cite the original publishers, not this aggregation.**

### 1. NHS Digital - Adult Psychiatric Morbidity Survey (APMS) 2023/24
Provides prevalence rates of common mental health conditions (anxiety, depression) among men in England.

[View source](https://digital.nhs.uk/data-and-information/publications/statistical/adult-psychiatric-morbidity-survey/survey-of-mental-health-and-wellbeing-england-2023-24/common-mental-health-conditions)

### 2. Office for National Statistics - Suicides in the UK
Age-standardised male suicide rates per 100,000 population for England.

[View source](https://www.ons.gov.uk/peoplepopulationandcommunity/birthsdeathsandmarriages/deaths/datasets/suicidesintheunitedkingdomreferencetables)

### 3. Priory Group - Men and Mental Health Survey
Public survey data on men's willingness to discuss mental health - revealing that 40% have never talked about it.

[View source](https://www.priorygroup.com/blog/40-of-men-wont-talk-to-anyone-about-their-mental-health)

### 4. Psychreg - UK Men's Help-Seeking Survey
Survey data showing the percentage of men who wouldn't talk to anyone about mental health problems.

[View source](https://www.psychreg.org/uk-men-would-not-talk-about-mental-health/)

### 5. NHS England - IAPT Statistics
Data on Improving Access to Psychological Therapies (talking therapies), including the proportion of referrals that are men.

[View source](https://www.england.nhs.uk/mental-health/)

## Getting Started

Open the Jupyter notebook to explore the data and generate visualizations:

```bash
jupyter notebook notebooks/metrics.ipynb
```

The notebook:
- Generates the CSV dataset using `gen_csv.py`
- Creates bar charts comparing metrics
- Visualizes the gap between prevalence and help-seeking behavior

You can also regenerate just the CSV by running the generator module directly from the notebooks directory.

## Licensing and Attribution

**Data:** Each metric is subject to the licensing terms of its original publisher (NHS Digital, ONS, NHS England, Priory Group, Psychreg).

**This repository:** The code and aggregation are available under a permissive license (MIT/CC-BY).

**Attribution:** Always cite the original sources when using this data - links are provided above and in the CSV itself.

## Important Notes

This is a compact, exploratory dataset - not an exhaustive review of men's mental health research.

**Methodological differences:** Official statistics (APMS, ONS) use rigorous sampling methodology, while survey-based figures (Priory Group, Psychreg) should be interpreted with more caution. They're included here to illustrate public attitudes rather than clinical prevalence.

**Not for clinical use:** This dataset is for awareness, education, and exploratory analysis - not for making clinical or policy decisions.

---

*Data compiled to raise awareness during Movember and beyond. Men's mental health matters.*
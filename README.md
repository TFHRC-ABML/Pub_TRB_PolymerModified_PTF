# Data and Analysis Code for TRB Manuscript

## Performance Evaluation of Polymer-Modified Asphalt Binders and Mixtures: Insights from FHWA's New Pavement Testing Facility

[![GitHub License](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/TFHRC-ABML/Pub_TRB_PolymerModified_PTF/blob/main/LICENSE)

📄 **[Paper Link (under review, will be out soon)](XXXX)**

### Authors and Contributors
- *Behnam Jahangiri (behnam.jahangiri.ctr@dot.gov)*
- *S. Farhad Abdollahi (farhad.abdollahi.ctr@dot.gov)*
- *Aaron Leavitt (aaron.leavitt@dot.gov)*
- *Adrian Anderiescu (adrian.anderiescu.ctr@dot.gov)*
- *Hamzeh Haghshenas (hhaghshenas@nas.edu)*
- *David Mensching (david.mensching@dot.gov)*

---

This repository contains the data and analysis code accompanying the TRB manuscript (currently under review) titled:  
**"Performance Evaluation of Polymer-Modified Asphalt Binders and Mixtures: Insights from FHWA's New Pavement Testing Facility."**

---

## Table of Contents

1. [Requirements](#requirements)
2. [Dataset](#dataset)
3. [Analysis Code](#analysis-code)
4. [Acknowledgments](#acknowledgments)
5. [Citation](#citation)

---

## Requirements

The analysis is implemented in Python and utilizes several external libraries. For full compatibility, it is recommended to install the specific 
configuration listed below. However, stable upgraded versions of these libraries are also expected to work properly:

- Python 3.8.20  
- `numpy` 1.24.3  
- `scipy` 1.10.1  
- `pandas` 2.0.3  
- `matplotlib` 3.7.2  

---

## Dataset

The dataset is provided as an Excel file, `Data.xlsx`, which contains multiple sheets corresponding to different laboratory tests and material properties:

- **HTPG**: Measured HTPG of tank and recovered binders.
- **MSCR**: Measured recovery (e.g., $R_{3.2}$) and non-recoverable creep compliance (e.g., $J_{nr,3.2}$) parameters for tank and recovered binder at 64°C. 
- **Glover-Rowe (G-R)**: |G*| and phase angle values at 44.7 °C and 10 rad/s used to compute the G-R parameter.
- **Binder Frequency Sweep**: Detailed binder frequency sweep results at different temperatures ranging from 10°C to 82°C and loading frequencies ranging from 0.1 rad/s to 100 rad/s for all the tank and recovered binders at different aging levels.  
- **DENT**: Results from the DENT test, including failure energy, maximum load, and ligament properties, which are used to calculate the CTOD.
- **DENT Curves**: Force-displacement data of the DENT test for one replicate of tank and recovered binders.
- **BBR (LTPG)**: Measured S-value and m-values at two pass/fail low temperatures used for calculating the LTPG and ΔTc parameters.  
- **FTIR**: Calculated Carbonyl and Sulfoxide indices (ICO & ISO) using the deconvolution method for tank and recovered binders at unaged and PAV-aged states. 
- **Gradation**: As-designed and as-produced gradation of the asphalt mixtures used in different lanes, along with their control points, based on Viriginia DOT specification. 
- **HWTT**: Summary results of the HWTT tests, including the corrected rut depth, stripping number, SIP, etc. 
- **HWTT Curves**: Raw rutting data from the Hamburg Wheel Tracking Test for all mixtures at STA aging condition.
- **IDEAL-RT**: Summary results of the IDEAL-RT test for all mixtures at STA aging condition.
- **IDEAL-CT**: Summary results of the IDEAL-CT test for all mixtures at both STA and LTA aging condition.
- **CF Sapp**: Calculated Sapp values obtained from the cyclic fatigue and dynamic modulus test results for all mixtures at STA and LTA aging conditions.  

**NOTE**: **Tank binders** refer to the binders collected from the asphalt binder tank in the asphalt plant during the production of the mixtures for construction. However, **recovered binders** refer to the binder extracted and recovered from the loose mixtures sampled right behind the asphalt paver. 

---

## Analysis Code

The analysis is organized into four Jupyter Notebooks:

- `Task01_Binder_Level.ipynb`: This notebook include the codes to read, analyze, and plot the binder-level test results.
- `Task02_Mixture_Level.ipynb`: This notebook include the codes to read, analyze and plot the mixture-level test results.

---

## Acknowledgments

We gratefully acknowledge Bethel La Plana, Steve Portillo, Scott Parobeck, and Frank Davis for their efforts in preparing and testing the asphalt binder and mixture samples used in this study.

---

## Citation

If you use this code or dataset in your research, please cite the following:

```bibtex
@misc{JahangiriPMB2025,
  title     = {Performance Evaluation of Polymer-Modified Asphalt Binders and Mixtures: Insights from FHWA's New Pavement Testing Facility},
  author    = {Jahangiri, Behnam and Abdollahi, Seyed Farhad and Leavitt, Aaron and Anderiescu, Adrian and Haghshenas, Hamzeh and Mensching, David},
  year      = {TBD},
  month     = {TBD},
  publisher = {Transportation Research Board},
  doi       = {XXXXX},
  urldate   = {2025-07-29},
  archiveprefix = {XXX},
  langid    = {english},
  keywords  = {Styrene-Butadiene-Styrene (SBS), Polymer Modification, Asphalt Binder, Stone Matrix Asphalt (SMA), Performance Testing}
}
```

---

📬 For questions or feedback, please contact **Farhad Abdollahi** at *farhad.abdollahi.ctr@dot.gov*.
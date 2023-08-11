# LLM-Latency-Analysis
This repo is used to generate histograms, scatterplots and regression plots for the datasets containing the latency time for different prompt sizes across the three LLMs - Starcoder, Starcoder Plus & LLaMa2-7B.

One objective here is to evaluate whether latency time(s) is impacted by prompt size(B). This is demonstrated when executing files: scatterplot_generator.py, distribution_generator_for_all_models.py and histogram_generator_for_all_models.py.

We also want to see the overall distribution of latency time(s). This is demonstrated when executing files: histogram_generator_for_time.py and distribution_curve_for_time.py

Three datasets were created to record the latency time when testing three instruction prompts on Hugging Face. The tests were executed 10 times to increase reliability and accuracy of the results. Anormalous results were extracted from datasets to improve accuracy when identifying the trends with latency time.

How to run this repo:

1. Install the relevant libraries (e.g. matplotlib, numpy, pandas, seaborn)
2. Choose any of the given py files and run on VSCode.


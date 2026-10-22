# SpaceX Falcon 9 landing analysis

Repository: https://github.com/Zeppelin567/ibm-spacex-capstone

IBM Applied Data Science Capstone project. All reported statistics come from executed code. The course target includes successful ocean outcomes, which do not necessarily mean recovery suitable for reuse.

## Files

- `SpaceX_Capstone_Analysis.ipynb`: executed collection, cleaning, EDA, SQL, Folium mapping and four-model comparison.
- `Data Science Capstone Project Report.pdf`: presentation for assessment submission.
- `SpaceX_Capstone_Presentation.pptx`: editable presentation, including native charts and tables.
- `spacex_dash_app.py`: working dashboard with site and payload filters.
- `launch_sites_map.html`, `launch_records_map.html`, `launch_site_proximity.html`: interactive maps.
- CSV, JSON and HTML files preserve official course data and the specified Wikipedia revision.
- PNG files show analysis figures and screenshots of the running applications.

## Reproduce

Use Python 3.12 with the packages in `requirements.txt`. Run the notebook from this directory. Select a local Python kernel if the saved `workpython` kernel name is unavailable. The notebook uses local snapshots and does not require live API access.

Run `python spacex_dash_app.py` and open http://127.0.0.1:8051. Open the map HTML files in a browser. Map tiles require internet access.

## Results and limits

The filtered API sample has 90 launches and 60 class-1 outcomes (66.7%). Five-fold training cross-validation selects a depth-3 decision tree with minimum leaf size 4. Its held-out test accuracy is 83.3% on 18 rows. The test confusion matrix is `[[3,3],[0,12]]`, with unsuccessful outcomes listed first.

The 101-row SQL and 56-row dashboard datasets are different historical populations. Keep their denominators separate. Payload mass was already mean-imputed in the official enriched API snapshot. In addition, `ReusedCount` may reflect reuse after a recorded launch. These data support a retrospective benchmark. Reconstruct features available at launch time and use a chronological holdout before prospective prediction or business use. Ocean landing success is not equivalent to reusable recovery.

## Sources and attribution

Accessed 21 October 2026:

- IBM API snapshot: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/API_call_spacex_api.json
- IBM enriched API dataset: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/dataset_part_1.csv
- IBM SQL dataset: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv
- IBM dashboard dataset: https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/datasets/spacex_launch_dash.csv
- Wikipedia contributors, List of Falcon 9 and Falcon Heavy launches, revision 1027686922: https://en.wikipedia.org/w/index.php?title=List_of_Falcon_9_and_Falcon_Heavy_launches&oldid=1027686922 . Wikipedia text is available under its applicable Creative Commons Attribution-ShareAlike terms. The preserved page retains attribution links.
- Interactive map basemaps: © OpenStreetMap contributors, https://www.openstreetmap.org/copyright

Original course datasets and materials retain their providers' terms. No license to third-party materials is implied by this repository.

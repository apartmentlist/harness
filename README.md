# Harness
This query harness is used to call the apartmentlist search endpoint and record the results in an output file

## Setup

In a separate environment, run `pip install -r requirements.txt`  

An environment variable - `TOKEN` needs to be set, which is the token of a an admin user

### Using the harness

Call the harness with:
`python query_harness.py [filename] [...treatment_names]`
Where `filename` is a file of line separated search queries to call, and treatment names represent the scoring variation used for each query.

### Output file Example
`python query_harness.py input_file.txt treatment1 treatment2`

The script will produce the following output file format.

The control scorer will be implicitly called, and another call to the search endpoint will be made for each treatment argument passed.

The output file will be called `responses.txt`, where the responses for each search query in the input file will be separated by the name of the scorer in the line above.

```
Control
{"analytics_metadata":{"search_uuid":"c53ca2bb-4aab-435e-bcc2-05e2b58514c0"}]}
treatment1
{"analytics_metadata":{"search_uuid":"c53ca2bb-4aab-435e-bcc2-05e2b58514c0"}]}
treatment2
{"analytics_metadata":{"search_uuid":"c53ca2bb-4aab-435e-bcc2-05e2b58514c0"}]}
...
...
```

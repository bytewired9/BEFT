# Definitions

## Formatting:

Definitions follow the typical minecraft json format, just with a little bit of extra organization

```py
index = {
    
}

attributes = {
    
}

properties = {
    
}

components = {
    
}

```

and so forth...

for values, we use the following placeholders,

* "[STR]" - for strings
* "[FLOAT]" - for decimals
* "[INT]" - for integers
* "[BOOL]" - for boolean values (true/false)
* "[LIST]" - for any list of strings, values etc.
* "[FILTER]" - for minecraft filters
* "[VECTOR]" - for vectors

if there is a default value, it would look like this:
"[PLACEHOLDER]/defaultvalue"
example:
"[INT]/4"

you can check out /behavior_packs/entities/1.8.0.py for an example

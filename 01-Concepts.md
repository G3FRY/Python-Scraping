# Scraping

## Basic Concepts

We can use _Xpath_ to reach an element within the **DOM**

```
xpath = '/html/body/div[2]
```

The defined _xpath_ variable is pointing to the second `div` nested inside the body tag.

```
all_tables = '//table'
```

The _all_tables_ variable points to all the included tables in the DOM

## Using attributes

In the Xpath we can ask for a particular attribute and value using [@attribute="attribute_value"] after the _Xpath_

For example, selecting a div whose _id_ attribute is equal to _first_ should be:

```
xpath = '//div[@id="first"]
```

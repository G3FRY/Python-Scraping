# _Styling_ **Text**

## Italic and Bold
Underscore _ is used before and after the text to make it _italics_ and double asterisks ** before and after to turn text **bold**

Italics and Bold can be **_combined!_**, also in a nested way

**this is _italic_ inside a bold text**

To use italics and bold at the same time, we use ***

***This is italic and bold text***

Also can be used in titles, like the title of this section.

## Strikethrough
Using ~~ at the beginning and end of the text will place a strke over the text

~~Like this one!!~~

## Quoting Code

To insert code inline we use ` at the start and end of the text. A code block is created by using triple quotes ( ``` )

These are some basic `Git commands`:

```
git status  
git add
git commit
```

## Subscript and Superscript

For **Subscripts** we use `<sub></sub>`

This is a text with <sub>SUBSCRIPT</sub>

For **Superscripts** we use `<sup></sup>`

This is a text with <sup>SUPERSCRIPT</sup>


# Headers
Use # to define a header element, the number of # determines the level of identation
## Level two
### Level three
#### Level four
##### Level five
###### level six
Level six is the last header size we can use

# Links (Also work in [headers](https://www.markdowntutorial.com))
To define a link we use [ ] to wrap the text and ( ) to put the hyperlink

[Visit GitHub](https://www.github.com)

Also, emphasis to link text is possible

[_Here_ is an **example**](http://www.dailykitten.com)

There is another type of link, called _reference_ link used to define references in another place in the document.

Here's a link [To some place][some place]

[some place]: www.someplace.com

# Images
Images are similar to links, the only difference is the preceding exclamation point ( ! ).

![This is alternative text](https://upload.wikimedia.org/wikipedia/commons/5/56/Tiger.50.jpg)

# Blockquotes
To add blockquotes we use the greater than ( > ) caret.

> "You can die anytime, but living takes courage" _Kenshin Himura_

If the quote span multiple lines, all lines must have the caret.

>"What is **truly good** about a person **can't be expressed in words**, that it can not. 
>
>What matters is the _feeling of trust_ one gets after spending time with him."
>
>_Kenshin Himura_

#Lists
For unordered lists we use a single asterisk
* Eggs
* Salmon
* Butter

An ordered list is prefaced with numbers, we can also format text and add links

1. Crack the **Eggs** 
2. Put the _Butter_ in a bowl
3. Add the **Eggs** to the bowl
4. Put the **Salmon** into the bowl

Also nested lists are possible

* Tintin
  * A reporter
  * Has poofy orange hair
  * Friends with the world's most awesome dog
* Haddock
  * A sea captain
  * Has a fantastic beard
  * Loves whiskey
  * Possibly also scotch?

# Paragraphs

Using double space we can add a _soft break_

Without double spaces:

>**_Do I contradict myself?
Very well then I contradict myself,
(I am large, I contain multitudes.)_**

Adding break lines to each line will produce a _hard break_:

>**_Do I contradict myself?_**
>
>**_Very well then I contradict myself,_**
>
>**_(I am large, I contain multitudes.)_**

Using double space to end each line

>**_Do I contradict myself?_**  
>**_Very well then I contradict myself,_**  
>**_(I am large, I contain multitudes.)_**  

# Color model

We can use backticks and a color model notation to call colors in the document

* background: `#ff55ff`

NOTE: This only works in `issues`, `pull requests` and `issues` inside GitHub.


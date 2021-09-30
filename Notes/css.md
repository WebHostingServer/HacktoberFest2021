# CSS basic concepts

# Three types of css

1. inline
1. Internal
1. External

## inline CSS

This is when we are applying style property to extreme Elements
using style tags 

## internal CSS

we use this when style element inside the hashtag of html document

## external CSS

---

# Rankings

**Inline style overrides Internal styles and internal overrides external styles**

# Styling elements

| Property      | Function |
| ----------    | ----------- |
| text-align-Justify | All the text is spaced across the available space |
| FontStyle     | Defines style of fonts
| FontWight     | Defines the thickness of the font 
| TextDecoration| To underline the texts overline, line-though 
| TextTransform | Uppercase lowercase capitalize 
| LetterSpacing | Increase space between letters
| lineHeight    | Changes the space between lines
| Border        | We can change border width style and colors
| Paragraph | Text  

### [CSS short hand](https://developer.mozilla.org/en-US/docs/Web/CSS/Shorthand_properties)

------
---------

## Margin and padding

Padding
: when we need space inside the borders we use padding

Margin
: when we need space outside the border we use margins 

## Styles to List

| ListStyleType | Properties |
| -----------   | ----------- |
| ListUpperAlpha| Alphabetical order and uppercase 
| UpperRoman    | Roman numbers with upper case 
| LowerRoman    | Roman numbers and lower case 
| ReducingWidth | Transform list into multi lined
| ListStyledPositions| Text and styling dint have indentions

## Different states of Link

1. link : this is the link is not visited
1. Visited : this is the link when its visited
1. Hover: this tis the state when mouse is hovered
1. Active: This is the state when link is clicked


# Display Value 

Display property:
 The display property specifies the display behavior (the type of rendering box) of an element.

In HTML, the default display property value is taken from the HTML specifications or from the browser/user default style sheet. The default value in XML is inline, including SVG elements.

## Inline block

Displays an element as an inline element (like <span>). Any height and width properties will have no effect

## Block

Displays an element as a block element (like <p>). It starts on a new line, and takes up the whole width

# Positioning HTML elements

## We have the following positioning values

1. Static
1. Relative
1. Absolute
1. Fixed
1. Sticky

## Static

Weather we declare it or not it is the default position for HTML elements

it positions element in normal order on the webpage

## Relative

it Helps to position HTML elements relative to normal position

It provides access to top right bottom and left property

## Absolute

It helps position HTML element relative to the parent elements

The parent elements need to have a position other than Static or else the absolute elements is positioned relative to the main HTML element

## Fixed

It helps position HTML elements relative to the main HTML elements being fixed at the defined position

The position fixed elements are not affected by scroll position of webPage.

# Handling Overflow

The CSS overflow property controls what happens to content that is too big to fit into an area.
The overflow property specifies whether to clip the content or to add scroll bars when the content of an element is too big to fit in the specified area.

## [Overflow Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/overflow)

1. Visible
1. Hidden
1. Scroll
1. Auto
The difference between scroll and hidden is when in auto scroll bars are only visible when content is larger than container

# Float

[Float](https://developer.mozilla.org/en-US/docs/Web/CSS/float):
The float CSS property places an element on the left or right side of its container, allowing text and inline elements to wrap around it. The element is removed from the normal flow of the page, though still remaining a part of the flow (in contrast to absolute positioning).


# [Box Model](https://www.w3schools.com/css/css_boxmodel.asp)

Every HTML element consists of a box surrounding the content 
1. Content
1. Padding
1. Border
1. Margin

## [Box-Sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/box-sizing) 
Box-sizing:
The box-sizing CSS property sets how the total width and height of an element is calculated.

By default in the CSS box model, the width and height you assign to an element is applied only to the element's content box. If the element has any border or padding, this is then added to the width and height to arrive at the size of the box that's rendered on the screen. This means that when you set width and height, you have to adjust the value you give to allow for any border or padding that may be added. For example, if you have four boxes with width: 25%;, if any has left or right padding or a left or right border, they will not by default fit on one line within the constraints of the parent container.

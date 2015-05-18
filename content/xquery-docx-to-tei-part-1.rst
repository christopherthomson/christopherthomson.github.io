XQuery: docx to TEI (part 1)
############################
:date: 2012-07-01 22:02
:author: chris
:category: Uncategorized
:slug: xquery-docx-to-tei-part-1

I'm working on converting a large bibliography from Microsoft Word docx
format to TEI.  `A few months ago`_ I was pretty certain I'd be
approaching this with a manual process, mostly because of the difficulty
of constructing divs for each type of bibliography entry and other
structured sections. But Word styles and `OxGarage`_ makes it possible
to convert from docx to TEI with enough structure that most of the
difficulties I saw then can be overcome.

Luckily, the original document had an index of authors which marked the
start of each entry, and styles had been applied fairly consistently to
distinguish headings, annotations and citations. Here's an example of
the structure of the entry I wanted to isolate:

``[gist]http://gist.github.com/3606192[/gist]``

The problem is that there's no tag to define where this entry ends - it
just lists another paragraph containing an author name and so on. The
first step needed was to go from an 'anchor' marking the start - in this
case I used the index element - to a complete XML element wrapping each
author's entry.  Google turned up `a rather complex piece of XQuery`_ to
solve the problem.

This required very little adjustment to get the result I was after. I
just changed the selection of the $childs and tweaked the formula used
within the element constructor to ensure the first paragraph was
included.

The next step was to split the file into a collection of separate files,
one for each entry.  Again, the work has been `done and documented`_.

This worked well with only a couple of small changes to the element
constructor from the example given: 1) I added the suggested $count to
generate a numbered filename, and 2) I needed to remove some stray
whitespace in the element I used for the entry name, using
fn:normalize-space(text()). I ran the query in the browser rather than
in oXygen 12.2, as I couldn't get oXygen to recognise the xmldb
namespace needed for this code (this seems to be because oXygen was
using Saxon rather than eXist to parse the XQuery, despite the
Preferences saying it should use eXist). The element constructor to be
returned looked like this:

[gist]https://gist.github.com/3606928[/gist]

The next step will be creating some more structure with div and
biblStruct elements, and then I'll need to pull apart the citations
themselves.

.. _A few months ago: http://christopherthomson.co.nz/blog/?p=68
.. _OxGarage: http://oxgarage.oucs.ox.ac.uk:8080/ege-webclient/
.. _a rather complex piece of XQuery: http://stackoverflow.com/questions/6865667/xpath-flat-hierarchy-and-stop-condition
.. _done and documented: http://en.wikibooks.org/wiki/XQuery/Splitting_Files

Title: DigitalNZ search with XQuery
Date: 2013-03-11 08:18
Author: chris
Category: Uncategorized
Slug: using-xquery-with-the-digitalnz-api

I decided I wanted to add an external search function as part of the
[bibliography] [1] I'm working on, and a [DigitalNZ] [2] search seemed to be
the obvious choice.  XQuery makes this really easy, and I'm surprised it
doesn't feature on their [list of code samples] [3].  Possibly it is so
straightforward that an example isn't necessary.

I wanted a list of results for each author in the bibliography, broken
down according to content provider offering those results. This can be
grabbed by specifying `facets=content\_partner` in the query string.  All
the work is done by the XQuery doc() function in the third line below -
everything else is presentation.

[[ gist christopherthomson:3943734 ]]

[1]: http://christopherthomson.co.nz/blog/?p=68	"bibliography"
[2]: http://www.digitalnz.org						"DigitalNZ"
[3]: http://www.digitalnz.org/developers/code-samples-and-libraries	"list of code samples"

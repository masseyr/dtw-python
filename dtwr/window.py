##
## Copyright (c) 2006-2019 of Toni Giorgino
##
## This file is part of the DTW package.
##
## DTW is free software: you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.
##
## DTW is distributed in the hope that it will be useful, but WITHOUT
## ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
## or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public
## License for more details.
##
## You should have received a copy of the GNU General Public License
## along with DTW.  If not, see <http://www.gnu.org/licenses/>.
##


#IMPORT_RDOCSTRING dtwWindowingFunctions
"""Global constraints and windowing functions for DTW


Various global constraints (windows) which can be applied to the
``window.type`` argument of [dtw()], including the Sakoe-Chiba band, the
Itakura parallelogram, and custom functions.


**Details**

Windowing functions can be passed to the ``window.type`` argument in
[dtw()] to put a global constraint to the warping paths allowed. They
take two integer arguments (plus optional parameters) and must return a
boolean value ``TRUE`` if the coordinates fall within the allowed region
for warping paths, ``FALSE`` otherwise.

User-defined functions can read variables ``reference.size``,
``query.size`` and ``window.size``; these are pre-set upon invocation.
Some functions require additional parameters which must be set (e.g.
``window.size``). User-defined functions are free to implement any
window shape, as long as at least one path is allowed between the
initial and final alignment points, i.e., they are compatible with the
DTW constraints.

The ``sakoeChibaWindow`` function implements the Sakoe-Chiba band, i.e.
``window.size`` elements around the ``main`` diagonal. If the window
size is too small, i.e. if ``reference.size``-``query.size`` >
``window.size``, warping becomes impossible.

An ``itakuraWindow`` global constraint is still provided with this
package. See example below for a demonstration of the difference between
a local the two.

The ``slantedBandWindow`` (package-specific) is a band centered around
the (jagged) line segment which joins element ``[1,1]`` to element
``[query.size,reference.size]``, and will be ``window.size`` columns
wide. In other words, the “diagonal” goes from one corner to the other
of the possibly rectangular cost matrix, therefore having a slope of
``M/N``, not 1.

``dtwWindow.plot`` visualizes a windowing function. By default it plots
a 200 x 220 rectangular region, which can be changed via
``reference.size`` and ``query.size`` arguments.



Parameters
----------

iw : 
    index in the query (row) -- automatically set
jw : 
    index in the reference (column) -- automatically set
query.size : 
    size of the query time series -- automatically set
reference.size : 
    size of the reference time series -- automatically set
window.size : 
    window size, used by some windowing functions -- must be
set
fun : 
    a windowing function
... : 
    additional arguments passed to windowing functions


Returns
-------

Windowing functions return ``TRUE`` if the coordinates passed as
arguments fall within the chosen warping window, ``FALSE`` otherwise.
User-defined functions should do the same.



Notes
-----

Although ``dtwWindow.plot`` resembles object-oriented notation, there is
not a such a dtwWindow class currently.

A widely held misconception is that the “Itakura parallelogram” (as
described in reference 2) is a *global* constraint, i.e. a window. To
the author’s knowledge, it instead arises from the local slope
restrictions imposed to the warping path, such as the one implemented by
the [typeIIIc()] step pattern.





"""
#ENDIMPORT


def noWindow(iw, jw, query_size, reference_size):
    return True

def sakoeChibaWindow(iw, jw, query_size, reference_size, window_size):
    ok = abs(jw-iw) <= window_size
    return ok

def itakuraWindow(iw, jw, query_size, reference_size):
	n<-query_size
	m<-reference_size
	ok =	(jw <  2*iw) and \
		(iw <= 2*jw) and \
		(iw >= n-1-2*(m-jw)) and \
		(jw >  m-1-2*(n-iw))
	return ok

   

def slantedBandWindow(iw, jw, query_size, reference_size, window_size):
    diagj = (iw*reference.size/query.size)
    return abs(jw-diagj)<=window.size;




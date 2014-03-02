# coding: utf-8
import py

from MoinMoin import wikiutil

import urllib

from MoinMoin.PageEditor import PageEditor
from MoinMoin.web.contexts import ScriptContext
from MoinMoin.Page import Page

pagename = u"Class_SharpAC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #AC^0^ - Sharp-AC0 =

----
CategoryClassical 

== Description ==

{{{#!description

The class of functions from {0,1}^n^ to nonnegative integers computed by polynomial-size constant-depth arithmetic circuits, using addition and multiplication gates and the constants 0 and 1.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_GapAC0|$\\text{GapAC}^\\text{0}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SharpAC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SharpAC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SharpGA"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #GA - Graph Automorphism =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems (Karp-)reducible to counting the number of automorphisms of a graph.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Counterpart of [[Class_GI|$\\text{GI}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SharpGA)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SharpGA because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SharpL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #L - Sharp-L =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_SharpP|$\\text{#P}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_SharpL|$\\text{#L}$]] is contained in [[Class_DET|$\\text{DET}$]] [[ZooRefs#AJ93|[AJ93] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SharpL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SharpL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SharpL/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #L/poly - Nonuniform #L =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_SharpL|$\\text{#L}$]] as [[Class_P/poly|$\\text{P/poly}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SharpL/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SharpL/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SharpP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #P - Sharp-P =

----
CategoryClassical 

== Description ==

{{{#!description

The class of function problems of the form "compute f(x)," where f is the number of accepting paths of an [[Class_NP|$\\text{NP}$]] machine.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The canonical #P-complete problem is #SAT: given a Boolean formula, compute how many satisfying assignments it has.



Defined in [[ZooRefs#Val79|[Val79] ]], where it was also shown that the problem of counting the number of perfect matchings in a bipartite graph (or equivalently, computing the permanent of a 0-1 matrix) is #P-complete.



What makes that interesting is that the associated decision problem (whether a bipartite graph has a perfect matching) is in [[Class_P|$\\text{P}$]].



[[Class_PH|$\\text{PH}$]] is in [[Class_PSharpP|$\\text{P}^\\text{#P}\\text{}$]] [[ZooRefs#Tod89|[Tod89] ]].



Any function in [[Class_SharpP|$\\text{#P}$]] can be approximated to within a polynomial factor in [[Class_BPP|$\\text{BPP}$]] with [[Class_NP|$\\text{NP}$]] oracle [[ZooRefs#Sto85|[Sto85] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SharpP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SharpP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SharpW[t]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #W[t] - Sharp-W[t] =

----
CategoryClassical 

== Description ==

{{{#!description

Roughly, the analogue of [[Class_SharpP|$\\text{#P}$]] for parameterized complexity.  I.e. the class of parameterized counting problems that are fixed-parameter parsimonious reducible to the following problem:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



#WSAT: Given a Boolean formula, count the number of satisfying assignments of Hamming weight k (where k is the parameter).



Defined in [[ZooRefs#FG02|[FG02] ]], which should be consulted for the full definition.  [[ZooRefs#FG02|[FG02] ]] also showed that there exist #W[1]-complete problems whose corresponding decision problems are fixed-parameter tractable (i.e. in [[Class_FPT|$\\text{FPT}$]]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SharpW[t])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SharpW[t] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_(Mk)P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= (M,,k,,)P - Acceptance Mechanism by Monoid Mk =

----
CategoryClassical 

== Description ==

{{{#!description

A monoid is a set with an associative operation and an identity element (so it's like a group, except that it need not have inverses).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Then (M,,k,,)P is the class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine with the following acceptance mechanism.  The i^th^ computation path (under some lexicographic ordering) outputs an element m,,i,, of M,,k,,.  Then the machine accepts if and only if m,,1,,m,,2,,...m,,s,, is the identity (where s is the number of paths).



Defined by Hertrampf [[ZooRefs#Her97|[Her97] ]], who also showed the following (in the special case M is a group):



If G is any nonsolvable group (for example S,,5,,, the symmetric group on 5 elements), then (G)P = [[Class_PSPACE|$\\text{PSPACE}$]].

(Z,,k,,)P = [[Class_coModkP|$\\text{coMod}_\\text{k}\\text{P}$]], where Z,,k,, is the cyclic group on k elements.

If |G|=k, then (G)P contains [[Class_coModkP|$\\text{coMod}_\\text{k}\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_(Mk)P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save (Mk)P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_(NP ∩ coNP)/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= (NP ∩ coNP)/poly - Nonuniform NP ∩ coNP =

----
CategoryClassical 

== Description ==

{{{#!description

Together with [[Class_NP/poly|$\\text{NP/poly}$]] ∩ [[Class_coNP/poly|$\\text{coNP/poly}$]], has the same relation to [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]] as [[Class_P/poly|$\\text{P/poly}$]] has to [[Class_P|$\\text{P}$]].  A language in ([[Class_NP|$\\text{NP}$]] ∩ coNP)/poly is defined by a single language in [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]] which is then modified by advice.  A language in [[Class_NP/poly|$\\text{NP/poly}$]] ∩ [[Class_coNP/poly|$\\text{coNP/poly}$]] comes from two possibly different languages in [[Class_NP|$\\text{NP}$]] and [[Class_coNP|$\\text{coNP}$]] which become the same with good advice.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



There is an oracle relative to which [[Class_NP/poly|$\\text{NP/poly}$]] ∩ [[Class_coNP/poly|$\\text{coNP/poly}$]], indeed NP/1 ∩ coNP/1, is not contained in ([[Class_NP|$\\text{NP}$]] ∩ coNP)/poly [[ZooRefs#FFK+93|[FFK+93] ]].  Recently they improved this to NP/1 ∩ [[Class_coNP|$\\text{coNP}$]] [[ZooRefs#FF..|[FF..] ]].



If [[Class_NP|$\\text{NP}$]] is contained in ([[Class_NP|$\\text{NP}$]] ∩ coNP)/poly, then [[Class_PH|$\\text{PH}$]] collapses to S,,2,,P^NP ∩ [[Class_coNP|$\\text{coNP}\\text{}$]] [[ZooRefs#CCH+01|[CCH+01] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_(NP ∩ coNP)/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save (NP ∩ coNP)/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_(NP,P-samplable)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= (NP,P-samplable) - Average NP With Samplable Distributions =

----
CategoryClassical 

== Description ==

{{{#!description

See [[Class_AvgP|$\\text{AvgP}$]] for basic notions of average-case complexity.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



(NP,P-samplable) is the same as [[Class_DistNP|$\\text{DistNP}$]], except that the distribution μ only needs to be samplable in polynomial time.  μ's cumulative density function does not need to be computable in polynomial time.



Any problem complete for [[Class_DistNP|$\\text{DistNP}$]] is also complete for (NP,P-samplable) [[ZooRefs#IL90|[IL90] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_(NP,P-samplable))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save (NP,P-samplable) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_0-1-NPC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= 0-1-NP,,C,, - Binary Restriction of NP Over The Complex Numbers =

----
CategoryClassical 

== Description ==

{{{#!description

The intersection of [[Class_NPC|$\\text{NP}_\\text{C}\\text{}$]] with {0,1}^*^ (i.e. the set of binary strings).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_NP|$\\text{NP}$]].



Is contained in [[Class_PSPACE|$\\text{PSPACE}$]], and in [[Class_AM|$\\text{AM}$]] assuming the Extended Riemann Hypothesis [[ZooRefs#Koi96|[Koi96] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_0-1-NPC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save 0-1-NPC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_1NAuxPDAp"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= 1NAuxPDA^p^ - One-Way NAuxPDAp =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#Bra77|[Bra77] ]], where it was also shown that [[Class_1NAuxPDAp|$\\text{1NAuxPDA}^\\text{p}\\text{}$]] strictly contains [[Class_CFL|$\\text{CFL}$]] and is strictly contained in [[Class_LOGCFL|$\\text{LOGCFL}$]]. The class corresponds to the closure of [[Class_CFL|$\\text{CFL}$]] under one-way log-space reductions.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_1NAuxPDAp)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save 1NAuxPDAp because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_A0PP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= A,,0,,PP - One-Sided Analog of AWPP =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_SBP|$\\text{SBP}$]], except that f is a nonnegative-valued [[Class_GapP|$\\text{GapP}$]] function rather than a [[Class_SharpP|$\\text{#P}$]] function.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Vya03|[Vya03] ]], where the following was also shown:



[[Class_A0PP|$\\text{A}_\\text{0}\\text{PP}$]] contains [[Class_QMA|$\\text{QMA}$]], [[Class_AWPP|$\\text{AWPP}$]], and [[Class_coC=P|$\\text{coC}_\\text{=}\\text{P}$]].

[[Class_A0PP|$\\text{A}_\\text{0}\\text{PP}$]] is contained in [[Class_PP|$\\text{PP}$]].

If [[Class_A0PP|$\\text{A}_\\text{0}\\text{PP}$]] = [[Class_PP|$\\text{PP}$]] then [[Class_PH|$\\text{PH}$]] is contained in [[Class_PP|$\\text{PP}$]].



Kuperberg ([[ZooRefs#Kup09|[Kup09] ]]) showed that [[Class_A0PP|$\\text{A}_\\text{0}\\text{PP}$]] = [[Class_SBQP|$\\text{SBQP}$]].



Same as [[Class_SBP|$\\text{SBP}$]], except that f is a [[Class_GapP|$\\text{GapP}$]] rather than [[Class_SharpP|$\\text{#P}$]] function.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_A0PP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save A0PP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AC - Unbounded Fanin Polylogarithmic-Depth Circuits =

----
CategoryClassical 

== Description ==

{{{#!description

AC^i^ is the class of decision problems solvable by a nonuniform family of Boolean circuits, with polynomial size, depth O(log^i^(n)), and unbounded fanin.  The gates allowed are AND, OR, and NOT.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Then [[Class_AC|$\\text{AC}$]] is the union of AC^i^ over all nonnegative i.



AC^i^ is contained in NC^i+1^; thus, [[Class_AC|$\\text{AC}$]] = [[Class_NC|$\\text{NC}$]].



Contains [[Class_NL|$\\text{NL}$]].



For a random oracle A, (AC^i^)^A^ is strictly contained in (AC^i+1^)^A^, and (uniform) AC^A^ is strictly contained in P^A^, with probability 1 [[ZooRefs#Mil92|[Mil92] ]].



fo-uniform [[Class_AC|$\\text{AC}$]] with depth $t(n)$ is equal to [[Class_FO[t(n)]|$\\text{FO[t(n)]}$]]
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AC^0^ - Unbounded Fanin Constant-Depth Circuits =

----
CategoryClassical 

== Description ==

{{{#!description

An especially important subclass of [[Class_AC|$\\text{AC}$]], corresponding to constant-depth, unbounded-fanin, polynomial-size circuits with AND, OR, and NOT gates.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Computing the Parity or Majority of n bits is not in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] [[ZooRefs#FSS84|[FSS84] ]].



There are functions in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] that are pseudorandom for all statistical tests in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] [[ZooRefs#NW94|[NW94] ]].  But there are no functions in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] that are pseudorandom for all statistical tests in [[Class_QP|$\\text{QP}$]] (quasipolynomial time) [[ZooRefs#LMN93|[LMN93] ]].



[[ZooRefs#LMN93|[LMN93] ]] showed furthermore that functions with [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] circuits of depth d are learnable in [[Class_QP|$\\text{QP}$]], given their outputs on O(2^log(n)^O(d)^) randomly chosen inputs.  On the other hand, this learning algorithm is essentially optimal, unless there is a 2^n^o(1)^ algorithm for factoring [[ZooRefs#Kha93|[Kha93] ]].



Although there are no good pseudorandom functions in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]], [[ZooRefs#IN96|[IN96] ]] showed that there are pseudorandom generators that stretch n bits to n+Θ(log n), assuming the hardness of a problem based on subset sum.



[[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] contains [[Class_NC0|$\\text{NC}^\\text{0}\\text{}$]], and is contained in [[Class_QACf0|$\\text{QAC}_\\text{f}\\text{}^\\text{0}\\text{}$]] and [[Class_MAC0|$\\text{MAC}^\\text{0}\\text{}$]].



In descriptive complexity, uniform [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] can be characterized as the class of problems expressible by first-order predicates with addition and multiplication operators - or indeed, with ordering and multiplication, or ordering and division (see [[ZooRefs#Lee02|[Lee02] ]]). So it's equivalent to the class [[Class_FO|$\\text{FO}$]] and to [[Class_AL|$\\text{AL}$]] the alternating logtime hierarchy.



[[ZooRefs#BLM+98|[BLM+98] ]] showed the following problem is complete for depth-k [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] circuits (with a uniformity condition):



Given a grid graph of polynomial length and width k, decide whether there is a path between vertices s and t (which can be given as part of the input).



Computing the parity or majority of n bits is not in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] [[ZooRefs#FSS84|[FSS84] ]].



Although there are no good pseudorandom functions in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]], [[ZooRefs#IN96|[IN96] ]] showed that there are pseudorandom generators in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] that stretch n bits to n+Θ(log n), assuming the hardness of a problem based on subset sum. Work of [[ZooRefs#AIK04|[AIK04] ]] shows pseudorandom generators in [[Class_NC0|$\\text{NC}^\\text{0}\\text{}$]] under more relaxed assumptions.



[[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] contains [[Class_NC0|$\\text{NC}^\\text{0}\\text{}$]], and is contained in [[Class_QAC0|$\\text{QAC}^\\text{0}\\text{}$]] and [[Class_MAC0|$\\text{MAC}^\\text{0}\\text{}$]].



In descriptive complexity, uniform [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] can be characterized as the class of problems expressible by first-order predicates with addition and multiplication operators - or indeed, with ordering and multiplication, or ordering and division (see [[ZooRefs#Lee02|[Lee02] ]]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AC0[m]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AC^0^[m] - AC0 With MOD m Gates =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]], but now "MOD m" gates (for a specific m) are allowed in addition to AND, OR, and NOT gates.  (A MOD m gate outputs 0 if the sum of its inputs is congruent to 0 modulo m, and 1 otherwise.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If m is a power of a prime p, then for any prime q not equal to p, deciding whether the sum of n bits is congruent to 0 modulo q is not in [[Class_AC0[m]|$\\text{AC}^\\text{0}\\text{[m]}$]] [[ZooRefs#Raz87|[Raz87] ]] [[ZooRefs#Smo87|[Smo87] ]].  It follows that, for any such m, [[Class_AC0[m]|$\\text{AC}^\\text{0}\\text{[m]}$]] is strictly contained in [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]].



However, if m is a product of distinct primes (e.g. 6), then it is not even known whether [[Class_AC0[m]|$\\text{AC}^\\text{0}\\text{[m]}$]] = NP!



See also: [[Class_QAC0[m]|$\\text{QAC}^\\text{0}\\text{[m]}$]].



However, if m is a product of distinct primes (i.e. 6), then it is not even known whether [[Class_AC0[m]|$\\text{AC}^\\text{0}\\text{[m]}$]] = NP!
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AC0[m])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AC0[m] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AC1"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AC^1^ - Unbounded Fanin Log-Depth Circuits =

----
CategoryClassical 

== Description ==

{{{#!description

See [[Class_AC|$\\text{AC}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AC1)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AC1 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ACC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ACC^0^ - AC0 With Arbitrary MOD Gates =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_AC0[m]|$\\text{AC}^\\text{0}\\text{[m]}$]], but now the constant-depth circuit can contain MOD m gates for any m.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]].



Indeed, can be simulated by depth-3 threshold circuits of quasipolynomial size [[ZooRefs#Yao90|[Yao90] ]].



According to [[ZooRefs#All96|[All96] ]], there is no good evidence for the existence of cryptographically secure functions in [[Class_ACC0|$\\text{ACC}^\\text{0}\\text{}$]].



There is no non-uniform [[Class_ACC0|$\\text{ACC}^\\text{0}\\text{}$]] circuits of polynomial size for NTIMES[2^n^] and no [[Class_ACC0|$\\text{ACC}^\\text{0}\\text{}$]] circuit of size 2^n^O(1)^^ for E^NP^ (The class [[Class_E|$\\text{E}$]] with an [[Class_NP|$\\text{NP}$]] oracle). These are the only two known nontrivial lower bounds against [[Class_ACC0|$\\text{ACC}^\\text{0}\\text{}$]] and were recently discovered by [[ZooRefs#Wil11|[Wil11] ]].



Contains 4-PBP [[ZooRefs#BT88|[BT88] ]].



See also: [[Class_QACC0|$\\text{QACC}^\\text{0}\\text{}$]].



In 1996, [[ZooRefs#All96|[All96] ]] suggested the existence of cryptographically secure functions in [[Class_ACC0|$\\text{ACC}^\\text{0}\\text{}$]] as an important open question. In 2004, work of [[ZooRefs#AIK04|[AIK04] ]] showed pseudorandom generators in [[Class_NC0|$\\text{NC}^\\text{0}\\text{}$]] based on widely-believed assumptions.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ACC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ACC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AH"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AH - Arithmetic Hierarchy =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

The analog of [[Class_PH|$\\text{PH}$]] in computability theory.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Let Δ,,0,, = Σ,,0,, = Π,,0,, = [[Class_R|$\\text{R}$]].  Then for i>0, let



Δ,,i,, = [[Class_R|$\\text{R}$]] with Σ,,i-1,, oracle.

Σ,,i,, = [[Class_RE|$\\text{RE}$]] with Σ,,i-1,, oracle.

Π,,i,, = [[Class_coRE|$\\text{coRE}$]] with Σ,,i-1,, oracle.



Then [[Class_AH|$\\text{AH}$]] is the union of these classes for all nonnegative constant i.



Each level of [[Class_AH|$\\text{AH}$]] strictly contains the levels below it.



An equivalent definition is: $\\Sigma_0=\\Delta_0=\\Pi_0$ is the set of numbers decided by formula with one free variable and bounded quantifier, where the primitives are + and $\\times$. A bounded quantifier is of the form $ \\phi=\\forall i<j \\psi $ or $\\phi=\\exists i<j  \\psi$ where  $j$ is considered to be free in $\\phi$. Then $\\Sigma_{i+1}$ is the sets of number validating a formula of the form $\\exists X_1\\dots\\exists X_n,\\psi$ with $\\psi\\in\\Delta_i$. $\\Delta_i$ is the set of formula who are negation of $\\Sigma_i$ formula. $\\Pi_i=\\Sigma_i\\cap\\Delta_i$
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AH)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AH because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AL - Alternating L =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_AP|$\\text{AP}$]], but for logarithmic-space instead of polynomial-time.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_AL|$\\text{AL}$]] = [[Class_P|$\\text{P}$]] [[ZooRefs#CKS81|[CKS81] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ALL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ALL - The Class of All Languages =

----
CategoryClassical 

== Description ==

{{{#!description

Literally, the class of [[Class_ALL|$\\text{ALL}$]] languages.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_ALL|$\\text{ALL}$]] is a gargantuan beast that's been wreaking havoc in the Zoo of late.



First [Aar04b] observed that PP/rpoly ([[Class_PP|$\\text{PP}$]] with polynomial-size randomized advice) equals [[Class_ALL|$\\text{ALL}$]], as does PostBQP/qpoly ([[Class_PostBQP|$\\text{PostBQP}$]] with polynomial-size quantum advice).



Then [[ZooRefs#Raz05|[Raz05] ]] showed that QIP/qpoly, and even IP(2)/rpoly, equal [[Class_ALL|$\\text{ALL}$]].



Nor is it hard to show that MA,,EXP,,/rpoly = [[Class_ALL|$\\text{ALL}$]].



On the other hand, even though [[Class_PSPACE|$\\text{PSPACE}$]] contains [[Class_PP|$\\text{PP}$]], and [[Class_EXPSPACE|$\\text{EXPSPACE}$]] contains [[Class_MAEXP|$\\text{MA}_\\text{EXP}\\text{}$]], it's easy to see that PSPACE/rpoly = [[Class_PSPACE/poly|$\\text{PSPACE/poly}$]] and EXPSPACE/rpoly = EXPSPACE/poly are not [[Class_ALL|$\\text{ALL}$]].



So does [[Class_ALL|$\\text{ALL}$]] have no respect for complexity class inclusions at ALL?  (Sorry.)



It is not as contradictory as it first seems.  The deterministic base class in all of these examples is modified by computational non-determinism after it is modified by advice.  For example, MA,,EXP,,/rpoly means M(A,,EXP,,/rpoly), while (MA,,EXP,,)/rpoly equals MA,,EXP,,/poly by a standard argument.  In other words, it's only the verifier, not the prover or post-selector, who receives the randomized or quantum advice. The prover knows a description of the advice state, but not its measured values.  Modification by /rpoly does preserve class inclusions when it is applied after other changes.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ALL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ALL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ALOGTIME"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ALOGTIME - Logarithmic time alternating RAM =

----
CategoryClassical 

== Description ==

{{{#!description

[[Class_ALOGTIME|$\\text{ALOGTIME}$]] is the class of languages decidable in logarithmic time by a random access alternating Turing machine.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Known to be equal to U,,E^*^,,-uniform [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ALOGTIME)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ALOGTIME because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AM"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AM - Arthur-Merlin =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which a "yes" answer can be verified by an Arthur-Merlin protocol, as follows.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Arthur, a [[Class_BPP|$\\text{BPP}$]] (i.e. probabilistic polynomial-time) verifier, generates a "challenge" based on the input, and sends it together with his random coins to Merlin.  Merlin sends back a response, and then Arthur decides whether to accept.  Given an algorithm for Arthur, we require that



If the answer is "yes," then Merlin can act in such a way that Arthur accepts with probability at least 2/3 (over the choice of Arthur's random bits).

If the answer is "no," then however Merlin acts, Arthur will reject with probability at least 2/3.



Surprisingly, it turns out that such a system is just as powerful as a private-coin one, in which Arthur does not need to send his random coins to Merlin [[ZooRefs#GS86|[GS86] ]].  So, Arthur never needs to hide information from Merlin.



Furthermore, define AM[k] similarly to [[Class_AM|$\\text{AM}$]], except that Arthur and Merlin have k rounds of interaction.  Then for all constant k>2, AM[k] = AM[2] = [[Class_AM|$\\text{AM}$]] [[ZooRefs#BM88|[BM88] ]].  Also, the result of [[ZooRefs#GS86|[GS86] ]] can then be stated as follows: IP[k] is contained in AM[k+2] for every k (constant or non-constant).



[[Class_AM|$\\text{AM}$]] contains graph nonisomorphism.



Contains [[Class_NP|$\\text{NP}$]], [[Class_BPP|$\\text{BPP}$]], and [[Class_SZK|$\\text{SZK}$]], and is contained in [[Class_Π2P|$\\text{Π}_\\text{2}\\text{P}$]] and [[Class_NP/poly|$\\text{NP/poly}$]].



If [[Class_AM|$\\text{AM}$]] contains [[Class_coNP|$\\text{coNP}$]] then [[Class_PH|$\\text{PH}$]] collapses to [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] ∩ [[Class_Π2P|$\\text{Π}_\\text{2}\\text{P}$]] [[ZooRefs#BHZ87|[BHZ87] ]].



There exists an oracle relative to which [[Class_AM|$\\text{AM}$]] is not contained in [[Class_PP|$\\text{PP}$]] [[ZooRefs#Ver92|[Ver92] ]].



[[Class_AM|$\\text{AM}$]] = [[Class_NP|$\\text{NP}$]] under a strong derandomization assumption: namely that some language in [[Class_NE|$\\text{NE}$]] ∩ [[Class_coNE|$\\text{coNE}$]] requires nondeterministic circuits of size 2^Ω(n)^ ([[ZooRefs#MV99|[MV99] ]], improving [[ZooRefs#KM99|[KM99] ]]).  (A nondeterministic circuit C has two inputs, x and y, and accepts on x if there exists a y such that C(x,y)=1.)
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AM)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AM because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AM ∩ coAM"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AM ∩ coAM - AM ∩ coAM =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which both "yes" and "no" answers can be verified by an [[Class_AM|$\\text{AM}$]] protocol.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If [[Class_EXP|$\\text{EXP}$]] requires exponential time even for [[Class_AM|$\\text{AM}$]] protocols, then [[Class_AM|$\\text{AM}$]] ∩ [[Class_coAM|$\\text{coAM}$]] = [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]] [[ZooRefs#GST03|[GST03] ]].



There exists an oracle relative to which [[Class_AM|$\\text{AM}$]] ∩ [[Class_coAM|$\\text{coAM}$]] is not contained in [[Class_PP|$\\text{PP}$]] [[ZooRefs#Ver95|[Ver95] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AM ∩ coAM)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AM ∩ coAM because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AMEXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AM,,EXP,, - Exponential-Time AM =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_AM|$\\text{AM}$]], except that Arthur is exponential-time and can exchange exponentially long messages with Merlin.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_MAEXP|$\\text{MA}_\\text{EXP}\\text{}$]], and is contained in [[Class_EH|$\\text{EH}$]] and indeed [[Class_S2-EXP•PNP|$\\text{S}_\\text{2}\\text{-EXP•P}^\\text{NP}\\text{}$]].



If [[Class_coNP|$\\text{coNP}$]] is contained in [[Class_AM[polylog]|$\\text{AM[polylog]}$]] then [[Class_EH|$\\text{EH}$]] collapses to [[Class_AMEXP|$\\text{AM}_\\text{EXP}\\text{}$]] [[ZooRefs#PV04|[PV04] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AMEXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AMEXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AM[polylog]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AM[polylog] - AM With Polylog Rounds =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_AM|$\\text{AM}$]], except that we allow polylog(n) rounds of interaction between Arthur and Merlin instead of a constant number.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Not much is known about [[Class_AM[polylog]|$\\text{AM[polylog]}$]] -- for example, whether it sits in [[Class_PH|$\\text{PH}$]].  However, [[ZooRefs#SS04|[SS04] ]] show that if [[Class_AM[polylog]|$\\text{AM[polylog]}$]] contains [[Class_coNP|$\\text{coNP}$]], then [[Class_EH|$\\text{EH}$]] collapses to [[Class_S2-EXP•PNP|$\\text{S}_\\text{2}\\text{-EXP•P}^\\text{NP}\\text{}$]].  ([[ZooRefs#PV04|[PV04] ]] improved the collapse to [[Class_AMEXP|$\\text{AM}_\\text{EXP}\\text{}$]].)
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AM[polylog])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AM[polylog] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AP - Alternating P =

----
CategoryClassical 

== Description ==

{{{#!description

An alternating Turing machine is a nondeterministic machine with two kinds of states, AND states and OR states.  It accepts if and only if the tree of all computation paths, considered as an AND-OR tree, evaluates to 1.  (Here 'Accept' corresponds to 1 and 'Reject' to 0.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Then [[Class_AP|$\\text{AP}$]] is the class of decision problems solvable in polynomial time by an alternating Turing machine.



[[Class_AP|$\\text{AP}$]] = [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#CKS81|[CKS81] ]].



The abbreviation [[Class_AP|$\\text{AP}$]] is also used for Approximable in Polynomial Time, see [[Class_AxP|$\\text{AxP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_APP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= APP - Amplified PP =

----
CategoryClassical 

== Description ==

{{{#!description

Roughly, the class of decision problems for which the following holds.  For all polynomials p(n), there exist [[Class_GapP|$\\text{GapP}$]] functions f and g such that for all inputs x with n=|x|,}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes" then 1 > f(x)/g(1^n^) > 1-2^-p(n)^.

If the answer is "no" then 0 < f(x)/g(1^n^) < 2^-p(n)^.



Defined in [[ZooRefs#Li93|[Li93] ]], where the following was also shown:



[[Class_APP|$\\text{APP}$]] is contained in [[Class_PP|$\\text{PP}$]], and indeed is low for [[Class_PP|$\\text{PP}$]].

[[Class_APP|$\\text{APP}$]] is closed under intersection, union, and complement.



[[Class_APP|$\\text{APP}$]] contains [[Class_AWPP|$\\text{AWPP}$]] [[ZooRefs#Fen02|[Fen02] ]].



The abbreviation [[Class_APP|$\\text{APP}$]] is also used for Approximable in Probabilistic Polynomial Time, see [[Class_AxPP|$\\text{AxPP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_APP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save APP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_APX"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= APX - Approximable =

----
CategoryClassical 

== Description ==

{{{#!description

The subclass of [[Class_NPO|$\\text{NPO}$]] problems that admit constant-factor approximation algorithms.  (I.e., there is a polynomial-time algorithm that is guaranteed to find a solution within a constant factor of the optimum cost.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_PTAS|$\\text{PTAS}$]].



Equals the closure of [[Class_MaxSNP|$\\text{MaxSNP}$]] and of [[Class_MaxNP|$\\text{MaxNP}$]] under [[Class_PTAS|$\\text{PTAS}$]] reduction [[ZooRefs#KMS+99|[KMS+99] ]], [[ZooRefs#CT94|[CT94] ]].



Defined in [[ZooRefs#ACG+99|[ACG+99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_APX)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save APX because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ATIME"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ATIME - Alternating TIME =

----
CategoryClassical 

== Description ==

{{{#!description

ATIME(f(n)) is the class of problems for which there are alternating Turing machines (see [[Class_AP|$\\text{AP}$]]) which decide the problem in time bounded by f(n).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



In particular, [[Class_AP|$\\text{AP}$]] = ATIME(poly(n)).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ATIME)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ATIME because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AUC-SPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AUC-SPACE(f(n)) - Randomized Alternating f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems decidable by an O(f(n))-space Turing machine with three kinds of quantifiers: existential, universal, and randomized.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains GAN-SPACE(f(n)).



AUC-SPACE(poly(n)) = [[Class_SAPTIME|$\\text{SAPTIME}$]] = [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#Pap83|[Pap83] ]].



[[ZooRefs#Con92|[Con92] ]] shows that AUC-SPACE(log n) has a natural complete problem, and is contained in [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AUC-SPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AUC-SPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AVBPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AVBPP - Average-Case BPP =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#OW93|[OW93] ]] to be the class of decision problems that have a good average-case [[Class_BPP|$\\text{BPP}$]] algorithm, whenever the input is chosen from an efficiently samplable distribution.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Note that this is not the same as the [[Class_BPP|$\\text{BPP}$]] version of [[Class_AvgP|$\\text{AvgP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AVBPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AVBPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AWPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AWPP - Almost WPP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that for some polynomial-time computable (i.e. [[Class_FP|$\\text{FP}$]]) function f,}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "no," then the difference between the number of accepting and rejecting paths is non-negative and at most 2^-poly(n)^f(x).

If the answer is "yes," then the difference is between (1-2^-poly(n)^)f(x) and f(x).



Defined in [[ZooRefs#FFK94|[FFK94] ]].



Contains [[Class_BQP|$\\text{BQP}$]] [[ZooRefs#FR98|[FR98] ]], [[Class_WAPP|$\\text{WAPP}$]] [[ZooRefs#BGM02|[BGM02] ]], [[Class_LWPP|$\\text{LWPP}$]], and [[Class_WPP|$\\text{WPP}$]].



Contained in [[Class_APP|$\\text{APP}$]] [[ZooRefs#Fen02|[Fen02] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AWPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AWPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AW[*]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AW[*] - Alternating W[*] =

----
CategoryClassical 

== Description ==

{{{#!description

The union of [[Class_AW[t]|$\\text{AW[t]}$]] over all t.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AW[*])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AW[*] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AW[P]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AW[P] - Alternating W[P] =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_AW[SAT]|$\\text{AW[SAT]}$]] but with 'circuit' instead of 'formula.'}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Has the same relation to [[Class_AW[SAT]|$\\text{AW[SAT]}$]] as [[Class_W[P]|$\\text{W[P]}$]] has to [[Class_W[SAT]|$\\text{W[SAT]}$]].



Defined in [[ZooRefs#DF99|[DF99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AW[P])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AW[P] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AW[SAT]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AW[SAT] - Alternating W[SAT] =

----
CategoryClassical 

== Description ==

{{{#!description

Basically has the same relation to [[Class_W[SAT]|$\\text{W[SAT]}$]] as [[Class_PSPACE|$\\text{PSPACE}$]] does to [[Class_NP|$\\text{NP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of decision problems of the form (x,r,k,,1,,,...,k,,r,,) (r,k,,1,,,...,k,,r,, parameters), that are fixed-parameter reducible to the following problem, for some constant h:



Parameterized QBFSAT: Given a Boolean formula F (with no restriction on depth), over disjoint variable sets S,,1,,,...,S,,r,,.  Does there exist an assignment to S,,1,, of Hamming weight k,,1,,, such that for all assignments to S,,2,, of Hamming weight k,,2,,, etc. (alternating 'there exists' and 'for all'), F is satisfied?



See [[Class_W[1]|$\\text{W[1]}$]] for the definition of fixed-parameter reducibility.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contains [[Class_AW[*]|$\\text{AW[*]}$]], and is contained in [[Class_AW[P]|$\\text{AW[P]}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AW[SAT])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AW[SAT] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AW[t]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AW[t] - Alternating W[t] =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_W[t]|$\\text{W[t]}$]] as [[Class_PSPACE|$\\text{PSPACE}$]] does to [[Class_NP|$\\text{NP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Same as [[Class_AW[SAT]|$\\text{AW[SAT]}$]], except that the formula F can have depth at most t.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contained in [[Class_AW[*]|$\\text{AW[*]}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AW[t])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AW[t] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AlgP/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AlgP/poly - Polynomial-Size Algebraic Circuits =

----
CategoryClassical 

== Description ==

{{{#!description

The class of multivariate polynomials over the integers that can be evaluated using a polynomial (in the input size n) number of additions, subtractions, and multiplications, together with the constants -1 and 1.  The class is nonuniform, in the sense that the polynomial for each input size n can be completely different.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Named in [[ZooRefs#Imp02|[Imp02] ]], though it has been considered since the 1970's.



If [[Class_P|$\\text{P}$]] = [[Class_BPP|$\\text{BPP}$]] (or even [[Class_BPP|$\\text{BPP}$]] is contained in [[Class_NE|$\\text{NE}$]]), then either [[Class_NEXP|$\\text{NEXP}$]] is not in [[Class_P/poly|$\\text{P/poly}$]], or else the permanent polynomial of a matrix is not in [[Class_AlgP/poly|$\\text{AlgP/poly}$]] [[ZooRefs#KI02|[KI02] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AlgP/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AlgP/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Almost-NP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Almost-NP - Languages Almost Surely in NPA =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems that are in NP^A^ with probability 1, where A is an oracle chosen uniformly at random.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_AM|$\\text{AM}$]] [[ZooRefs#NW94|[NW94] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Almost-NP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Almost-NP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Almost-P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Almost-P - Languages Almost Surely in PA =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems that are in P^A^ with probability 1, where A is an oracle chosen uniformly at random.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#BG81|[BG81] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Almost-P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Almost-P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Almost-PSPACE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Almost-PSPACE - Languages Almost Surely in PSPACEA =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems that are in PSPACE^A^ with probability 1, where A is an oracle chosen uniformly at random.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_Almost-PSPACE|$\\text{Almost-PSPACE}$]] is not known to equal [[Class_PSPACE|$\\text{PSPACE}$]] -- rather surprisingly, given the fact that [[Class_PSPACE|$\\text{PSPACE}$]] equals BPPSPACE and even [[Class_PPSPACE|$\\text{PPSPACE}$]].



What's known is that [[Class_Almost-PSPACE|$\\text{Almost-PSPACE}$]] = BP^exp^•PSPACE, where BP^exp^• is like the BP• operator but with exponentially-long strings [[ZooRefs#BVW98|[BVW98] ]].  It follows that [[Class_Almost-PSPACE|$\\text{Almost-PSPACE}$]] is contained in NEXP^NP^ ∩ coNEXP^NP^.



Whereas both BP^exp^•PSPACE and BPPSPACE machines are allowed exponentially many random bits, the former has a reusable record of all of these bits on a witness tape, while the latter can only preserve a fraction of them on the work tape.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Almost-PSPACE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Almost-PSPACE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AmpMP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AmpMP - Amplifiable MP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems such that for some [[Class_SharpP|$\\text{#P}$]] function f(x,0^m^),}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The answer on input x is 'yes' if and only if the middle bit of f(x) is 1.

The m bits of f(x) to the left and right of the middle bit are all 0.



Defined in [[ZooRefs#GKR+95|[GKR+95] ]].



Contains [[Class_PH|$\\text{PH}$]] and Contained in [[Class_MP|$\\text{MP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AmpMP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AmpMP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AmpP-BQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AmpP-BQP - BQP Restricted To AmpP States =

----
CategoryClassical 

== Description ==

{{{#!description

Similar to [[Class_TreeBQP|$\\text{TreeBQP}$]] except that the quantum computer's state at each time step is restricted to being exponentially close to a state in AmpP (that is, a state for which the amplitudes are computable by a classical polynomial-size circuit).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [Aar03b], where it was also observed that [[Class_AmpP-BQP|$\\text{AmpP-BQP}$]] is contained in the third level of [[Class_PH|$\\text{PH}$]], just as [[Class_TreeBQP|$\\text{TreeBQP}$]] is.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AmpP-BQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AmpP-BQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AuxPDA"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AuxPDA - Auxiliary Pushdown Automata =

----
CategoryClassical 

== Description ==

{{{#!description

Equivalent to [[Class_NAuxPDAp|$\\text{NAuxPDA}^\\text{p}\\text{}$]] without the running-time restriction.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_P|$\\text{P}$]] [Coo71b].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AuxPDA)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AuxPDA because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AvgE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AvgE - Average Exponential-Time With Linear Exponent =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_E|$\\text{E}$]] as [[Class_AvgP|$\\text{AvgP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AvgE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AvgE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AvgP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AvgP - Average Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

A distributional problem consists of a decision problem A, and a probability distribution μ over problem instances.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A function f, from strings to integers, is polynomial on μ-average if there exists a constant ε>0 such that the expectation of f^ε^(x) is finite, when x is drawn from μ.



Then (A,μ) is in [[Class_AvgP|$\\text{AvgP}$]] if there is an algorithm for A whose running time is polynomial on μ-average.



This convoluted definition is due to Levin [[ZooRefs#Lev86|[Lev86] ]], who realized that simpler definitions lead to classes that fail to satisfy basic closure properties.  Also see [[ZooRefs#Gol97|[Gol97] ]] for more information.



If [[Class_AvgP|$\\text{AvgP}$]] = [[Class_DistNP|$\\text{DistNP}$]] then [[Class_EXP|$\\text{EXP}$]] = [[Class_NEXP|$\\text{NEXP}$]] [[ZooRefs#BCG+92|[BCG+92] ]].



Strictly contained in [[Class_HeurP|$\\text{HeurP}$]] [[ZooRefs#NS05|[NS05] ]].



See also: (NP,P-samplable).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AvgP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AvgP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AxP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AxP - Approximable in Polynomial Time =

----
CategoryClassical 

== Description ==

{{{#!description

Usually called [[Class_AP|$\\text{AP}$]] in the literature.  I've renamed it [[Class_AxP|$\\text{AxP}$]] to distinguish it from the "other" [[Class_AP|$\\text{AP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of real-valued functions from {0,1}^n^ to [0,1] that can be approximated within any ε>0 by a deterministic Turing machine in time polynomial in n and 1/ε.



Defined by [[ZooRefs#KRC00|[KRC00] ]], who also showed that the set of [[Class_AxP|$\\text{AxP}$]] machines is in [[Class_RE|$\\text{RE}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AxP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AxP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_AxPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= AxPP - Approximable in Probabilistic Polynomial Time =

----
CategoryClassical 

== Description ==

{{{#!description

Usually called [[Class_APP|$\\text{APP}$]].  I've renamed it [[Class_AxPP|$\\text{AxPP}$]] to distinguish it from the "other" [[Class_APP|$\\text{APP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of real-valued functions from {0,1}^n^ to [0,1] that can be approximated within any ε>0 by a probabilistic Turing machine in time polynomial in n and 1/ε.



Defined by [[ZooRefs#KRC00|[KRC00] ]], who also show the following:



Approximating the acceptance probability of a Boolean circuit is AxPP-complete.  The authors argue that this makes [[Class_AxPP|$\\text{AxPP}$]] a more natural class than [[Class_BPP|$\\text{BPP}$]], since the latter is not believed to have complete problems.

If [[Class_AxPP|$\\text{AxPP}$]] = [[Class_AxP|$\\text{AxP}$]], then [[Class_BPP|$\\text{BPP}$]] = [[Class_P|$\\text{P}$]].

On the other hand, there exists an oracle relative to which [[Class_BPP|$\\text{BPP}$]] = [[Class_P|$\\text{P}$]] but [[Class_AxPP|$\\text{AxPP}$]] does not equal [[Class_AxP|$\\text{AxP}$]].



[[Class_AxPP|$\\text{AxPP}$]] is recursively enumerable [Jeř07].



Interestingly, it is unclear whether the set of [[Class_AxPP|$\\text{AxPP}$]] machines is in [[Class_RE|$\\text{RE}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_AxPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save AxPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BH"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BH - Boolean Hierarchy Over NP =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

The smallest class that contains [[Class_NP|$\\text{NP}$]] and is closed under union, intersection, and complement.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The levels are defined as follows:



BH,,1,, = [[Class_NP|$\\text{NP}$]].

BH,,2i,, is the class of languages that are the intersection of a BH,,2i-1,, language with a [[Class_coNP|$\\text{coNP}$]] language.

BH,,2i+1,, is the class of languages that are the union of a BH,,2i,, language with an [[Class_NP|$\\text{NP}$]] language.



Then [[Class_BH|$\\text{BH}$]] is the union over all i of BH,,i,,.



Defined in [[ZooRefs#WW85|[WW85] ]].



For more detail see [[ZooRefs#CGH+88|[CGH+88] ]].



Contained in [[Class_Δ2P|$\\text{Δ}_\\text{2}\\text{P}$]] and indeed in [[Class_PNP[log]|$\\text{P}^\\text{NP[log]}\\text{}$]].



If [[Class_BH|$\\text{BH}$]] collapses at any level, then [[Class_PH|$\\text{PH}$]] collapses to Σ,,3,,P [[ZooRefs#Kad88|[Kad88] ]].



See also: [[Class_DP|$\\text{DP}$]], [[Class_QH|$\\text{QH}$]].



See also: [[Class_QH|$\\text{QH}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BH)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BH because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPE - Bounded-Error Probabilistic E =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_E|$\\text{E}$]] as [[Class_BPP|$\\text{BPP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_EE|$\\text{EE}$]] = [[Class_BPE|$\\text{BPE}$]] if and only if [[Class_EXP|$\\text{EXP}$]] = [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#IKW01|[IKW01] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPEE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPEE - Bounded-Error Probabilistic EE =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_EE|$\\text{EE}$]] as [[Class_BPP|$\\text{BPP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPEE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPEE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPHSPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BP,,H,,SPACE(f(n)) - Bounded-Error Halting Probabilistic f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable in O(f(n))-space with error probability at most 1/3, by a Turing machine that halts on every input and every random tape setting.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains R,,H,,SPACE(f(n)).



Is contained in DSPACE(f(n)^3/2^) [[ZooRefs#SZ95|[SZ95] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPHSPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPHSPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPL - Bounded-Error Probabilistic L =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_BPP|$\\text{BPP}$]] does to [[Class_P|$\\text{P}$]].  The Turing machine has to halt with probability 1 on every input.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_SC|$\\text{SC}$]] [[ZooRefs#Nis92|[Nis92] ]] and in [[Class_PL|$\\text{PL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP - Bounded-Error Probabilistic Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'yes' then at least 2/3 of the computation paths accept.

If the answer is 'no' then at most 1/3 of the computation paths accept.



(Here all computation paths have the same length.)



Often identified as the class of feasible problems for a computer with access to a genuine random-number source.



Defined in [[ZooRefs#Gil77|[Gil77] ]].



Contained in [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] ∩ [[Class_Π2P|$\\text{Π}_\\text{2}\\text{P}$]] [[ZooRefs#Lau83|[Lau83] ]], and indeed in ZPP^NP^ [[ZooRefs#GZ97|[GZ97] ]].



If [[Class_BPP|$\\text{BPP}$]] contains [[Class_NP|$\\text{NP}$]], then [[Class_RP|$\\text{RP}$]] = [[Class_NP|$\\text{NP}$]] [Ko82,Gil77] and [[Class_PH|$\\text{PH}$]] is contained in [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#Zac88|[Zac88] ]].



If any problem in [[Class_E|$\\text{E}$]] requires circuits of size 2^Ω(n)^, then [[Class_BPP|$\\text{BPP}$]] = [[Class_P|$\\text{P}$]] [[ZooRefs#IW97|[IW97] ]] (in other words, [[Class_BPP|$\\text{BPP}$]] can be derandomized).



Indeed, any proof that [[Class_BPP|$\\text{BPP}$]] = [[Class_P|$\\text{P}$]] requires showing either that [[Class_NEXP|$\\text{NEXP}$]] is not in [[Class_P/poly|$\\text{P/poly}$]], or else that [[Class_SharpP|$\\text{#P}$]] requires superpolynomial-size arithmetic circuits [[ZooRefs#KI02|[KI02] ]].



[[Class_BPP|$\\text{BPP}$]] is not known to contain complete problems.  [[ZooRefs#Sip82|[Sip82] ]], [[ZooRefs#HH86|[HH86] ]] give oracles relative to which [[Class_BPP|$\\text{BPP}$]] has no complete problems.



There exist oracles relative to which [[Class_P|$\\text{P}$]] = [[Class_RP|$\\text{RP}$]] but still [[Class_P|$\\text{P}$]] is not equal to [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#BF99|[BF99] ]].



In contrast to the case of [[Class_P|$\\text{P}$]], it is unknown whether [[Class_BPP|$\\text{BPP}$]] collapses to BPTIME(n^c^) for some fixed constant c.  However, [[ZooRefs#Bar02|[Bar02] ]] and [[ZooRefs#FS04|[FS04] ]] have shown hierarchy theorems for [[Class_BPP|$\\text{BPP}$]] with a small amount of advice.



A zero-one law exists stating that [[Class_BPP|$\\text{BPP}$]] has p-measure zero unless [[Class_BPP|$\\text{BPP}$]] = [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#Mel00|[Mel00] ]].



Equals [[Class_Almost-P|$\\text{Almost-P}$]].



See also: [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]].



If [[Class_BPP|$\\text{BPP}$]] contains [[Class_NP|$\\text{NP}$]], then [[Class_RP|$\\text{RP}$]] = [[Class_NP|$\\text{NP}$]] [[ZooRefs#Ko82|[Ko82] ]] and [[Class_PH|$\\text{PH}$]] is contained in [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#Zac88|[Zac88] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPP-OBDD"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP-OBDD - Polynomial-Size Bounded-Error Ordered Binary Decision Diagram =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_P-OBDD|$\\text{P-OBDD}$]], except that probabilistic transitions are allowed and the OBDD need only accept with probability at least 2/3.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Does not contain the integer multiplication problem [[ZooRefs#AK96|[AK96] ]].



Strictly contained in [[Class_BQP-OBDD|$\\text{BQP-OBDD}$]] [[ZooRefs#NHK00|[NHK00] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPP-OBDD)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPP-OBDD because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPP//log"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP//log - BPP With Logarithmic Randomness-Dependent Advice =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by a [[Class_BPP|$\\text{BPP}$]] machine that is given O(log n) advice bits, which can depend on both the machine's random coin flips and the input length n, but not on the input itself.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#TV02|[TV02] ]], where it was also shown that if [[Class_EXP|$\\text{EXP}$]] is in [[Class_BPP//log|$\\text{BPP//log}$]] then

[[Class_EXP|$\\text{EXP}$]] = [[Class_BPP|$\\text{BPP}$]], and if [[Class_PSPACE|$\\text{PSPACE}$]] is in [[Class_BPP//log|$\\text{BPP//log}$]] then [[Class_PSPACE|$\\text{PSPACE}$]] = [[Class_BPP|$\\text{BPP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPP//log)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPP//log because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPP/log"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP/log - BPP With Logarithmic Karp-Lipton Advice =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by a semantic [[Class_BPP|$\\text{BPP}$]] machine with O(log n) advice bits that depend only on the input length n.  If the advice is good, the output must be correct with probability at least 2/3.  If it is bad, the machine must provide some answer with probability at least 2/3.  See the discussion for [[Class_BQP/poly|$\\text{BQP/poly}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_BPP/mlog|$\\text{BPP/mlog}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPP/log)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPP/log because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPP/mlog"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP/mlog - BPP With Logarithmic Deterministic Merlin-Like Advice =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by a syntactic [[Class_BPP|$\\text{BPP}$]] machine with O(log n) advice bits that depend only on the input length n.  If the advice is good, the output must be correct with probability at least 2/3.  If it is bad, it need not be.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_BPP/rlog|$\\text{BPP/rlog}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPP/mlog)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPP/mlog because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPP/rlog"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP/rlog - BPP With Logarithmic Deterministic Merlin-Like Advice =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by a syntactic [[Class_BPP|$\\text{BPP}$]] machine with O(log n) random advice bits whose probability distribution depends only on the input length n.  For each n, there exists good advice such that the output is correct with probability at least 2/3.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_BPP/mlog|$\\text{BPP/mlog}$]].  The inclusion is strict, because [[Class_BPP/rlog|$\\text{BPP/rlog}$]] contains any finitely sparse language by fingerprinting; see the discussion for [[Class_ALL|$\\text{ALL}$]].



Contained in [[Class_BPP//log|$\\text{BPP//log}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPP/rlog)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPP/rlog because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPPKT"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP^KT^ - BPP With Time-Bounded Kolmogorov Complexity Oracle =

----
CategoryClassical 

== Description ==

{{{#!description

[[Class_BPP|$\\text{BPP}$]] with an oracle that, given a string x, returns the minimum over all programs [[Class_P|$\\text{P}$]] that output x,,i,, on input i, of the length of [[Class_P|$\\text{P}$]] plus the maximum time taken by [[Class_P|$\\text{P}$]] on any input.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A similar class was defined in [[ZooRefs#ABK+02|[ABK+02] ]], where it was also shown that in [[Class_BPPKT|$\\text{BPP}^\\text{KT}\\text{}$]] one can factor, compute discrete logarithms, and more generally invert any one-way function on a non-negligible fraction of inputs.



See also: [[Class_PK|$\\text{P}^\\text{K}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPPKT)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPPKT because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPPcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP^cc^ - Communication Complexity BPP =

----
CategoryClassical 

== Description ==

{{{#!description

The analogue of [[Class_Pcc|$\\text{P}^\\text{cc}\\text{}$]] for bounded-error probabilistic communication complexity.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Does not equal [[Class_Pcc|$\\text{P}^\\text{cc}\\text{}$]], and is not contained in [[Class_NPcc|$\\text{NP}^\\text{cc}\\text{}$]], because of the EQUALITY problem.



Defined in [[ZooRefs#BFS86|[BFS86] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPPcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPPcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPPkcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP,,k,,^cc^ - BPPcc in NOF model,  players =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_BPPcc|$\\text{BPP}^\\text{cc}\\text{}$]] and [[Class_BPP|$\\text{BPP}$]] as [[Class_Pkcc|$\\text{P}_\\text{k}\\text{}^\\text{cc}\\text{}$]] does to [[Class_Pcc|$\\text{P}^\\text{cc}\\text{}$]] and [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_NPkcc|$\\text{NP}_\\text{k}\\text{}^\\text{cc}\\text{}$]] is not contained in [[Class_BPPkcc|$\\text{BPP}_\\text{k}\\text{}^\\text{cc}\\text{}$]] for $k\\le(1-\\delta)\\cdot\\log n$ players, for any constant $\\delta>0$ [[ZooRefs#DP08|[DP08] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPPkcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPPkcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPPpath"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP,,path,, - Threshold BPP =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_BPP|$\\text{BPP}$]], except that now the computation paths need not all have the same length.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#HHT97|[HHT97] ]], where the following was also shown:



[[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] contains [[Class_MA|$\\text{MA}$]] and [[Class_PNP[log]|$\\text{P}^\\text{NP[log]}\\text{}$]], and is contained in [[Class_PP|$\\text{PP}$]] and BPP^NP^.

[[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] is closed under complementation, intersection, and union.

If [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] = BPP,,path,,^BPP,,path,,^, then [[Class_PH|$\\text{PH}$]] collapses to [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]].

If [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] contains [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]], then [[Class_PH|$\\text{PH}$]] collapses to BPP^NP^.



There exists an oracle relative to which [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] is not contained in [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] [[ZooRefs#BGM02|[BGM02] ]].



An alternate characterization of [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] uses the idea of post-selection. That is, [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] is the class of languages $L$ for which there exists a pair of polynomial-time Turing machines $A$ and $B$ such that the following conditions hold for all $x$:



If x\in [[Class_L|$\\text{L}$]], \Pr_{r\in\{0,1\}^{\mathrm{poly}(\left\vert x\right\vert)}}\left[A(x,r)\mid B(x,r)\right]\ge \frac23.

 If x\notin [[Class_L|$\\text{L}$]], \Pr_{r\in\{0,1\}^{\mathrm{poly}(\left\vert x\right\vert)}}\left[A(x,r)\mid B(x,r)\right]< \frac13.

 \Pr_{r\in\{0,1\}^{\mathrm{poly}(n)}}\left[B(x,r)\right]>0.



We say that $B$ is the post-selector. Intuitively, this characterization allows a [[Class_BPP|$\\text{BPP}$]] machine to require that its random bits have some special but easily verifiable property. This characterization makes the inclusion [[Class_NP|$\\text{NP}$]] ⊆ [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] nearly trivial.



See Also: [[Class_PostBQP|$\\text{PostBQP}$]] (quantum analogue).



[[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] contains [[Class_MA|$\\text{MA}$]] and [[Class_PNP[log]|$\\text{P}^\\text{NP[log]}\\text{}$]], and is contained in [[Class_PP|$\\text{PP}$]] and BPP^NP^.

[[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] is closed under complementation, intersection, and union.

If [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] = BPP,,path,,^BPPpath^, then [[Class_PH|$\\text{PH}$]] collapses to [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]].

If [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]] contains [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]], then [[Class_PH|$\\text{PH}$]] collapses to BPP^NP^.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPPpath)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPPpath because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPQP - Bounded-Error Probabilistic QP =

----
CategoryClassical 

== Description ==

{{{#!description

Equals BPTIME(2^O((log n)^k)^); that is, the class of problems solvable in quasipolynomial-time on a bounded-error machine.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#CNS99|[CNS99] ]], where the following was also shown:



If either (1) [[Class_SharpP|$\\text{#P}$]] does not have a subexponential-time bounded-error algorithm, or (2) [[Class_EXP|$\\text{EXP}$]] does not have subexponential-size circuits, then the [[Class_BPQP|$\\text{BPQP}$]] hierarchy is strict -- that is, for all a < b at least 1, BPTIME(2^(log n)^a^) is strictly contained in BPTIME(2^(log n)^b^).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPSPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPSPACE(f(n)) - Bounded-Error Probabilistic f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable in O(f(n))-space with error probability at most 1/3, by a Turing machine that halts with probability 1 on every input.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains RSPACE(f(n)) and BP,,H,,SPACE(f(n)).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPSPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPSPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPTIME(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPTIME(f(n)) - Bounded-Error Probabilistic f(n)-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_BPP|$\\text{BPP}$]], but with f(n)-time (for some constructible function f) rather than polynomial-time machines.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Gil77|[Gil77] ]].



BPTIME(n^log n^) does not equal BPTIME(2^n^ε^) for any ε>0 [[ZooRefs#KV88|[KV88] ]].  Proving a stronger time hierarchy theorem for BPTIME is a longstanding open problem; see [[ZooRefs#BH97|[BH97] ]] for details.



[[ZooRefs#Bar02|[Bar02] ]] has shown the following:



If we allow a small number of advice bits (say log n), then there is a strict hierarchy: for every d at least 1, BPTIME(n^d^)/(log n) does not equal BPTIME(n^d+1^)/(log n).

In the uniform setting, if [[Class_BPP|$\\text{BPP}$]] has complete problems then BPTIME(n^d^) does not equal BPTIME(n^d+1^).

BPTIME(n) does not equal [[Class_NP|$\\text{NP}$]].



Subsequently, [[ZooRefs#FS04|[FS04] ]] managed to reduce the number of advice bits to only 1: BPTIME(n^d^)/1 does not equal BPTIME(n^d+1^)/1.  They also proved a hierarchy theorem for HeurBPTIME.



For another bounded-error hierarchy result, see [[Class_BPQP|$\\text{BPQP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPTIME(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPTIME(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BPd(P)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BP,,d,,(P) - Polynomial Size d-Times-Only Branching Program =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#Weg88|[Weg88] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of decision problems solvable by a family of polynomial size branching programs, with the additional condition that each bit of the input is tested at most d times.



BP,,d,,(P) strictly contains BP,,d-1,,(P), for every d > 1 [[ZooRefs#Tha98|[Tha98] ]].



Contained in [[Class_PBP|$\\text{PBP}$]].



See also: [[Class_P-OBDD|$\\text{P-OBDD}$]], [[Class_k-PBP|$\\text{k-PBP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BPd(P))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BPd(P) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BP•NP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BP•NP - Probabilistic NP =

----
CategoryClassical 

== Description ==

{{{#!description

Equals [[Class_AM|$\\text{AM}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BP•NP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BP•NP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQNC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQNC - Alternate Name for QNC =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQNC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQNC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQNP - Alternate Name for QMA =

----
CategoryQuantum 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQP - Bounded-Error Quantum Polynomial-Time =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems solvable in polynomial time by a quantum Turing machine, with at most 1/3 probability of error.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



One can equivalently define [[Class_BQP|$\\text{BQP}$]] as the class of decision problems solvable by a uniform family of polynomial-size quantum circuits, with at most 1/3 probability of error [[ZooRefs#Yao93|[Yao93] ]].  Any universal gate set can be used as a basis; however, a technicality is that the transition amplitudes must be efficiently computable, since otherwise one could use them to encode the solutions to hard problems (see [[ZooRefs#ADH97|[ADH97] ]]).



[[Class_BQP|$\\text{BQP}$]] is often identified as the class of feasible problems for quantum computers.



Contains the factoring and discrete logarithm problems [[ZooRefs#Sho97|[Sho97] ]], the hidden Legendre symbol problem [[ZooRefs#DHI02|[DHI02] ]], the Pell's equation and principal ideal problems [[ZooRefs#Hal02|[Hal02] ]], and some other problems not thought to be in [[Class_BPP|$\\text{BPP}$]].



Defined in [[ZooRefs#BV97|[BV97] ]], where it is also shown that [[Class_BQP|$\\text{BQP}$]] contains [[Class_BPP|$\\text{BPP}$]] and is contained in [[Class_P|$\\text{P}$]] with a [[Class_SharpP|$\\text{#P}$]] oracle.



BQP^BQP^ = [[Class_BQP|$\\text{BQP}$]] [[ZooRefs#BV97|[BV97] ]].



[[ZooRefs#ADH97|[ADH97] ]] showed that [[Class_BQP|$\\text{BQP}$]] is contained in [[Class_PP|$\\text{PP}$]], and [[ZooRefs#FR98|[FR98] ]] showed that [[Class_BQP|$\\text{BQP}$]] is contained in [[Class_AWPP|$\\text{AWPP}$]].



There exist oracles relative to which:



[[Class_BQP|$\\text{BQP}$]] does not equal to [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#BV97|[BV97] ]] (and by similar arguments, is not in [[Class_P/poly|$\\text{P/poly}$]]).

[[Class_BQP|$\\text{BQP}$]] is not contained in [[Class_MA|$\\text{MA}$]] [[ZooRefs#Wat00|[Wat00] ]].

[[Class_BQP|$\\text{BQP}$]] is not contained in Mod,,p,,P for prime p [[ZooRefs#GV02|[GV02] ]].

[[Class_NP|$\\text{NP}$]], and indeed [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]], are not contained in [[Class_BQP|$\\text{BQP}$]]  with probability 1 relative to a random oracle and a random permutation oracle, respectively [[ZooRefs#BBB+97|[BBB+97] ]].

[[Class_SZK|$\\text{SZK}$]] is not contained in [[Class_BQP|$\\text{BQP}$]] [[ZooRefs#Aar02|[Aar02] ]].

[[Class_BQP|$\\text{BQP}$]] is not contained in [[Class_SZK|$\\text{SZK}$]] (follows easily using the quantum walk problem in [[ZooRefs#CCD+03|[CCD+03] ]]).

[[Class_PPAD|$\\text{PPAD}$]] is not contained in [[Class_BQP|$\\text{BQP}$]] [[ZooRefs#Li11|[Li11] ]].



[[Class_BQP|$\\text{BQP}$]] does not equal [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#BV97|[BV97] ]] (and by similar arguments, is not in [[Class_P/poly|$\\text{P/poly}$]]).

[[Class_BQP|$\\text{BQP}$]] is not contained in [[Class_MA|$\\text{MA}$]] [[ZooRefs#Wat00|[Wat00] ]].

[[Class_BQP|$\\text{BQP}$]] is not contained in Mod,,p,,P for prime p [[ZooRefs#GV02|[GV02] ]].

[[Class_NP|$\\text{NP}$]], and indeed [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]], are not contained in [[Class_BQP|$\\text{BQP}$]] (in fact, this holds with probability 1 relative to a random oracle and a random permutation oracle, respectively) [[ZooRefs#BBB+97|[BBB+97] ]].

[[Class_SZK|$\\text{SZK}$]] is not contained in [[Class_BQP|$\\text{BQP}$]] [[ZooRefs#Aar02|[Aar02] ]].

[[Class_BQP|$\\text{BQP}$]] is not contained in [[Class_SZK|$\\text{SZK}$]] (follows easily using the quantum walk problem in [[ZooRefs#CCD+03|[CCD+03] ]]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQP-OBDD"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQP-OBDD - Polynomial-Size Bounded-Error Quantum Ordered Binary Decision Diagram =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_P-OBDD|$\\text{P-OBDD}$]], except that unitary (quantum) transitions are allowed and the OBDD need only accept with probability at least 2/3.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Strictly contains [[Class_BPP-OBDD|$\\text{BPP-OBDD}$]] [[ZooRefs#NHK00|[NHK00] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQP-OBDD)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQP-OBDD because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQP/log"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQP/log - BQP With Logarithmic-Size Karp-Lipton Advice =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_BQP/poly|$\\text{BQP/poly}$]] except that the advice is O(log n) bits instead of a polynomial number.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_BQP/mlog|$\\text{BQP/mlog}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQP/log)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQP/log because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQP/mlog"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQP/mlog - BQP With Logarithmic-Size Deterministic Merlin-Like Advice =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]] except that the advice is O(log n) bits instead of a polynomial number.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Strictly contained in [[Class_BQP/qlog|$\\text{BQP/qlog}$]] [[ZooRefs#NY03|[NY03] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQP/mlog)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQP/mlog because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQP/mpoly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQP/mpoly - BQP With Polynomial-Size Deterministic Merlin-Like Advice =

----
CategoryClassical 

== Description ==

{{{#!description

The class of languages recognized by a syntactic [[Class_BQP|$\\text{BQP}$]] machine with deterministic polynomial advice that depends only on the input length, such that the output is correct with probability 2/3 when the advice is good.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Can also be defined as the class of problems solvable by a nonuniform family of polynomial-size quantum circuits, just as [[Class_P/poly|$\\text{P/poly}$]] is the class solvable by a nonuniform family of polynomial-size classical circuits.



Referred to with a variety of other ad hoc names, including [[Class_BQP/poly|$\\text{BQP/poly}$]] on occassion.



Contains [[Class_BQP/qlog|$\\text{BQP/qlog}$]], and is contained in [[Class_BQP/qpoly|$\\text{BQP/qpoly}$]].



Does not contain [[Class_ESPACE|$\\text{ESPACE}$]] [[ZooRefs#NY03|[NY03] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQP/mpoly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQP/mpoly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQP/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQP/poly - BQP With Polynomial-Size Karp-Lipton Advice =

----
CategoryClassical 

== Description ==

{{{#!description

Is to [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]] as [[Class_∃BPP|$\\text{∃BPP}$]] is to [[Class_MA|$\\text{MA}$]].  Namely, the [[Class_BQP|$\\text{BQP}$]] machine is required to give some answer with probability at least 2/3 even if the advice is bad.  Even though [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]] is a more natural class, [[Class_BQP/poly|$\\text{BQP/poly}$]] follows the standard definition of advice as a class operator [[ZooRefs#KL82|[KL82] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]] and contains [[Class_BQP/log|$\\text{BQP/log}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQP/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQP/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQP/qlog"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQP/qlog - BQP With Logarithmic-Size Quantum Advice =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_BQP/mlog|$\\text{BQP/mlog}$]] except that the advice is quantum instead of classical.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Strictly contains [[Class_BQP/mlog|$\\text{BQP/mlog}$]] [[ZooRefs#NY03|[NY03] ]].



Contained in [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQP/qlog)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQP/qlog because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQP/qpoly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQP/qpoly - BQP With Polynomial-Size Quantum Advice =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of problems solvable by a [[Class_BQP|$\\text{BQP}$]] machine that receives a quantum state ψ,,n,, as advice, which depends only on the input length n.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



As with [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]], the acceptance probability does not need to be bounded away from 1/2 if the machine is given bad advice. (Thus, we are discussing the class that [[ZooRefs#NY03|[NY03] ]] call BQP/*Qpoly.) Indeed, such a condition would make quantum advice unusable, by a continuity argument.



Does not contain [[Class_EESPACE|$\\text{EESPACE}$]] [[ZooRefs#NY03|[NY03] ]].



[Aar04b] shows the following:



There exists an oracle relative to which [[Class_BQP/qpoly|$\\text{BQP/qpoly}$]] does not contain [[Class_NP|$\\text{NP}$]].

[[Class_BQP/qpoly|$\\text{BQP/qpoly}$]] is contained in [[Class_PP/poly|$\\text{PP/poly}$]].



A classical oracle separation between [[Class_BQP/qpoly|$\\text{BQP/qpoly}$]] and [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]] is presently unknown, but there is a quantum oracle separation [[ZooRefs#AK06|[AK06] ]].  An unrelativized separation is too much to hope for, since it would imply that [[Class_PP|$\\text{PP}$]] is not contained in [[Class_P/poly|$\\text{P/poly}$]].



Contains [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQP/qpoly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQP/qpoly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQPCTC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQP,,CTC,, - BQP With Closed Time Curves =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_BQP|$\\text{BQP}$]] with access to two sets of qubits: causality-respecting qubits and CTC qubits.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [Aar05c], where it was shown that [[Class_PSPACE|$\\text{PSPACE}$]] is contained in [[Class_BQPCTC|$\\text{BQP}_\\text{CTC}\\text{}$]], which in turn is contained in [[Class_SQG|$\\text{SQG}$]].



See also [[Class_PCTC|$\\text{P}_\\text{CTC}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQPCTC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQPCTC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQPSPACE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQPSPACE - Bounded-Error Quantum PSPACE =

----
CategoryQuantum 

== Description ==

{{{#!description

Equals [[Class_PSPACE|$\\text{PSPACE}$]] and [[Class_PPSPACE|$\\text{PPSPACE}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQPSPACE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQPSPACE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQPtt/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQP,,tt,,/poly - BQP/mpoly With Truth-Table Queries =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]], except that the machine only gets to make nonadaptive queries to whatever oracle it might have.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [NY03b], where it was also shown that [[Class_P|$\\text{P}$]] is not contained in [[Class_BQPtt/poly|$\\text{BQP}_\\text{tt}\\text{/poly}$]] relative to an oracle.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQPtt/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQPtt/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_BQTIME(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BQTIME(f(n)) - Bounded-Error Quantum f(n)-Time =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_BQP|$\\text{BQP}$]], but with f(n)-time (for some constructible function f) rather than polynomial-time machines.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BV97|[BV97] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_BQTIME(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save BQTIME(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_C=AC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= C,,=,,AC^0^ - Exact-Counting AC0 =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems for which there exists a [[Class_DiffAC0|$\\text{DiffAC}^\\text{0}\\text{}$]] function f such that the answer is "yes" on input x if and only if f(x)=0.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] and [[Class_PAC0|$\\text{PAC}^\\text{0}\\text{}$]] under logspace uniformity [[ZooRefs#ABL98|[ABL98] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_C=AC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save C=AC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_C=L"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= C,,=,,L - Exact-Counting L =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_C=P|$\\text{C}_\\text{=}\\text{P}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



C,,=,,L^C=L^ = L^C=L^ [[ZooRefs#ABO99|[ABO99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_C=L)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save C=L because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_C=P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= C,,=,,P - Exact-Counting Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that the number of accepting paths exactly equals the number of rejecting paths, if and only if the answer is 'yes.'}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_coNQP|$\\text{coNQP}$]] [[ZooRefs#FGH+98|[FGH+98] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_C=P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save C=P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CC - Comparator Circuits =

----
CategoryClassical 

== Description ==

{{{#!description

A comparator gate consists of two inputs and outputs the minimum of its two inputs on its first output wire and outputs the maximum of its two inputs on its second output wire. One important restriction is that each output of a comparator gate has fanout at most one. The Comparator Circuit Value Problem (CCVP) is defined as following. Given a circuit composed of comparator gates, the inputs to the circuit, and one output of the circuit, calculate the value of this output.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_CC|$\\text{CC}$]] is defined as the class of problems log-space many-one reducible to CCVP [[ZooRefs#MS89|[MS89] ]]. At present it is only known that NL$\\subseteq$CC$\\subseteq$P [[ZooRefs#MS89|[MS89] ]]. [[Class_CC|$\\text{CC}$]] is an example of a complexity class neither known to be in [[Class_NC|$\\text{NC}$]] nor P-complete.



Natural complete problems for the [[Class_CC|$\\text{CC}$]] class include Stable Marriage Problem, Stable Roommate Problem, Lex-first Maximal Matching [[ZooRefs#Sub94|[Sub94] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CC^0^ - Constant-Depth MODm Circuits =

----
CategoryClassical 

== Description ==

{{{#!description

The set of problems solvable by by constant-depth circuits having only MOD,,m,, gates for constant $m$.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



This complexity class entry is a stub. If you feel so inclined, please help out!
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CFL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CFL - Context-Free Languages =

----
CategoryClassical 

== Description ==

{{{#!description

Does not equal [[Class_QCFL|$\\text{QCFL}$]] [[ZooRefs#MC00|[MC00] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_LOGCFL|$\\text{LOGCFL}$]].



Strictly contains [[Class_DCFL|$\\text{DCFL}$]] [[ZooRefs#Bra77|[Bra77] ]] and indeed [[Class_UCFL|$\\text{UCFL}$]].



Strictly contains [[Class_DCFL|$\\text{DCFL}$]] [[ZooRefs#Bra77|[Bra77] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CFL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CFL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CH"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CH - Counting Hierarchy =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

The union of the C,,k,,P's over all constant k.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_PSPACE|$\\text{PSPACE}$]].



Strictly contains DLOGTIME-uniform [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] [[ZooRefs#CMTV98|[CMTV98] ]].



It is an open problem whether there exists an oracle relative to which [[Class_CH|$\\text{CH}$]] is infinite, or even unequal to [[Class_PSPACE|$\\text{PSPACE}$]].  This is closely related to the problem of whether [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] = [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]], since a padding argument shows that [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] = [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] implies [[Class_CH|$\\text{CH}$]] = [[Class_PSPACE|$\\text{PSPACE}$]].



It is an open problem whether there exists an oracle relative to which [[Class_CH|$\\text{CH}$]] is infinite, or even unequal to [[Class_PSPACE|$\\text{PSPACE}$]].  This is closely related to the problem of whether [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] = [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CH)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CH because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CLSharpP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CL#P - Cluster Sharp-P =

----
CategoryClassical 

== Description ==

{{{#!description

The class of [[Class_SharpP|$\\text{#P}$]] function problems such that some underlying [[Class_NP|$\\text{NP}$]] machine $M$ witnessing membership in [[Class_SharpP|$\\text{#P}$]] has}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==

"clustered" accepting paths. That is:



There exists a polynomial p such that each computation path of M on each input x is exactly p(|x|) bits long.

There is a length-respecting total order A having polynomial-time computable adjacency checks on the computation paths of M.

The accepting paths of M on any input x are contiguous with respect to A.



Defined in [[ZooRefs#HHK+05|[HHK+05] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CLSharpP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CLSharpP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CLOG"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CLOG - Continuous Logarithmic-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Roughly, the class of continuous problems solvable by an ordinary differential equation (ODE) with convergence time logarithmic in the size of the input.  The vector field of the ODE is specified by an [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] formula, with n parameters that represent the input.  The point to which the ODE converges (assuming it does) is the output.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BSF02|[BSF02] ]], which should be consulted for more details.



[[ZooRefs#BSF02|[BSF02] ]] show that finding the maximum of n integers is in [[Class_CLOG|$\\text{CLOG}$]].  Thus, [[Class_CLOG|$\\text{CLOG}$]] is best thought of as the continuous-time analog of [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]], not of DTIME(log n).



Contained in [[Class_CP|$\\text{CP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CLOG)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CLOG because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CNP - Continuous NP =

----
CategoryClassical 

== Description ==

{{{#!description

A nondeterministic analog of [[Class_CP|$\\text{CP}$]].  Defined in [[ZooRefs#SF98|[SF98] ]], which should be consulted for the definition (it has something to do with strange attractors, I think).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The authors raise the question of whether [[Class_CP|$\\text{CP}$]] equals [[Class_CNP|$\\text{CNP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CP - Continuous P =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_CLOG|$\\text{CLOG}$]], except that the convergence time can be polynomial rather than logarithmic in the input size.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BSF02|[BSF02] ]] and [[ZooRefs#SF98|[SF98] ]].



Finding a maximum flow, which is P-complete, can be done in [[Class_CP|$\\text{CP}$]] [[ZooRefs#BSF02|[BSF02] ]].  Based on this the authors argue that "P is contained in CP," but this seems hard to formalize, since [[Class_CP|$\\text{CP}$]] is not a complexity class in the usual sense.  They also conjecture that "CP is contained in P" (i.e. the class of ODE's they consider can be integrated efficiently on a standard Turing machine), but this is open.



Contained in [[Class_CNP|$\\text{CNP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CSIZE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CSIZE(f(n)) - Circuit Size f(n) =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a (nonuniform) family of Boolean circuits of size O(f(n)).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



So for example, CSIZE(poly(n)) (the union of CSIZE(n^k^) over all k) equals [[Class_P/poly|$\\text{P/poly}$]].



Defined in [[ZooRefs#SM02|[SM02] ]] among other places.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CSIZE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CSIZE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CSL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CSL - Context Sensitive Languages =

----
CategoryClassical 

== Description ==

{{{#!description

The class of languages generated by context-sensitive grammars.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals NSPACE(n) [[ZooRefs#Kur64|[Kur64] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CSL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CSL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CSP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CSP - Constraint Satisfaction Problems =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#FV93|[FV93] ]] as the class of languages corresponding to fixed templates (where a template is a set of allowed constraints on values and variables) in the general Constraint Satisfaction Problem. Under this construction, 3SAT may be expressed as the fixed template (over the alphabet $\\{0,1\\}$) containing $C_0, C_1, C_2, C_3$:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



$\\begin{matrix}

    C_0 & = & \\{0,1\\}^3 \\backslash (0,0,0) \\\\

    C_1 & = & \\{0,1\\}^3 \\backslash (1,0,0) \\\\

    C_2 & = & \\{0,1\\}^3 \\backslash (1,1,0) \\\\

    C_3 & = & \\{0,1\\}^3 \\backslash (1,1,1)

\\end{matrix}$



For example, a 3SAT clause $(x \\vee y \\vee \\neg z)$ is represented in the [[Class_CSP|$\\text{CSP}$]] construction as $C_1(z, x, y) \\in I$. By similar constructions, any k-SAT problem can be seen to be in [[Class_CSP|$\\text{CSP}$]]. The class also includes Graph k-Coloring (for $k\\in\\mathbb{N}$), Graph H-Coloring (for some graph $H$) and Linear Programming mod $q$.



In [[ZooRefs#FV93|[FV93] ]], where the class is defined, the authors show that every problem in [[Class_MMSNP|$\\text{MMSNP}$]] is reducible under randomized polynomial-time reductions to a problem in [[Class_CSP|$\\text{CSP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CSP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CSP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CZK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CZK - Computational Zero-Knowledge =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_SZK|$\\text{SZK}$]], except that now the two distributions are merely required to be computationally indistinguishable by any [[Class_BPP|$\\text{BPP}$]] algorithm; they don't have to be statistically close.  (The "two distributions" are (1) the distribution over the verifier's view of their interaction with the prover, conditioned on the verifier's random coins, and (2) the distribution over views that the verifier can simulate without the prover's help.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Unlike [[Class_SZK|$\\text{SZK}$]], it is not known if [[Class_CZK|$\\text{CZK}$]] is closed under complement.  [[Class_CZK|$\\text{CZK}$]] is now known to share other properties with [[Class_SZK|$\\text{SZK}$]]: the verifier may as well be honest and may as well show their coins, and [[Class_CZK|$\\text{CZK}$]] is closed under unions [[ZooRefs#Vad06|[Vad06] ]].  (Previously, these properties were only established in the presence of one-way functions [[ZooRefs#GMW91|[GMW91] ]].)



Assuming the existence of one-way functions, [[Class_CZK|$\\text{CZK}$]] contains [[Class_NP|$\\text{NP}$]] [[ZooRefs#GMW91|[GMW91] ]], and actually equals IP=PSPACE [[ZooRefs#BGG+90|[BGG+90] ]].  However, none of these implications of one-way functions relativize (Impagliazzo, unpublished).



On the other hand, if one-way functions do not exist then [[Class_CZK|$\\text{CZK}$]] = [[Class_AVBPP|$\\text{AVBPP}$]] [[ZooRefs#OW93|[OW93] ]].



Contains [[Class_PZK|$\\text{PZK}$]] and [[Class_SZK|$\\text{SZK}$]].



Same as [[Class_SZK|$\\text{SZK}$]], except that now the two distributions are merely required to be computationally indistinguishable by any [[Class_BPP|$\\text{BPP}$]] algorithm; they don't have to be statistically close.  (The "two distributions" are (1) the distribution over Arthur's view of his interaction with Merlin, conditioned on Arthur's random coins, and (2) the distribution over views that Arthur can simulate without Merlin's help.)



Unlike [[Class_SZK|$\\text{SZK}$]], it is not known if [[Class_CZK|$\\text{CZK}$]] is closed under complement.  [[Class_CZK|$\\text{CZK}$]] is now known to share other properties with [[Class_SZK|$\\text{SZK}$]]: the verifier may as well be honest and may as well show his coins, and [[Class_CZK|$\\text{CZK}$]] is closed under unions [[ZooRefs#Vad06|[Vad06] ]].  (Previously, these properties were only established in the presence of one-way functions.)



Assuming the existence of one-way functions, [[Class_CZK|$\\text{CZK}$]] contains [[Class_NP|$\\text{NP}$]] [[ZooRefs#GMW91|[GMW91] ]], and indeed equals IP=PSPACE [[ZooRefs#BGG+90|[BGG+90] ]].  However, none of these implications of one-way functions relativize (Impagliazzo, unpublished).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CZK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CZK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Check"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Check - Checkable Languages =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems such that a polynomial-time program [[Class_P|$\\text{P}$]] that allegedly solves them can be checked efficiently.  That is, f is in [[Class_Check|$\\text{Check}$]] if there exists a [[Class_BPP|$\\text{BPP}$]] algorithm C such that for all programs [[Class_P|$\\text{P}$]] and inputs x,}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If P(y)=f(y) for all inputs y, then C^P^(x) (C with oracle access to [[Class_P|$\\text{P}$]]) accepts with probability at least 2/3.

If P(x) is not equal to f(x) then C^P^(x) accepts with probability at most 1/3.



Introduced in [[ZooRefs#BK89|[BK89] ]], where it was also shown that [[Class_Check|$\\text{Check}$]] equals [[Class_frIP|$\\text{frIP}$]] ∩ [[Class_cofrIP|$\\text{cofrIP}$]].



[[Class_Check|$\\text{Check}$]] is contained in [[Class_NEXP|$\\text{NEXP}$]] ∩ [[Class_coNEXP|$\\text{coNEXP}$]] [[ZooRefs#FRS88|[FRS88] ]].



[[ZooRefs#BG94|[BG94] ]] show that if [[Class_NEE|$\\text{NEE}$]] is not contained in [[Class_BPEE|$\\text{BPEE}$]] then [[Class_NP|$\\text{NP}$]] is not contained in [[Class_Check|$\\text{Check}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Check)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Check because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CkP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= C,,k,,P - kth Level of CH =

----
CategoryClassical 

== Description ==

{{{#!description

Defined as follows:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



C,,0,,P = [[Class_P|$\\text{P}$]]

C,,1,,P = [[Class_PP|$\\text{PP}$]]

C,,2,,P = PP^PP^

In general, C,,k+1,,P is [[Class_PP|$\\text{PP}$]] with [[Class_CkP|$\\text{C}_\\text{k}\\text{P}$]] oracle



The union of the C,,k,,P's is called the counting hierarchy, [[Class_CH|$\\text{CH}$]].



Defined in [[ZooRefs#Wag86|[Wag86] ]].



See [[ZooRefs#Tor91|[Tor91] ]] or [[ZooRefs#AW90|[AW90] ]] for more information.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_CkP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CkP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Coh"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Coh - Coherent Languages =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems [[Class_L|$\\text{L}$]] that are efficiently autoreducible, in the sense that given an input x and access to an oracle for [[Class_L|$\\text{L}$]], a [[Class_BPP|$\\text{BPP}$]] machine can compute L(x) by querying [[Class_L|$\\text{L}$]] only on points that differ from x.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [Yao90b].



[[ZooRefs#BG94|[BG94] ]] show that, assuming [[Class_NEE|$\\text{NEE}$]] is not contained in [[Class_BPEE|$\\text{BPEE}$]], [[Class_Coh|$\\text{Coh}$]] ∩ [[Class_NP|$\\text{NP}$]] is not contained in any of [[Class_compNP|$\\text{compNP}$]], [[Class_Check|$\\text{Check}$]], or [[Class_frIP|$\\text{frIP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Coh)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Coh because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DSharpP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= D#P - Alternate Name for P#P =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DSharpP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DSharpP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DCFL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DCFL - Deterministic CFL =

----
CategoryClassical 

== Description ==

{{{#!description

The class of languages accepted by deterministic pushdown automata.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GG66|[GG66] ]], where it was also shown that [[Class_DCFL|$\\text{DCFL}$]] is strictly contained in [[Class_CFL|$\\text{CFL}$]], contained in [[Class_UCFL|$\\text{UCFL}$]], and strictly contains [[Class_REG|$\\text{REG}$]].  The inclusion in [[Class_UCFL|$\\text{UCFL}$]] is also strict.



Defined in [[ZooRefs#GG66|[GG66] ]], where it was also shown that [[Class_DCFL|$\\text{DCFL}$]] is strictly contained in [[Class_CFL|$\\text{CFL}$]] and strictly contains [[Class_REG|$\\text{REG}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DCFL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DCFL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DET"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DET - Determinant =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems reducible in [[Class_L|$\\text{L}$]] to the problem of computing the determinant of an n-by-n matrix of n-bit integers.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Coo85|[Coo85] ]].



Contained in [[Class_NC2|$\\text{NC}^\\text{2}\\text{}$]], and contains [[Class_NL|$\\text{NL}$]] and [[Class_PL|$\\text{PL}$]] [[ZooRefs#BCP83|[BCP83] ]].



Graph isomorphism is hard for [[Class_DET|$\\text{DET}$]] under L-reductions [[ZooRefs#Tor00|[Tor00] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DET)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DET because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DP - Difference Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

[[Class_DP|$\\text{DP}$]] = BH,,2,,, the second level of the Boolean hierarchy.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#PY84|[PY84] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DQP - Dynamical Quantum Polynomial-Time =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems solvable by a [[Class_BQP|$\\text{BQP}$]] machine with oracle access to a dynamical simulator. When given a polynomial-size quantum circuit, the simulator returns a sample from the distribution over "classical histories" induced by the circuit. The simulator can adversarially choose any history distribution that satisfies the axioms of "symmetry" and "locality" -- so that the [[Class_DQP|$\\text{DQP}$]] algorithm has to work for any distribution satisfying these axioms.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



See [[ZooRefs#Aar05|[Aar05] ]] for a full definition.



There it is also shown that [[Class_SZK|$\\text{SZK}$]] is contained in [[Class_DQP|$\\text{DQP}$]].



Contains [[Class_BQP|$\\text{BQP}$]], and is contained in [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#Aar05|[Aar05] ]].



There exists an oracle relative to which [[Class_DQP|$\\text{DQP}$]] does not contain [[Class_NP|$\\text{NP}$]] [[ZooRefs#Aar05|[Aar05] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DSPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DSPACE(f(n)) - Deterministic f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a Turing machine in space O(f(n)).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The Space Hierarchy Theorem: For constructible f(n) greater than log

n, DSPACE(f(n)) is strictly contained in DSPACE(f(n) log(f(n))) [[ZooRefs#HLS65|[HLS65] ]].



For space constructible f(n), strictly contains DTIME(f(n)) [[ZooRefs#HPV77|[HPV77] ]].



DSPACE(n) does not equal [[Class_NP|$\\text{NP}$]] (though we have no idea if one contains the other)!



See also: NSPACE(f(n)).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DSPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DSPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DTIME(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DTIME(f(n)) - Deterministic f(n)-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a Turing machine in time $O(f(n))$. Note that some authors choose to call this class TIME.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Of great relevance to DTIME is the Time Hierarchy Theorem: For any constructible function $f(n)$ greater than $n$, DTIME($f(n)$) is strictly contained in DTIME($f(n) \\log(f(n)) \\log\\log(f(n))$) [[ZooRefs#HS65|[HS65] ]]. As a corollary, [[Class_P|$\\text{P}$]] ⊂ [[Class_EXP|$\\text{EXP}$]].



For any space constructible $f(n)$, DTIME($f(n)$) is strictly contained in DSPACE($f(n)$) [[ZooRefs#HPV77|[HPV77] ]].



Also, DTIME($n$) is strictly contained in NTIME(n) [[ZooRefs#PPS+83|[PPS+83] ]] (this result does not work for arbitrary $f(n)$).



For any constructible superpolynomial $f(n)$, DTIME($f(n)$) with [[Class_PP|$\\text{PP}$]] oracle is not in [[Class_P/poly|$\\text{P/poly}$]] (see [[ZooRefs#All96|[All96] ]]).



The class of decision problems solvable by a Turing machine in time O(f(n)).



The Time Hierarchy Theorem: For constructible f(n) greater than n, DTIME(f(n)) is strictly contained in DTIME(f(n) log(f(n)) loglog(f(n))) [[ZooRefs#HS65|[HS65] ]].



For any space constructible f(n), DTIME(f(n)) is strictly contained in DSPACE(f(n)) [[ZooRefs#HPV77|[HPV77] ]].



Also, DTIME(n) is strictly contained in NTIME(n) [[ZooRefs#PPS+83|[PPS+83] ]] (this result does not work for arbitrary f(n)).



For any constructible superpolynomial f(n), DTIME(f(n)) with [[Class_PP|$\\text{PP}$]] oracle is not in [[Class_P/poly|$\\text{P/poly}$]] (see [[ZooRefs#All96|[All96] ]]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DTIME(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DTIME(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DTISP(t(n),s(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DTISP(t(n),s(n)) - Simultaneous t(n)-Time and s(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a Turing machine that uses time O(t(n)) and space O(s(n)) simultaneously.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Thus [[Class_SC|$\\text{SC}$]] = DTISP(poly,polylog) for example.



Defined in [[ZooRefs#Nis92|[Nis92] ]], where it was also shown that for all space-constructible s(n)=Ω(log n), BPSPACE(s(n)) is contained in DTISP(2^O(s(n))^,s^2^(n)).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DTISP(t(n),s(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DTISP(t(n),s(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DiffAC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DiffAC^0^ - Difference #AC0 =

----
CategoryClassical 

== Description ==

{{{#!description

The class of functions from {0,1}^n^ to integers expressible as the difference of two [[Class_SharpAC0|$\\text{#AC}^\\text{0}\\text{}$]] functions.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_GapAC0|$\\text{GapAC}^\\text{0}\\text{}$]] under logspace uniformity [[ZooRefs#ABL98|[ABL98] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DiffAC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DiffAC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DisNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DisNP - Disjoint NP Pairs =

----
CategoryClassical 

== Description ==

{{{#!description

The class of pairs (A,B), where A and B are [[Class_NP|$\\text{NP}$]] problems whose sets of "yes" instances are nonempty and disjoint.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If there exists an optimal propositional proof system, then [[Class_DisNP|$\\text{DisNP}$]] has a complete pair [[ZooRefs#Raz94|[Raz94] ]].  On the other hand, there exists an oracle relative to which [[Class_DisNP|$\\text{DisNP}$]] does not have a complete pair [[ZooRefs#GSS+03|[GSS+03] ]].



If [[Class_P|$\\text{P}$]] does not equal [[Class_UP|$\\text{UP}$]], then [[Class_DisNP|$\\text{DisNP}$]] contains pairs not separated by any set in [[Class_P|$\\text{P}$]] [[ZooRefs#GS88|[GS88] ]].  On the other hand, there exists an oracle relative to which [[Class_P|$\\text{P}$]] does not equal [[Class_NP|$\\text{NP}$]] but still [[Class_DisNP|$\\text{DisNP}$]] does not contain any P-inseparable pairs [[ZooRefs#HS92|[HS92] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DisNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DisNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DistNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DistNP - Distributional NP =

----
CategoryClassical 

== Description ==

{{{#!description

(also called (NP,P-computable) or RNP)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A distributional problem consists of a decision problem A, and a probability distribution μ over problem instances.



(A,μ) is in [[Class_DistNP|$\\text{DistNP}$]] if A is in [[Class_NP|$\\text{NP}$]], and μ is P-computable (meaning that its cumulative density function can be evaluated in polynomial time).



[[Class_DistNP|$\\text{DistNP}$]] has complete problems [[ZooRefs#Lev86|[Lev86] ]] (see also [[ZooRefs#Gur87|[Gur87] ]]), although unlike for [[Class_NP|$\\text{NP}$]] this is not immediate.



Any DistNP-complete problem is also complete for (NP,P-samplable) [[ZooRefs#IL90|[IL90] ]].



[[Class_DistNP|$\\text{DistNP}$]] has complete problems [[ZooRefs#Gur87|[Gur87] ]], although unlike for [[Class_NP|$\\text{NP}$]] this is not immediate.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_DistNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save DistNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Dyn-FO"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Dyn-FO - Dynamic FO =

----
CategoryClassical 

== Description ==

{{{#!description

The class of dynamic problems solvable using first-order predicates.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Basically what this means is that an algorithm maintains some polynomial-size data structure (say a graph), and receives a sequence of updates (add this edge, delete that one, etc.).  For each update, it computes a new value for the data structure in [[Class_FO|$\\text{FO}$]] -- that is, for each bit of the data structure, there is an [[Class_FO|$\\text{FO}$]] function representing the new value of that bit, which takes as input both the update and the previous value of the data structure.  At the end the algorithm needs to answer some question (i.e. is the graph connected?).



See [[ZooRefs#HI02|[HI02] ]] for more information, and a complete problem for [[Class_Dyn-FO|$\\text{Dyn-FO}$]].



See also [[Class_Dyn-ThC0|$\\text{Dyn-ThC}^\\text{0}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Dyn-FO)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Dyn-FO because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Dyn-ThC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Dyn-ThC^0^ - Dynamic Threshold Circuits =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_Dyn-FO|$\\text{Dyn-FO}$]], except that now updates are computed via constant-depth predicates that have "COUNT" available, in addition to AND, OR, and NOT -- so it's a uniform version of [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] rather than of [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



See [[ZooRefs#HI02|[HI02] ]] for more information.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Dyn-ThC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Dyn-ThC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_E"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= E - Exponential Time With Linear Exponent =

----
CategoryClassical 

== Description ==

{{{#!description

Equals DTIME(2^O(n)^).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Does not equal [[Class_NP|$\\text{NP}$]] [[ZooRefs#Boo72|[Boo72] ]] or [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#Boo74|[Boo74] ]] relative to any oracle.  However, there is an oracle relative to which [[Class_E|$\\text{E}$]] is contained in [[Class_NP|$\\text{NP}$]] (see [[Class_ZPP|$\\text{ZPP}$]]), and an oracle relative to [[Class_PSPACE|$\\text{PSPACE}$]] is contained in [[Class_E|$\\text{E}$]] (by equating the former with [[Class_P|$\\text{P}$]]).



There exists a problem that is complete for [[Class_E|$\\text{E}$]] under polynomial-time Turing reductions but not polynomial-time truth-table reductions [[ZooRefs#Wat87|[Wat87] ]].



Problems hard for [[Class_BPP|$\\text{BPP}$]] under Turing reductions have measure 1 in [[Class_E|$\\text{E}$]] [[ZooRefs#AS94|[AS94] ]].



It follows that, if the problems complete for [[Class_E|$\\text{E}$]] under Turing reductions do not have measure 1 in [[Class_E|$\\text{E}$]], then [[Class_BPP|$\\text{BPP}$]] does not equal [[Class_EXP|$\\text{EXP}$]].



[[ZooRefs#IT89|[IT89] ]] gave an oracle relative to which [[Class_E|$\\text{E}$]] = [[Class_NE|$\\text{NE}$]] but still there is an exponential-time binary predicate whose corresponding search problem is not in [[Class_E|$\\text{E}$]].



[[ZooRefs#BF03|[BF03] ]] gave a proof that if [[Class_E|$\\text{E}$]] = [[Class_NE|$\\text{NE}$]], then no sparse set is collapsing, where they defined a set $A$ to be collapsing if $A\\notin\\mathsf{P}$ and if for all $B$ such that $A$ and $B$ are Turing reducible to each other, $A$ and $B$ are many-to-one reducible to each other.



Contrast with [[Class_EXP|$\\text{EXP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_E)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save E because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EE - Double-Exponential Time With Linear Exponent =

----
CategoryClassical 

== Description ==

{{{#!description

Equals DTIME(2^2^O(n)^^) (though some authors alternatively define it as being equal to DTIME(2^O(2^n^)^)).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_EE|$\\text{EE}$]] = [[Class_BPE|$\\text{BPE}$]] if and only if [[Class_EXP|$\\text{EXP}$]] = [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#IKW01|[IKW01] ]].



Contained in [[Class_EEXP|$\\text{EEXP}$]] and [[Class_NEE|$\\text{NEE}$]].



Equals DTIME(2^2^O(n)^) (though some authors alternatively define it as being equal to DTIME(2^O(2^n)^)).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EEE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EEE - Triple-Exponential Time With Linear Exponent =

----
CategoryClassical 

== Description ==

{{{#!description

Equals DTIME(2^2^2^O(n)^^^).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



In contrast to the case of [[Class_EE|$\\text{EE}$]], it is not known whether [[Class_EEE|$\\text{EEE}$]] = [[Class_BPEE|$\\text{BPEE}$]] implies [[Class_EE|$\\text{EE}$]] = [[Class_BPE|$\\text{BPE}$]] [[ZooRefs#IKW01|[IKW01] ]].



Equals DTIME(2^2^2^O(n)^).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EEE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EEE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EESPACE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EESPACE - Double-Exponential Space With Linear Exponent =

----
CategoryClassical 

== Description ==

{{{#!description

Equals DSPACE(2^2^O(n)^^).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Is not contained in [[Class_BQP/qpoly|$\\text{BQP/qpoly}$]] [[ZooRefs#NY03|[NY03] ]].



Equals DSPACE(2^2^O(n)^).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EESPACE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EESPACE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EEXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EEXP - Double-Exponential Time =

----
CategoryClassical 

== Description ==

{{{#!description

Equals DTIME(2^2^p(n)^^) for p a polynomial.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Also known as 2-EXP.



Contains [[Class_EE|$\\text{EE}$]], and is contained in [[Class_NEEXP|$\\text{NEEXP}$]].



Equals DTIME(2^2^p(n)^) for p a polynomial.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EEXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EEXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EH"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EH - Exponential-Time Hierarchy With Linear Exponent =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

Has roughly the same relationship to [[Class_E|$\\text{E}$]] as [[Class_PH|$\\text{PH}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



More formally, [[Class_EH|$\\text{EH}$]] is defined as the union of [[Class_E|$\\text{E}$]], [[Class_NE|$\\text{NE}$]], NE^NP^, [[Class_NE|$\\text{NE}$]] with [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] oracle, and so on.



See [[ZooRefs#Har87|[Har87] ]] for more information.



If [[Class_coNP|$\\text{coNP}$]] is contained in [[Class_AM[polylog]|$\\text{AM[polylog]}$]], then [[Class_EH|$\\text{EH}$]] collapses to [[Class_S2-EXP•PNP|$\\text{S}_\\text{2}\\text{-EXP•P}^\\text{NP}\\text{}$]] [[ZooRefs#SS04|[SS04] ]] and indeed [[Class_AMEXP|$\\text{AM}_\\text{EXP}\\text{}$]] [[ZooRefs#PV04|[PV04] ]].



On the other hand, [[Class_coNE|$\\text{coNE}$]] is contained in [[Class_NE/poly|$\\text{NE/poly}$]], so perhaps it wouldn't be so surprising if [[Class_NE|$\\text{NE}$]] collapses.



There exists an oracle relative to which [[Class_EH|$\\text{EH}$]] does not contain [[Class_SEH|$\\text{SEH}$]] [[ZooRefs#Hem89|[Hem89] ]]. [[Class_EH|$\\text{EH}$]] and [[Class_SEH|$\\text{SEH}$]] are incomparable for all anyone knows.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EH)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EH because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ELEMENTARY"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ELEMENTARY - Iterated Exponential Time =

----
CategoryClassical 

== Description ==

{{{#!description

Equals the union of DTIME(2^n^), DTIME(2^2^n^^), DTIME(2^2^2^n^^^), and so on.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_PR|$\\text{PR}$]].



Equals the union of DTIME(2^n^), DTIME(2^2^n^), DTIME(2^2^2^n^), and so on.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ELEMENTARY)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ELEMENTARY because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ELkP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EL,,k,,P - Extended Low Hierarchy =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

An extension of [[Class_LkP|$\\text{L}_\\text{k}\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of problems A such that Σ,,k,,P^A^ is contained in Σ,,k-1,,P^A,NP^.



Defined in [[ZooRefs#BBS86|[BBS86] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ELkP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ELkP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EP - NP with 2k Accepting Paths =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'no,' then all computation paths reject.

If the answer is 'yes,' then the number of accepting paths is a power of two.



Contained in [[Class_C=P|$\\text{C}_\\text{=}\\text{P}$]], and in [[Class_ModkP|$\\text{Mod}_\\text{k}\\text{P}$]] for any odd k.  Contains [[Class_UP|$\\text{UP}$]].



Defined in [[ZooRefs#BHR00|[BHR00] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EPTAS"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EPTAS - Efficient Polynomial-Time Approximation Scheme =

----
CategoryClassical 

== Description ==

{{{#!description

The class of optimization problems such that, given an instance of length n, we can find a solution within a factor 1+ε of the optimum in time f(ε)p(n), where p is a polynomial and f is arbitrary.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_FPTAS|$\\text{FPTAS}$]] and is contained in [[Class_PTAS|$\\text{PTAS}$]].



Defined in [[ZooRefs#CT97|[CT97] ]], where the following was also shown:



If [[Class_FPT|$\\text{FPT}$]] = [[Class_XPuniform|$\\text{XP}_\\text{uniform}\\text{}$]] then [[Class_EPTAS|$\\text{EPTAS}$]] = [[Class_PTAS|$\\text{PTAS}$]].

If [[Class_EPTAS|$\\text{EPTAS}$]] = [[Class_PTAS|$\\text{PTAS}$]] then [[Class_FPT|$\\text{FPT}$]] = [[Class_W[P]|$\\text{W[P]}$]].

If [[Class_FPT|$\\text{FPT}$]] is strictly contained in [[Class_W[1]|$\\text{W[1]}$]], then there is a natural problem that is in [[Class_PTAS|$\\text{PTAS}$]] but not in [[Class_EPTAS|$\\text{EPTAS}$]].  (See [[ZooRefs#CT97|[CT97] ]] for the statement of the problem, since it's not that natural.)
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EPTAS)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EPTAS because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EQP - Exact Quantum Polynomial-Time =

----
CategoryQuantum 

== Description ==

{{{#!description

The same as [[Class_BQP|$\\text{BQP}$]], except that the quantum algorithm must return the correct answer with probability 1, and run in polynomial time with probability 1.  Unlike bounded-error quantum computing, there is no theory of universal QTMs for exact quantum computing models.  In the original definition in [[ZooRefs#BV97|[BV97] ]], each language in [[Class_EQP|$\\text{EQP}$]] is computed by a single QTM, equivalently to a uniform family of quantum circuits with a finite gate set [[Class_K|$\\text{K}$]] whose amplitudes can be computed in polynomial time. See [[Class_EQPK|$\\text{EQP}_\\text{K}\\text{}$]].  However, some results require an infinite gate set.  The official definition here is that the gate set should be finite.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Without loss of generality, the amplitudes in the gate set [[Class_K|$\\text{K}$]] are algebraic numbers [[ZooRefs#ADH97|[ADH97] ]].



There is an oracle that separates [[Class_EQP|$\\text{EQP}$]] from [[Class_NP|$\\text{NP}$]] [[ZooRefs#BV97|[BV97] ]], indeed from [[Class_Δ2P|$\\text{Δ}_\\text{2}\\text{P}$]] [[ZooRefs#GP01|[GP01] ]].  There is also an oracle relative to which [[Class_EQP|$\\text{EQP}$]] is not in Mod,,p,,P where p is prime [[ZooRefs#GV02|[GV02] ]].  On the other hand, [[Class_EQP|$\\text{EQP}$]] is in [[Class_LWPP|$\\text{LWPP}$]] [[ZooRefs#FR98|[FR98] ]].



P^||NP[2k]^ is contained in EQP^||NP[k]^, where "||NP[k]" denotes k nonadaptive oracle queries to [[Class_NP|$\\text{NP}$]] (queries that cannot depend on the results of previous queries) [[ZooRefs#BD99|[BD99] ]].



See also [[Class_ZBQP|$\\text{ZBQP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EQPK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EQP,,K,, - Exact Quantum Polynomial-Time with Gate Set K =

----
CategoryQuantum 

== Description ==

{{{#!description

The set of problems that can be answered by a uniform family of polynomial-sized quantum circuits whose gates are drawn from a set [[Class_K|$\\text{K}$]], and that return the correct answer with probability 1, and run in polynomial time with probability 1, and the allowed gates are drawn from a set [[Class_K|$\\text{K}$]].  [[Class_K|$\\text{K}$]] may be either finite or countable and enumerated.  If S is a ring, the union of [[Class_EQPK|$\\text{EQP}_\\text{K}\\text{}$]] over all finite gate sets [[Class_K|$\\text{K}$]] whose amplitudes are in the ring [[Class_R|$\\text{R}$]] can be written EQP,,S,,.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#ADH97|[ADH97] ]] in the special case of a finite set of 1-qubit gates controlled by a second qubit.  It was shown there that transcendental gates may be replaced by algebraic gates without decreasing the size of [[Class_EQPK|$\\text{EQP}_\\text{K}\\text{}$]].



[[ZooRefs#FR98|[FR98] ]] show that EQP,,Q,, is in [[Class_LWPP|$\\text{LWPP}$]].  The proof can be generalized to any finite, algebraic gate set [[Class_K|$\\text{K}$]].



The hidden shift problem for a vector space over Z/2 is in EQP,,Q,, by Simon's algorithm.  The discrete logarithm problem over Z/p is in EQP,,Q-bar,, using infinitely many gates [[ZooRefs#MZ03|[MZ03] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EQPK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EQPK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EQTIME(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EQTIME(f(n)) - Exact Quantum f(n)-Time =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_EQP|$\\text{EQP}$]], but with f(n)-time (for some constructible function f) rather than polynomial-time machines.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BV97|[BV97] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EQTIME(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EQTIME(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ESPACE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ESPACE - Exponential Space With Linear Exponent =

----
CategoryClassical 

== Description ==

{{{#!description

Equals DSPACE(2^O(n)^).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If [[Class_E|$\\text{E}$]] = [[Class_ESPACE|$\\text{ESPACE}$]] then [[Class_P|$\\text{P}$]] = [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#HY84|[HY84] ]].



Indeed if [[Class_E|$\\text{E}$]] has nonzero measure in [[Class_ESPACE|$\\text{ESPACE}$]] then [[Class_P|$\\text{P}$]] = [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#Lut91|[Lut91] ]].



[[Class_ESPACE|$\\text{ESPACE}$]] is not contained in [[Class_P/poly|$\\text{P/poly}$]] [[ZooRefs#Kan82|[Kan82] ]].



Is not contained in [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]] [[ZooRefs#NY03|[NY03] ]].



See also: [[Class_EXPSPACE|$\\text{EXPSPACE}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ESPACE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ESPACE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EXP - Exponential Time =

----
CategoryClassical 

== Description ==

{{{#!description

Equals the union of DTIME(2^p(n)^) over all polynomials p.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Also equals [[Class_P|$\\text{P}$]] with [[Class_E|$\\text{E}$]] oracle.



If [[Class_L|$\\text{L}$]] = [[Class_P|$\\text{P}$]] then [[Class_PSPACE|$\\text{PSPACE}$]] = [[Class_EXP|$\\text{EXP}$]].



If [[Class_EXP|$\\text{EXP}$]] is in [[Class_P/poly|$\\text{P/poly}$]] then [[Class_EXP|$\\text{EXP}$]] = [[Class_MA|$\\text{MA}$]] [[ZooRefs#BFL91|[BFL91] ]].



Problems complete for [[Class_EXP|$\\text{EXP}$]] under many-one reductions have measure 0 in [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#May94|[May94] ]], [[ZooRefs#JL95|[JL95] ]].



There exist oracles relative to which



[[Class_EXP|$\\text{EXP}$]] = [[Class_NP|$\\text{NP}$]] = [[Class_ZPP|$\\text{ZPP}$]] [Hel84a], [Hel84b], [[ZooRefs#Kur85|[Kur85] ]], [[ZooRefs#Hel86|[Hel86] ]],

[[Class_EXP|$\\text{EXP}$]] = [[Class_NEXP|$\\text{NEXP}$]] but still [[Class_P|$\\text{P}$]] does not equal [[Class_NP|$\\text{NP}$]] [[ZooRefs#Dek76|[Dek76] ]],

[[Class_EXP|$\\text{EXP}$]] does not equal [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#Dek76|[Dek76] ]].



[[ZooRefs#BT04|[BT04] ]] show the following rather striking result: let A be many-one complete for [[Class_EXP|$\\text{EXP}$]], and let S be any set in [[Class_P|$\\text{P}$]] of subexponential density.  Then A-S is Turing-complete for [[Class_EXP|$\\text{EXP}$]].



[[ZooRefs#SM03|[SM03] ]] show that if [[Class_EXP|$\\text{EXP}$]] has circuits of polynomial size, then [[Class_P|$\\text{P}$]] can be simulated in [[Class_MAPOLYLOG|$\\text{MA}_\\text{POLYLOG}\\text{}$]] such that no deterministic polynomial-time adversary can generate a list of inputs for a [[Class_P|$\\text{P}$]] problem that includes one which fails to be simulated. As a result, [[Class_EXP|$\\text{EXP}$]] ⊆ [[Class_MA|$\\text{MA}$]] if [[Class_EXP|$\\text{EXP}$]] has circuits of polynomial size.



[[ZooRefs#SU05|[SU05] ]] show that [[Class_EXP|$\\text{EXP}$]] $\\not\\subseteq$ [[Class_NP/poly|$\\text{NP/poly}$]] implies [[Class_EXP|$\\text{EXP}$]] $\\not\\subseteq$ P^||NP^/poly.



In descriptive complexity EXPTIME can be defined as SO(2^{n^{O(1)}}) which is also SO(LFP)



[[Class_EXP|$\\text{EXP}$]] = [[Class_NP|$\\text{NP}$]] = [[Class_ZPP|$\\text{ZPP}$]] [[ZooRefs#Hel84|[Hel84] ]],

[[Class_EXP|$\\text{EXP}$]] = [[Class_NEXP|$\\text{NEXP}$]] but still [[Class_P|$\\text{P}$]] does not equal [[Class_NP|$\\text{NP}$]] [[ZooRefs#Dek76|[Dek76] ]],

[[Class_EXP|$\\text{EXP}$]] does not equal [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#Dek76|[Dek76] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EXP/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EXP/poly - Exponential Time With Polynomial-Size Advice =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable in [[Class_EXP|$\\text{EXP}$]] with the help of a polynomial-length advice string that depends only on the input length.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_BQP/qpoly|$\\text{BQP/qpoly}$]] [Aar04b].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EXP/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EXP/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_EXPSPACE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= EXPSPACE - Exponential Space =

----
CategoryClassical 

== Description ==

{{{#!description

Equals the union of DSPACE(2^p(n)^) over all polynomials p.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



See also: [[Class_ESPACE|$\\text{ESPACE}$]].



Given a first-order statement about real numbers, involving only addition and comparison (no multiplication), we can decide in [[Class_EXPSPACE|$\\text{EXPSPACE}$]] whether it's true or not [[ZooRefs#Ber80|[Ber80] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_EXPSPACE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save EXPSPACE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_F-TAPE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= F-TAPE(f(n)) - Provable DSPACE(f(n)) For Formal System F =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems that can be proven to be solvable in O(f(n)) space on a deterministic Turing machine, from the axioms of formal system F.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Har78|[Har78] ]].



See also F-TIME(f(n)).  The results about F-TAPE mirror those about F-TIME, but in some cases are sharper.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_F-TAPE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save F-TAPE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_F-TIME(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= F-TIME(f(n)) - Provable DTIME(f(n)) For Formal System F =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems that can be proven to be solvable in O(f(n)) time on a deterministic Turing machine, from the axioms of formal system F.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Har78|[Har78] ]], where the following was also shown:



If F-TIME(f(n)) = DTIME(f(n)), then DTIME(f(n)) is strictly contained in DTIME(f(n)g(n)) for any nondecreasing, unbounded, recursive g(n).

There exist recursive, monotonically increasing f(n) such that F-TIME(f(n)) is strictly contained in DTIME(f(n)).



See also F-TAPE(f(n)).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_F-TIME(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save F-TIME(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FBQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FBQP - Function BQP =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_BQP|$\\text{BQP}$]] as [[Class_FNP|$\\text{FNP}$]] does to [[Class_NP|$\\text{NP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



There exists an oracle relative to which [[Class_PLS|$\\text{PLS}$]] is not contained in [[Class_FBQP|$\\text{FBQP}$]] [[ZooRefs#Aar03|[Aar03] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FBQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FBQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FH"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FH - Fourier Hierarchy =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

FH,,k,, is the class of problems solvable by a uniform family of polynomial-size quantum circuits, with k levels of Hadamard gates and all other gates preserving the computational basis.  (Conditional phase flip gates are fine, for example.)  Thus}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



FH,,0,, = [[Class_P|$\\text{P}$]]

FH,,1,, = [[Class_BPP|$\\text{BPP}$]]

FH,,2,, contains factoring because of Kitaev's phase estimation algorithm



It is an open problem to show that the Fourier hierarchy is infinite relative to an oracle (that is, FH,,k,, is strictly contained in FH,,k+1,,).



Defined in [[ZooRefs#Shi03|[Shi03] ]].



FH,,0,, = [[Class_P|$\\text{P}$]]

FH,,1,, = [[Class_BPP|$\\text{BPP}$]]

FH,,2,, contains factoring, because of Kitaev's phase estimation algorithm
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FH)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FH because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FIXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FIXP - Fixed Point =

----
CategoryClassical 

== Description ==

{{{#!description

The class of fixed point problems. In the framework of fixed point problems, an instance I is associated with a (continuous) function F,,I,,, and a solution of I is a fixed point of F,,I,,.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Properties of [[Class_FIXP|$\\text{FIXP}$]] problems:



the function F,,I,, is represented by an algebraic circuit over {+, -, *, /, max, min} with rational constants

 there is a polynomial time algorithm that computes the circuit from I.



Every [[Class_FIXP|$\\text{FIXP}$]] problem has Partial Computation, Decision, (Strong) Approximation, and Existence counterparts; these can all be solved in [[Class_PSPACE|$\\text{PSPACE}$]].



The Nash equilibrium problem for 3 or more players is FIXP-complete.



Linear-FIXP = [[Class_PPAD|$\\text{PPAD}$]].



Defined in [[ZooRefs#EY07|[EY07] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FIXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FIXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FNL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FNL - Function NL =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_NL|$\\text{NL}$]] as [[Class_FNP|$\\text{FNP}$]] does to [[Class_NP|$\\text{NP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined by [[ZooRefs#AJ93|[AJ93] ]], who also showed that if [[Class_NL|$\\text{NL}$]] = [[Class_UL|$\\text{UL}$]], then [[Class_FNL|$\\text{FNL}$]] is contained in [[Class_SharpL|$\\text{#L}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FNL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FNL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FNL/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FNL/poly - Nonuniform FNL =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_FNL|$\\text{FNL}$]] as [[Class_P/poly|$\\text{P/poly}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_SharpL/poly|$\\text{#L/poly}$]] [[ZooRefs#RA00|[RA00] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FNL/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FNL/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FNP - Function NP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of function problems of the following form:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Given an input x and a polynomial-time predicate F(x,y), if there exists a y satisfying F(x,y) then output any such y, otherwise output 'no.'



[[Class_FNP|$\\text{FNP}$]] generalizes [[Class_NP|$\\text{NP}$]], which is defined in terms of decision problems only.



Actually the word "function" is misleading, since there could be many valid outputs y.  That's unavoidable, since given a predicate F there's no "syntactic" criterion ensuring that y is unique.



[[Class_FP|$\\text{FP}$]] = [[Class_FNP|$\\text{FNP}$]] if and only if [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]].



Contains [[Class_TFNP|$\\text{TFNP}$]].



A basic question about [[Class_FNP|$\\text{FNP}$]] problems is whether they're self-reducible; that is, whether they reduce to the corresponding [[Class_NP|$\\text{NP}$]] decision problems.  Although this is true for all [[Class_NPC|$\\text{NPC}$]] problems, [[ZooRefs#BG94|[BG94] ]] shows that if [[Class_EE|$\\text{EE}$]] does not equal [[Class_NEE|$\\text{NEE}$]], then there is a problem in [[Class_NP|$\\text{NP}$]] such that no corresponding [[Class_FNP|$\\text{FNP}$]] problem can be reduced to it.  [[ZooRefs#BG94|[BG94] ]] cites Impagliazzo and Sudan as giving the same conclusion under the assumption that [[Class_NE|$\\text{NE}$]] does not equal [[Class_coNE|$\\text{coNE}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FO"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FO - First-Order logic =

----
CategoryClassical 

== Description ==

{{{#!description

First order logic is the smallest logical class of logic language. It is the base of Descriptive complexity and equal to the class [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] and to [[Class_AH|$\\text{AH}$]], the alternating logtime hierarchy.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



When we use logic formalism, the input is a structure, usually it is either strings (of bits or over an alphabet) whose elements are position of the strings, or graphs whose elements are vertices. The mesure of the input will there be the size of the structure.

Whatever the structure is, we can suppose that there are relation that you can test, by example $E(x,y)$ is true iff there is an edge from $x$ to $y$ if the structure is a graph, and $P(n)$ is true iff the nth letter of the string is 1. We also have constant, who are special elements of the structure, by example if we want to check reachability in a graph, we will have to choose two constant s and t.



In descriptive complexity we almost always suppose that there is a total order over the elements and that we can check equality between elements. This let us consider elements as number, $x$ is the number $n$ iff there is $(n-1)$ elements $y$ such that $y<x$. Thanks to this we also want the primitive "bit", where $bit(x,y)$ is true if only the $y$th bith of $x$ is 1. (We can replace $bit$ by plus and time, ternary relation such that $plus(x,y,z)$ is true iff $x+y=z$ and $times(x,y,z)$ is true iff $x*y=z$).



Since in a computer elements are only pointers or string of bit, thoses assumptions make sens, and those primitive function can be calculated in most of the small complexity classes. We can also imagine [[Class_FO|$\\text{FO}$]] without those primitives, which gives us smaller complexity classes.



The language [[Class_FO|$\\text{FO}$]] is then defined as the closure by conjunction ( $\\wedge$), negation ($\\neg$) and universal quantification ($\\forall$) over element of the structures. We also often use existantial quantification ($\\exists$) and disjunction ($\\vee$) but those can be defined thanks to the 3 first symbols.



The semantics of the formulae in [[Class_FO|$\\text{FO}$]] is straightforward, $\\neg A$ is true iff $A$ is false, $A\\wedge B$ is true iff $A$ is true and $B$ is true, and ($\\forall x P$) is true iff whatever element we decide that $x$ is we can choose, $P$ is true.



A querie in [[Class_FO|$\\text{FO}$]] will then be to check if a [[Class_FO|$\\text{FO}$]] formulae is true over a given structure, this structure is the input of the problem. One should not confuse this kind of problem with checking if a quantified boolean formula is true, which is the definition of QBF, which is Pspace-complete. The difference between those two problem is that in QBF the size of the problem is the size of the formula and elements are just boolean value, whereas in [[Class_FO|$\\text{FO}$]] the size of the problem is the size of the structure and the formula is fixed.



Every formulae is equivalent to a formulae in prenexe normal form where we put recursively every quantifier and then a quantifier-free formulae.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FO)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FO because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FO(DTC)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FO(DTC) - First-order with deterministic transitive closure =

----
CategoryClassical 

== Description ==

{{{#!description

FO(DTC) is defined as FO(tc) where the transitive closure operator is deterministic, which means that when we apply DTC($\\phi_{u,v}$), we know that for all $u$, there exist at most one $v$ such that phi(u,v).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



We can suppose that DTC($\\phi_{u,v}$) is syntactic sugar for TC($\\psi_{u,v}$) where $\\psi(u,v)=\\phi(u,v)\\wedge \\forall x, (x=v \\vee \\neg \\psi(u,x))$.



It was shown in [[ZooRefs#Imm99|[Imm99] ]] page 144 that this class is equal to [[Class_L|$\\text{L}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FO(DTC))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FO(DTC) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FO(LFP)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FO(LFP) - First-order with least fixed point =

----
CategoryClassical 

== Description ==

{{{#!description

FO(LFP) is the set of boolean queries definable with first-order fixed-point formulae where the partial fixed point is limited to be monotone, which means that if the second order variable is $P$, then $P_i(x)$ always implies $P_{i+1}(x)$.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



We can obtain the monotony by restricting the formula $\\phi$ to have only positive occurrences of $P$ (i.e. there is an even number of negations before every occurrence of $P$). We can also describe LFP($\\phi_{P,x}$) as syntactic sugar of PFP($\\psi_{P,x}$) where $\\psi(P,x)=\\phi(P,x)\\vee P(x)$.



Thanks to monotonicity we only add and never remove vectors to the truth table of $P$, and since there is only $n^k$ possible vectors we always find a fixed point before $n^k$ iterations. Hence it was shown in [[ZooRefs#Imm82|[Imm82] ]] that FO(LFP)=P. This definition is equivalent to FO(n^{O(1)}).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FO(LFP))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FO(LFP) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FO(PFP)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FO(PFP) - First-order with partial fixed point =

----
CategoryClassical 

== Description ==

{{{#!description

FO(pfp) is the set of boolean queries definable with first-order formulae with a partial fixed point operator.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Let $k$ be an integer, $x, y$  vectors of $k$ variables, $P$ a second-order variable of arity $k$, and $\\phi$ a FO(PFP) function using $x$ and $P$ as variables, then we can define iteratively $(P_i)_{i\\in N}$ such that $P_0(x)=false$ and $P_i(x)=\\phi(P_{i-1},x)$ which means that the property $P_i$ is true on the input $x$ if $\\phi$ is true on input $x$, and when the variable $P$ is replaced by $P_{i-1}$. Then, either there is a fixed point, or the list of $(P_i)$ is looping.



PFP($\\phi_{P,x})(y)$ is defined as the value of the fixed point of $(P_i)$ on y if there is a fixed point, else as false.



Since $P$s are property of arity $k$, there is at most $2^{n^k}$ values for the $P_i$s, so with a poly-space counter we can check if there is a loop or not.



It was proved in [[ZooRefs#Imm98|[Imm98] ]] that FO(pfp) is equal to [[Class_PSPACE|$\\text{PSPACE}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FO(PFP))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FO(PFP) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FO(TC)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FO(TC) - First-order with transitive closure =

----
CategoryClassical 

== Description ==

{{{#!description

FO(TC) is the set of boolean queries definable with first-order formulae with a transitive closure (TC) operator.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



TC is defined this way: let $k$ be a positiver integer and $u,v,x,y$ be vectors of $k$ variables, then TC($\\phi_{u,v})(x,y)$ is true if there exist $n$ variables $(x_i)$ such that $x_1=x, x_n=y$ and for all $i<n$ $\\phi_{u,v}(x_i,x_{i+1})$. Here, $\\phi_{u,v}$ is a formula over $u,v$ written in FO(TC) and $\\phi_{u,v}(x,y)$ means that the variables $u$ and $v$ are replaced by $x$ and $y$.



Every formula of TC can be written in a normal form FO($\\phi_{u,v})(0,max)$ where $\\phi$ is a [[Class_FO|$\\text{FO}$]] formula and we suppose that there is an order on the model where variables are quantified, so we can choose the minimum and maximum element.



It was shown in [[ZooRefs#Imm98|[Imm98] ]] page 150 that this class is equal to [[Class_NL|$\\text{NL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FO(TC))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FO(TC) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FO(t(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FO(t(n)) - First-Order =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which a "yes" answer can be expressed by a first-order logic predicate, with a block of restricted quantifiers repeated t(n) times.  See [[ZooRefs#Imm98|[Imm98] ]] for a full definition.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



FO(poly(n)) = [[Class_P|$\\text{P}$]] (see [[ZooRefs#Var82|[Var82] ]] for example).



FO(poly(n)) is contained in [[Class_SO-E|$\\text{SO-E}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FO(t(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FO(t(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FOLL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FOLL - First-Order loglog n =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a uniform family of polynomial-size, unbounded-fanin, depth O(log log n) circuits with AND, OR, and NOT gates. Equals FO(log log n).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BKL+00|[BKL+00] ]], where it was also shown that many problems on finite groups are in [[Class_FOLL|$\\text{FOLL}$]].



Contains uniform [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]], and is contained in uniform [[Class_AC1|$\\text{AC}^\\text{1}\\text{}$]].



Is not known to be comparable to [[Class_L|$\\text{L}$]] or [[Class_NL|$\\text{NL}$]].



The class of decision problems solvable by a nonuniform family of polynomial-size, unbounded-fanin, depth O(loglog n) circuits with AND, OR, and NOT gates.



Contains [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]], and is contained in [[Class_AC1|$\\text{AC}^\\text{1}\\text{}$]].



Is not known to be comparable to [[Class_L/poly|$\\text{L/poly}$]] or [[Class_NL/poly|$\\text{NL/poly}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FOLL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FOLL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FO[t(n)]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FO[$t(n)$] - Iterated First-Order logic =

----
CategoryClassical 

== Description ==

{{{#!description

Let $t(n)$ be a function from integers to integers.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==

$(\\forall x [[Class_P|$\\text{P}$]]) Q$ abbreviates $(\\forall x (P\\Rightarrow Q))$ and $(\\exists x [[Class_P|$\\text{P}$]]) Q$ abbreviates $(\\exists x ([[Class_P|$\\text{P}$]] \\wedge Q))$.



A quantifier block is a list $(Q_1 x_1. \\phi_1)...(Q_k x_k. \\phi_k)$ where the $\\phi_i$s are quantifier free FO-formulae and each $Q_i$s is either $\\forall$ or $\\exists$.

If $Q$ is a quantifier block then $[Q]^{t(n)}$ is the block consisting of $t(n)$ iterated copies of $Q$. 

Note that there are $k*t(n)$ quantifiers in the list, but only k variables; each variable is used $t(n)$ times.



FO[$t(n)$] consists of the FO-formulae with quantifier blocks that are iterated $\\Theta(t(n))$ times.



In Descriptive complexity we can see that :



FO[(\log n)^i] is equal to fo-uniform AC^i^, and in fact [[Class_FO[t(n)]|$\\text{FO[t(n)]}$]] is fo-uniform [[Class_AC|$\\text{AC}$]] of depth t(n)

FO[(\log n)^{O(1)}] is equal to [[Class_NC|$\\text{NC}$]]

FO[n^{O(1)}] is equal to [[Class_P|$\\text{P}$]] and FO(LFP)

FO[2^{n^{O(1)}}] is equal to [[Class_PSPACE|$\\text{PSPACE}$]] and FO(PFP)
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FO[t(n)])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FO[t(n)] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FP - Function Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Sometimes defined as the class of functions computable in polynomial time by a Turing machine.  (Generalizes [[Class_P|$\\text{P}$]], which is defined in terms of decision problems only.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



However, if we want to compare [[Class_FP|$\\text{FP}$]] to [[Class_FNP|$\\text{FNP}$]], we should instead define it as the class of [[Class_FNP|$\\text{FNP}$]] problems (that is, polynomial-time predicates P(x,y)) for which there exists a polynomial-time algorithm that, given x, outputs any y such that P(x,y).  That is, there could be more than one valid output, even though any given algorithm only returns one of them.



[[Class_FP|$\\text{FP}$]] = [[Class_FNP|$\\text{FNP}$]] if and only if [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]].



If FP^NP^ = [[Class_FPNP[log]|$\\text{FP}^\\text{NP[log]}\\text{}$]] (that is, allowed only a logarithmic number of queries), then [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]] [[ZooRefs#Kre88|[Kre88] ]].  The corresponding result for [[Class_PNP|$\\text{P}^\\text{NP}\\text{}$]] versus [[Class_PNP[log]|$\\text{P}^\\text{NP[log]}\\text{}$]] is not known, and indeed fails relative to some oracles (see [Har87b]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FPNP[log]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FP^NP[log]^ - FP With Logarithmically Many Queries To NP =

----
CategoryClassical 

== Description ==

{{{#!description

Given a graph, the problem of outputting the size of its maximum clique is complete for [[Class_FPNP[log]|$\\text{FP}^\\text{NP[log]}\\text{}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FPNP[log])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FPNP[log] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FPR"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FPR - Fixed-Parameter Randomized =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_FPT|$\\text{FPT}$]] as [[Class_RP|$\\text{RP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#AR01|[AR01] ]], where it was shown that, if the Resolution proof system is automatizable (that is, if a refutation can always be found in time polynomial in the length of the shortest refutation), then [[Class_W[P]|$\\text{W[P]}$]] is contained in [[Class_FPR|$\\text{FPR}$]].



Has the same relation to [[Class_FPT|$\\text{FPT}$]] as [[Class_R|$\\text{R}$]] does to [[Class_P|$\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FPR)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FPR because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FPRAS"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FPRAS - Fully Polynomial Randomized Approximation Scheme =

----
CategoryClassical 

== Description ==

{{{#!description

The subclass of [[Class_SharpP|$\\text{#P}$]] counting problems whose answer, y, is approximable in the following sense.  There exists a randomized algorithm that, with probability at least 1-δ, approximates y to within an ε multiplicative factor in time polynomial in n (the input size), 1/ε, and log(1/δ).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The permanent of a nonnegative matrix is in [[Class_FPRAS|$\\text{FPRAS}$]] [[ZooRefs#JSV01|[JSV01] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FPRAS)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FPRAS because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FPT"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FPT - Fixed-Parameter Tractable =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems of the form (x,k), k a parameter, that are solvable in time f(k)p(|x|), where f is arbitrary and p is a polynomial.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The basic class of the theory of fixed-parameter tractability, as described by Downey and Fellows [[ZooRefs#DF99|[DF99] ]].



To separate [[Class_FPT|$\\text{FPT}$]] and W[2], one could show there is no proof system for CNF formulae that admits proofs of size f(k)n^O(1)^, where f is a computable function and n is the size of the formula.



Contained in [[Class_FPTnu|$\\text{FPT}_\\text{nu}\\text{}$]], [[Class_W[1]|$\\text{W[1]}$]], and [[Class_FPR|$\\text{FPR}$]].



Contains [[Class_FPTAS|$\\text{FPTAS}$]] [[ZooRefs#CC97|[CC97] ]], as well as [[Class_FPTsu|$\\text{FPT}_\\text{su}\\text{}$]].



Contains [[Class_EPTAS|$\\text{EPTAS}$]] unless [[Class_FPT|$\\text{FPT}$]] = [[Class_W[1]|$\\text{W[1]}$]] [[ZooRefs#Baz95|[Baz95] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FPT)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FPT because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FPTAS"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FPTAS - Fully Polynomial-Time Approximation Scheme =

----
CategoryClassical 

== Description ==

{{{#!description

The subclass of [[Class_NPO|$\\text{NPO}$]] problems that admit an approximation scheme in the following sense.  For any ε>0, there is an algorithm that is guaranteed to find a solution whose cost is within a 1+ε factor of the optimum cost.  Furthermore, the running time of the algorithm is polynomial in n (the size of the problem) and in 1/ε.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_PTAS|$\\text{PTAS}$]].



Defined in [[ZooRefs#ACG+99|[ACG+99] ]].



Contained in [[Class_FPT|$\\text{FPT}$]] [[ZooRefs#CC97|[CC97] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FPTAS)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FPTAS because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FPTnu"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FPT,,nu,, - Fixed-Parameter Tractable (nonuniform) =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_FPT|$\\text{FPT}$]] except that the algorithm can vary with the parameter k (though its running time must always be O(p(|x|)), for a fixed polynomial p).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



An alternate view is that a single algorithm can take a polynomial-length advice string, depending on k.



Defined in [[ZooRefs#DF99|[DF99] ]] (though they did not use our notation).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FPTnu)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FPTnu because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FPTsu"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FPT,,su,, - Fixed-Parameter Tractable (strongly uniform) =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_FPT|$\\text{FPT}$]] except that f has to be recursive.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#DF99|[DF99] ]] (though they did not use our notation).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FPTsu)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FPTsu because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FQMA"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FQMA - Function QMA =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of problems for which the task is to output a quantum certificate for a [[Class_QMA|$\\text{QMA}$]] problem, when such a certificate exists.  Thus, the desired output is a quantum state.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#JWB03|[JWB03] ]], where it is also shown that state preparation for 3-local Hamiltonians is FQMA-complete.  The authors also observe that, in contrast to the case of [[Class_FNP|$\\text{FNP}$]] versus [[Class_NP|$\\text{NP}$]], there is no obvious reduction of [[Class_FQMA|$\\text{FQMA}$]] problems to [[Class_QMA|$\\text{QMA}$]] problems.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FQMA)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FQMA because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Few"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Few - FewP With Flexible Acceptance Mechanism =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The number of accepting paths a is bounded by a polynomial in the size of the input x.

For some polynomial-time predicate [[Class_Q|$\\text{Q}$]], Q(x,a) is true if and only if the answer is 'yes.'



Also called FewPaths.



Defined in [[ZooRefs#CH89|[CH89] ]].



Contains [[Class_FewP|$\\text{FewP}$]], and is contained in P^FewP^ [[ZooRefs#Kob89|[Kob89] ]] and in [[Class_SPP|$\\text{SPP}$]] [[ZooRefs#FFK94|[FFK94] ]].



See also the survey [[ZooRefs#Tor90|[Tor90] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Few)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Few because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FewEXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FewEXP - NEXP With Few Witnesses =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NEXP|$\\text{NEXP}$]] machine such that, given a "yes" instance, no more than an exponential number of computation paths accept.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in MIP[NP^FewEXP^] ([[Class_MIP|$\\text{MIP}$]] where provers are not unbounded in computational power, but are limited to NP^FewEXP^) [[ZooRefs#AKS+94|[AKS+94] ]].



Alternatively, [[Class_FewEXP|$\\text{FewEXP}$]] can refer to the sparsity of accepting paths in a given instance. In [[ZooRefs#AKR+03|[AKR+03] ]], the authors show that the conjectures "FewEXP search instances are EXP-solvable" and "FewEXP decision instances are EXP/poly-solvable" are equivalent. That is, for all [[Class_NEXP|$\\text{NEXP}$]] machines $N$, the following conditions are equivalent:



There exists an [[Class_EXP|$\\text{EXP}$]] machine M such that if given a string x, N(x) accepts and has exponentially bounded accepting paths, then M(x) produces one such path.

 There exists an [[Class_EXP/poly|$\\text{EXP/poly}$]] machine M which accepts a string x if and only N(x) accepts.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FewEXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FewEXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FewP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FewP - NP With Few Witnesses =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'no,' then all computation paths reject.

If the answer is 'yes,' then at least one path accepts; furthermore, the number of accepting paths is upper-bounded by a polynomial in n, the size of the input.



Defined in [[ZooRefs#AR88|[AR88] ]].



Is contained in [[Class_⊕P|$\\text{⊕P}$]] [[ZooRefs#CH89|[CH89] ]].



There exists an oracle relative to which [[Class_P|$\\text{P}$]], [[Class_UP|$\\text{UP}$]], [[Class_FewP|$\\text{FewP}$]], and [[Class_NP|$\\text{NP}$]] are all distinct [[ZooRefs#Rub88|[Rub88] ]].



Also, there exists an oracle relative to which [[Class_FewP|$\\text{FewP}$]] does not have a Turing-complete set [[ZooRefs#HJV93|[HJV93] ]].



Contained in [[Class_Few|$\\text{Few}$]].



See also the survey [[ZooRefs#Tor90|[Tor90] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_FewP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FewP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_GA"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= GA - Graph Automorphism =

----
CategoryClassical 

== Description ==

{{{#!description

Can be defined as the class of problems polynomial-time Turing reducible to the Graph Automorphism problem.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_P|$\\text{P}$]] and is contained in [[Class_GI|$\\text{GI}$]].



See [[ZooRefs#KST93|[KST93] ]] for much more information about [[Class_GA|$\\text{GA}$]].



Can be defined as the class of problems polynomial-time Turing reducible to the problem of deciding whether a given graph has any nontrivial automorphisms.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_GA)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save GA because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_GAN-SPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= GAN-SPACE(f(n)) - Games Against Nature f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems decidable by an O(f(n))-space Turing machine with two kinds of quantifiers: existential and randomized.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains NSPACE(f(n)) and BPSPACE(f(n)), and is contained in AUC-SPACE(f(n)).



By linear programming, GAN-SPACE(log n) is contained in [[Class_P|$\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_GAN-SPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save GAN-SPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_GC(s(n),C)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= GC(s(n),C) - Guess and Check =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which a "yes" answer can be verified by}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



guessing s(n) bits, then

verifying the answer in complexity class C.



For example, GC(p(n),P) = [[Class_NP|$\\text{NP}$]] where p is a polynomial.



Defined in [[ZooRefs#CC93|[CC93] ]].



Umans [[ZooRefs#Uma98|[Uma98] ]] has shown that given a DNF expression Φ, the Shortest Implicant problem is GC(log^2^n, coNP)-complete.



Umans [[ZooRefs#Uma98|[Uma98] ]] has shown that given a DNF expression Φ, the Shortest Implicant problem (is there a conjunction of at most k negated or non-negated literals that implies Φ?) is GC(log^2^n, coNP)-complete.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_GC(s(n),C))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save GC(s(n),C) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_GCSL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= GCSL - Growing CSL =

----
CategoryClassical 

== Description ==

{{{#!description

The class of languages generated by context-sensitive grammars in which the right-hand side of each transformation is either strictly longer than the left-hand side or the left-hand side consists of the start symbol.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#DW86|[DW86] ]] and shown to be contained in [[Class_LOGCFL|$\\text{LOGCFL}$]] (and therefore in [[Class_P|$\\text{P}$]] among others).



Shown to be equivalent to Acyclic [[Class_CSL|$\\text{CSL}$]] in [[ZooRefs#Nie02|[Nie02] ]].



The class of languages generated by context-sensitive grammars in which the right-hand side of each transformation is strictly longer than the left-hand side.



Defined in [[ZooRefs#DW86|[DW86] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_GCSL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save GCSL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_GI"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= GI - Graph Isomorphism =

----
CategoryClassical 

== Description ==

{{{#!description

Can be defined as the class of problems polynomial-time Turing reducible to the Graph Isomorphism problem.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_GA|$\\text{GA}$]] and is contained in [[Class_Δ2P|$\\text{Δ}_\\text{2}\\text{P}$]].



The Graph Isomorphism problem itself (as opposed to the set of problems Turing reducible to Graph Isomorphism) is contained in [[Class_NP|$\\text{NP}$]] as well as [[Class_coAM|$\\text{coAM}$]] (and indeed [[Class_SZK|$\\text{SZK}$]]).  So in particular, if Graph Isomorphism is NP-complete, then [[Class_PH|$\\text{PH}$]] collapses.



See [[ZooRefs#KST93|[KST93] ]] for much more information about [[Class_GI|$\\text{GI}$]].



Can be defined as the class of problems polynomial-time Turing reducible to the problem of deciding whether two graphs are isomorphic.



The [[Class_GI|$\\text{GI}$]] problem itself (as opposed to the set of problems Turing reducible to [[Class_GI|$\\text{GI}$]]) is contained in [[Class_NP|$\\text{NP}$]] as well as [[Class_coAM|$\\text{coAM}$]] (and indeed [[Class_SZK|$\\text{SZK}$]]).  So in particular, if graph isomorphism is NP-complete, then [[Class_PH|$\\text{PH}$]] collapses.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_GI)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save GI because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_GLO"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= GLO - Guaranteed Local Optima =

----
CategoryClassical 

== Description ==

{{{#!description

The class of [[Class_NPO|$\\text{NPO}$]] problems which have the property that for all locally optimal solutions, the ratio between the values of the local and global optima is upper-bounded by a constant.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#AP95|[AP95] ]], where it was also shown that [[Class_GLO|$\\text{GLO}$]] is strictly contained in [[Class_APX|$\\text{APX}$]].



[[ZooRefs#KMS+99|[KMS+99] ]] showed that [[Class_MaxSNP|$\\text{MaxSNP}$]] is not contained in [[Class_GLO|$\\text{GLO}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_GLO)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save GLO because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_GPCD(r(n),q(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= GPCD(r(n),q(n)) - Generalized Probabilistically Checkable Debate =

----
CategoryClassical 

== Description ==

{{{#!description

Same as PCD(r(n),q(n)), except that now the verifier is allowed nonadaptively to query O(q(n)) rounds of the debate, with no restriction on the number of bits it looks at within each round.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#CFL+93|[CFL+93] ]], who also showed that PCD(log n, q(n)) = GPCD(log n, q(n)) for every q(n).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_GPCD(r(n),q(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save GPCD(r(n),q(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_G[t]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= G[t] - Stratification of Fixed-Parameter Tractable Problems =

----
CategoryClassical 

== Description ==

{{{#!description

(Basically) the class of decision problems of the form (x,k) (k a parameter), that are solvable by a parameterized family of circuits with unbounded fanin and depth t.  A uniformity condition may also be imposed.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#DF99|[DF99] ]], which should be consulted for the full definition.



Uniform G[P] (i.e. with no restriction on depth) is equal to [[Class_FPT|$\\text{FPT}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_G[t])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save G[t] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_GapAC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= GapAC^0^ - Gap #AC0 =

----
CategoryClassical 

== Description ==

{{{#!description

The class of functions from {0,1}^n^ to integers computable by constant-depth, polynomial-size arithmetic circuits with addition and multiplication gates and the constants 0, 1, and -1.  (The only difference from [[Class_SharpAC0|$\\text{#AC}^\\text{0}\\text{}$]] is the ability to subtract, using the constant -1.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_DiffAC0|$\\text{DiffAC}^\\text{0}\\text{}$]] under logspace uniformity [[ZooRefs#ABL98|[ABL98] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_GapAC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save GapAC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_GapL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= GapL - Gap Logarithmic-Space =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_GapP|$\\text{GapP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_GapL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save GapL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_GapP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= GapP - Gap Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of functions f(x) such that for some [[Class_NP|$\\text{NP}$]] machine, f(x) is the number of accepting paths minus the number of rejecting paths.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equivalently, the closure of the [[Class_SharpP|$\\text{#P}$]] functions under subtraction.



Defined in [[ZooRefs#FFK94|[FFK94] ]] and independently [[ZooRefs#Gup95|[Gup95] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_GapP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save GapP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HO"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HO - High-Order logic =

----
CategoryClassical 

== Description ==

{{{#!description

High order logic is an extension of Second order, First order where we add quantification over higher order variables.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



We define a relation of order $o$ and arity $k$ to be a subset of $k$-tuple of relation of order $o-1$ and arity $k$. When $o=1$ it is by extension a first order variable. The quantification of formula in [[Class_HO|$\\text{HO}$]] is over a given order (which is a straightforward extension of [[Class_SO|$\\text{SO}$]] where we add quantification over constant (first-order variable) and relation (second-order variables). The atomic predicates now can be general application of relation of order $o$ and arity $k$ to $k$ relations of order $o-1$ and arity $a$ and  test of equality between two relations of the same order and arity.



$HO^o$ is the set of formulae with quantification up to order O. $\\Sigma^i_j$(resp. $\\Pi_j^i$) is defined as the set of formula in $HO^{i+1}$ beginning by an existantial (resp universal) quantifier followed by at most $j-1$ alternation of quantifiers.



This class was define in [[ZooRefs#HT06|[HT06] ]], and it was proved that $\\Sigma^i_j=\\exp_2^{i-1}(n^O(1))^{\\Sigma^P_{j-1}}$ where $\\Sigma^P_{j-1}$ is the $j$th level of the polynomial hierarchy.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_HO)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HO because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HVSZK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HVSZK - Honest-Verifier SZK =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems that have [[Class_SZK|$\\text{SZK}$]] protocols assuming an honest verifier (i.e. one who doesn't try to learn more about the problem by deviating from the protocol).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_SZK|$\\text{SZK}$]] [[ZooRefs#Oka96|[Oka96] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_HVSZK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HVSZK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HalfP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HalfP - RP With Exactly Half Acceptance =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'yes,' exactly 1/2 of computation paths accept.

If the answer is 'no,' all computation paths reject.



Significantly, the number of candidate witnesses is restricted to be a power of 2.  (This is implicit if they are binary strings.)



Contained in [[Class_RP|$\\text{RP}$]], [[Class_EP|$\\text{EP}$]], and [[Class_ModkP|$\\text{Mod}_\\text{k}\\text{P}$]] for every odd k.  Contained in [[Class_EQP|$\\text{EQP}$]] by the Deutsch-Jozsa algorithm.



Defined in [[ZooRefs#BB92|[BB92] ]], where it was called C,,==,,P[half].  The name used here is from [[ZooRefs#BS00|[BS00] ]].  There it was shown that [[Class_HalfP|$\\text{HalfP}$]] is contained in every similar class in which 1/2 is replaced by some other dyadic fraction.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_HalfP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HalfP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HeurBPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HeurBPP - Heuristic BPP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems for which a 1-1/poly(n) fraction of instances are solvable by a [[Class_BPP|$\\text{BPP}$]] machine.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[ZooRefs#FS04|[FS04] ]] showed a strict hierarchy theorem for [[Class_HeurBPP|$\\text{HeurBPP}$]]; thus, [[Class_HeurBPP|$\\text{HeurBPP}$]] does not equal HeurBPTIME(n^c^) for any fixed c.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_HeurBPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HeurBPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HeurBPTIME(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HeurBPTIME(f(n)) - Heuristic BPTIME(f(n)) =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems for which a 1-1/poly(n) fraction of instances are solvable by a BPTIME(f(n)) machine. Thus, HeurBPTIME(f(n)) has the same relationship with BPTIME as HeurDTIME.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Thus [[Class_HeurBPP|$\\text{HeurBPP}$]] is the union of HeurBPTIME(n^c^) over all c.



The class of problems for which a 1-1/poly(n) fraction of instances are solvable by a BPTIME(f(n)) machine.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_HeurBPTIME(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HeurBPTIME(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HeurDTIME\delta(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HeurDTIME,,\delta,,(f(n)) - Heuristic DTIME =

----
CategoryClassical 

== Description ==

{{{#!description

For functions $f(n)$ and $\\delta(n)$, we say that tuple $(L,D)\\in\\mathsf{HeurDTIME}_{\\delta}(f(n))$, where $L$ is a language and $D$ is a distribution of problem instances, if there exists a heuristic deterministic algorithm $A$ such that for all $x$ in the support of $D$, $A$ runs in time bounded by $f(n)$ and with failure probability bounded by $\\delta(n)$ [[ZooRefs#BT06|[BT06] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_HeurDTIME\delta(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HeurDTIME\delta(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HeurNTIME\delta"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HeurNTIME,,\delta,, - Heuristic NTIME =

----
CategoryClassical 

== Description ==

{{{#!description

Defined as Heur,,\delta,,DTIME, but for non-deterministic heuristic algorithms.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_NP|$\\text{NP}$]] is not contained in HeurNTIME,,1/2+1/{n^a},,($n^c$) for any constants $a,c$ [[ZooRefs#Per07|[Per07] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_HeurNTIME\delta)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HeurNTIME\delta because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HeurP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HeurP - Heuristic P =

----
CategoryClassical 

== Description ==

{{{#!description

The class of distributional problems solvable by a [[Class_P|$\\text{P}$]] machine. Defined in [[ZooRefs#Imp95|[Imp95] ]], though he calls the class HP.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Alternately, [[ZooRefs#BT06|[BT06] ]] define [[Class_HeurP|$\\text{HeurP}$]] as being the set of tuples $(L,D)$, where $L$ is a language and $D$ is a distribution of problem instances, such that there exists an algorithm $A$ satisfying two properties:



For every n\in\mathbb{N}, for every x in the support of D, and for every \delta>0, A(x;n,\delta) runs in time bounded by \mathrm{poly}(n/\delta).

 For every \delta>0, A(\cdot;\cdot,\delta) is a heuristic algorithm for (L,D) whose error probability is bounded by \delta.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_HeurP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HeurP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HeurPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HeurPP - Heuristic PP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of distributional problems solvable by a [[Class_PP|$\\text{PP}$]] machine. Defined in [[ZooRefs#Ill95|[Ill95] ]], though he calls the class HPP.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_HeurPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HeurPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HkP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= H,,k,,P - High Hierarchy In NP =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

The class of problems A in [[Class_NP|$\\text{NP}$]] such that Σ,,k,,P^A^ = Σ,,k+1,,P; that is, adding A as an oracle increases the power of the k^th^ level of the polynomial hierarchy by a maximum amount.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



For all k, H,,k,, is contained in H,,k+1,,.



H,,0,, consists exactly of the problems complete for [[Class_NP|$\\text{NP}$]] under Cook reductions.



H,,1,, consists exactly of the problems complete for [[Class_NP|$\\text{NP}$]] under strong non-deterministic Turing reductions [[ZooRefs#Sch83|[Sch83] ]].



Defined in [[ZooRefs#Sch83|[Sch83] ]].



See also [[Class_LkP|$\\text{L}_\\text{k}\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_HkP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HkP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_IC[log,poly]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= IC[log,poly] - Logarithmic Instance Complexity, Polynomial Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems such that, for every n-bit string x, there exists a program A of size O(log n) that, given x as input, "correctly decides" the answer on x in time polynomial in n.  This means:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



There exists a polynomial p such that for any input y, A returns either "yes", "no", or "I don't know" in time p(|y|).

Whenever A returns "yes" or "no", it is correct.

A returns either "yes" or "no" on x.



Defined in [[ZooRefs#OKS+94|[OKS+94] ]]; see also [[ZooRefs#LV97|[LV97] ]].



If [[Class_NP|$\\text{NP}$]] is contained in [[Class_IC[log,poly]|$\\text{IC[log,poly]}$]], then [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]] [[ZooRefs#OKS+94|[OKS+94] ]].  Indeed, any self-reducible problem in [[Class_IC[log,poly]|$\\text{IC[log,poly]}$]] is also in [[Class_P|$\\text{P}$]].



Strictly contains [[Class_P/log|$\\text{P/log}$]], and is strictly contained in [[Class_P/poly|$\\text{P/poly}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_IC[log,poly])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save IC[log,poly] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_IP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= IP - Interactive Proof =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which a "yes" answer can be verified by an interactive proof.  Here a probabilistic polynomial-time verifier sends messages back and forth with an all-powerful prover.  They can have polynomially many rounds of interaction. Given the verifier's algorithm, at the end:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes," the prover must be able to behave in such a way that the verifier accepts with probability at least 2/3 (over the choice of the verifier's random bits).

If the answer is "no," then however the prover behaves the verifier must reject with probability at least 2/3.



Defined in [[ZooRefs#GMR89|[GMR89] ]], with the motivation of providing a framework for the introduction of zero-knowledge proofs (see the class [[Class_ZK|$\\text{ZK}$]]). Interestingly, the power of general interactive proof systems is not decreased if the verifier is only allowed random queries (i.e., it merely tosses coins and sends any outcome to the prover). The latter model, known as the Arthur-Merlin (or public-coin) model was introduced independently (but later) in [[ZooRefs#Bab85|[Bab85] ]], and a strong equivalent (which preserves the number of rounds) is proved in [[ZooRefs#GS86|[GS86] ]]. 

Often, it is required that the prover can convince the verifier to accept correct assertions with probability 1; this is called perfect completeness.

However, the definitions with one-sided and two-sided error can be shown to be equivalent (see [[ZooRefs#FGM+89|[FGM+89] ]]).



First demonstration to the power of interactive proofs was given by showing that for graph nonisomorphism (a problem not known in [[Class_NP|$\\text{NP}$]]) has such proofs [[ZooRefs#GMW91|[GMW91] ]]. Five years later is was shown that

[[Class_IP|$\\text{IP}$]] contains [[Class_PH|$\\text{PH}$]] [[ZooRefs#LFK+90|[LFK+90] ]], and indeed (this was discovered only a few weeks later) equals [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#Sha90|[Sha90] ]].  On the other hand, [[Class_coNP|$\\text{coNP}$]] is not contained in [[Class_IP|$\\text{IP}$]] relative to a random oracle [[ZooRefs#CCG+94|[CCG+94] ]].



See also: [[Class_MIP|$\\text{MIP}$]], [[Class_QIP|$\\text{QIP}$]], [[Class_MA|$\\text{MA}$]], [[Class_AM|$\\text{AM}$]].



The class of decision problems for which a "yes" answer can be verified by an interactive proof.  Here a [[Class_BPP|$\\text{BPP}$]] (i.e. probabilistic polynomial-time) verifier sends messages back and forth with an all-powerful prover.  They can have polynomially many rounds of interaction. Given the verifier's algorithm, at the end:



[[Class_IP|$\\text{IP}$]] contains [[Class_PH|$\\text{PH}$]] [[ZooRefs#LFK+90|[LFK+90] ]], and indeed (this was discovered only a few days later) equals [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#Sha90|[Sha90] ]].  On the other hand, [[Class_coNP|$\\text{coNP}$]] is not contained in [[Class_IP|$\\text{IP}$]] relative to a random oracle [[ZooRefs#CCG+94|[CCG+94] ]].



See also: [[Class_MIP|$\\text{MIP}$]], [[Class_QIP|$\\text{QIP}$]], [[Class_MA|$\\text{MA}$]], [[Class_AM|$\\text{AM}$]].
== Relations ==

{{{#!class_relations
{"version": 1.0, "class": "IP", "relations": {"contained_in": [], "equals": [{"class": "PSPACE"}, {"class": "QIP"}]}}
}}}


== See Also ==

<<FullSearch(linkto:Class_IP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save IP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_IPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= IPP - Unbounded IP =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_IP|$\\text{IP}$]], except that if the answer is "yes," there need only be a prover strategy that causes the verifier to accept with probability greater than 1/2, while if the answer is "no," then for all prover strategies the verifier accepts with probability less than 1/2.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#CCG+94|[CCG+94] ]], where it was also shown that [[Class_IPP|$\\text{IPP}$]] = [[Class_PSPACE|$\\text{PSPACE}$]] relative to all oracles.  Since [[Class_IP|$\\text{IP}$]] is strictly contained in [[Class_PSPACE|$\\text{PSPACE}$]] relative to a random oracle, the authors interpreted this as evidence against the Random Oracle Hypothesis (a slight change in definition can cause the behavior of a class relative to a random oracle to change drastically).



See also: [[Class_PPSPACE|$\\text{PPSPACE}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_IPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save IPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_IP[polylog]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= IP[polylog] - Alternate Name for AM[polylog] =

----
CategoryClassical 

== Description ==

{{{#!description

Alternate name for [[Class_AM[polylog]|$\\text{AM[polylog]}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_IP[polylog])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save IP[polylog] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_K"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= K - Feasibly recursive functions =

----
CategoryClassical 

== Description ==

{{{#!description

A class of number-theoretic functions, defined as the closure of basic integer arithmetic operations ($+, -, \\cdot, \\lfloor x/y\\rfloor$, as well as constants 0, 1, and projections) under composition and polynomially long sums and products. Defined by [[ZooRefs#Con73|[Con73] ]], who mistakenly claimed it coincides with [[Class_FP|$\\text{FP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals U,,D,,-uniform FTC^0^ by [[ZooRefs#Hes01|[Hes01] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_K)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save K because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_L"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= L - Logarithmic Space =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a Turing machine restricted to use an amount of memory logarithmic in the size of the input, n.  (The input itself is not counted as part of the memory.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_L|$\\text{L}$]] is contained in [[Class_P|$\\text{P}$]].  [[Class_L|$\\text{L}$]] contains [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] [[ZooRefs#Bor77|[Bor77] ]], and is contained in generalizations including [[Class_NL|$\\text{NL}$]], [[Class_L/poly|$\\text{L/poly}$]], [[Class_SL|$\\text{SL}$]], [[Class_RL|$\\text{RL}$]], [[Class_⊕L|$\\text{⊕L}$]], and [[Class_ModkL|$\\text{Mod}_\\text{k}\\text{L}$]].



Reingold [[ZooRefs#Rei04|[Rei04] ]] showed that, remarkably, [[Class_L|$\\text{L}$]] = [[Class_SL|$\\text{SL}$]].  In other words, undirected graph connectivity is solvable in deterministic logarithmic space.



Immerman [[ZooRefs#Imm83|[Imm83] ]] showed that [[Class_L|$\\text{L}$]] is the class FO(dtc) of first-order expressible queries with a deterministic transitive closure.



[[Class_L|$\\text{L}$]] queries are exactly the one that can be written in a syntactic restriction of  While languages.



[[Class_L|$\\text{L}$]] contains [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] [[ZooRefs#Bor77|[Bor77] ]], and is contained in generalizations including [[Class_NL|$\\text{NL}$]], [[Class_L/poly|$\\text{L/poly}$]], [[Class_SL|$\\text{SL}$]], [[Class_RL|$\\text{RL}$]], [[Class_⊕L|$\\text{⊕L}$]], and [[Class_ModkL|$\\text{Mod}_\\text{k}\\text{L}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_L)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save L because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_L/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= L/poly - Nonuniform Logarithmic Space =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_P/poly|$\\text{P/poly}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_PBP|$\\text{PBP}$]] [[ZooRefs#Cob66|[Cob66] ]].



Contains [[Class_SL|$\\text{SL}$]] [[ZooRefs#AKL+79|[AKL+79] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_L/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save L/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= LC^0^ - Unbounded Fanin Linear Size Constant-Depth Circuits =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a nonuniform family of Boolean circuits, with linear size, constant depth and unbounded fanin.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



It is equivalent to [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] with bounded fanout and it is properly contained in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] [[ZooRefs#CR96|[CR96] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LH"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= LH - Logarithmic Time Hierarchy =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

A Turing machine with random access owns a special tape where it can write a binary number $n$, and it can query the value of the $n$th bit of the input. Hence any bit of the input can be read in only logtime.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The $i$th level of the Logarithmic Time Hierarchy is the set of languages recognised by alternating Turing machine in logtime with random access and $i-1$ alternation, begining with existantial state. [[Class_LH|$\\text{LH}$]] is the union of all levels and is equal to tothe class [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] and to [[Class_FO|$\\text{FO}$]] Descriptive complexity.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LH)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LH because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LIN"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= LIN - Linear Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a deterministic Turing machine in linear time.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Strictly Contained in [[Class_NLIN|$\\text{NLIN}$]]. [[ZooRefs#PPS+83|[PPS+83] ]].



Contained in [[Class_NLIN|$\\text{NLIN}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LIN)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LIN because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LOGCFL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= LOGCFL - Logarithmically Reducible to CFL =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems reducible in [[Class_L|$\\text{L}$]] to the problem of deciding membership in a context-free language.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equivalently, [[Class_LOGCFL|$\\text{LOGCFL}$]] is the class of decision problems solvable by a uniform family of [[Class_AC1|$\\text{AC}^\\text{1}\\text{}$]] circuits, in which no AND gate has fan-in exceeding 2 (see e.g. [[ZooRefs#Joh90|[Joh90] ]], p. 137).



[[Class_LOGCFL|$\\text{LOGCFL}$]] is closed under complement [[ZooRefs#BCD+89|[BCD+89] ]].



Contains [[Class_NL|$\\text{NL}$]] [[ZooRefs#Sud78|[Sud78] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LOGCFL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LOGCFL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LOGLOG"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= LOGLOG - loglog Space =

----
CategoryClassical 

== Description ==

{{{#!description

There are several possible definitions of this class; the most common is the class of languages which can be computed in space O(log log n) by a deterministic Turing machine with two-way access to the input. A typical nonregular language in this class has a form such as 00..00a00..01b00..10b00..11a..., with the successive numbers having logarithmic length. It is the smallest of a collection of sublogarithmically bounded space classes, since any smaller space class contains only the regular languages. These and related classes are studied extensively in [[ZooRefs#Szep94|[Szep94] ]] and [[ZooRefs#LiRe93|[LiRe93] ]]. The alternation hierarchy for this class is infinite ([[ZooRefs#BGR93|[BGR93] ]]), and the $Pi_n$ and $Sigma_n$ levels are incomparable unless $n = 1$; however, the nondeterministic version of the class is closed under complement ([[ZooRefs#Geff91|[Geff91] ]]).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Sublogarithmically-bounded Turing reductions are equivalent to "regular" (constant-bounded) reductions, however ([[ZooRefs#Agr01|[Agr01] ]]).



Note that while there are no decision problems that can be tested in one-way loglog space, there are promise problems which can be so tested, such as Balanced Monotone Boolean Sentence Value [[ZooRefs#Buss91|[Buss91] ]]. Also, the alternation hierarchy over 1-way loglog space still does not collapse.



Obviously contained in [[Class_L|$\\text{L}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LOGLOG)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LOGLOG because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LOGNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= LOGNP - Logarithmically-Restricted NP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems expressible in logical form as}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists y such that for all j in S, the predicate φ(I,s,,j,,,x,y,j) holds.  Here x and y are logarithmic-length strings, or equivalently polynomially bounded numbers, and φ is computable in [[Class_P|$\\text{P}$]].



LOGNP,,0,, is the subclass in which φ is a first-order predicate without quantifiers and x and y are bounded lists of indices of input bits.  [[Class_LOGNP|$\\text{LOGNP}$]] is also the closure of LOGNP,,0,, under many-one reduction.



The motivation is that the analogue of LOGNP,,0,, without the logarithmic bound on |S| is [[Class_SO-E|$\\text{SO-E}$]], which by Fagin's theorem equals [[Class_NP|$\\text{NP}$]] [[ZooRefs#Fag74|[Fag74] ]].



Defined in [[ZooRefs#PY96|[PY96] ]], where it was also shown that the following problem is complete for [[Class_LOGNP|$\\text{LOGNP}$]] under many-one reductions:



Vapnik-Chervonenkis (V-C) Dimension.  Given a family F of subsets of a set U, find a subset of S of U of maximum cardinality, such that every subset of S can be written as the intersection of S with some set in F.



Contains [[Class_LOGSNP|$\\text{LOGSNP}$]], and is contained in [[Class_βP|$\\text{βP}$]] (indeed β,,2,,P).



The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists y such that for all j, the predicate φ(I,s,,j,,,x,y,j) holds.  Here x and y are logarithmic-length strings, or equivalently polynomially bounded numbers, and φ is computable in [[Class_P|$\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LOGNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LOGNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LOGSNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= LOGSNP - Logarithmically-Restricted SNP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems expressible in logical form as}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists j in S such that the predicate φ(I,s,,j,,,x,j) holds.  Here x is a logarithmic-length string, or equivalently a polynomially bounded number, and φ is computable in [[Class_P|$\\text{P}$]].



LOGSNP,,0,, is the subclass in which φ is a first-order predicate without quantifiers and x is a bounded lists of indices of input bits.  [[Class_LOGSNP|$\\text{LOGSNP}$]] is also the closure of LOGSNP,,0,, under many-one reduction.  See [[Class_LOGNP|$\\text{LOGNP}$]] and [[Class_SNP|$\\text{SNP}$]] for the motivation.



Defined in [[ZooRefs#PY96|[PY96] ]].



Contained in [[Class_LOGNP|$\\text{LOGNP}$]], and therefore [[Class_QPLIN|$\\text{QPLIN}$]].



If [[Class_P|$\\text{P}$]] = [[Class_LOGSNP|$\\text{LOGSNP}$]], then for every constructible f(n) > n, NTIME(f(n)) is contained in DTIME(g(n)^sqrt(g(n))^), where g(n) = O(f(n) logf(n)) [[ZooRefs#FK97|[FK97] ]].



The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists j such that the predicate φ(I,s,,j,,,x,j) holds.  Here x and y are logarithmic-length strings, or equivalently polynomially bounded numbers, and φ is computable in [[Class_P|$\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LOGSNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LOGSNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LWPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= LWPP - Length-Dependent Wide PP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "no," then the number of accepting computation paths exactly equals the number of rejecting paths.

If the answer is "yes," then the difference of these numbers equals a function f(|x|) computable in polynomial time (i.e. [[Class_FP|$\\text{FP}$]]).  Here |x| is the length of the input x, and ``polynomial time means polynomial in |x|, the length of x, rather than the length of |x|.



Defined in [[ZooRefs#FFK94|[FFK94] ]], where it was also shown that [[Class_LWPP|$\\text{LWPP}$]] is low for [[Class_PP|$\\text{PP}$]] and [[Class_C=P|$\\text{C}_\\text{=}\\text{P}$]].  (I.e. adding [[Class_LWPP|$\\text{LWPP}$]] as an oracle does not increase the power of these classes.)



Contained in [[Class_WPP|$\\text{WPP}$]] and [[Class_AWPP|$\\text{AWPP}$]].



Contains [[Class_SPP|$\\text{SPP}$]].



Also, contains the graph isomorphism problem [[ZooRefs#KST92|[KST92] ]].



Contains a whole litter of problems for solvable black-box groups: group intersection, group factorization, coset intersection, and double-coset membership [[ZooRefs#Vin04|[Vin04] ]].



Contains a whole litter of problems for solvable black-box groups: group intersection, group factorization, coset intersection, and double-coset membership [[ZooRefs#Vin04|[Vin04] ]]
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LWPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LWPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LkP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= L,,k,,P - Low Hierarchy In NP =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

The class of problems A such that Σ,,k,,P^A^ = Σ,,k,,P; that is, adding A as an oracle does not increase the power of the k^th^ level of the polynomial hierarchy.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



L,,1,,P = [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]].



For all k, L,,k,, is contained in L,,k+1,, and in [[Class_NP|$\\text{NP}$]].



Defined in [[ZooRefs#Sch83|[Sch83] ]].



See also [[Class_HkP|$\\text{H}_\\text{k}\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LkP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LkP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LogFew"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= LogFew - Logspace-Bounded Few =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NL|$\\text{NL}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The number of accepting paths on input x is f(x), and

The answer is 'yes' if and only if R(x,f(x))=1, where [[Class_R|$\\text{R}$]] is some predicate computable in [[Class_L|$\\text{L}$]].



Defined in [[ZooRefs#BDH+92|[BDH+92] ]], where it was also shown that [[Class_LogFew|$\\text{LogFew}$]] is contained in [[Class_ModkL|$\\text{Mod}_\\text{k}\\text{L}$]] for all k>1.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LogFew)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LogFew because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_LogFewNL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= LogFewNL - Logspace-Bounded FewP =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_FewP|$\\text{FewP}$]] but for logspace-bounded (i.e. [[Class_NL|$\\text{NL}$]]) machines.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BDH+92|[BDH+92] ]], where it was also shown that [[Class_LogFewNL|$\\text{LogFewNL}$]] is contained in [[Class_ModZkL|$\\text{ModZ}_\\text{k}\\text{L}$]] for all k>1.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_LogFewNL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save LogFewNL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MA"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MA - Merlin-Arthur =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a Merlin-Arthur protocol, which goes as follows.  Merlin, who has unbounded computational resources, sends Arthur a polynomial-size purported proof that the answer to the problem is "yes."  Arthur must verify the proof in [[Class_BPP|$\\text{BPP}$]] (i.e. probabilistic polynomial-time), so that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes," then there exists a proof such that Arthur accepts with probability at least 2/3.

If the answer is "no," then for all proofs Arthur accepts with probability at most 1/3.



An alternative definition requires that if the answer is "yes," then there exists a proof such that Arthur accepts with certainty.  However, the definitions with one-sided and two-sided error can be shown to be equivalent (see [[ZooRefs#FGM+89|[FGM+89] ]]).



Contains [[Class_NP|$\\text{NP}$]] and [[Class_BPP|$\\text{BPP}$]] 

(in fact also [[Class_∃BPP|$\\text{∃BPP}$]]), and is contained in [[Class_AM|$\\text{AM}$]] and in [[Class_QMA|$\\text{QMA}$]].



Also contained in [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] ∩ [[Class_Π2P|$\\text{Π}_\\text{2}\\text{P}$]].



There exists an oracle relative to which [[Class_BQP|$\\text{BQP}$]] is not in [[Class_MA|$\\text{MA}$]] [[ZooRefs#Wat00|[Wat00] ]].



Equals [[Class_NP|$\\text{NP}$]] under a derandomization assumption: if [[Class_E|$\\text{E}$]] requires exponentially-sized circuits, then [[Class_PromiseBPP|$\\text{PromiseBPP}$]] = [[Class_PromiseP|$\\text{PromiseP}$]], implying that [[Class_MA|$\\text{MA}$]] = [[Class_NP|$\\text{NP}$]] [[ZooRefs#IW97|[IW97] ]].



Shown in [[ZooRefs#San07|[San07] ]] that MA/1 does not have circuits of size $n^k$ for any $k>0$. In the same paper, the result was used to show that MA/1 cannot be solved on more than a $1/2 + 1/{n^k}$ fraction of inputs having length $n$ by any circuit of size $n^k$. Finally, it was shown that [[Class_MA|$\\text{MA}$]] does not have arithmetic circuits of size $n^k$.



See also: [[Class_MAE|$\\text{MA}_\\text{E}\\text{}$]], [[Class_MAEXP|$\\text{MA}_\\text{EXP}\\text{}$]].



An alternative definition requires that if the answer is "yes," then there exists a proof such that Arthur accepts with certainty.  However, the definitions with one-sided and two-sided error can be shown to be equivalent (exercise for the Zoo visitor).



Contains [[Class_NP|$\\text{NP}$]] and [[Class_∃BPP|$\\text{∃BPP}$]], and is contained in [[Class_AM|$\\text{AM}$]] and in [[Class_QMA|$\\text{QMA}$]].



Equals [[Class_NP|$\\text{NP}$]] under a derandomization assumption.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MA)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MA because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MA'"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MA' - Sparse MA =

----
CategoryClassical 

== Description ==

{{{#!description

The subclass of [[Class_MA|$\\text{MA}$]] such that for each input size n, there is a sparse set S,,n,, that Merlin's proof string always belongs to (no matter what the input is).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#KST93|[KST93] ]], where it is also observed that if graph isomorphism is in [[Class_P/poly|$\\text{P/poly}$]], then the complement of graph isomorphism is in [[Class_MA'|$\\text{MA'}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MA')>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MA' because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MAC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MAC^0^ - Majority of AC0 =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]], except now we're allowed a single unbounded-fanin majority gate at the root.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#JKS02|[JKS02] ]].



[[Class_MAC0|$\\text{MAC}^\\text{0}\\text{}$]] is strictly contained in [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] [[ZooRefs#ABF+94|[ABF+94] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MAC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MAC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MAE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MA,,E,, - Exponential-Time MA With Linear Exponent =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_MA|$\\text{MA}$]], except now Arthur is [[Class_E|$\\text{E}$]] instead of polynomial-time.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If [[Class_MAE|$\\text{MA}_\\text{E}\\text{}$]] = [[Class_NEE|$\\text{NEE}$]] then [[Class_MA|$\\text{MA}$]] = [[Class_NEXP|$\\text{NEXP}$]] ∩ [[Class_coNEXP|$\\text{coNEXP}$]] [[ZooRefs#IKW01|[IKW01] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MAE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MAE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MAEXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MA,,EXP,, - Exponential-Time MA =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_MA|$\\text{MA}$]], except now Arthur is [[Class_EXP|$\\text{EXP}$]] instead of polynomial-time, and the message from Merlin can be exponentially long.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



There is a problem in [[Class_MAEXP|$\\text{MA}_\\text{EXP}\\text{}$]] that does not have polynomial-size circuits [[ZooRefs#BFT98|[BFT98] ]].  On the other hand, there is an oracle relative to which every problem in [[Class_MAEXP|$\\text{MA}_\\text{EXP}\\text{}$]] does have polynomial-size circuits.



[[ZooRefs#MVW99|[MVW99] ]] considered the best circuit lower bound obtainable for a problem in [[Class_MAEXP|$\\text{MA}_\\text{EXP}\\text{}$]], using current techniques.  They found that this bound is half-exponential: i.e. a function f such that f(f(n))=2^n^.  Such functions exist, but are not expressible using standard asymptotic notation.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MAEXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MAEXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MAPOLYLOG"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MA,,POLYLOG,, - MA With Polylog Verifier =

----
CategoryClassical 

== Description ==

{{{#!description

Identical to [[Class_MA|$\\text{MA}$]] except for that Arthur (the verifier) has random access to the proof string given by Merlin, and is limited to running times of order $O(\\textrm{poly}(\\log n))$.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



This class was used by [[ZooRefs#SM03|[SM03] ]] to show that if [[Class_EXP|$\\text{EXP}$]] has circuits of polynomial size, then [[Class_EXP|$\\text{EXP}$]] = [[Class_MA|$\\text{MA}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MAPOLYLOG)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MAPOLYLOG because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MIP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MIP - Multi-Prover Interactive Proof =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_IP|$\\text{IP}$]], except that now the verifier can exchange messages with many provers, not just one.  The provers cannot communicate with each other during the execution of the protocol, so the verifier can "cross-check" their assertions (as with suspects in separate interrogation rooms).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BGK+88|[BGK+88] ]].



Let MIP[k] be the class of decision problems for which a "yes" answer can be verified with k provers.  Then for all k>2, MIP[k] = MIP[2] = [[Class_MIP|$\\text{MIP}$]] [[ZooRefs#BGK+88|[BGK+88] ]].



[[Class_MIP|$\\text{MIP}$]] equals [[Class_NEXP|$\\text{NEXP}$]] [[ZooRefs#BFL91|[BFL91] ]]; this is a famous non-relativizing result.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MIP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MIP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MIP*"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MIP* - MIP With Quantum Provers =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_MIP|$\\text{MIP}$]], except that the provers can share arbitrarily many entangled qubits.  The verifier is classical, as are all messages between the provers and verifier.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#CHT+04|[CHT+04] ]], where evidence was given suggesting that [[Class_MIP*|$\\text{MIP*}$]] does not "obviously" equal [[Class_NEXP|$\\text{NEXP}$]].



[[Class_MIP*|$\\text{MIP*}$]] contains [[Class_NEXP|$\\text{NEXP}$]] [[ZooRefs#IV12|[IV12] ]]. By contrast, [[Class_MIP|$\\text{MIP}$]], the corresponding class without entanglement, equals [[Class_NEXP|$\\text{NEXP}$]] (and even MIP[2,1] with two provers and one round equals [[Class_NEXP|$\\text{NEXP}$]]).



Even MIP*[4,poly] and MIP[5,1] contain [[Class_NEXP|$\\text{NEXP}$]] [[ZooRefs#IV12|[IV12] ]].



[[Class_MIP*[2,1]|$\\text{MIP*[2,1]}$]] contains [[Class_XOR-MIP*[2,1]|$\\text{XOR-MIP*[2,1]}$]].



In 2012 it was shown that [[Class_QMIP|$\\text{QMIP}$]] = [[Class_MIP*|$\\text{MIP*}$]] [[ZooRefs#RUV12|[RUV12] ]]
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MIP*)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MIP* because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MIP*[2,1]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MIP*[2,1] - 2-Prover, 1-Round MIP With Quantum Provers =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as MIP[2], except that now only one round is allowed, and the two provers can share arbitrarily many entangled qubits.  The verifier is classical, as are all messages between the provers and verifier.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#CHT+04|[CHT+04] ]], where evidence was given suggesting that [[Class_MIP*|$\\text{MIP*}$]] does not "obviously" equal [[Class_NEXP|$\\text{NEXP}$]].  By contrast, MIP[2,1], the corresponding class without entanglement, equals [[Class_NEXP|$\\text{NEXP}$]].



Indeed, the relationship between [[Class_MIP*|$\\text{MIP*}$]] and [[Class_MIP|$\\text{MIP}$]] = [[Class_NEXP|$\\text{NEXP}$]] is completely unknown -- either could contain the other, or they could be incomparable.



It is also unknown whether increasing the number of provers or rounds changes [[Class_MIP*[2,1]|$\\text{MIP*[2,1]}$]].



Contains [[Class_XOR-MIP*[2,1]|$\\text{XOR-MIP*[2,1]}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MIP*[2,1])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MIP*[2,1] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MIPEXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MIP,,EXP,, - Exponential-Time Multi-Prover Interactive Proof =

----
CategoryClassical 

== Description ==

{{{#!description

The exponential-time analogue of [[Class_MIP|$\\text{MIP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



In the unrelativized world, equals [[Class_NEEXP|$\\text{NEEXP}$]].



There exists an oracle relative to which [[Class_MIPEXP|$\\text{MIP}_\\text{EXP}\\text{}$]] equals the intersection of [[Class_P/poly|$\\text{P/poly}$]], [[Class_PNP|$\\text{P}^\\text{NP}\\text{}$]], and [[Class_⊕P|$\\text{⊕P}$]] [[ZooRefs#BFT98|[BFT98] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MIPEXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MIPEXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MM"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MM - Problems reducible to matrix multiplication =

----
CategoryClassical 

== Description ==

{{{#!description

The set of all problems reducible to matrix multiplication. That is, the set of problems $P$ that can be reduced to the multiplication of two square matrices can be reduced to $P$ in linear time.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Currently, the best known algorithm for multiplying two $n\\times n$ matrices is the Coppersmith–Winograd_algorithm, which has a time complexity of $O(n^{2.376})$ [[ZooRefs#CW90|[CW90] ]]. Note that for the general problem, a lower bound of $\\Omega(n^2)$ is trivial from the number of elements being considered.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MM)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MM because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MMSNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MMSNP - Monadic Monotone SNP =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#FV93|[FV93] ]] as a subclass of [[Class_SNP|$\\text{SNP}$]].  There are three syntactic restrictions defining the subclass [[Class_MMSNP|$\\text{MMSNP}$]], based on the form of the [[Class_SNP|$\\text{SNP}$]] formula defining the language:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The second order existentially quantified variables, known as the proof relations, are restricted to be monadic.  (Monadic relations can be treated as sets.)

 Any relations in the formula other than the proof relations must occur only negated (the formula is monotone).

 No inequality relations can occur in the formula.



[[Class_MMSNP|$\\text{MMSNP}$]] seems to obey dichotomy, by excluding languages that are NP-intermediate.  This is still open but widely believed.  Dropping any of the restrictions monotone/monadic/without inequalities allows NP-intermediate languages unless [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]], since any problem in [[Class_NP|$\\text{NP}$]] is polynomial time equivalent to a problem in each of these broader classes.  [[Class_MMSNP|$\\text{MMSNP}$]] therefore seems to be a maximal fragment of [[Class_NP|$\\text{NP}$]] where NP-intermediate languages are excluded.



Every constraint satisfaction problem with a fixed target structure is expressible in [[Class_MMSNP|$\\text{MMSNP}$]], and there is a polynomial time Turing reduction from every [[Class_MMSNP|$\\text{MMSNP}$]] query to finitely many constraint satisfaction problems.  [[Class_MMSNP|$\\text{MMSNP}$]] therefore seems to capture the class of constraint satisfaction problems with fixed templates, [[Class_CSP|$\\text{CSP}$]].



Defined in [[ZooRefs#FV93|[FV93] ]] as a subclass of [[Class_SNP|$\\text{SNP}$]], where the second order existentially quantified variables are sets (monadic) and any relations in the first-order part occur negated (monotone).  Further, no inequalities can occur in the first-order part.



[[Class_MMSNP|$\\text{MMSNP}$]] seems to obey dichotomy, by excluding Ladner languages.  This is still open but widely believed.  Dropping any of the restrictions monotone/monadic/without inequalities          allows Ladner languages unless [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]], since any problem in [[Class_NP|$\\text{NP}$]] is polynomial time equivalent to a problem in each of these broader classes.  [[Class_MMSNP|$\\text{MMSNP}$]] therefore seems to be a maximal fragment of [[Class_NP|$\\text{NP}$]] where Ladner languages are excluded.



Every constraint satisfaction problem is expressible in [[Class_MMSNP|$\\text{MMSNP}$]], and there is a polynomial time Turing reduction from every [[Class_MMSNP|$\\text{MMSNP}$]] query to finitely many constraint satisfaction problems.  [[Class_MMSNP|$\\text{MMSNP}$]] therefore seems to capture the class of constraint satisfaction problems.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MMSNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MMSNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MP - Middle-Bit P =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems such that for some [[Class_SharpP|$\\text{#P}$]] function f, the answer on input x is 'yes' if and only if the middle bit of f(x) is 1.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GKR+95|[GKR+95] ]].



Contains [[Class_AmpMP|$\\text{AmpMP}$]] and [[Class_PH|$\\text{PH}$]].



[[Class_MP|$\\text{MP}$]] with [[Class_ModP|$\\text{ModP}$]] oracle equals [[Class_MP|$\\text{MP}$]] with [[Class_SharpP|$\\text{#P}$]] oracle [[ZooRefs#KT96|[KT96] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MPC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MPC - Monotone Planar Circuits =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a family of monotone stratified planar circuits (a uniformity condition may also be imposed).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Such a circuit can contain only AND and OR gates of bounded fanin.  It must be embeddable in the plane with no wires crossing.  Furthermore, the input bits can only be accessed at the bottom level, where they are listed in order (x,,1,,,...,x,,n,,).



Defined in [[ZooRefs#DC89|[DC89] ]].



[[ZooRefs#BLM+99|[BLM+99] ]] showed that we can assume without loss of generality that the circuit has width n and depth n^3^.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MPC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MPC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MaxNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MaxNP - Maximization NP =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_NP|$\\text{NP}$]] as [[Class_MaxSNP|$\\text{MaxSNP}$]] does to [[Class_SNP|$\\text{SNP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_MaxPB|$\\text{MaxPB}$]].



The closure of [[Class_MaxNP|$\\text{MaxNP}$]] under [[Class_PTAS|$\\text{PTAS}$]] reduction is [[Class_APX|$\\text{APX}$]] [[ZooRefs#KMS+99|[KMS+99] ]], [[ZooRefs#CT94|[CT94] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MaxNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MaxNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MaxPB"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MaxPB - MaxNP Polynomially Bounded =

----
CategoryClassical 

== Description ==

{{{#!description

The subclass of [[Class_MaxNP|$\\text{MaxNP}$]] problems for which the cost function is guaranteed always to be bounded by a polynomial.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_MinPB|$\\text{MinPB}$]] can be defined similarly.



Defined in [[ZooRefs#KT94|[KT94] ]].



The closure of [[Class_MaxPB|$\\text{MaxPB}$]] under [[Class_PTAS|$\\text{PTAS}$]] reductions equals [[Class_NPOPB|$\\text{NPOPB}$]] [[ZooRefs#CKS+99|[CKS+99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MaxPB)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MaxPB because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MaxSNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MaxSNP - Maximization SNP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of optimization problems reducible by an "L-reduction" to a problem in [[Class_MaxSNP0|$\\text{MaxSNP}_\\text{0}\\text{}$]].  (Note: 'L' stands for linear -- this is not the same as an [[Class_L|$\\text{L}$]] reduction!  For more details see [[ZooRefs#PY88|[PY88] ]].)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#PY88|[PY88] ]], where the following was also shown:



Max3SAT is MaxSNP-complete.  (Max3SAT is the problem of finding an assignment that maximizes the number of satisfied clauses in a CNF formula with at most 3 literals per clause.)

Any problem in [[Class_MaxSNP|$\\text{MaxSNP}$]] can be approximated to within a fixed ratio.



The closure of [[Class_MaxSNP|$\\text{MaxSNP}$]] under [[Class_PTAS|$\\text{PTAS}$]] reduction is [[Class_APX|$\\text{APX}$]] [[ZooRefs#KMS+99|[KMS+99] ]], [[ZooRefs#CT94|[CT94] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MaxSNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MaxSNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MaxSNP0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MaxSNP,,0,, - Generating Class of MaxSNP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of function problems expressible as "find a relation such that the set of k-tuples for which a given [[Class_SNP|$\\text{SNP}$]] predicate holds has maximum cardinality."}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



For example (see [[ZooRefs#Pap94|[Pap94] ]]), the Max-Cut problem can be expressed as follows:



Given a graph G, find a subset S of vertices that maximizes the number of pairs (u,v) of vertices such that u is in S, and v is not in S, and G has an edge from u to v.



Defined in [[ZooRefs#PY88|[PY88] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MaxSNP0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MaxSNP0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_MinPB"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= MinPB - MinNP Polynomially Bounded =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_MaxPB|$\\text{MaxPB}$]] but for minimization instead of maximization problems.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_MinPB)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save MinPB because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ModL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ModL - ModL =

----
CategoryClassical 

== Description ==

{{{#!description

A language $L\\in\\mathsf{ModL}$ if there are functions $f\\in\\mathsf{GapL}$ and $g\\in\\mathsf{FL}$ such that for all strings $x$:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



There exists a prime p and a natural number \alpha such that g(x)=0^{p^{\alpha}}.

 x\in [[Class_L|$\\text{L}$]] if and only if f(x)\equiv0(\left|g(x)\right|).



Thus, for any prime $p$ and natural number $\\alpha$, $\\mathsf{Mod}_{p^{\\alpha}}\\mathsf{L}\\subseteq\\mathsf{ModL}$. Moreover, FL^ModL^ = FL^GapL^ [[ZooRefs#AV04|[AV04] ]].



Defined in [[ZooRefs#AV04|[AV04] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ModL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ModL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ModP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ModP - ModkP With Arbitrary k =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a [[Class_ModkP|$\\text{Mod}_\\text{k}\\text{P}$]] machine where k can vary depending on the input.  The only requirement is that 0^k^ be computable in polynomial time.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#KT96|[KT96] ]], where it was also shown that [[Class_ModP|$\\text{ModP}$]] is contained in [[Class_AmpMP|$\\text{AmpMP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ModP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ModP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ModZkL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ModZ,,k,,L - Restricted ModkL =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a nondeterministic logspace Turing machine, such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes," then the number of accepting paths is not congruent to 0 mod k.

If the answer is "no," then there are no accepting paths.



Defined in [[ZooRefs#BDH+92|[BDH+92] ]], where it was also shown that [[Class_ModZkL|$\\text{ModZ}_\\text{k}\\text{L}$]] contains [[Class_LogFewNL|$\\text{LogFewNL}$]] for all k>1.



Contained in [[Class_ModkL|$\\text{Mod}_\\text{k}\\text{L}$]] and in [[Class_NL|$\\text{NL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ModZkL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ModZkL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ModkL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Mod,,k,,L - Mod-k L =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_ModkP|$\\text{Mod}_\\text{k}\\text{P}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



For any prime k, [[Class_ModkL|$\\text{Mod}_\\text{k}\\text{L}$]] contains [[Class_SL|$\\text{SL}$]] [[ZooRefs#KW93|[KW93] ]].



For any prime k, Mod,,k,,L^ModkL^ = [[Class_ModkL|$\\text{Mod}_\\text{k}\\text{L}$]] [[ZooRefs#HRV00|[HRV00] ]].



For any k>1, contains [[Class_LogFew|$\\text{LogFew}$]] [[ZooRefs#BDH+92|[BDH+92] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ModkL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ModkL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ModkP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Mod,,k,,P - Mod-k Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

For any k>1: The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that the number of accepting paths is divisible by k, if and only if the answer is "no."}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Mod,,2,,P is more commonly known as [[Class_⊕P|$\\text{⊕P}$]] "parity-P."



For every k, [[Class_ModkP|$\\text{Mod}_\\text{k}\\text{P}$]] contains graph isomorphism [[ZooRefs#AK02|[AK02] ]].



Defined in [[ZooRefs#CH89|[CH89] ]], [[ZooRefs#Her90|[Her90] ]].



[[ZooRefs#Her90|[Her90] ]] and [[ZooRefs#BG92|[BG92] ]] showed that [[Class_ModkP|$\\text{Mod}_\\text{k}\\text{P}$]] is the set of unions of languages in Mod,,p,,P for each prime p that divides k.  In particular, if p is prime, then Mod,,p,,P = Mod,,p^m,,P for all positive integers m.  A further fact is that Mod,,p,,P is closed under union, intersection, and complement for p prime.



On the other hand, if k is not a prime power, then there exists an oracle relative to which [[Class_ModkP|$\\text{Mod}_\\text{k}\\text{P}$]] is not closed under intersection or complement [[ZooRefs#BBR94|[BBR94] ]].



For prime p, there exists an oracle relative to which Mod,,p,,P does not contain [[Class_EQP|$\\text{EQP}$]] [[ZooRefs#GV02|[GV02] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ModkP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ModkP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NAuxPDAp"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NAuxPDA^p^ - Nondeterministic Auxiliary Pushdown Automata =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by nondeterministic logarithmic-space and polynomial-time Turing machines with auxiliary pushdown.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_LOGCFL|$\\text{LOGCFL}$]] [[ZooRefs#Sud78|[Sud78] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NAuxPDAp)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NAuxPDAp because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NC - Nick's Class =

----
CategoryClassical 

== Description ==

{{{#!description

(Named in honor of Nick Pippenger.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



NC^i^ is the class of decision problems solvable by a uniform family of Boolean circuits, with polynomial size, depth O(log^i^(n)), and fan-in 2.



Then [[Class_NC|$\\text{NC}$]] is the union of NC^i^ over all nonnegative i.



Also, [[Class_NC|$\\text{NC}$]] equals the union of PT/WK(log^k^n, n^k^)/poly over all constants k.



NC^i^ is contained in AC^i^; thus, [[Class_NC|$\\text{NC}$]] = [[Class_AC|$\\text{AC}$]].



Contains [[Class_NL|$\\text{NL}$]].



Generalizations include [[Class_RNC|$\\text{RNC}$]] and [[Class_QNC|$\\text{QNC}$]].



[[ZooRefs#IN96|[IN96] ]] construct a candidate pseudorandom generator in [[Class_NC|$\\text{NC}$]] based on the subset sum problem.



For a random oracle A, (NC^i^)^A^ is strictly contained in (NC^i+1^)^A^, and uniform NC^A^ is strictly contained in P^A^, with probability 1 [[ZooRefs#Mil92|[Mil92] ]].



In descriptive complexity, [[Class_NC|$\\text{NC}$]] can be defined by FO[ \log(n)^{O(1)}]



NC^i^ is the class of decision problems solvable by a nonuniform family of Boolean circuits, with polynomial size, depth O(log^i^(n)), and fan-in 2.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NC^0^ - Level 0 of NC =

----
CategoryClassical 

== Description ==

{{{#!description

By definition, a decision problem in [[Class_NC0|$\\text{NC}^\\text{0}\\text{}$]] can depend on only a constant number of bits of the input.  Thus, [[Class_NC0|$\\text{NC}^\\text{0}\\text{}$]] usually refers to functions computable by constant-depth, bounded-fanin circuits.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



There is a family of permutations computable by a uniform family of [[Class_NC0|$\\text{NC}^\\text{0}\\text{}$]] circuits that is P-hard to invert [[ZooRefs#Has88|[Has88] ]].



Recently [[ZooRefs#AIK04|[AIK04] ]] solved a longstanding open problem by showing that there exist pseudorandom generators and one-way functions in [[Class_NC0|$\\text{NC}^\\text{0}\\text{}$]], based on (for example) the hardness of factoring.  Specifically, in these generators every bit of the output depends on only 4 input bits.  Whether the dependence can be reduced to 3 bits under the same cryptographic assumptions is open, but [[ZooRefs#AIK04|[AIK04] ]] have some partial results in this direction.  It is known that the dependence cannot be reduced to 2 bits.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NC1"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NC^1^ - Level 1 of NC =

----
CategoryClassical 

== Description ==

{{{#!description

See [[Class_NC|$\\text{NC}$]] for definition.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[ZooRefs#KV94|[KV94] ]] give a family of functions that is computable in [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]], but not efficiently learnable unless there exists an efficient algorithm for factoring Blum integers.



Was shown to equal 5-PBP [[ZooRefs#Bar89|[Bar89] ]].  On the other hand, width 5 is necessary unless [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] = [[Class_ACC0|$\\text{ACC}^\\text{0}\\text{}$]] [[ZooRefs#BT88|[BT88] ]].



As an application of this result, [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] can be simulated on a quantum computer with three qubits, one initialized to a pure state and the remaining two in the maximally mixed state [[ZooRefs#ASV00|[ASV00] ]].  Surprisingly, [[ZooRefs#AMP02|[AMP02] ]] showed that only a single qubit is needed to simulate [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] - i.e. that [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] is contained in 2-EQBP.  (Complex amplitudes are needed for this result.)



Is contained in [[Class_L|$\\text{L}$]] [[ZooRefs#Bor77|[Bor77] ]].



Contains [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]].



[[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] contains the integer division problem [[ZooRefs#BCH86|[BCH86] ]], even if an L-uniformity condition is imposed [[ZooRefs#CDL01|[CDL01] ]].



U,,E^*^,,-uniform [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] is equal to [[Class_ALOGTIME|$\\text{ALOGTIME}$]] [[ZooRefs#RUZ81|[RUZ81] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NC1)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NC1 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NC2"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NC^2^ - Level 2 of NC =

----
CategoryClassical 

== Description ==

{{{#!description

See [[Class_NC|$\\text{NC}$]] for definition.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_NL|$\\text{NL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NC2)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NC2 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NE - Nondeterministic E =

----
CategoryClassical 

== Description ==

{{{#!description

Nondeterministic exponential time with linear exponent (i.e. NTIME(2^O(n)^)).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



P^NE^ = NP^NE^ [[ZooRefs#Hem89|[Hem89] ]].



Contained in [[Class_NEXP|$\\text{NEXP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NE/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NE/poly - Nonuniform NE =

----
CategoryClassical 

== Description ==

{{{#!description

Contains [[Class_coNE|$\\text{coNE}$]], just as [[Class_NEXP/poly|$\\text{NEXP/poly}$]] contains [[Class_coNEXP|$\\text{coNEXP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NE/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NE/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NEE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NEE - Nondeterministic EE =

----
CategoryClassical 

== Description ==

{{{#!description

Nondeterministic double-exponential time with linear exponent (i.e. NTIME(2^2^O(n)^^)).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If [[Class_MAE|$\\text{MA}_\\text{E}\\text{}$]] = [[Class_NEE|$\\text{NEE}$]] then [[Class_MA|$\\text{MA}$]] = [[Class_NEXP|$\\text{NEXP}$]] ∩ [[Class_coNEXP|$\\text{coNEXP}$]] [[ZooRefs#IKW01|[IKW01] ]].



Contained in [[Class_NEEXP|$\\text{NEEXP}$]].



Nondeterministic double-exponential time with linear exponent (i.e. NTIME(2^2^O(n)^)).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NEE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NEE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NEEE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NEEE - Nondeterministic EEE =

----
CategoryClassical 

== Description ==

{{{#!description

Nondeterministic triple-exponential time with linear exponent.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NEEE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NEEE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NEEXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NEEXP - Nondeterministic EEXP =

----
CategoryClassical 

== Description ==

{{{#!description

Nondeterministic double-exponential time (i.e. NTIME(2^2^p(n)^^) for p a polynomial).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_MIPEXP|$\\text{MIP}_\\text{EXP}\\text{}$]] (unrelativized).



Nondeterministic double-exponential time (i.e. NTIME(2^2^p(n)^) for p a polynomial).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NEEXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NEEXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NEXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NEXP - Nondeterministic EXP =

----
CategoryClassical 

== Description ==

{{{#!description

Nondeterministic exponential time (i.e. NTIME(2^p(n)^) for p a polynomial).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_MIP|$\\text{MIP}$]] [[ZooRefs#BFL91|[BFL91] ]] (but not relative to all oracles).



[[Class_NEXP|$\\text{NEXP}$]] is in [[Class_MIP*|$\\text{MIP*}$]] [[ZooRefs#IV12|[IV12] ]].



[[Class_NEXP|$\\text{NEXP}$]] is in [[Class_P/poly|$\\text{P/poly}$]] if and only if [[Class_NEXP|$\\text{NEXP}$]] = [[Class_MA|$\\text{MA}$]] [[ZooRefs#IKW01|[IKW01] ]].



[[ZooRefs#KI02|[KI02] ]] show the following:



If [[Class_P|$\\text{P}$]] = [[Class_RP|$\\text{RP}$]], then [[Class_NEXP|$\\text{NEXP}$]] is not computable by polynomial-size arithmetic circuits.

If [[Class_P|$\\text{P}$]] = [[Class_BPP|$\\text{BPP}$]] and if checking whether a Boolean circuit computes a function that is close to a low-degree polynomial over a finite field is in [[Class_P|$\\text{P}$]], then [[Class_NEXP|$\\text{NEXP}$]] is not in [[Class_P/poly|$\\text{P/poly}$]].

If [[Class_NEXP|$\\text{NEXP}$]] is in [[Class_P/poly|$\\text{P/poly}$]], then matrix permanent is NEXP-complete.



Does not equal [[Class_NP|$\\text{NP}$]] [[ZooRefs#SFM78|[SFM78] ]].



Does not equal [[Class_EXP|$\\text{EXP}$]] if and only if there is a sparse set in [[Class_NP|$\\text{NP}$]] that is not in [[Class_P|$\\text{P}$]].



There exists an oracle relative to which [[Class_EXP|$\\text{EXP}$]] = [[Class_NEXP|$\\text{NEXP}$]] but still [[Class_P|$\\text{P}$]] does not equal [[Class_NP|$\\text{NP}$]] [[ZooRefs#Dek76|[Dek76] ]].



The theory of reals with addition (see [[Class_EXPSPACE|$\\text{EXPSPACE}$]]) is hard for [[Class_NEXP|$\\text{NEXP}$]] [[ZooRefs#FR74|[FR74] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NEXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NEXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NEXP/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NEXP/poly - Nonuniform NEXP =

----
CategoryClassical 

== Description ==

{{{#!description

Contains [[Class_coNEXP|$\\text{coNEXP}$]] (folklore result reported in [weblog]).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NEXP/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NEXP/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NIPZK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NIPZK - Non-Interactive PZK =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [M08] based on [[ZooRefs#DDPY98|[DDPY98] ]],[[ZooRefs#BFM88|[BFM88] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_PZK|$\\text{PZK}$]].



[M08] showed a complete promise-problem for [[Class_NIPZK|$\\text{NIPZK}$]], called Unifrom (UN). Instances 

in UN are circuits with n+1 output bits. The first n bits represent the uniform distribution, and the last bit is 1 with probability at least 2/3. For instances not in UN, when the last bit is 1, at most 1/3 of the strings of length n can appear as the output of the circuit. The problem is to decide which is the case.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NIPZK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NIPZK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NIQSZK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NIQSZK - Non-Interactive QSZK =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_QSZK|$\\text{QSZK}$]] as [[Class_NISZK|$\\text{NISZK}$]] does to [[Class_SZK|$\\text{SZK}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Kob02|[Kob02] ]], where it was also shown that the following promise problem is complete for [[Class_NIQSZK|$\\text{NIQSZK}$]].  Given a quantum circuit, we are promised that the state it prepares (when run on the all-0 state, and tracing out non-output qubits) has trace distance either at most 1/3 or at least 2/3 from the maximally mixed state. The problem is to output "no" in the former case and "yes" in the latter.



NIQPZK can be defined similarly.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NIQSZK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NIQSZK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NISZK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NISZK - Non-Interactive SZK =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#DDP+98|[DDP+98] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_SZK|$\\text{SZK}$]].



[[ZooRefs#GSV99|[GSV99] ]] showed the following:



If [[Class_SZK|$\\text{SZK}$]] does not equal [[Class_BPP|$\\text{BPP}$]] then [[Class_NISZK|$\\text{NISZK}$]] does not equal [[Class_BPP|$\\text{BPP}$]].

[[Class_NISZK|$\\text{NISZK}$]] equals [[Class_SZK|$\\text{SZK}$]] if and only if [[Class_NISZK|$\\text{NISZK}$]] is closed under complement.

[[Class_NISZK|$\\text{NISZK}$]] has natural complete promise problems:

  

    Statistical Distance from Uniform (SDU): Given a circuit, consider the distribution over outputs when the circuit is given a uniformly random n-bit string.  We're promised that the trace distance between this distribution and the uniform distribution is either at most 1/3 or at least 2/3.  The problem is to output "yes" in the former case and "no" in the latter.

    Entropy Approximation (EA): Now we're promised that the entropy of the circuit's output distribution is either at least k+1 or at most k-1.  The problem is to output "yes" in the former case and "no" in the latter.



[[Class_NIPZK|$\\text{NIPZK}$]] can be defined similarly.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NISZK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NISZK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NISZKh"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NISZK,,h,, - NISZK With Limited Help =

----
CategoryClassical 

== Description ==

{{{#!description

The non-interactive analogue of [[Class_SZKh|$\\text{SZK}_\\text{h}\\text{}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BG03|[BG03] ]], where the following was also shown:



[[Class_NISZKh|$\\text{NISZK}_\\text{h}\\text{}$]] contains [[Class_NISZK|$\\text{NISZK}$]] and is contained in [[Class_SZK|$\\text{SZK}$]].

Graph Isomorphism is in [[Class_NISZKh|$\\text{NISZK}_\\text{h}\\text{}$]].

The following problem is complete for [[Class_NISZKh|$\\text{NISZK}_\\text{h}\\text{}$]]: Given two functions from {0,1}^n^ to {0,1}^n^ (specified by circuits), decide whether their ranges are almost equal or almost disjoint, given that one of these is the case.



The quantum lower bound for the set comparison problem in [[ZooRefs#Aar02|[Aar02] ]] implies an oracle relative to which [[Class_NISZKh|$\\text{NISZK}_\\text{h}\\text{}$]] is not in [[Class_BQP|$\\text{BQP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NISZKh)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NISZKh because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NL - Nondeterministic Logarithmic-Space =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_NP|$\\text{NP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



In a breakthrough result, was shown to equal [[Class_coNL|$\\text{coNL}$]] [[ZooRefs#Imm88|[Imm88] ]] [[ZooRefs#Sze87|[Sze87] ]].  (Though contrast to [[Class_mNL|$\\text{mNL}$]].)



Is contained in [[Class_LOGCFL|$\\text{LOGCFL}$]] [[ZooRefs#Sud78|[Sud78] ]], as well as [[Class_NC2|$\\text{NC}^\\text{2}\\text{}$]].



Is contained in [[Class_UL/poly|$\\text{UL/poly}$]] [[ZooRefs#RA00|[RA00] ]].



Deciding whether a bipartite graph has a perfect matching is hard for [[Class_NL|$\\text{NL}$]] [[ZooRefs#KUW86|[KUW86] ]].



[[Class_NL|$\\text{NL}$]] can be defined in a logical formalism as SO(krom) and also as FO(tc), reachability in directed graph is NL-Complete under FO-reduction.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NL/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NL/poly - Nonuniform NL =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_NL|$\\text{NL}$]] as [[Class_P/poly|$\\text{P/poly}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Is contained in [[Class_⊕L/poly|$\\text{⊕L/poly}$]] [[ZooRefs#GW96|[GW96] ]], as well as [[Class_SAC1|$\\text{SAC}^\\text{1}\\text{}$]].



Equals [[Class_UL/poly|$\\text{UL/poly}$]] [[ZooRefs#RA00|[RA00] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NL/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NL/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NLIN"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NLIN - Nondeterministic LIN =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_LIN|$\\text{LIN}$]] as [[Class_NP|$\\text{NP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NLIN)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NLIN because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NLOG"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NLOG - NL With Nondeterministic Oracle Tape =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_NL|$\\text{NL}$]] -- but if there's an oracle, then [[Class_NLOG|$\\text{NLOG}$]] can make queries nondeterministically on a polynomial-size, one-way oracle tape.  ([[Class_NL|$\\text{NL}$]], by contrast, can use nondeterministic transitions only on the worktape; oracle queries have to be deterministic.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



See [[ZooRefs#LL76|[LL76] ]] or [[ZooRefs#HCK+88|[HCK+88] ]] for more information.



Although [[Class_NLOG|$\\text{NLOG}$]] is contained in [[Class_P|$\\text{P}$]], there exists an oracle relative to which that is not the case.  This illustrates that care is needed when defining oracle access mechanisms.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NLOG)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NLOG because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NLT"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NLT - Nearly Linear Time =

----
CategoryClassical 

== Description ==

{{{#!description

Class of functions computable in nearly linear time n(log n)^O(1)^ on deterministic random access machines.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GS89|[GS89] ]].



See also [[Class_QL|$\\text{QL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NLT)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NLT because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NNC(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NNC(f(n)) - NC with O(f(n)) nondeterministic gates =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_NC|$\\text{NC}$]], but with O(f(n)) nondeterministic gates. A nondeterministic gate has no inputs and a single output bit.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Wol94|[Wol94] ]], where the author proves various inclusions, including but not limited to NNC(poly(n))=NP, NNC(log(n))=NC, and NNC(polylog)⊆DSPACE(polylog).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NNC(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NNC(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NNLT"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NNLT - Nondeterministic Nearly Linear Time =

----
CategoryClassical 

== Description ==

{{{#!description

Class of functions computable in nearly linear time n(log n)^O(1)^ on nondeterministic random access machines.  Equals [[Class_NQL|$\\text{NQL}$]] [[ZooRefs#GS89|[GS89] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GS89|[GS89] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NNLT)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NNLT because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NONE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NONE - The Empty Class =

----
CategoryClassical 

== Description ==

{{{#!description

The class that does not contain any languages.  (It might not surprise you that I put this one in at the suggestion of a mathematician...)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Is the opposite of [[Class_ALL|$\\text{ALL}$]], but does not equal the complement coALL = [[Class_ALL|$\\text{ALL}$]].



Is closed under polynomial-time Turing reductions :-).



Equals [[Class_SPARSE|$\\text{SPARSE}$]] ∩ [[Class_coSPARSE|$\\text{coSPARSE}$]] and [[Class_TALLY|$\\text{TALLY}$]] ∩ coTALLY.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NONE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NONE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NP - Nondeterministic Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of dashed hopes and idle dreams.}}}

== Complete Problem ==

{{{#!complete_problem

<<Include(Problem_k-SAT, "k-SAT", 3, from="^== Description ==$", to="^== Properties ==$")>>

}}}

== Comments ==



More formally: an "NP machine" is a nondeterministic polynomial-time Turing machine.



Then [[Class_NP|$\\text{NP}$]] is the class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that



If the answer is "yes," at least one computation path accepts.

If the answer is "no," all computation paths reject.



Equivalently, [[Class_NP|$\\text{NP}$]] is the class of decision problems such that, if the answer is "yes," then there is a proof of this fact, of length polynomial in the size of the input, that can be verified in [[Class_P|$\\text{P}$]] (i.e. by a deterministic polynomial-time algorithm).  On the other hand, if the answer is "no," then the algorithm must declare invalid any purported proof that the answer is "yes."



For example, the SAT problem is to decide whether a given Boolean formula has any satisfying truth assignments. SAT is in [[Class_NP|$\\text{NP}$]], since a "yes" answer can be proved by just exhibiting a satisfying assignment.



A decision problem is NP-complete if (1) it is in [[Class_NP|$\\text{NP}$]], and (2) any problem in [[Class_NP|$\\text{NP}$]] can be reduced to it (under some notion of reduction).  The class of NP-complete problems is sometimes called [[Class_NPC|$\\text{NPC}$]].



That NP-complete problems exist is immediate from the definition.  The seminal result of Cook [[ZooRefs#Coo71|[Coo71] ]], Karp [[ZooRefs#Kar72|[Kar72] ]], and Levin [[ZooRefs#Lev73|[Lev73] ]] is that many natural problems (that have nothing to do with Turing machines) are NP-complete.



The first such problem to be shown NP-complete was SAT [[ZooRefs#Coo71|[Coo71] ]].  Other classic NP-complete problems include:



3-Colorability: Given a graph, can each vertex be colored red, green, or blue so that no two neighboring vertices have the same color?

Hamiltonian Cycle: Given a graph, is there a cycle that visits each vertex exactly once?

Traveling Salesperson: Given a set of n cities, and the distance

between each pair of cities, is there a route that visits each city exactly

once before returning to the starting city, and has length at most T?

Maximum Clique: Given a graph, are there k vertices all of which are neighbors of each other?

Subset Sum: Given a collection of integers, is there a subset of the integers that sums to exactly x?



For many, many more NP-complete problems, see [[ZooRefs#GJ79|[GJ79] ]].



[[Class_NP|$\\text{NP}$]] contains [[Class_P|$\\text{P}$]].  I've discovered a marvelous proof that [[Class_NP|$\\text{NP}$]] and [[Class_P|$\\text{P}$]] are unequal, but this web page is too small to contain it.  Too bad, since otherwise I'd be eligible for $1,000,000 [[ZooRefs#CMI00|[CMI00] ]].



There exists an oracle relative to which [[Class_P|$\\text{P}$]] and [[Class_NP|$\\text{NP}$]] are unequal [[ZooRefs#BGS75|[BGS75] ]].  Indeed, [[Class_P|$\\text{P}$]] and [[Class_NP|$\\text{NP}$]] are unequal relative to a random oracle with probability 1 [[ZooRefs#BG81|[BG81] ]] (see [[ZooRefs#AFM01|[AFM01] ]] for a novel take on this result).  Though random oracle results are not always indicative about the unrelativized case [[ZooRefs#CCG+94|[CCG+94] ]].



There even exists an oracle relative to which the [[Class_P|$\\text{P}$]] versus [[Class_NP|$\\text{NP}$]] problem is outside the usual axioms of set theory [[ZooRefs#HH76|[HH76] ]].



If we restrict to monotone classes, [[Class_mP|$\\text{mP}$]] is strictly contained in [[Class_mNP|$\\text{mNP}$]] [[ZooRefs#Raz85|[Raz85] ]].



Perhaps the most important insight anyone has had into [[Class_P|$\\text{P}$]] versus [[Class_NP|$\\text{NP}$]] is to be found in [[ZooRefs#RR97|[RR97] ]].  There the authors show that no 'natural proof' can separate [[Class_P|$\\text{P}$]] from [[Class_NP|$\\text{NP}$]] (or more precisely, place [[Class_NP|$\\text{NP}$]] outside of [[Class_P/poly|$\\text{P/poly}$]]), unless secure pseudorandom generators do not exist.  A proof is 'natural' if it satisfies two conditions called constructivity and largeness; essentially all lower bound techniques known to date satisfy these conditions.  To obtain unnatural proof techniques, some people suspect we need to relate [[Class_P|$\\text{P}$]] versus [[Class_NP|$\\text{NP}$]] to heavy-duty 'traditional' mathematics, for instance algebraic geometry.  See [[ZooRefs#MS02|[MS02] ]] (and the survey article [[ZooRefs#Reg02|[Reg02] ]]) for a development of this point of view.



For more on [[Class_P|$\\text{P}$]] versus [[Class_NP|$\\text{NP}$]] (circa 1992) see [[ZooRefs#Sip92|[Sip92] ]].  For an opinion poll, see [[ZooRefs#Gas02|[Gas02] ]].



If [[Class_P|$\\text{P}$]] equals [[Class_NP|$\\text{NP}$]], then [[Class_NP|$\\text{NP}$]] equals its complement [[Class_coNP|$\\text{coNP}$]].  Whether [[Class_NP|$\\text{NP}$]] equals [[Class_coNP|$\\text{coNP}$]] is also open.  [[Class_NP|$\\text{NP}$]] and [[Class_coNP|$\\text{coNP}$]] can be extended to the polynomial hierarchy [[Class_PH|$\\text{PH}$]].



The set of decision problems in [[Class_NP|$\\text{NP}$]], but not in [[Class_P|$\\text{P}$]] or [[Class_NPC|$\\text{NPC}$]], is sometimes called [[Class_NPI|$\\text{NPI}$]].  If [[Class_P|$\\text{P}$]] does not equal [[Class_NP|$\\text{NP}$]] then [[Class_NPI|$\\text{NPI}$]] is nonempty [[ZooRefs#Lad75|[Lad75] ]].



Probabilistic generalizations of [[Class_NP|$\\text{NP}$]] include [[Class_MA|$\\text{MA}$]] and [[Class_AM|$\\text{AM}$]].  If [[Class_NP|$\\text{NP}$]] is in [[Class_coAM|$\\text{coAM}$]] (or [[Class_BPP|$\\text{BPP}$]]) then [[Class_PH|$\\text{PH}$]] collapses to [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] [[ZooRefs#BHZ87|[BHZ87] ]].



[[Class_PH|$\\text{PH}$]] also collapses to [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] if [[Class_NP|$\\text{NP}$]] is in [[Class_P/poly|$\\text{P/poly}$]] [[ZooRefs#KL82|[KL82] ]].



There exist oracles relative to which [[Class_NP|$\\text{NP}$]] is not in [[Class_BQP|$\\text{BQP}$]] [[ZooRefs#BBB+97|[BBB+97] ]].



An alternate characterization is [[Class_NP|$\\text{NP}$]] = PCP(log n, O(1)) [[ZooRefs#ALM+98|[ALM+98] ]].



Also, [[ZooRefs#Fag74|[Fag74] ]] showed that [[Class_NP|$\\text{NP}$]] is precisely the class of decision problems reducible to a graph-theoretic property expressible in second-order existential logic. This leads to the subclass [[Class_SNP|$\\text{SNP}$]].



It is known that if any NP-complete language is sparse (contains no more than a polynomial number of strings of length $n$), then [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]]. [[ZooRefs#BH08|[BH08] ]] improved this result, showing that if any language in [[Class_NP|$\\text{NP}$]] has an NP-hard set of subexponential density, then [[Class_coNP|$\\text{coNP}$]] is contained in [[Class_NP/poly|$\\text{NP/poly}$]] and thus, by [[ZooRefs#Yap82|[Yap82] ]], [[Class_PH|$\\text{PH}$]] collapses to the third level.



[[Class_NP|$\\text{NP}$]] is equal to [[Class_SO-E|$\\text{SO-E}$]], the second-order queries where the second-order quantifiers are only existantials.



For example, the SAT problem is to decide whether a given Boolean formula has any satisfying truth assignments.  SAT is in [[Class_NP|$\\text{NP}$]], since a "yes" answer can be proved by just exhibiting a satisfying assignment.



Also, [[ZooRefs#Fag74|[Fag74] ]] gave a logical characterization of [[Class_NP|$\\text{NP}$]], which leads to the subclass [[Class_SNP|$\\text{SNP}$]].
== Relations ==

{{{#!class_relations
{"version": 1.0, "class": "NP", "relations": {"contained_in": [{"class": "EXP"}], "equals": [{"class": "PCP(r(n),q(n))", "condition": "$r(n) = \\\\log(n), q(n) = O(1)$"}]}}
}}}


== See Also ==

<<FullSearch(linkto:Class_NP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NP ∩ coNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NP ∩ coNP - NP ∩ coNP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems in both [[Class_NP|$\\text{NP}$]] and [[Class_coNP|$\\text{coNP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains factoring [[ZooRefs#Pra75|[Pra75] ]].



Contains graph isomorphism under the assumption that some language in [[Class_NE|$\\text{NE}$]] ∩ [[Class_coNE|$\\text{coNE}$]] requires nondeterministic circuits of size 2^Ω(n)^ ([[ZooRefs#MV99|[MV99] ]], improving [[ZooRefs#KM99|[KM99] ]]).  (A nondeterministic circuit C has two inputs, x and y, and accepts on x if there exists a y such that C(x,y)=1.)



Equals [[Class_PNP|$\\text{P}^\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}\\text{}$]] [[ZooRefs#Bra79|[Bra79] ]].  In particular, if a problem in [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]] is NP-hard with Turing reduction, then [[Class_NP|$\\text{NP}$]] = [[Class_coNP|$\\text{coNP}$]].



Is not believed to contain complete problems.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NP ∩ coNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NP ∩ coNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NP/log"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NP/log - NP With Logarithmic Advice =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_NP/poly|$\\text{NP/poly}$]], except that now the advice string is logarithmic-size.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Shown in [[ZooRefs#FK05|[FK05] ]] that [[Class_EXP|$\\text{EXP}$]] ⊆ [[Class_NP/log|$\\text{NP/log}$]] if and only if [[Class_EXP|$\\text{EXP}$]] = [[Class_P||NP|$\\text{P}^\\text{||NP}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NP/log)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NP/log because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NP/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NP/poly - Nonuniform NP =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_NP|$\\text{NP}$]] as [[Class_P/poly|$\\text{P/poly}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_AM|$\\text{AM}$]].  On the other hand, if [[Class_NP/poly|$\\text{NP/poly}$]] contains [[Class_coNP|$\\text{coNP}$]] then [[Class_PH|$\\text{PH}$]] collapses to the third level.



NP/poly-natural proofs cannot show that circuit families are outside [[Class_P/poly|$\\text{P/poly}$]], under a pseudorandomness assumption [[ZooRefs#Rud97|[Rud97] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NP/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NP/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NP,,C,, - NP Over The Complex Numbers =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems such that (1) they're in [[Class_NP|$\\text{NP}$]] and (2) every problem in [[Class_NP|$\\text{NP}$]] is reducible to them (under some notion of reduction).  In other words, the hardest problems in [[Class_NP|$\\text{NP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Two notions of reduction from problem A to problem B are usually considered:



Karp or many-one reductions.  Here a polynomial-time algorithm is given as input an instance of problem A, and must produce as output an instance of problem B.

Turing reductions, in this context also called Cook reductions.  Here the algorithm for problem B can make arbitrarily many calls to an oracle for problem A.



Some examples of NP-complete problems are discussed under the entry for [[Class_NP|$\\text{NP}$]].



The classic reference on [[Class_NPC|$\\text{NPC}$]] is [[ZooRefs#GJ79|[GJ79] ]].



Unless [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]], [[Class_NPC|$\\text{NPC}$]] does not contain any sparse problems: that is, problems such that the number of 'yes' instances of size n is upper-bounded by a polynomial in n [[ZooRefs#Mah82|[Mah82] ]].



A famous conjecture [[ZooRefs#BH77|[BH77] ]] asserts that all NP-complete problems are polynomial-time isomorphic -- i.e. between any two problems, there is a one-to-one and onto Karp reduction. If that's true, the NP-complete problems could be interpreted as mere "relabelings" of one another.



NP-complete problems are p-superterse unless [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]] [[ZooRefs#BKS95|[BKS95] ]].  This means that, given k Boolean formulas F,,1,,,...,F,,k,,, if you can rule out even one of the 2^k^ possibilities in polynomial time (e.g., "if F,,1,,,...,F,,k-1,, are all unsatisfiable then F,,k,, is satisfiable"), then [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]].



An analog of [[Class_NP|$\\text{NP}$]] for Turing machines over a complex number field.



Defined in [[ZooRefs#BCS+97|[BCS+97] ]].



It is unknown whether [[Class_PC|$\\text{P}_\\text{C}\\text{}$]] = [[Class_NPC|$\\text{NP}_\\text{C}\\text{}$]], nor are implications known among this question, [[Class_PR|$\\text{P}_\\text{R}\\text{}$]] versus [[Class_NPR|$\\text{NP}_\\text{R}\\text{}$]], and [[Class_P|$\\text{P}$]] versus [[Class_NP|$\\text{NP}$]].



However, [[ZooRefs#CKK+95|[CKK+95] ]] show that if [[Class_P/poly|$\\text{P/poly}$]] does not equal [[Class_NP/poly|$\\text{NP/poly}$]] then [[Class_PC|$\\text{P}_\\text{C}\\text{}$]] does not equal [[Class_NPC|$\\text{NP}_\\text{C}\\text{}$]].



[[ZooRefs#BCS+97|[BCS+97] ]] show the following striking result.  For a positive integer n, let t(n) denote the minimum number of additions, subtractions, and multiplications needed to construct n, starting from 1.  If for every sequence {n,,k,,} of positive integers, t(n,,k,, k!) grows faster than polylogarithmically in k, then [[Class_PC|$\\text{P}_\\text{C}\\text{}$]] does not equal [[Class_NPC|$\\text{NP}_\\text{C}\\text{}$]].



See also [[Class_VNPk|$\\text{VNP}_\\text{k}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPI"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPI - NP-Intermediate =

----
CategoryClassical 

== Description ==

{{{#!description

Sometimes used to denote the set of decision problems in [[Class_NP|$\\text{NP}$]] that are neither NP-complete (that is, in [[Class_NPC|$\\text{NPC}$]]) nor in [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Is thought to contain (for example) decision versions of factoring and graph isomorphism.



Is nonempty if [[Class_P|$\\text{P}$]] does not equal [[Class_NP|$\\text{NP}$]] [[ZooRefs#Lad75|[Lad75] ]].  Indeed, under this assumption, it contains an infinite number of distinct polynomial-time equivalence classes.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPI)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPI because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPMV"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPMV - NP Multiple Value =

----
CategoryClassical 

== Description ==

{{{#!description

The class of all (possibly partial, possibly multivalued) functions computed by an [[Class_NP|$\\text{NP}$]] machine as follows: ignore the rejecting paths, and consider any output of an accepting path to be "one of the outputs."}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_NPSV|$\\text{NPSV}$]] and [[Class_NPMVt|$\\text{NPMV}_\\text{t}\\text{}$]].



Defined in [[ZooRefs#BLS84|[BLS84] ]].



Contrast with [[Class_FNP|$\\text{FNP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPMV)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPMV because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPMV-sel"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPMV-sel - NPMV Selective =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_NPMV|$\\text{NPMV}$]] as [[Class_P-Sel|$\\text{P-Sel}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#HHN+95|[HHN+95] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPMV-sel)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPMV-sel because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPMVt"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPMV,,t,, - NPMV Total =

----
CategoryClassical 

== Description ==

{{{#!description

The class of all (possibly multivalued) [[Class_NPMV|$\\text{NPMV}$]] functions that are total (that is, defined for every input).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPMVt)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPMVt because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPMVt-sel"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPMV,,t,,-sel - NPMVt Selective =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_NPMVt|$\\text{NPMV}_\\text{t}\\text{}$]] as [[Class_P-Sel|$\\text{P-Sel}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#HHN+95|[HHN+95] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPMVt-sel)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPMVt-sel because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPO"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPO - NP Optimization =

----
CategoryClassical 

== Description ==

{{{#!description

The class of function problems of the form, "Find any n-bit string x that maximizes a cost function C(x), where C is computable in [[Class_FP|$\\text{FP}$]] (i.e. polynomial-time)."}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#ACG+99|[ACG+99] ]].



Contains [[Class_APX|$\\text{APX}$]] and [[Class_NPOPB|$\\text{NPOPB}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPO)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPO because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPOPB"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPOPB - NPO Polynomially Bounded =

----
CategoryClassical 

== Description ==

{{{#!description

The subclass of [[Class_NPO|$\\text{NPO}$]] problems for which the cost function is guaranteed always to be bounded by a polynomial in n (the input size).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



See [[ZooRefs#ACG+99|[ACG+99] ]].



[[Class_NPOPB|$\\text{NPOPB}$]] equals the closure of [[Class_MaxPB|$\\text{MaxPB}$]] under [[Class_PTAS|$\\text{PTAS}$]] reductions [[ZooRefs#CKS+99|[CKS+99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPOPB)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPOPB because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPR"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NP,,R,, - NP Over The Reals =

----
CategoryClassical 

== Description ==

{{{#!description

An analog of [[Class_NP|$\\text{NP}$]] for Turing machines over a real number field.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BCS+97|[BCS+97] ]].



It is unknown whether [[Class_PR|$\\text{P}_\\text{R}\\text{}$]] = [[Class_NPR|$\\text{NP}_\\text{R}\\text{}$]], nor are implications known among this question, [[Class_PC|$\\text{P}_\\text{C}\\text{}$]] versus [[Class_NPC|$\\text{NP}_\\text{C}\\text{}$]], and [[Class_P|$\\text{P}$]] versus [[Class_NP|$\\text{NP}$]].



Also, in contrast to the case of [[Class_NPC|$\\text{NP}_\\text{C}\\text{}$]], it is an open problem to show that [[Class_P/poly|$\\text{P/poly}$]] distinct from [[Class_NP/poly|$\\text{NP/poly}$]] implies [[Class_PR|$\\text{P}_\\text{R}\\text{}$]] distinct from [[Class_NPR|$\\text{NP}_\\text{R}\\text{}$]].  The difference is that in the real case, a comparison (or greater-than) operator is available, and it is not known how much power this yields in comparison to the complex case.



See also [[Class_VNPk|$\\text{VNP}_\\text{k}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPR)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPR because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPSPACE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPSPACE - Nondeterministic PSPACE =

----
CategoryClassical 

== Description ==

{{{#!description

Equals [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#Sav70|[Sav70] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



On the other hand, this result does not relativize if we allow strings of unbounded length to be written to the oracle tape.  In particular, there exists an oracle relative to which [[Class_NPSPACE|$\\text{NPSPACE}$]] is not contained in [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#GTW+91|[GTW+91] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPSPACE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPSPACE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPSV"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPSV - NP Single Value =

----
CategoryClassical 

== Description ==

{{{#!description

The class of [[Class_NPMV|$\\text{NPMV}$]] functions that are single-valued (i.e., such that every accepting path outputs the same value).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BLS84|[BLS84] ]].



Contains [[Class_NPSVt|$\\text{NPSV}_\\text{t}\\text{}$]].



[[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]] if and only if [[Class_FP|$\\text{FP}$]] = [[Class_NPSV|$\\text{NPSV}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPSV)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPSV because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPSV-sel"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPSV-sel - NPSV Selective =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_NPSV|$\\text{NPSV}$]] as [[Class_P-Sel|$\\text{P-Sel}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#HHN+95|[HHN+95] ]].



Has the same relation to href="#npsv">NPSV as [[Class_P-Sel|$\\text{P-Sel}$]] does to [[Class_P|$\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPSV-sel)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPSV-sel because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPSVt"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPSV,,t,, - NPSV Total =

----
CategoryClassical 

== Description ==

{{{#!description

The class of all [[Class_NPSV|$\\text{NPSV}$]] functions that are total (that is, defined on every input).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_NPMVt|$\\text{NPMV}_\\text{t}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPSVt)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPSVt because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPSVt-sel"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NPSV,,t,,-sel - NPSVt Selective =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_NPSVt|$\\text{NPSV}_\\text{t}\\text{}$]] as [[Class_P-Sel|$\\text{P-Sel}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Also known as NP-sel.



Defined in [[ZooRefs#HHN+95|[HHN+95] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPSVt-sel)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPSVt-sel because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NP^cc^ - Communication Complexity NP =

----
CategoryClassical 

== Description ==

{{{#!description

The analogue of [[Class_Pcc|$\\text{P}^\\text{cc}\\text{}$]] for nondeterministic communication complexity.  Both communication bits and nondeterministic guess bits count toward the complexity.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Does not equal [[Class_Pcc|$\\text{P}^\\text{cc}\\text{}$]] or [[Class_coNPcc|$\\text{coNP}^\\text{cc}\\text{}$]] because of the EQUALITY problem.  Also, does not contain [[Class_BPPcc|$\\text{BPP}^\\text{cc}\\text{}$]] because of that problem.



Defined in [[ZooRefs#BFS86|[BFS86] ]].



Contained in [[Class_PHcc|$\\text{PH}^\\text{cc}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NPkcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NP,,k,,^cc^ - NPcc in NOF model,  players =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_NPcc|$\\text{NP}^\\text{cc}\\text{}$]] and [[Class_NP|$\\text{NP}$]] as [[Class_Pkcc|$\\text{P}_\\text{k}\\text{}^\\text{cc}\\text{}$]] does to [[Class_Pcc|$\\text{P}^\\text{cc}\\text{}$]] and [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_NPkcc|$\\text{NP}_\\text{k}\\text{}^\\text{cc}\\text{}$]] is not contained in [[Class_BPPkcc|$\\text{BPP}_\\text{k}\\text{}^\\text{cc}\\text{}$]] for $k\\le(1-\\delta)\\cdot\\log n$ players, for any constant $\\delta>0$. As a result, [[Class_NPkcc|$\\text{NP}_\\text{k}\\text{}^\\text{cc}\\text{}$]] is not equal to [[Class_RPkcc|$\\text{RP}_\\text{k}\\text{}^\\text{cc}\\text{}$]] under the same conditions [[ZooRefs#DP08|[DP08] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NPkcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NPkcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NQL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NQL - Nondet Quasi-Linear =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems that can be decided in quasi-linear time by a multitape nondeterministic Turing machine.  Quasi-linear here means n(log n)^k^ + k, for some k.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_NNLT|$\\text{NNLT}$]].



SAT is NQL-complete under quasi-linear-time reductions (which can be computed in deterministic quasi-linear time) [[ZooRefs#Sch78|[Sch78] ]].



Defined in [[ZooRefs#Sch78|[Sch78] ]].



See also: [[Class_NLT|$\\text{NLT}$]], [[Class_Q|$\\text{Q}$]], [[Class_QL|$\\text{QL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NQL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NQL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NQP - Nondeterministic Quantum Polynomial-Time =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems solvable by a QTM in polynomial time such that a particular '|Accept>' state has nonzero amplitude at the end of the computation, if and only if the answer is 'yes.'  Since it has an exact amplitude condition, [[Class_NQP|$\\text{NQP}$]] has the same technical caveats as [[Class_EQP|$\\text{EQP}$]].  Or it would, except that it turns out to equal [[Class_coC=P|$\\text{coC}_\\text{=}\\text{P}$]] [[ZooRefs#FGH+98|[FGH+98] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#ADH97|[ADH97] ]].



Contrast with [[Class_QMA|$\\text{QMA}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NSPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NSPACE(f(n)) - Nondeterministic f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_NPSPACE|$\\text{NPSPACE}$]], but with f(n)-space (for some constructible function f) rather than polynomial-space machines.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in DSPACE(f(n)^2^) [[ZooRefs#Sav70|[Sav70] ]], and indeed RevSPACE(f(n)^2^) 95|[[ZooRefs#CP95|[CP95] ]].



NSPACE(n^k^) is strictly contained in NSPACE(n^k+ε^) for ε>0 [[ZooRefs#Iba72|[Iba72] ]] (actually the hierarchy theorem is stronger than this, but pretty technical to state).



Contained in DSPACE(f(n)^2^) [[ZooRefs#Sav70|[Sav70] ]], and indeed RevSPACE(f(n)^2^) [[ZooRefs#CP95|[CP95] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NSPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NSPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NT"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NT - Near-Testable =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems such that whether the answer on input x agrees with the answer on input x-1 (that is, the lexicographic predecessor of x) is solvable in polynomial time.  The Turing machine has to decide agreement or disagreement without access to the answer for x-1.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Is contained in [[Class_E|$\\text{E}$]], [[Class_NT*|$\\text{NT*}$]], and [[Class_⊕P|$\\text{⊕P}$]].  Defined in [[ZooRefs#GHJ+91|[GHJ+91] ]] to study ⊕P-complete problems.  They show  that [[Class_P|$\\text{P}$]], [[Class_NT|$\\text{NT}$]], [[Class_NT*|$\\text{NT*}$]], and [[Class_⊕P|$\\text{⊕P}$]] are either all equal or strictly nested.  In particular, they differ with probability 1 relative to a random oracle.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NT)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NT because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NT*"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NT* - Near-Testable With Forest Ordering =

----
CategoryClassical 

== Description ==

{{{#!description

Defined like [[Class_NT|$\\text{NT}$]], but with a more general ordering on inputs.  A problem [[Class_L|$\\text{L}$]] is in [[Class_NT*|$\\text{NT*}$]] if, first, there is a partially defined predecessor function pred(x) in [[Class_FP|$\\text{FP}$]] that organizes the space of inputs into a forest.  The size of the lineage of each x must also be bounded by 2^poly(|x|)^.  Second, if L(x) is the Boolean answer to [[Class_L|$\\text{L}$]] on input x, then L(x)+L(pred(x)) is computable in polynomial time; or if pred(x) does not exist, L(x) is computable in polynomial time.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GHJ+91|[GHJ+91] ]].



Contains [[Class_NT|$\\text{NT}$]] and is contained in [[Class_⊕P|$\\text{⊕P}$]].  The inclusions are either both strict or both equalities (whence [[Class_⊕P|$\\text{⊕P}$]] = [[Class_P|$\\text{P}$]] as well).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NT*)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NT* because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_NTIME(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NTIME(f(n)) - Nondeterministic f(n)-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_NP|$\\text{NP}$]], but with f(n)-time (for some constructible function f) rather than polynomial-time machines.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The Nondeterministic Time Hierarchy Theorem: If f and g are time-constructible and f(n+1)=o(g), then NTIME(f(n)) does not equal NTIME(g(n)) [[ZooRefs#SFM78|[SFM78] ]] (this is actually stronger than the hierarchy theorem for DTIME).



NTIME(n) strictly contains DTIME(n) [[ZooRefs#PPS+83|[PPS+83] ]] (this result does not work for arbitrary f(n)).



For any constructible superpolynomial f, NTIME(f(n)) with [[Class_NP|$\\text{NP}$]] oracle is not in [[Class_P/poly|$\\text{P/poly}$]] [[ZooRefs#Kan82|[Kan82] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_NTIME(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save NTIME(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Nearly-P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Nearly-P - Languages Superpolynomially Close to P =

----
CategoryClassical 

== Description ==

{{{#!description

The set of languages [[Class_L|$\\text{L}$]] such that for every k, there is a language L_k in [[Class_P|$\\text{P}$]] that differs from [[Class_L|$\\text{L}$]] on at most 2^n^/n^k^ inputs of length n.  Discussed in [[ZooRefs#NS05|[NS05] ]] and implicitly defined in [[ZooRefs#Yam99|[Yam99] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The set of languages [[Class_L|$\\text{L}$]] such that for every k, there is a language L_k in [[Class_P|$\\text{P}$]] that differs from [[Class_L|$\\text{L}$]] on at most 2^n/n^k inputs of length n.  Discussed in [[ZooRefs#NS05|[NS05] ]] and implicitly defined in [[ZooRefs#Yam99|[Yam99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Nearly-P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Nearly-P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_OCQ"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= OCQ - One Clean Qubit =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by a [[Class_BQP|$\\text{BQP}$]] machine in which a single qubit is initialized to the '0' state, and the remaining qubits are initialized to the maximally mixed state.  (This definition is not known to be robust, so one also needs to specify a gate set.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



We also need to stipulate that there are no "strong measurements" -- intermediate measurements on which later operations are conditioned -- since otherwise we can do all of [[Class_BQP|$\\text{BQP}$]] by first initializing the computer to the all-0 state.  Parker and Plenio [[ZooRefs#PP00|[PP00] ]] failed to appreciate this point.



Defined by [[ZooRefs#ASV00|[ASV00] ]] (though they didn't use the name [[Class_OCQ|$\\text{OCQ}$]]), who also showed that if [[Class_OCQ|$\\text{OCQ}$]] = [[Class_BQP|$\\text{BQP}$]], something other than gate-by-gate simulation will be needed to show this.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_OCQ)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save OCQ because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_OptP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= OptP - Optimum Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of functions computable by taking the maximum of the output values over all accepting paths of an [[Class_NP|$\\text{NP}$]] machine.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Kre88|[Kre88] ]].



Contrast with [[Class_FNP|$\\text{FNP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_OptP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save OptP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P - Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class that started it all.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of decision problems solvable in polynomial time by a Turing machine.  (See also [[Class_FP|$\\text{FP}$]], for function problems.)



Defined in [[ZooRefs#Edm65|[Edm65] ]], [[ZooRefs#Cob64|[Cob64] ]], [[ZooRefs#Rab60|[Rab60] ]], and other seminal early papers.



Contains some highly nontrivial problems, including linear programming [[ZooRefs#Kha79|[Kha79] ]] and finding a maximum matching in a general graph [[ZooRefs#Edm65|[Edm65] ]].



Contains the problem of testing whether an integer is prime [[ZooRefs#AKS02|[AKS02] ]], an important result that improved on a proof requiring an assumption of the generalized Riemann hypothesis [[ZooRefs#Mil76|[Mil76] ]].



A decision problem is P-complete if it is in [[Class_P|$\\text{P}$]], and if every problem in [[Class_P|$\\text{P}$]] can be reduced to it in [[Class_L|$\\text{L}$]] (logarithmic space).  The canonical P-complete problem is circuit evaluation: given a Boolean circuit and an input, decide what the circuit outputs when given the input.



Important subclasses of [[Class_P|$\\text{P}$]] include [[Class_L|$\\text{L}$]], [[Class_NL|$\\text{NL}$]], [[Class_NC|$\\text{NC}$]], and [[Class_SC|$\\text{SC}$]].



[[Class_P|$\\text{P}$]] is contained in [[Class_NP|$\\text{NP}$]], but whether they're equal seemed to be an open problem when I last checked.



Efforts to generalize [[Class_P|$\\text{P}$]] resulted in [[Class_BPP|$\\text{BPP}$]] and [[Class_BQP|$\\text{BQP}$]].



The nonuniform version is [[Class_P/poly|$\\text{P/poly}$]], the monotone version is [[Class_mP|$\\text{mP}$]], and versions over the real and complex number fields are [[Class_PR|$\\text{P}_\\text{R}\\text{}$]] and [[Class_PC|$\\text{P}_\\text{C}\\text{}$]] respectively.



In descriptive complexity, [[Class_P|$\\text{P}$]] can be defined by three different kind of formulae, FO(lfp) which is also FO(n^{O(1)})], and also as SO(Horn)



[[Class_P|$\\text{P}$]] queries are exactly the one that can be written in the While^/cons^ languages.
== Relations ==

{{{#!class_relations
{"version": 1.0, "class": "P", "relations": {"contained_in": [{"class": "EXP"}, {"class": "NP"}], "equals": []}}
}}}


== See Also ==

<<FullSearch(linkto:Class_P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PSharpP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^#P^ - P With #P Oracle =

----
CategoryClassical 

== Description ==

{{{#!description

I decided this class is so important that it deserves an entry of its own, apart from [[Class_SharpP|$\\text{#P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_PH|$\\text{PH}$]] [[ZooRefs#Tod89|[Tod89] ]], and is contained in [[Class_PSPACE|$\\text{PSPACE}$]].



Equals [[Class_PPP|$\\text{P}^\\text{PP}\\text{}$]] (exercise for the visitor).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PSharpP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PSharpP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PSharpP[1]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^#P[1]^ - P With Single Query To #P Oracle =

----
CategoryClassical 

== Description ==

{{{#!description

Contains [[Class_PH|$\\text{PH}$]] [[ZooRefs#Tod89|[Tod89] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PSharpP[1])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PSharpP[1] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_P-Close"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P-Close - Problems Close to P =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a polynomial-time algorithm that outputs the wrong answer on only a sparse (that is, polynomially-bounded) set of instances.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Yes83|[Yes83] ]].



Contains [[Class_Almost-P|$\\text{Almost-P}$]] and is contained in [[Class_P/poly|$\\text{P/poly}$]] [[ZooRefs#Sch86|[Sch86] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_P-Close)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save P-Close because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_P-OBDD"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P-OBDD - Polynomial-Size Ordered Binary Decision Diagram =

----
CategoryClassical 

== Description ==

{{{#!description

An ordered binary decision diagram (OBDD) is a branching program (see [[Class_k-PBP|$\\text{k-PBP}$]]), with the additional constraint that if x,,i,, is queried before x,,j,, on any path, then i<j.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Then [[Class_P-OBDD|$\\text{P-OBDD}$]] is the class of decision problems solvable by polynomial-size OBDD's.



Contained in [[Class_PBP|$\\text{PBP}$]], as well as [[Class_BPP-OBDD|$\\text{BPP-OBDD}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_P-OBDD)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save P-OBDD because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_P-Sel"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P-Sel - P-Selective Sets =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which there's a polynomial-time algorithm with the following property.  Whenever it's given two instances, a "yes" and a "no" instance, the algorithm can always decide which is the "yes" instance.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Sel79|[Sel79] ]], where it was also shown that if [[Class_NP|$\\text{NP}$]] is contained in [[Class_P-Sel|$\\text{P-Sel}$]] then [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]].



There exist P-selective sets that are not recursive (i.e. not in [[Class_R|$\\text{R}$]]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_P-Sel)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save P-Sel because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_P/log"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P/log - P With Logarithmic Advice =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_P/poly|$\\text{P/poly}$]], except that the advice string for input size n can have length at most logarithmic in n, rather than polynomial.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Strictly contained in [[Class_IC[log,poly]|$\\text{IC[log,poly]}$]].



If [[Class_NP|$\\text{NP}$]] is contained in [[Class_P/log|$\\text{P/log}$]] then [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_P/log)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save P/log because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_P/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P/poly - Nonuniform Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a family of polynomial-size Boolean circuits.  The family can be nonuniform; that is, there could be a completely different circuit for each input length.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equivalently, [[Class_P/poly|$\\text{P/poly}$]] is the class of decision problems solvable by a polynomial-time Turing machine that receives an 'advice string,' that depends only on the size n of the input, and that itself has size upper-bounded by a polynomial in n.



Contains [[Class_BPP|$\\text{BPP}$]] by the progenitor of derandomization arguments [[ZooRefs#Adl78|[Adl78] ]] [[ZooRefs#KL82|[KL82] ]].  By extension, BPP/poly, BPP/mpoly, and BPP/rpoly all equal [[Class_P/poly|$\\text{P/poly}$]]. (By contrast, there is an oracle relative to which [[Class_BPP/log|$\\text{BPP/log}$]] does not equal [[Class_BPP/mlog|$\\text{BPP/mlog}$]], while [[Class_BPP/mlog|$\\text{BPP/mlog}$]] and [[Class_BPP/rlog|$\\text{BPP/rlog}$]] are not equal relative to any oracle.)



[[ZooRefs#KL82|[KL82] ]] showed that, if [[Class_P/poly|$\\text{P/poly}$]] contains [[Class_NP|$\\text{NP}$]], then [[Class_PH|$\\text{PH}$]] collapses to the second level, [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]].



They also showed:



If [[Class_PSPACE|$\\text{PSPACE}$]] is in [[Class_P/poly|$\\text{P/poly}$]] then [[Class_PSPACE|$\\text{PSPACE}$]] equals [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] ∩ [[Class_Π2P|$\\text{Π}_\\text{2}\\text{P}$]].

If [[Class_EXP|$\\text{EXP}$]] is in [[Class_P/poly|$\\text{P/poly}$]] then [[Class_EXP|$\\text{EXP}$]] = [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]].



It was later shown that, if [[Class_NP|$\\text{NP}$]] is contained in [[Class_P/poly|$\\text{P/poly}$]], then [[Class_PH|$\\text{PH}$]] collapses to ZPP^NP^ [[ZooRefs#KW98|[KW98] ]] and indeed [[Class_S2P|$\\text{S}_\\text{2}\\text{P}$]] [[ZooRefs#Cai01|[Cai01] ]]. This seems close to optimal, since there exists an oracle relative to which the collapse cannot be improved to [[Class_Δ2P|$\\text{Δ}_\\text{2}\\text{P}$]] [[ZooRefs#Wil85|[Wil85] ]].



If [[Class_NP|$\\text{NP}$]] is not contained in [[Class_P/poly|$\\text{P/poly}$]], then [[Class_P|$\\text{P}$]] does not equal [[Class_NP|$\\text{NP}$]].  Much of the effort toward separating [[Class_P|$\\text{P}$]] from [[Class_NP|$\\text{NP}$]] is based on this observation.  However, a 'natural proof' as defined by [[ZooRefs#RR97|[RR97] ]] cannot be used to show [[Class_NP|$\\text{NP}$]] is outside [[Class_P/poly|$\\text{P/poly}$]], if there is any pseudorandom generator in [[Class_P/poly|$\\text{P/poly}$]] that has hardness 2^Ω(n^ε)^ for some ε>0.



If [[Class_NP|$\\text{NP}$]] is contained in [[Class_P/poly|$\\text{P/poly}$]], then [[Class_MA|$\\text{MA}$]] = [[Class_AM|$\\text{AM}$]] [[ZooRefs#AKS+95|[AKS+95] ]]



The monotone version of [[Class_P/poly|$\\text{P/poly}$]] is [[Class_mP/poly|$\\text{mP/poly}$]].



[[Class_P/poly|$\\text{P/poly}$]] has measure 0 in [[Class_E|$\\text{E}$]] with [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] oracle [May94b].



Strictly contains [[Class_IC[log,poly]|$\\text{IC[log,poly]}$]] and [[Class_P/log|$\\text{P/log}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_P/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save P/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PAC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PAC^0^ - Probabilistic AC0 =

----
CategoryClassical 

== Description ==

{{{#!description

The Political Action Committee for computational complexity research.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of problems for which there exists a [[Class_DiffAC0|$\\text{DiffAC}^\\text{0}\\text{}$]] function f such that the answer is "yes" on input x if and only if f(x)>0.



Equals [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] and [[Class_C=AC0|$\\text{C}_\\text{=}\\text{AC}^\\text{0}\\text{}$]] under logspace uniformity [[ZooRefs#ABL98|[ABL98] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PAC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PAC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PBP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PBP - Polynomial-Size Branching Program =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_k-PBP|$\\text{k-PBP}$]] but with no width restriction.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_L/poly|$\\text{L/poly}$]] [[ZooRefs#Cob66|[Cob66] ]].



Contains [[Class_P-OBDD|$\\text{P-OBDD}$]], BP,,d,,(P).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PBP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PBP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P,,C,, - Polynomial-Time Over The Complex Numbers =

----
CategoryClassical 

== Description ==

{{{#!description

An analog of [[Class_P|$\\text{P}$]] for Turing machines over a complex number field.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BCS+97|[BCS+97] ]].



See also [[Class_PR|$\\text{P}_\\text{R}\\text{}$]], [[Class_NPC|$\\text{NP}_\\text{C}\\text{}$]], [[Class_NPR|$\\text{NP}_\\text{R}\\text{}$]], [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PCD(r(n),q(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PCD(r(n),q(n)) - Probabilistically Checkable Debate =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems decidable by a probabilistically checkable debate system, as follows.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Two debaters B and C alternate writing strings on a "debate tape," with B arguing that the answer is "yes" and C arguing the answer is "no."  Then a polynomial-time verifier flips O(r(n)) random coins and makes O(q(n)) nonadaptive queries to the debate tape (meaning that they depend only on the input and the random coins, not the results of previous queries).  The verifier then outputs an answer, which should be correct with high probability.



Defined in [[ZooRefs#CFL+93|[CFL+93] ]], who also showed that PCD(log n, 1) = [[Class_PSPACE|$\\text{PSPACE}$]].  This result was used to show that certain problems are PSPACE-hard even to approximate.



Contained in GPCD(r(n),q(n)).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PCD(r(n),q(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PCD(r(n),q(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PCP(r(n),q(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PCP(r(n),q(n)) - Probabilistically Checkable Proof =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems such that a "yes" answer can be verified by a probabilistically checkable proof, as follows.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The verifier is a polynomial-time Turing machine with access to O(r(n)) uniformly random bits.  It has random access to a proof (which might be exponentially long), but can query only O(q(n)) bits of the proof.



Then we require the following:



If the answer is "yes," there exists a proof such that the verifier accepts with certainty.

If the answer is "no," then for all proofs the verifier rejects with probability at least 1/2 (over the choice of the O(r(n)) random bits).



Defined in [[ZooRefs#AS98|[AS98] ]].



By definition [[Class_NP|$\\text{NP}$]] = PCP(0,poly(n)).



[[Class_MIP|$\\text{MIP}$]] = PCP(poly(n),poly(n)).



PCP(r(n),q(n)) is contained in NTIME(2^O(r(n))^q(n) + poly(n)).



[[Class_NP|$\\text{NP}$]] = PCP(log n, log n) [[ZooRefs#AS98|[AS98] ]].



In fact, [[Class_NP|$\\text{NP}$]] = PCP(log n, 1) [[ZooRefs#ALM+98|[ALM+98] ]]!



On the other hand, if [[Class_NP|$\\text{NP}$]] is contained in PCP(o(log n), o(log n)), then [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]] [[ZooRefs#FGL+91|[FGL+91] ]].



Also, even though there exists an oracle relative to which [[Class_NP|$\\text{NP}$]] = [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#Hel84|[Hel84] ]], if we could show there exists an oracle relative to which PCP(log n, 1) = [[Class_EXP|$\\text{EXP}$]], then we'd have proved [[Class_P|$\\text{P}$]] not equal to [[Class_NP|$\\text{NP}$]] [[ZooRefs#For94|[For94] ]].



Another weird oracle fact: since [[Class_NP|$\\text{NP}$]] does not equal [[Class_NEXP|$\\text{NEXP}$]] [[ZooRefs#SFM78|[SFM78] ]], PCP(log n, log n) does not equal PCP(poly(n), poly(n)).  However, there exist oracles relative to which the latter inequality is false [[ZooRefs#HCC+92|[HCC+92] ]].



Another weird oracle fact: since [[Class_NP|$\\text{NP}$]] does not equal [[Class_NEXP|$\\text{NEXP}$]] [[ZooRefs#SFM78|[SFM78] ]], PCP(0,log n) does not equal PCP(0,poly(n)).  However, there exist oracles relative to which the latter inequality is false [[ZooRefs#HCC+92|[HCC+92] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PCP(r(n),q(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PCP(r(n),q(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PCTC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P,,CTC,, - P With Closed Time Curves =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_P|$\\text{P}$]] with access to bits along a closed time curve.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Implicitly defined in [Aar05c], where it was shown that [[Class_PSPACE|$\\text{PSPACE}$]] = [[Class_PCTC|$\\text{P}_\\text{CTC}\\text{}$]].



See also [[Class_BQPCTC|$\\text{BQP}_\\text{CTC}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PCTC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PCTC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PEXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PEXP - Probabilistic Exponential-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_EXP|$\\text{EXP}$]] as [[Class_PP|$\\text{PP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Is not contained in [[Class_P/poly|$\\text{P/poly}$]] [[ZooRefs#BFT98|[BFT98] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PEXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PEXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PF"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PF - Alternate Name for FP =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PF)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PF because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PFCHK(t(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PFCHK(t(n)) - Proof-Checker =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable in time O(t(n)) by a nondeterministic Turing machine, as follows.  The machine is given oracle access to a proof string of unbounded length.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes," then there exists a value of the proof string such that all computation paths accept.

If the answer is "no," then for all values of the proof string, there exists a computation path that rejects.



Credited in [[ZooRefs#For94|[For94] ]] to S. Arora, [[Class_R|$\\text{R}$]]. Impagliazzo, and U. Vazirani.



An interesting question is whether [[Class_NP|$\\text{NP}$]] = PFCHK(log n) relative to all possible oracles.  Fortnow [[ZooRefs#For94|[For94] ]] observes that the answer depends on what oracle access mechanism is used.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PFCHK(t(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PFCHK(t(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PH"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PH - Polynomial-Time Hierarchy =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

Let Δ,,0,,P = Σ,,0,,P = Π,,0,,P = [[Class_P|$\\text{P}$]].  Then for i>0, let}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Δ,,i,,P = [[Class_P|$\\text{P}$]] with Σ,,i-1,,P oracle.

Σ,,i,,P = [[Class_NP|$\\text{NP}$]] with Σ,,i-1,,P oracle.

Π,,i,,P = [[Class_coNP|$\\text{coNP}$]] with Σ,,i-1,,P oracle.



Then [[Class_PH|$\\text{PH}$]] is the union of these classes for all nonnegative constant i.



[[Class_PH|$\\text{PH}$]] can also be defined using alternating quantifiers: it's the class of problems of the form, "given an input x, does there exist a y such that for all z, there exists a w ... such that φ(x,y,z,w,...)," where y,z,w,... are polynomial-size strings and φ is a polynomial-time computable predicate.  It's not totally obvious that this is equivalent to the first definition, since the first one involves adaptive [[Class_NP|$\\text{NP}$]] oracle queries and the second one doesn't, but it is.



Defined in [[ZooRefs#Sto76|[Sto76] ]].



Contained in [[Class_P|$\\text{P}$]] with a [[Class_PP|$\\text{PP}$]] oracle [[ZooRefs#Tod89|[Tod89] ]].



Contains [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#Lau83|[Lau83] ]].



Relative to a random oracle, [[Class_PH|$\\text{PH}$]] is strictly contained in [[Class_PSPACE|$\\text{PSPACE}$]] with probability 1 [[ZooRefs#Cai86|[Cai86] ]].



Furthermore, there exist oracles separating any Σ,,i,,P from Σ,,i+1,,P.  On the other hand, it is unknown whether Σ,,i,,P is strictly contained in Σ,,i+1,,P relative to a random oracle with probability 1 (see [[ZooRefs#Has87|[Has87] ]]).  Book [[ZooRefs#Boo94|[Boo94] ]] shows that if [[Class_PH|$\\text{PH}$]] collapses relative to a random oracle with probability 1, then it collapses unrelativized.



It was shown in [CPO7] that if the [[Class_NP|$\\text{NP}$]] Machine Hypothesis holds, then

$

    \\mathsf{P}^{\\mathrm{SAT}[1]} = \\mathsf{P}^{\\mathrm{SAT}[2]} \\Rightarrow \\mathsf{PH} \\subseteq \\mathsf{NP}

$.



For a compendium of problems complete for different classes of the Polynomial Hierarchy see [Sch02a] and [Sch02b].



[[Class_PH|$\\text{PH}$]] is equal to the set of boolean queries recognizable by a concurent random acess machine using exponentially many processors and constant time[[ZooRefs#Imm89|[Imm89] ]].



Since [[Class_NP|$\\text{NP}$]] is the class of query expressible in second-order existantial logic, [[Class_PH|$\\text{PH}$]] can also be defined as the query expressible in second-order logic.
== Relations ==

{{{#!class_relations
{"version": 1.0, "class": "PH", "relations": {"contained_in": [{"class": "IP"}], "equals": []}}
}}}


== See Also ==

<<FullSearch(linkto:Class_PH)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PH because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PHcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PH^cc^ - Communication Complexity PH =

----
CategoryClassical 

== Description ==

{{{#!description

The obvious generalization of [[Class_NPcc|$\\text{NP}^\\text{cc}\\text{}$]] and [[Class_coNPcc|$\\text{coNP}^\\text{cc}\\text{}$]] to a nondeterministic hierarchy.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



It is unknown whether Σ,,2,,^cc^ equals Π,,2,,^cc^.



Defined in [[ZooRefs#BFS86|[BFS86] ]], where it was also shown (among other things) that [[Class_BPPcc|$\\text{BPP}^\\text{cc}\\text{}$]] is contained in Σ,,2,,^cc^ ∩ Π,,2,,^cc^.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PHcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PHcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PINC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PINC - Polynomial Ignorance of Names of Classes =

----
CategoryClassical 

== Description ==

{{{#!description

(Actually, I've since been informed that [[Class_PINC|$\\text{PINC}$]] means "Incremental Polynomial-Time.")}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of function problems, f:{0,1}^n^->{0,1}^m^, such that the k^th^ output bit is computable in time polynomial in n and k.



Defined in [[ZooRefs#JY88|[JY88] ]].



Contained in [[Class_PIO|$\\text{PIO}$]].  This containment is strict, since if m=2^n^ (say), then computing the first bit of f(x) might be EXP-complete.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PINC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PINC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PIO"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PIO - Polynomial Input Output =

----
CategoryClassical 

== Description ==

{{{#!description

The class of function problems, f:{0,1}^n^->{0,1}^m^, such that f(x) is computable in time polynomial in n and m.  Allows us to discuss whether a function is "efficiently computable" or not, even if the output is too long to write down in polynomial time.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Yan81|[Yan81] ]].



Strictly contains [[Class_PINC|$\\text{PINC}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PIO)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PIO because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^K^ - P With Kolmogorov-Complexity Oracle =

----
CategoryClassical 

== Description ==

{{{#!description

[[Class_P|$\\text{P}$]] equipped with an oracle that, given a string x, returns the length of the shortest program that outputs x.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A similar class was defined in [[ZooRefs#ABK+02|[ABK+02] ]], where it was also shown that [[Class_PK|$\\text{P}^\\text{K}\\text{}$]] contains [[Class_PSPACE|$\\text{PSPACE}$]].  It is not known whether [[Class_PK|$\\text{P}^\\text{K}\\text{}$]] contains all of [[Class_R|$\\text{R}$]], or even any recursive problem not in [[Class_PSPACE|$\\text{PSPACE}$]].



See also: [[Class_BPPKT|$\\text{BPP}^\\text{KT}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PKC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PKC - Perfect Knowledge Complexity =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_PZK|$\\text{PZK}$]] as [[Class_SKC|$\\text{SKC}$]] does to [[Class_SZK|$\\text{SZK}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GP91|[GP91] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PKC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PKC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PL - Probabilistic L =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] that [[Class_PP|$\\text{PP}$]] has to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_BPL|$\\text{BPL}$]].



PL^PL^ = [[Class_PL|$\\text{PL}$]] (see [[ZooRefs#HO02|[HO02] ]]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PL1"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PL,,1,, - Polynomially-Bounded L1 Spectral Norm =

----
CategoryClassical 

== Description ==

{{{#!description

The class of Boolean functions f:{-1,1}^n^->{-1,1} such that the sum of absolute values of Fourier coefficients of f is bounded by a polynomial in n.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BS90|[BS90] ]], where it was also shown that [[Class_PL1|$\\text{PL}_\\text{1}\\text{}$]] is contained in [[Class_PT1|$\\text{PT}_\\text{1}\\text{}$]] (and this inclusion is strict).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PL1)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PL1 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PLF"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PLF - Polynomial Leaf =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#Pap90|[Pap90] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



I believe it's the same as [[Class_PPA|$\\text{PPA}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PLF)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PLF because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PLL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PLL - Polynomial Local Lemma =

----
CategoryClassical 

== Description ==

{{{#!description

The class of [[Class_TFNP|$\\text{TFNP}$]] function problems that are guaranteed to have a solution because of the Lovász Local Lemma.  Defined in [Pap94b].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PLL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PLL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PLS"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PLS - Polynomial Local Search =

----
CategoryClassical 

== Description ==

{{{#!description

The subclass of [[Class_TFNP|$\\text{TFNP}$]] function problems that are guaranteed to have a solution because of the lemma that "every finite directed acyclic graph has a sink."}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



More precisely, for each input, there's a finite set of solutions (i.e. strings), and a polynomial-time algorithm that computes a cost for each solution, and a neighboring solution of lower cost provided that one exists.  Then the problem is to return any solution that has cost less than or equal to all of its neighbors.  (In other words, a local optimum.)



(Note: In the Zookeeper's humble opinion, [[Class_PLS|$\\text{PLS}$]] should have been defined as follows: there exist polynomial-time algorithms that compute the cost of a solution, and the set of all neighbors of a given solution, not just a single solution of lower cost. Of course we'd require that every solution has only polynomially many neighbors.  The two definitions are not obviously equivalent, and it's conceivable that knowing all the neighbors would be helpful -- for example, in simulated annealing one sometimes makes uphill moves.)



(Note to Note: The equivalance of these classes was shown (though not stated explicitly) in Theorem 1 of [[ZooRefs#JPY88|[JPY88] ]].)



Defined in [[ZooRefs#JPY88|[JPY88] ]], [[ZooRefs#PY88|[PY88] ]].



There exists an oracle relative to which [[Class_PLS|$\\text{PLS}$]] is not contained in [[Class_FBQP|$\\text{FBQP}$]] [[ZooRefs#Aar03|[Aar03] ]].



Also, there exist oracles relative to which [[Class_PLS|$\\text{PLS}$]] is not contained in [[Class_PPA|$\\text{PPA}$]] [[ZooRefs#BM04|[BM04] ]], and [[Class_PPA|$\\text{PPA}$]] and [[Class_PPP|$\\text{PPP}$]] are not contained in [[Class_PLS|$\\text{PLS}$]] [[ZooRefs#Mor01|[Mor01] ]].



Whether [[Class_PLS|$\\text{PLS}$]] is not in [[Class_PPP|$\\text{PPP}$]] relative to some oracle remains open.



[[ZooRefs#CT07|[CT07] ]] conjecture that if [[Class_PPAD|$\\text{PPAD}$]] is in [[Class_P|$\\text{P}$]], then [[Class_PLS|$\\text{PLS}$]] is in [[Class_P|$\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PLS)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PLS because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PL∞"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PL,,∞,, - Polynomially-Bounded L∞-1 Spectral Norm =

----
CategoryClassical 

== Description ==

{{{#!description

The class of Boolean functions f:{-1,1}^n^->{-1,1} such that the maximum of |α|^-1^, over all Fourier coefficients α of f, is upper-bounded by a polynomial in n.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BS90|[BS90] ]], where it was also shown that [[Class_PL∞|$\\text{PL}_\\text{∞}\\text{}$]] contains [[Class_PT1|$\\text{PT}_\\text{1}\\text{}$]] (and this inclusion is strict).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PL∞)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PL∞ because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^NP^ - P With Oracle Access To NP =

----
CategoryClassical 

== Description ==

{{{#!description

See [[Class_Δ2P|$\\text{Δ}_\\text{2}\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PNP[k]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^NP[k]^ - P With k NP Queries(for constant k) =

----
CategoryClassical 

== Description ==

{{{#!description

Equals [[Class_P|$\\text{P}$]] with 2^k^-1 parallel queries to [[Class_NP|$\\text{NP}$]] (i.e. queries that do not depend on the outcomes of previous queries) ([[ZooRefs#BH91|[BH91] ]] and [[ZooRefs#Hem89|[Hem89] ]] independently).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If P^NP[1]^ = P^NP[2]^, then P^NP[1]^ = [[Class_PNP[log]|$\\text{P}^\\text{NP[log]}\\text{}$]] and indeed [[Class_PH|$\\text{PH}$]] collapses to Δ,,3,,P (attributed in [Har87b] to J. Kadin).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PNP[k])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PNP[k] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PNP[log]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^NP[log]^ - P With Log NP Queries =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a [[Class_P|$\\text{P}$]] machine, that can make O(log n) queries to an [[Class_NP|$\\text{NP}$]] oracle (where n is the length of the input).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_P||NP|$\\text{P}^\\text{||NP}\\text{}$]], the class of decision problems solvable by a [[Class_P|$\\text{P}$]] machine that can make polynomially many nonadaptive queries to an [[Class_NP|$\\text{NP}$]] oracle (i.e. queries that do not depend on the outcomes of previous queries) ([[ZooRefs#BH91|[BH91] ]] and [[ZooRefs#Hem89|[Hem89] ]] independently).



[[Class_PNP[log]|$\\text{P}^\\text{NP[log]}\\text{}$]] is contained in [[Class_PP|$\\text{PP}$]] [[ZooRefs#BHW89|[BHW89] ]].



Determining the winner in an election system proposed in 1876 by Charles Dodgson (a.k.a. Lewis Carroll) has been shown to be complete for [[Class_PNP[log]|$\\text{P}^\\text{NP[log]}\\text{}$]] [[ZooRefs#HHR97|[HHR97] ]].



Contains [[Class_PNP[k]|$\\text{P}^\\text{NP[k]}\\text{}$]] for all constants k.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PNP[log])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PNP[log] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PNP[log^2]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^NP[log^2]^ - P With Log2 NP Queries =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_PNP[log]|$\\text{P}^\\text{NP[log]}\\text{}$]], except that now log^2^ queries can be made.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The model-checking problem for a certain temporal logic is P^NP[log^2]^-complete [[ZooRefs#Sch03|[Sch03] ]].



For all k, [[Class_P|$\\text{P}$]] with log^k^ adaptive queries to [[Class_NP|$\\text{NP}$]] coincides with [[Class_P|$\\text{P}$]] with log^k+1^ nonadaptive queries [[ZooRefs#CS92|[CS92] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PNP[log^2])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PNP[log^2] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PODN"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PODN - Polynomial Odd Degree Node =

----
CategoryClassical 

== Description ==

{{{#!description

The subclass of [[Class_TFNP|$\\text{TFNP}$]] function problems that are guaranteed to have a solution because of the lemma that "every finite graph has an even number of odd-degree nodes."}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_PPA|$\\text{PPA}$]] [[ZooRefs#Pap90|[Pap90] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PODN)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PODN because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PP - Probabilistic Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'yes' then at least 1/2 of computation paths accept.

If the answer is 'no' then less than 1/2 of computation paths accept.



Defined in [[ZooRefs#Gil77|[Gil77] ]].



[[Class_PP|$\\text{PP}$]] is closed under union and intersection [[ZooRefs#BRS91|[BRS91] ]] (this was an open problem for 14 years).



Contains [[Class_PNP[log]|$\\text{P}^\\text{NP[log]}\\text{}$]] [[ZooRefs#BHW89|[BHW89] ]].



Equals PP^BPP^ [KST+89b] as well as [[Class_PostBQP|$\\text{PostBQP}$]] [Aar05b].



However, there exists an oracle relative to which [[Class_PP|$\\text{PP}$]] does not contain [[Class_Δ2P|$\\text{Δ}_\\text{2}\\text{P}$]] [[ZooRefs#Bei94|[Bei94] ]].



[[Class_PH|$\\text{PH}$]] is in [[Class_PPP|$\\text{P}^\\text{PP}\\text{}$]] [[ZooRefs#Tod89|[Tod89] ]].



[[Class_BQP|$\\text{BQP}$]] is low for [[Class_PP|$\\text{PP}$]]; i.e. PP^BQP^ = [[Class_PP|$\\text{PP}$]] [[ZooRefs#FR98|[FR98] ]].



For a random oracle A, [[Class_PPA|$\\text{PP}^\\text{A}\\text{}$]] is strictly contained in PSPACE^A^ with probability 1 [[ZooRefs#ABF+94|[ABF+94] ]].



For any fixed k, there exists a language in [[Class_PP|$\\text{PP}$]] that does not have circuits of size n^k^ [Vin04b].  Indeed, there exists a language in [[Class_PP|$\\text{PP}$]] that does not even have quantum circuits of size n^k^ with quantum advice [[ZooRefs#Aar06|[Aar06] ]].



By contrast, there exists an oracle relative to which [[Class_PP|$\\text{PP}$]] has linear-size circuits [[ZooRefs#Aar06|[Aar06] ]].



[[Class_PP|$\\text{PP}$]] can be generalized to the counting hierarchy [[Class_CH|$\\text{CH}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PP/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PP/poly - Nonuniform PP =

----
CategoryClassical 

== Description ==

{{{#!description

Contains [[Class_BQP/qpoly|$\\text{BQP/qpoly}$]] [Aar04b].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If [[Class_PP/poly|$\\text{PP/poly}$]] = [[Class_P/poly|$\\text{P/poly}$]] then [[Class_PP|$\\text{PP}$]] is contained in [[Class_P/poly|$\\text{P/poly}$]].  Indeed this is true with any syntactically defined class in place of [[Class_PP|$\\text{PP}$]].  An implication is that any unrelativized separation of [[Class_BQP/qpoly|$\\text{BQP/qpoly}$]] from [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]] would imply that [[Class_PP|$\\text{PP}$]] does not have polynomial-size circuits.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PP/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PP/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PPA"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PPA - Polynomial Parity Argument =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [Pap94b]; see also [[ZooRefs#BCE+95|[BCE+95] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The subclass of [[Class_TFNP|$\\text{TFNP}$]] function problems that are guaranteed to have a solution because of the lemma that "all graphs of maximum degree 2

have an even number of leaves."



More precisely, there's a polynomial-time algorithm that, given any string, computes its 'neighbor' strings (of which there are at most two). Then given a leaf string (i.e. one with only one neighbor), the problem is to output another leaf string.



As an example, suppose you're given a cubic graph (one where every vertex has degree 3), and a Hamiltonian cycle H on that graph.  Then by making a sequence of modifications to H (albeit possibly exponentially many), it is always possible to find a second Hamilton cycle (see [[ZooRefs#Pap94|[Pap94] ]]).  So this problem is in [[Class_PPA|$\\text{PPA}$]].



Another problem in [[Class_PPA|$\\text{PPA}$]] is finding an Arrow-Debreu equilibrium, given the goods and utility functions of traders in a marketplace.



Contained in [[Class_TFNP|$\\text{TFNP}$]].



Contains [[Class_PPAD|$\\text{PPAD}$]].



There exist oracles relative to which [[Class_PPA|$\\text{PPA}$]] does not contain [[Class_PLS|$\\text{PLS}$]] [[ZooRefs#BM04|[BM04] ]] and [[Class_PPP|$\\text{PPP}$]] [[ZooRefs#BCE+95|[BCE+95] ]].  There also exists an oracle relative to which [[Class_PPA|$\\text{PPA}$]] is not contained in [[Class_PPP|$\\text{PPP}$]] [[ZooRefs#BCE+95|[BCE+95] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PPA)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PPA because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PPAD"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PPAD - Polynomial Parity Argument (Directed) =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [Pap94b]; see also [[ZooRefs#BCE+95|[BCE+95] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Same as [[Class_PPA|$\\text{PPA}$]], except now the graph is directed, and we're asked to find either a source or a sink.



Contained in [[Class_PPA|$\\text{PPA}$]] and [[Class_PPADS|$\\text{PPADS}$]].



NASH, the problem of finding a Nash equilibrium in a normal form game of two or more players with specified utilities, is in [[Class_PPAD|$\\text{PPAD}$]] [Pap94b], and proved to be complete for [[Class_PPAD|$\\text{PPAD}$]] with four players in [[ZooRefs#DGP05|[DGP05] ]], and shortly after extended to the case of three players [[ZooRefs#DP05|[DP05] ]] and independently [[ZooRefs#CD05|[CD05] ]].



There exists an oracle relative to which [[Class_PPP|$\\text{PPP}$]] is not contained in [[Class_PPAD|$\\text{PPAD}$]] [[ZooRefs#BCE+95|[BCE+95] ]].

There exists an oracle relative to which [[Class_PPAD|$\\text{PPAD}$]] is not contained in [[Class_BQP|$\\text{BQP}$]] [[ZooRefs#Li11|[Li11] ]].



There exists an oracle relative to which [[Class_PPP|$\\text{PPP}$]] is not contained in [[Class_PPAD|$\\text{PPAD}$]] [[ZooRefs#BCE+95|[BCE+95] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PPAD)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PPAD because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PPADS"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PPADS - Polynomial Parity Argument (Directed, Sink) =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [Pap94b]; see also [[ZooRefs#BCE+95|[BCE+95] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Same as [[Class_PPA|$\\text{PPA}$]], except now the graph is directed, and we're asked to find a sink.



Contained in [[Class_PPP|$\\text{PPP}$]].



Contains [[Class_PPAD|$\\text{PPAD}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PPADS)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PPADS because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^PP^ - P With PP Oracle =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [Pap94b]; see also [[ZooRefs#BCE+95|[BCE+95] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The subclass of [[Class_TFNP|$\\text{TFNP}$]] function problems that are guaranteed to have a solution because of the Pigeonhole Principle.



More precisely, we're given a Boolean circuit, that maps n-bit strings to n-bit strings.  The problem is to return either an input that maps to 0^n^, or two inputs that map to the same output.



Contained in [[Class_TFNP|$\\text{TFNP}$]].



Contains [[Class_PPADS|$\\text{PPADS}$]].



[[ZooRefs#BCE+95|[BCE+95] ]] give oracles relative to which [[Class_PPP|$\\text{PPP}$]] is not contained in [[Class_PPA|$\\text{PPA}$]] and [[Class_PPAD|$\\text{PPAD}$]], and [[Class_PPA|$\\text{PPA}$]] is not contained in [[Class_PPP|$\\text{PPP}$]].



[[ZooRefs#Mor01|[Mor01] ]] gives an oracle relative to which [[Class_PPP|$\\text{PPP}$]] is not contained in [[Class_PLS|$\\text{PLS}$]].



Whether [[Class_PLS|$\\text{PLS}$]] is not contained in [[Class_PPP|$\\text{PPP}$]] relative to some oracle remains open.



A level of the counting hierarchy [[Class_CH|$\\text{CH}$]].



It is not known whether there exists an oracle relative to which [[Class_PPP|$\\text{P}^\\text{PP}\\text{}$]] does not equal [[Class_PSPACE|$\\text{PSPACE}$]].



Contains PP^PH^ [[ZooRefs#Tod89|[Tod89] ]].



Equals [[Class_PSharpP|$\\text{P}^\\text{#P}\\text{}$]] (exercise for the visitor).



Since the permanent of a matrix is #P-complete [[ZooRefs#Val79|[Val79] ]], Toda's theorem implies that any problem in the polynomial hierarchy can be solved by computing a sequence of permanents.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PPSPACE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PPSPACE - Probabilistic PSPACE =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_IPP|$\\text{IPP}$]], except that [[Class_IPP|$\\text{IPP}$]] uses private coins while [[Class_PPSPACE|$\\text{PPSPACE}$]] uses public coins.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Can also be defined as a probabilistic version of [[Class_PSPACE|$\\text{PSPACE}$]].



Equals [[Class_PSPACE|$\\text{PSPACE}$]].



Defined in [[ZooRefs#Pap83|[Pap83] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PPSPACE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PPSPACE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PPcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PP^cc^ - Analogue of PP for Communication Complexity =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#BFS86|[BFS86] ]], [[Class_PPcc|$\\text{PP}^\\text{cc}\\text{}$]] is one of two ways to define a communication complexity analogue of [[Class_PP|$\\text{PP}$]]. In [[Class_PPcc|$\\text{PP}^\\text{cc}\\text{}$]], we note that in an algorithm that uses an amount of random bits bounded by $c$, the bias between the accept and reject probabilities can be no smaller than $2^c$. Thus, in [[Class_PPcc|$\\text{PP}^\\text{cc}\\text{}$]], the communication complexity is defined as the sum of the traditional communication complexity (the number of exchanged bits) and the log of the reciprocal of the worst-case (smallest) bias.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The difference between this class and [[Class_UPPcc|$\\text{UPP}^\\text{cc}\\text{}$]] is discussed further in [[ZooRefs#BVW07|[BVW07] ]], where it is shown that [[Class_PPcc|$\\text{PP}^\\text{cc}\\text{}$]] ⊂ [[Class_UPPcc|$\\text{UPP}^\\text{cc}\\text{}$]].



See Also: [[Class_UPPcc|$\\text{UPP}^\\text{cc}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PPcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PPcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PQUERY"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PQUERY - PSPACE With Polynomial Queries =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable in polynomial space using at most a polynomial number of queries to the oracle.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Thus, [[Class_PQUERY|$\\text{PQUERY}$]] = [[Class_PSPACE|$\\text{PSPACE}$]], but PQUERY^A^ does not equal PSPACE^A^ for some oracles A.



Defined in [[ZooRefs#Kur83|[Kur83] ]], where it was actually put forward as a serious argument (!!) against believing relativization results.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PQUERY)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PQUERY because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PR"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P,,R,, - Polynomial-Time Over The Reals =

----
CategoryClassical 

== Description ==

{{{#!description

Basically, the class of functions definable by recursively building up arithmetic functions: addition, multiplication, exponentiation, tetration, etc.  What's not allowed is to "diagonalize" a whole series of such functions to produce an even faster-growing one.  Thus, the Ackermann function was proposed in 1928 as an example of a recursive function that's not primitive recursive, showing that [[Class_PR|$\\text{PR}$]] is strictly contained in [[Class_R|$\\text{R}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Alternatively, the [[Class_PR|$\\text{PR}$]] functions are exactly those functions that can be computed via programs in any reasonable, idealized ALGOL-like programming language where only definite loops are allowed, that is, loops where the number of iterations is specified before the loop starts (so FOR-loops are okay but not WHILE- or REPEAT-loops), and recursive calls are not allowed.



An interesting difference is that [[Class_PR|$\\text{PR}$]] functions can be explicitly enumerated, whereas functions in [[Class_R|$\\text{R}$]] cannot be (since otherwise the halting problem would be decidable).  That is, [[Class_PR|$\\text{PR}$]] is a "syntactic" class whereas [[Class_R|$\\text{R}$]] is "semantic."



On the other hand, we can "enumerate" any [[Class_RE|$\\text{RE}$]] set by a [[Class_PR|$\\text{PR}$]] function in the following sense: given an input (M,k), where M is a Turing machine and k is an integer, if M halts within k steps then output M; otherwise output nothing.  Then the union of the outputs, over all possible inputs (M,k), is exactly the set of M that halt.



[[Class_PR|$\\text{PR}$]] strictly contains [[Class_ELEMENTARY|$\\text{ELEMENTARY}$]].



An analog of [[Class_P|$\\text{P}$]] for Turing machines over a real number field.



Defined in [[ZooRefs#BCS+97|[BCS+97] ]].



See also [[Class_PC|$\\text{P}_\\text{C}\\text{}$]], [[Class_NPC|$\\text{NP}_\\text{C}\\text{}$]], [[Class_NPR|$\\text{NP}_\\text{R}\\text{}$]], [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PR)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PR because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PSK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PSK - Polynomial Sink =

----
CategoryClassical 

== Description ==

{{{#!description

Yeah, I'm told that's what the S and [[Class_K|$\\text{K}$]] stand for.  Go figure.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of total function problems definable as follows: given a directed graph of indegree and outdegree at most 1, and given a source, find a sink.



Defined in [[ZooRefs#Pap90|[Pap90] ]].



Equals [[Class_PPADS|$\\text{PPADS}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PSK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PSK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PSPACE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PSPACE - Polynomial-Space =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a Turing machine in polynomial space.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_NPSPACE|$\\text{NPSPACE}$]] [[ZooRefs#Sav70|[Sav70] ]], [[Class_AP|$\\text{AP}$]] [[ZooRefs#CKS81|[CKS81] ]], [[Class_IP|$\\text{IP}$]] [[ZooRefs#Sha90|[Sha90] ]], and, assuming the existence of one-way functions, [[Class_CZK|$\\text{CZK}$]] [[ZooRefs#BGG+90|[BGG+90] ]].



Contains [[Class_P|$\\text{P}$]] with [[Class_SharpP|$\\text{#P}$]] oracle.



A canonical PSPACE-complete problem is QBF.



Relative to a random oracle, [[Class_PSPACE|$\\text{PSPACE}$]] strictly contains [[Class_PH|$\\text{PH}$]] with probability 1 [[ZooRefs#Cai86|[Cai86] ]].



[[Class_PSPACE|$\\text{PSPACE}$]] has a complete problem that is both downward self-reducible and random self-reducible [[ZooRefs#TV02|[TV02] ]].  It is the largest class with such a complete problem.



Contained in [[Class_EXP|$\\text{EXP}$]].  There exists an oracle relative to which this containment is proper [[ZooRefs#Dek76|[Dek76] ]].



In descriptive complexity, [[Class_PSPACE|$\\text{PSPACE}$]] can be defined with 4 differents kind of formulae, FO(2^{n^{O(1)}}) which is also FO(PFP) and SO(n^{O(1)}) which is also SO(TC).



A canonical PSPACE-complete problem is Quantified Boolean Formula (QBF): Given a Boolean formula with universal and existential quantifiers, decide whether it's true or false.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PSPACE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PSPACE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PSPACE/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PSPACE/poly - PSPACE With Polynomial-Size Advice =

----
CategoryClassical 

== Description ==

{{{#!description

Contains [[Class_QMA/qpoly|$\\text{QMA/qpoly}$]] [Aar06b].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PSPACE/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PSPACE/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PT/WK(f(n),g(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PT/WK(f(n),g(n)) - Parallel Time f(n) / Work g(n) =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a uniform family of Boolean circuits with depth upper-bounded by f(n) and size (number of gates) upper-bounded by g(n).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The union of PT/WK(log^k^n, n^k^) over all constants k equals [[Class_NC|$\\text{NC}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PT/WK(f(n),g(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PT/WK(f(n),g(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PT1"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PT,,1,, - Polynomial Threshold Functions =

----
CategoryClassical 

== Description ==

{{{#!description

The class of Boolean functions f:{-1,1}^n^->{-1,1} such that f(x)=sgn(p(x)), where p is a polynomial having a number of terms polynomial in n.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BS90|[BS90] ]], where it was also shown that [[Class_PT1|$\\text{PT}_\\text{1}\\text{}$]] contains [[Class_PL1|$\\text{PL}_\\text{1}\\text{}$]] (and this inclusion is strict), and that [[Class_PT1|$\\text{PT}_\\text{1}\\text{}$]] is contained in [[Class_PL∞|$\\text{PL}_\\text{∞}\\text{}$]] (and this inclusion is strict).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PT1)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PT1 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PTAPE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PTAPE - Archaic for PSPACE =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PTAPE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PTAPE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PTAS"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PTAS - Polynomial-Time Approximation Scheme =

----
CategoryClassical 

== Description ==

{{{#!description

The subclass of [[Class_NPO|$\\text{NPO}$]] problems that admit an approximation scheme in the following sense.  For any ε>0, there is a polynomial-time algorithm that is guaranteed to find a solution whose cost is within a 1+ε factor of the optimum cost.  (However, the exponent of the polynomial might depend strongly on ε.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_FPTAS|$\\text{FPTAS}$]], and is contained in [[Class_APX|$\\text{APX}$]].



As an example, the Traveling Salesman Problem in the Euclidean plane is in [[Class_PTAS|$\\text{PTAS}$]] [[ZooRefs#Aro96|[Aro96] ]].



Defined in [[ZooRefs#ACG+99|[ACG+99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PTAS)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PTAS because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PZK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PZK - Perfect Zero Knowledge =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_SZK|$\\text{SZK}$]], but now the two distributions must be identical, not merely statistically close.  (The "two distributions" are (1) the distribution over the verifier's view of his interaction with the prover, conditioned on the verifier's random coins, and (2) the distribution over views that the verifier can simulate without the prover's help.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_SZK|$\\text{SZK}$]].



See also: [[Class_CZK|$\\text{CZK}$]].



Same as [[Class_SZK|$\\text{SZK}$]], but now the two distributions must be identical, not merely statistically close.  (The "two distributions" are (1) the distribution over Arthur's view of his interaction with Merlin, conditioned on Arthur's random coins, and (2) the distribution over views that Arthur can simulate without Merlin's help.)
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PZK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PZK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Pcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^cc^ - Communication Complexity P =

----
CategoryClassical 

== Description ==

{{{#!description

In a two-party communication complexity problem, Alice and Bob have n-bit strings x and y respectively, and they wish to evaluate some Boolean function f(x,y) using as few bits of communication as possible.  [[Class_Pcc|$\\text{P}^\\text{cc}\\text{}$]] is the class of (infinite families of) f's, such that the amount of communication needed is only O(polylog(n)), even if Alice and Bob are restricted to a deterministic protocol.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Note that all functions of the form above are solvable given $O(n)$ bits of communication, since no bounds are placed on the computational abilities of Alice and Bob. Thus, when discussing this class, "polynomially" is sometimes used in place of "polylogarithmically."



Is strictly contained in [[Class_NPcc|$\\text{NP}^\\text{cc}\\text{}$]] and in [[Class_BPPcc|$\\text{BPP}^\\text{cc}\\text{}$]] because of the EQUALITY problem.



Equals [[Class_NPcc|$\\text{NP}^\\text{cc}\\text{}$]] ∩ [[Class_coNPcc|$\\text{coNP}^\\text{cc}\\text{}$]].



Defined in [[ZooRefs#BFS86|[BFS86] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Pcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Pcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PermUP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PermUP - Self-Permuting UP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of languages [[Class_L|$\\text{L}$]] in [[Class_UP|$\\text{UP}$]] such that the mapping from an input x to the unique witness for x is a permutation of [[Class_L|$\\text{L}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_P|$\\text{P}$]].



Defined in [[ZooRefs#HT03|[HT03] ]], where it was also shown that the closure of [[Class_PermUP|$\\text{PermUP}$]] under polynomial-time one-to-one reductions is [[Class_UP|$\\text{UP}$]].



On the other hand, they show that if [[Class_PermUP|$\\text{PermUP}$]] = [[Class_UP|$\\text{UP}$]] then [[Class_E|$\\text{E}$]] = [[Class_UE|$\\text{UE}$]].



See also: [[Class_SelfNP|$\\text{SelfNP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PermUP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PermUP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PhP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PhP - Physical Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Defined by Valiant [[ZooRefs#Val03|[Val03] ]] to be "the class of physically constructible polynomial resource computers" (characterizing what "can be computed in the physical world in practice").  There he says that [[Class_PhP|$\\text{PhP}$]] contains [[Class_P|$\\text{P}$]] and [[Class_BPP|$\\text{BPP}$]], but that it is open whether [[Class_PhP|$\\text{PhP}$]] contains [[Class_BQP|$\\text{BQP}$]], since no scalable quantum computing proposal has been demonstrated beyond reasonable doubt.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



For what it's worth, the present zookeeper has more qualms about admitting DTIME(n^1000^) into [[Class_PhP|$\\text{PhP}$]] than BQTIME(n^2^).  It is very possible that the total number of bits or bit tranisitions that can be witnessed by any one observer in the universe is finite.  (Recent observations of the cosmological constant combined with plausible fundamental physics yields a bound of 10^k^ with k in the low hundreds.)  In practice, less than 10^50^ bits and less than 10^80^ bit transitions are available for human use.  (This is combining the number of atoms in the Earth with the number of signals that they can exchange in a millenium.)



The present veterinarian concurs that [[Class_PhP|$\\text{PhP}$]] is an unhealthy animal, although it is valid to ask whether [[Class_BQP|$\\text{BQP}$]] is a realistic class.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PhP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PhP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Pkcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P,,k,,^cc^ - Pcc in NOF model,  players =

----
CategoryClassical 

== Description ==

{{{#!description

Like [[Class_Pcc|$\\text{P}^\\text{cc}\\text{}$]], but with $k$ players, where each player can see all of the other player's bits, but not their own. Intuitively, each player has their bits written on their forehead.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



More formally, [[Class_Pkcc|$\\text{P}_\\text{k}\\text{}^\\text{cc}\\text{}$]] is the class of functions $F:X_1\\times X_2 \\times \\cdots \\times X_k \\to \\{0,1\\}$ where for all $i\\in[1..k]$, $X_k\\in\\{0,1\\}^n$, such that $F$ is solvable in a deterministic sense by $k$ players, each of which is aware of all inputs $X_i$ other than his own, and such that $O\\left(\\mathrm{poly}(\\log n)\\right)$ bits of communication are used.



[[Class_Pkcc|$\\text{P}_\\text{k}\\text{}^\\text{cc}\\text{}$]] is trivially contained in [[Class_BPPkcc|$\\text{BPP}_\\text{k}\\text{}^\\text{cc}\\text{}$]], [[Class_RPkcc|$\\text{RP}_\\text{k}\\text{}^\\text{cc}\\text{}$]] and [[Class_NPkcc|$\\text{NP}_\\text{k}\\text{}^\\text{cc}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Pkcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Pkcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PostBQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PostBQP - BQP With Postselection =

----
CategoryClassical 

== Description ==

{{{#!description

A class inspired by the proverb, "if at first you don't succeed, try, try again."}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Formally, the class of decision problems solvable by a [[Class_BQP|$\\text{BQP}$]] machine such that



If the answer is 'yes' then the second qubit has at least 2/3 probability of being measured 1, conditioned on the first qubit having been measured 1.

If the answer is 'no' then the second qubit has at most 1/3 probability of being measured 1, conditioned on the first qubit having been measured 1.

On any input, the first qubit has a nonzero probability of being measured 1.



Defined in [Aar05b], where it is also shown that [[Class_PostBQP|$\\text{PostBQP}$]] equals [[Class_PP|$\\text{PP}$]].



[Aar05b] also gives the following alternate characterizations of [[Class_PostBQP|$\\text{PostBQP}$]] (and therefore of [[Class_PP|$\\text{PP}$]]):



The quantum analogue of [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]].

The class of problems solvable in quantum polynomial time if we allow arbitrary linear operations (not just unitary ones). Before measuring, we divide all amplitudes by a normalizing factor to make the probabilities sum to 1.

The class of problems solvable in quantum polynomial time if we take the probability of measuring a basis state with amplitude α to be not |α|^2^ but |α|^p^, where p is an even integer greater than 2.  (Again we need to divide all amplitudes by a normalizing factor to make the probabilities sum to 1.)
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PostBQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PostBQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PrHSPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Pr,,H,,SPACE(f(n)) - Unbounded-Error Halting Probabilistic f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to DSPACE(f(n)) as [[Class_PP|$\\text{PP}$]] does to [[Class_P|$\\text{P}$]].  The Turing machine has to halt on every input and every setting of the random tape.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals PrSPACE(f(n)) [[ZooRefs#Jun85|[Jun85] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PrHSPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PrHSPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PrSPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PrSPACE(f(n)) - Unbounded-Error Probabilistic f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to DSPACE(f(n)) as [[Class_PP|$\\text{PP}$]] does to [[Class_P|$\\text{P}$]].  The Turing machine has to halt with probability 1 on every input.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in DSPACE(f(n)^2^) [[ZooRefs#BCP83|[BCP83] ]].



Equals Pr,,H,,SPACE(f(n)) [[ZooRefs#Jun85|[Jun85] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PrSPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PrSPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PromiseBPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PromiseBPP - Promise-Problem BPP =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_PromiseRP|$\\text{PromiseRP}$]], but for [[Class_BPP|$\\text{BPP}$]] instead of [[Class_RP|$\\text{RP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BF99|[BF99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PromiseBPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PromiseBPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PromiseBQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PromiseBQP - Promise-Problem BQP =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_PromiseBPP|$\\text{PromiseBPP}$]], but for [[Class_BQP|$\\text{BQP}$]] instead of [[Class_BPP|$\\text{BPP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If [[Class_PromiseBQP|$\\text{PromiseBQP}$]] = [[Class_PromiseP|$\\text{PromiseP}$]] then [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]] = [[Class_P/poly|$\\text{P/poly}$]].



Same as [[Class_PromiseBQP|$\\text{PromiseBQP}$]], but for [[Class_BQP|$\\text{BQP}$]] instead of [[Class_BPP|$\\text{BPP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PromiseBQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PromiseBQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PromiseP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PromiseP - Promise-Problem P =

----
CategoryClassical 

== Description ==

{{{#!description

The class of promise problems solvable by a [[Class_P|$\\text{P}$]] machine.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PromiseP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PromiseP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PromiseRP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PromiseRP - Promise-Problem RP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of promise problems solvable by an [[Class_RP|$\\text{RP}$]] machine. I.e., the machine must accept with probability at least 1/2 for "yes" inputs, and with probability 0 for "no" inputs, but could have acceptance probability between 0 and 1/2 for inputs that do not satisfy the promise.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BF99|[BF99] ]], where it was also shown that [[Class_BPP|$\\text{BPP}$]] is in RP^PromiseRP[1]^ (i.e. with a single oracle query to [[Class_PromiseRP|$\\text{PromiseRP}$]]).



Contained in [[Class_PromiseBPP|$\\text{PromiseBPP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PromiseRP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PromiseRP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_PromiseUP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PromiseUP - Promise-Problem UP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of promise problems solvable by an [[Class_UP|$\\text{UP}$]] machine. I.e., the nondeterministic machine must have a unique accepting path for "yes" inputs, and no accepting paths "no" inputs, but could have any number of accepting paths for inputs that do not satisfy the promise.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Although not originally stated with this notation, the main result of [[ZooRefs#VV86|[VV86] ]] is that [[Class_NP|$\\text{NP}$]] is contained in RP^PromiseUP^.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_PromiseUP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save PromiseUP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_P||NP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^||NP^ - P With Parallel Queries To NP =

----
CategoryClassical 

== Description ==

{{{#!description

Equals [[Class_PNP[log]|$\\text{P}^\\text{NP[log]}\\text{}$]] ([[ZooRefs#BH91|[BH91] ]] and [[ZooRefs#Hem89|[Hem89] ]] independently).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_P||NP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save P||NP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Q"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Q - Quasi-Realtime Languages =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by a nondeterministic multitape Turing machine in linear time. Defined in [[ZooRefs#BG69|[BG69] ]], where it was shown that [[Class_Q|$\\text{Q}$]] equals the class of problems solvable by a nondeterministic multitape Turing machine in exactly n steps (as opposed to O(n) steps).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_GCSL|$\\text{GCSL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Q)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Q because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QAC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QAC^0^ - Quantum AC0 =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems solvable by a family of constant-depth, polynomial-size quantum circuits.  Here each layer of the circuit is a tensor product of one-qubit gates and Toffoli gates, or is a tensor product of controlled-NOT gates.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A uniformity condition may also be imposed.



Defined in [[ZooRefs#Moo99|[Moo99] ]].



It is contained in [[Class_QACf0|$\\text{QAC}_\\text{f}\\text{}^\\text{0}\\text{}$]], but it is not known if it contains [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]]. Notice that the latter containment is not obvious, since the set of gates in [[Class_QAC0|$\\text{QAC}^\\text{0}\\text{}$]] do not allow to implement fanout in any way we may take for granted.



Contains [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]], and is contained in [[Class_QACf0|$\\text{QAC}_\\text{f}\\text{}^\\text{0}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QAC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QAC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QAC0[m]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QAC^0^[m] - Quantum AC0[m] =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QAC0|$\\text{QAC}^\\text{0}\\text{}$]], except that now Mod-m gates are also allowed.  A Mod-m gate computes whether the sum of a given set of bits is congruent to 0 modulo m, and exclusive-OR's the answer into another bit.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Moo99|[Moo99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QAC0[m])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QAC0[m] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QACC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QACC^0^ - Quantum ACC0 =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QAC0[m]|$\\text{QAC}^\\text{0}\\text{[m]}$]], except that Mod-m gates are allowed for any m.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Moo99|[Moo99] ]].



[[ZooRefs#GHP00|[GHP00] ]] showed that [[Class_QACC0|$\\text{QACC}^\\text{0}\\text{}$]] equals QAC^0^[p] for any prime p.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QACC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QACC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QACf0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QAC,,f,,^0^ - QAC0 With Fanout =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_QAC0|$\\text{QAC}^\\text{0}\\text{}$]], except that an additional "quantum fanout" gate is available, which CNOT's a qubit into arbitrarily many target qubits in a single step.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Moo99|[Moo99] ]], where it was also shown that [[Class_QACf0|$\\text{QAC}_\\text{f}\\text{}^\\text{0}\\text{}$]] =

QAC^0^[2] = [[Class_QACC0|$\\text{QACC}^\\text{0}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QACf0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QACf0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QAM"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QAM - Quantum AM =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems for which a "yes" answer can be verified by a public-coin quantum [[Class_AM|$\\text{AM}$]] protocol, as follows.  Arthur generates a uniformly random (classical) string and sends it to Merlin.  Merlin responds with a polynomial-size quantum certificate, on which Arthur can perform any [[Class_BQP|$\\text{BQP}$]] operation.  The completeness and soundness requirements are the same as for [[Class_AM|$\\text{AM}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined by Marriott and Watrous [[ZooRefs#MW05|[MW05] ]].



Contains [[Class_QMA|$\\text{QMA}$]] and is contained in [[Class_QIP[2]|$\\text{QIP[2]}$]] and BP•PP (and therefore [[Class_PSPACE|$\\text{PSPACE}$]]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QAM)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QAM because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QCFL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QCFL - Quantum CFL =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems recognized by quantum context-free languages, which are defined in [[ZooRefs#MC00|[MC00] ]].  The authors also showed that [[Class_QCFL|$\\text{QCFL}$]] does not equal [[Class_CFL|$\\text{CFL}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QCFL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QCFL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QCMA"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QCMA - Quantum Classical MA =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems for which a "yes" answer can be verified by a quantum computer with access to a classical proof. Also known as the subclass of of [[Class_QMA|$\\text{QMA}$]] with classical witnesses.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Called MQA by Watrous [[ZooRefs#Wat09|[Wat09] ]].



Contains [[Class_MA|$\\text{MA}$]], and is contained in [[Class_QMA|$\\text{QMA}$]].



Given a black-box group G and a subgroup H, the problem of testing non-membership in H has polynomial [[Class_QCMA|$\\text{QCMA}$]] query complexity [[ZooRefs#AK06|[AK06] ]].



See [[ZooRefs#AK06|[AK06] ]] for a "quantum oracle separation" between [[Class_QCMA|$\\text{QCMA}$]] and [[Class_QMA|$\\text{QMA}$]].  No classical oracle separation between [[Class_QCMA|$\\text{QCMA}$]] and [[Class_QMA|$\\text{QMA}$]] is currently known.



The class of decision problems for which a "yes" answer can be verified by a quantum computer with access to a classical proof.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QCMA)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QCMA because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QH"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QH - Query Hierarchy Over NP =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

QH,,k,, is defined to be [[Class_PNP[k]|$\\text{P}^\\text{NP[k]}\\text{}$]]; that is, [[Class_P|$\\text{P}$]] with k queries to an [[Class_NP|$\\text{NP}$]] oracle (where k is a constant).  Then [[Class_QH|$\\text{QH}$]] is the union of QH,,k,, over all nonnegative k.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_QH|$\\text{QH}$]] = [[Class_BH|$\\text{BH}$]] [[ZooRefs#Wag88|[Wag88] ]]; thus, either both hierarchies are infinite or both collapse to some finite level.



QH,,i,, is defined to be [[Class_PNP[k]|$\\text{P}^\\text{NP[k]}\\text{}$]]; that is, [[Class_P|$\\text{P}$]] with k queries to an [[Class_NP|$\\text{NP}$]] oracle (where k is a constant).  Then [[Class_QH|$\\text{QH}$]] is the union of QH,,i,, over all nonnegative i.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QH)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QH because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QIP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QIP - Quantum IP =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems such that a "yes" answer can be verified by a quantum interactive proof.  Here the verifier is a [[Class_BQP|$\\text{BQP}$]] (i.e. quantum polynomial-time) algorithm, while the prover has unbounded computational resources (though cannot violate the linearity of quantum mechanics). The prover and verifier exchange a polynomial number of messages, which can be quantum states.  Thus, the verifier's and prover's states may become entangled during the course of the protocol.  Given the verifier's algorithm, we require that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes," then the prover can behave in such a way that the verifier accepts with probability at least 2/3.

If the answer is "no," then however the prover behaves, the verifier rejects with probability at least 2/3.



Let QIP[k] be [[Class_QIP|$\\text{QIP}$]] where the prover and verifier are restricted to exchanging k messages (with the prover going last).



Defined in [[ZooRefs#Wat99|[Wat99] ]], where it was also shown that [[Class_PSPACE|$\\text{PSPACE}$]] is in QIP[3].



Subsequently [[ZooRefs#KW00|[KW00] ]] showed that for all k>3, QIP[k] = QIP[3] = [[Class_QIP|$\\text{QIP}$]].



[[Class_QIP|$\\text{QIP}$]] is contained in [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#KW00|[KW00] ]].



[[Class_QIP|$\\text{QIP}$]] = [[Class_IP|$\\text{IP}$]] = [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#JJUW09|[JJUW09] ]]; thus quantum computing adds no power to interactive proofs.



QIP(1) is more commonly known as [[Class_QMA|$\\text{QMA}$]].



See also: [[Class_QIP[2]|$\\text{QIP[2]}$]], [[Class_QSZK|$\\text{QSZK}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QIP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QIP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QIP[2]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QIP[2] - 2-Message Quantum IP =

----
CategoryQuantum 

== Description ==

{{{#!description

See [[Class_QIP|$\\text{QIP}$]] for definition.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_QSZK|$\\text{QSZK}$]] [[ZooRefs#Wat02|[Wat02] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QIP[2])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QIP[2] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QL - Quasi-Linear =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems that can be decided in quasi-linear time by a multitape deterministic Turing machine.  Quasi-linear time here means n(log n)^k^ + k, for some k.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Sch78|[Sch78] ]].



See also: [[Class_Q|$\\text{Q}$]], [[Class_NQL|$\\text{NQL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QMA"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QMA - Quantum MA =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems such that a "yes" answer can be verified by a 1-message quantum interactive proof.  That is, a [[Class_BQP|$\\text{BQP}$]] (i.e. quantum polynomial-time) verifier is given a quantum state (the "proof").  We require that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes," then there exists a state such that verifier accepts with probability at least 2/3.

If the answer is "no," then for all states the verifier rejects with probability at least 2/3.



[[Class_QMA|$\\text{QMA}$]] = QIP(1).



Defined in [[ZooRefs#Wat00|[Wat00] ]], where it is also shown that group non-membership is in [[Class_QMA|$\\text{QMA}$]].



Based on this, [[ZooRefs#Wat00|[Wat00] ]] gives an oracle relative to which [[Class_MA|$\\text{MA}$]] is strictly contained in [[Class_QMA|$\\text{QMA}$]].



Kitaev and Watrous (unpublished) showed [[Class_QMA|$\\text{QMA}$]] is contained in [[Class_PP|$\\text{PP}$]] (see [[ZooRefs#MW05|[MW05] ]] for a proof).  Combining that result with [[ZooRefs#Ver92|[Ver92] ]], one can obtain an oracle relative to which [[Class_AM|$\\text{AM}$]] is not in [[Class_QMA|$\\text{QMA}$]].



Kitaev ([[ZooRefs#KSV02|[KSV02] ]], see also [[ZooRefs#AN02|[AN02] ]]) showed that the 5-Local Hamiltonians Problem is QMA-complete. Subsequently, Kempe and Regev [[ZooRefs#KR03|[KR03] ]] showed that even 3-Local Hamiltonians is QMA-complete.  A subsequent paper by Kempe, Kitaev, and Regev [[ZooRefs#KKR04|[KKR04] ]], has hit rock bottom (assuming [[Class_P|$\\text{P}$]] does not equal [[Class_QMA|$\\text{QMA}$]]), by showing 2-local Hamiltonians QMA-complete.



Compare to [[Class_NQP|$\\text{NQP}$]].



If [[Class_QMA|$\\text{QMA}$]] = [[Class_PP|$\\text{PP}$]] then [[Class_PP|$\\text{PP}$]] contains [[Class_PH|$\\text{PH}$]] [[ZooRefs#Vya03|[Vya03] ]].  This result uses the fact that [[Class_QMA|$\\text{QMA}$]] is contained in [[Class_A0PP|$\\text{A}_\\text{0}\\text{PP}$]].



Approximating the ground state energy of a system composed of a line of quantum particles is QMA-complete [[ZooRefs#AGK07|[AGK07] ]].



See also: [[Class_QCMA|$\\text{QCMA}$]], [[Class_QMA/qpoly|$\\text{QMA/qpoly}$]], [[Class_QSZK|$\\text{QSZK}$]], QMA(2), [[Class_QMA-plus|$\\text{QMA-plus}$]].



Defined in [[ZooRefs#Wat00|[Wat00] ]], where it is also shown that group non-membership is in [[Class_QMA|$\\text{QMA}$]].  That is: let G be a group, whose elements are represented by polynomial-size strings.  We're given a "black box" that correctly multiplies and inverts elements of G.  Then given elements g and h,,1,,,...,h,,k,,, we can verify in [[Class_QMA|$\\text{QMA}$]] that g is not in the subgroup generated by h,,1,,,...,h,,k,,.



Kitaev and Watrous (unpublished) showed [[Class_QMA|$\\text{QMA}$]] is contained in [[Class_PP|$\\text{PP}$]].  Combining that result with [[ZooRefs#Ver92|[Ver92] ]], one can obtain an oracle relative to which [[Class_AM|$\\text{AM}$]] is not in [[Class_QMA|$\\text{QMA}$]].



[[ZooRefs#KSV02|[KSV02] ]]



[[ZooRefs#AN02|[AN02] ]]



5-Local Hamiltonians.  Given an n-qubit Hilbert space, as well as a collection H,,1,,,...,H,,k,, of Hamiltonians (i.e. Hermitian positive semidefinite matrices), each of which acts on at most 5 qubits of the space.  Also given reals a,b such that b-a = Θ(1/poly(n)).  Decide whether the smallest eigenvalue of H=H,,1,,+...+H,,k,, is less than a or greater than b, promised that one of these is the case.



Subsequently Kempe and Regev [[ZooRefs#KR03|[KR03] ]] showed that even 3-Local Hamiltonians is QMA-complete.  A subsequent paper by Kempe, Kitaev, and Regev [[ZooRefs#KKR04|[KKR04] ]], has hit rock bottom (assuming [[Class_P|$\\text{P}$]] does not equal [[Class_QMA|$\\text{QMA}$]]), by showing 2-local Hamiltonians QMA-complete.



[[Class_NQP|$\\text{NQP}$]]
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QMA)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QMA because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QMA(2)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QMA(2) - Quantum MA With Multiple Certificates =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QMA|$\\text{QMA}$]], except that now the verifier is given two polynomial-size quantum certificates, which are guaranteed to be unentangled.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#KMY01|[KMY01] ]].



It was shown in [[ZooRefs#ABD+08|[ABD+08] ]] that a conjecture they call the Strong Amplification Conjecture implies that QMA(2) is contained in [[Class_PSPACE|$\\text{PSPACE}$]]. The authors also show that there exists no perfectly disentangler that can be used to simulate QMA(2) in [[Class_QMA|$\\text{QMA}$]], though other approaches to showing [[Class_QMA|$\\text{QMA}$]] = QMA(2) may still exist.



It was shown in [[ZooRefs#HM13|[HM13] ]] that QMA(k) = QMA(2) for k >= 2. However we still do not know if QMA(2) = [[Class_QMA|$\\text{QMA}$]] and we also do not know any upper bound for QMA(2) better than [[Class_NEXP|$\\text{NEXP}$]].



Defined in [[ZooRefs#KMY01|[KMY01] ]].  It is unknown whether QMA(k) = QMA(2) for all k>2, and also whether QMA(2) = [[Class_QMA|$\\text{QMA}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QMA(2))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QMA(2) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QMA-plus"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QMA-plus - QMA With Super-Verifier =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QMA|$\\text{QMA}$]], except now the verifier can directly obtain the probability that a given observable of the certificate state, if measured, would equal 1.  (In the usual model, by contrast, one can only sample an observable.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#AR03|[AR03] ]], where it was also shown that [[Class_QMA-plus|$\\text{QMA-plus}$]] = [[Class_QMA|$\\text{QMA}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QMA-plus)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QMA-plus because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QMA/qpoly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QMA/qpoly - QMA With Polynomial-Size Quantum Advice =

----
CategoryQuantum 

== Description ==

{{{#!description

Is contained in [[Class_PSPACE/poly|$\\text{PSPACE/poly}$]] [Aar06b].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QMA/qpoly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QMA/qpoly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QMA1"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QMA,,1,, - One Sided QMA =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QMA|$\\text{QMA}$]] except that for a "yes" instance, there exists a state that is accepted with probability 1.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Bra06|[Bra06] ]]. It was shown there that Quantum k-SAT is QMA,,1,,-complete for any $ k \\geq 4$. It was also shown there that Quantum 2-SAT is in [[Class_P|$\\text{P}$]].



This result was later improved in [[ZooRefs#GN13|[GN13] ]] where it was shown that Quantum 3-SAT is QMA,,1,,-complete.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QMA1)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QMA1 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QMAM"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QMAM - Quantum Merlin-Arthur-Merlin Public-Coin Interactive Proofs =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems for which a "yes" answer can be verified by a public-coin quantum MAM protocol, as follows.  Merlin sends a polynomial-size quantum state to Arthur.  Arthur then flips some classical coins (in fact, he only has to flip one without loss of generality) and sends the outcome to Merlin.  At this stage Arthur is not yet allowed to perform any quantum operations.  Merlin then sends Arthur another quantum state.  Finally, Arthur performs a [[Class_BQP|$\\text{BQP}$]] operation on both of the states simultaneously, and either accepts or rejects.  The completeness and soundness requirements are the same as for [[Class_AM|$\\text{AM}$]].  Also, Merlin's messages might be entangled.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined by Marriott and Watrous [[ZooRefs#MW05|[MW05] ]], who also showed that [[Class_QMAM|$\\text{QMAM}$]] = QIP(3) = [[Class_QIP|$\\text{QIP}$]].



Hence [[Class_QMAM|$\\text{QMAM}$]] contains [[Class_PSPACE|$\\text{PSPACE}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QMAM)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QMAM because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QMAlog"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QMA,,log,, - QMA With Logarithmic-Size Proofs =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QMA|$\\text{QMA}$]] except that the quantum proof has O(log n) qubits instead of a polynomial number.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_BQP|$\\text{BQP}$]] [[ZooRefs#MW05|[MW05] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QMAlog)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QMAlog because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QMIP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QMIP - Quantum Multi-Prover Interactive Proofs =

----
CategoryQuantum 

== Description ==

{{{#!description

The quantum generalization of [[Class_MIP|$\\text{MIP}$]], and the multi-prover generalization of [[Class_QIP|$\\text{QIP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A quantum multi-prover interactive proof system is the same as a classical one, except that all messages and verifier computations are quantum.  As in [[Class_MIP|$\\text{MIP}$]], there is no communication among the provers; however, the provers share unlimited prior entanglement.  The number of provers and number of rounds can both be polynomial in n.



Defined in [[ZooRefs#KM02|[KM02] ]].



Shown to be equal to [[Class_MIP*|$\\text{MIP*}$]] in [[ZooRefs#RUV12|[RUV12] ]].



[[Class_QMIP|$\\text{QMIP}$]] contains [[Class_NEXP|$\\text{NEXP}$]] simply because [[Class_MIP*|$\\text{MIP*}$]] contains [[Class_NEXP|$\\text{NEXP}$]] [[ZooRefs#IV12|[IV12] ]]. Since we know that [[Class_NEXP|$\\text{NEXP}$]] = [[Class_QMIPne|$\\text{QMIP}_\\text{ne}\\text{}$]], this tells us that giving the provers unlimited prior entanglement does not make the class less powerful.



Fascinatingly, no relationship between [[Class_QMIP|$\\text{QMIP}$]] and [[Class_NEXP|$\\text{NEXP}$]] is known.  We don't know whether allowing the provers unlimited prior entanglement makes the class more powerful, less powerful, or both!
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QMIP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QMIP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QMIPle"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QMIP,,le,, - Quantum Multi-Prover Interactive Proofs With Limited Prior Entanglement =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QMIP|$\\text{QMIP}$]], except that now the provers share only a polynomial number of EPR pairs, instead of an unlimited number.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#KM02|[KM02] ]], where it was also shown that [[Class_QMIPle|$\\text{QMIP}_\\text{le}\\text{}$]] is contained in [[Class_NEXP|$\\text{NEXP}$]] = [[Class_QMIPne|$\\text{QMIP}_\\text{ne}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QMIPle)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QMIPle because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QMIPne"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QMIP,,ne,, - Quantum Multi-Prover Interactive Proofs With No Prior Entanglement =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QMIP|$\\text{QMIP}$]], except that now the provers have no prior entanglement.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#KM02|[KM02] ]], where it was also shown that [[Class_QMIPne|$\\text{QMIP}_\\text{ne}\\text{}$]] = [[Class_NEXP|$\\text{NEXP}$]].  Thus, [[Class_QMIPne|$\\text{QMIP}_\\text{ne}\\text{}$]] contains [[Class_QMIPle|$\\text{QMIP}_\\text{le}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QMIPne)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QMIPne because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QNC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QNC - Quantum NC =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems solvable by polylogarithmic-depth quantum circuits with bounded probability of error.  (A uniformity condition may also be imposed.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Has the same relation to [[Class_NC|$\\text{NC}$]] as [[Class_BQP|$\\text{BQP}$]] does to [[Class_P|$\\text{P}$]].



[[ZooRefs#CW00|[CW00] ]] showed that factoring is in [[Class_ZPP|$\\text{ZPP}$]] with a [[Class_QNC|$\\text{QNC}$]] oracle.



Is incomparable with [[Class_BPP|$\\text{BPP}$]] as far as anyone knows.



See also: [[Class_RNC|$\\text{RNC}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QNC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QNC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QNC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QNC^0^ - Quantum NC0 =

----
CategoryQuantum 

== Description ==

{{{#!description

Constant-depth quantum circuits without fanout gates.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Spa02|[Spa02] ]].



Contained in [[Class_QNCf0|$\\text{QNC}_\\text{f}\\text{}^\\text{0}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QNC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QNC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QNC1"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QNC^1^ - Quantum NC1 =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QNC1|$\\text{QNC}^\\text{1}\\text{}$]], but for the exact rather than bounded-error case.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



In contrast to [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]], it is not clear how to simulate [[Class_QNC1|$\\text{QNC}^\\text{1}\\text{}$]] on a quantum computer in which one qubit is initialized to a pure state, and the remaining qubits are in the maximally mixed state [[ZooRefs#ASV00|[ASV00] ]].



See also [[ZooRefs#MN02|[MN02] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QNC1)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QNC1 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QNCf0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QNC,,f,,^0^ - Quantum NC0 With Unbounded Fanout =

----
CategoryQuantum 

== Description ==

{{{#!description

Constant-depth quantum circuits with unbounded-fanout gates.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Spa02|[Spa02] ]].



Contains [[Class_QNC0|$\\text{QNC}^\\text{0}\\text{}$]], and is contained in [[Class_QACC0|$\\text{QACC}^\\text{0}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QNCf0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QNCf0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QP - Quasipolynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Equals DTIME(2^polylog(n)^).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QPLIN"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QPLIN - Linear Quasipolynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Equals DTIME(n^O(log n)^).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Has the same relationship to [[Class_QP|$\\text{QP}$]] that [[Class_E|$\\text{E}$]] does to [[Class_EXP|$\\text{EXP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QPLIN)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QPLIN because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QPSPACE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QPSPACE - Quasipolynomial-Space =

----
CategoryClassical 

== Description ==

{{{#!description

Equals DSPACE(2^polylog(n)^).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



According to [[ZooRefs#BG94|[BG94] ]], Beigel and Feigenbaum and (independently) Krawczyk showed that [[Class_QPSPACE|$\\text{QPSPACE}$]] is not contained in [[Class_Check|$\\text{Check}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QPSPACE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QPSPACE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QRG"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QRG - Quantum Refereed Games =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_RG|$\\text{RG}$]], except that now the verifier is a [[Class_BQP|$\\text{BQP}$]] machine, and can exchange polynomially many quantum messages with the competing provers.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The two provers are computationally unbounded, but must obey the laws of quantum mechanics.  Also, we can assume without loss of generality that the provers share no entanglement, because adversaries gain no advantage by sharing information.



Defined in [[ZooRefs#Gut05|[Gut05] ]], where it was also shown that [[Class_QRG|$\\text{QRG}$]] is contained in [[Class_NEXP|$\\text{NEXP}$]] ∩ [[Class_coNEXP|$\\text{coNEXP}$]].



[[Class_QRG|$\\text{QRG}$]] trivially contains [[Class_RG|$\\text{RG}$]] (and hence [[Class_EXP|$\\text{EXP}$]]), as well as [[Class_SQG|$\\text{SQG}$]].



[[Class_QRG|$\\text{QRG}$]] is contained in [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#GW07|[GW07] ]].  Hence [[Class_QRG|$\\text{QRG}$]] = [[Class_RG|$\\text{RG}$]] = [[Class_EXP|$\\text{EXP}$]] and finding optimal strategies for zero-sum quantum games is no harder than finding optimal strategies for zero-sum classical games.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QRG)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QRG because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QRG(1)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QRG(1) - One-turn Quantum Refereed Games =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of problems for which there exists a [[Class_BQP|$\\text{BQP}$]] machine M such that:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes," then there exists a quantum state ρ such that for all quantum states σ, M(ρ,σ) accepts with probability at least 2/3.

If the answer is "no," then there exists a σ such that for all ρ, M(ρ,σ) rejects with probability at least 2/3.



In other words, it's the same as QRG(k) for $k=1$, the class of problems that admit quantum interactive proofs with competing provers in which there's no communication from the verifier back to the provers.  QRG(1) is the quantum version of RG(1).



Defined in [[ZooRefs#JW09|[JW09] ]], where it was shown that QRG(1) is contained in [[Class_PSPACE|$\\text{PSPACE}$]] .



QRG(1) trivially contains [[Class_QMA|$\\text{QMA}$]] (and indeed P^QMA^).



QRG(1) is trivially contained in QRG(2) (and hence [[Class_PSPACE|$\\text{PSPACE}$]]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QRG(1))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QRG(1) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QRG(2)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QRG(2) - Two-turn (one-round) Quantum Refereed Games =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QRG|$\\text{QRG}$]], except that now the verifier can exchange only two messages with each prover.  Messages are exchanged in parallel, so the verifier cannot process the answer from one prover before preparing the question for the other.  QRG(2) is the quantum version of RG(2).  See also QRG(k).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



QRG(2) trivially contains RG(2) (and hence [[Class_PSPACE|$\\text{PSPACE}$]]).



QRG(2) is trivially contained in [[Class_SQG|$\\text{SQG}$]] (and hence [[Class_PSPACE|$\\text{PSPACE}$]]).  Hence QRG(2) = RG(2) = [[Class_PSPACE|$\\text{PSPACE}$]] and finding optimal strategies for two-turn zero-sum quantum games is no harder than finding optimal strategies for two-turn zero-sum classical games.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QRG(2))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QRG(2) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QRG(k)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QRG(k) - k-turn Quantum Refereed Games =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as [[Class_QRG|$\\text{QRG}$]], except that now the verifier exchanges exactly k messages with each prover where k is a polynomial-bounded function of the input length.  Messages are exchanged in parallel.  QRG(k) is the quantum version of RG(k).  By definition, QRG(poly) = [[Class_QRG|$\\text{QRG}$]].  See also QRG(1) and QRG(2).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



QRG(k) trivially contains RG(k) for each k (and hence [[Class_PSPACE|$\\text{PSPACE}$]] when $ k \\geq 2$).  QRG(4) trivially contains [[Class_SQG|$\\text{SQG}$]].



QRG(k) is trivially contained in [[Class_QRG|$\\text{QRG}$]] for each k (and hence [[Class_EXP|$\\text{EXP}$]]).



Other than these trivial bounds, very little is known of QRG(k) for intermediate values of k.  For example, does QRG(k) = RG(k) for each k?
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QRG(k))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QRG(k) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QS2P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QS,,2,,P - Quantum S2P =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of problems for which there exists a [[Class_BQP|$\\text{BQP}$]] machine M such that:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes," then there exists a quantum state ρ such that for all quantum states σ, M(ρ,Ï) accepts with probability at least 2/3.

If the answer is "no," then there exists a σ such that for all ρ, M(ρ,σ) rejects with probability at least 2/3.



In other words, it's the same as [[Class_SQG|$\\text{SQG}$]], but without communication from the verifier back to the provers.



Contains [[Class_QMA|$\\text{QMA}$]] (and indeed P^QMA^), and is contained in [[Class_SQG|$\\text{SQG}$]] and hence [[Class_EXP|$\\text{EXP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QS2P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QS2P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_QSZK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= QSZK - Quantum Statistical Zero-Knowledge =

----
CategoryQuantum 

== Description ==

{{{#!description

A quantum analog of [[Class_SZK|$\\text{SZK}$]] (or more precisely [[Class_HVSZK|$\\text{HVSZK}$]]).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Arthur is a [[Class_BQP|$\\text{BQP}$]] (i.e. quantum) verifier who can exchange quantum messages with Merlin.  So Arthur and Merlin's states may become entangled during the course of the protocol.



Arthur's "view" of his interaction with Merlin is taken to be the sequence of mixed states he has, over all steps of the protocol.  The zero-knowledge requirement is that each of these states must have trace distance at most (say) 1/10 from a state that Arthur could prepare himself (in [[Class_BQP|$\\text{BQP}$]]), without help from Merlin.  Arthur is assumed to be an honest verifier.



Defined in [[ZooRefs#Wat02|[Wat02] ]], where the following was also shown:



[[Class_QSZK|$\\text{QSZK}$]] is contained in [[Class_PSPACE|$\\text{PSPACE}$]].

[[Class_QSZK|$\\text{QSZK}$]] is closed under complement.

Any protocol can be parallelized to consist of two messages, so that [[Class_QSZK|$\\text{QSZK}$]] is in [[Class_QIP[2]|$\\text{QIP[2]}$]].

One can assume without loss of generality that protocols are public-coin, as for [[Class_SZK|$\\text{SZK}$]].

[[Class_QSZK|$\\text{QSZK}$]] has a natural complete promise problem, called Quantum State Distinguishability (QSD).  We are given quantum circuits Q,,0,, and Q,,1,,.  Let ρ,,0,, and ρ,,1,, be the mixed states they produce respectively, when run on the all-0 state (and when non-output qubits are traced out).  We are promised that the trace distance between ρ,,0,, and ρ,,1,, is either at most α or at least β, where α and β are constants in [0,1] satisfying α < β^2^.  The problem is to decide which of these is the case.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_QSZK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save QSZK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_R"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= R - Recursive Languages =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a Turing machine.  Often identified with the class of 'effectively computable' functions (the Church-Turing thesis).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Tur36|[Tur36] ]], [[ZooRefs#Chu41|[Chu41] ]], and other seminal early papers.



Equals [[Class_RE|$\\text{RE}$]] ∩ [[Class_coRE|$\\text{coRE}$]].



Strictly contains [[Class_PR|$\\text{PR}$]], the primitive recursive functions (see [[ZooRefs#Kle71|[Kle71] ]]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_R)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save R because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RBQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RBQP - Strict Quantum RP =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of problems in [[Class_NP|$\\text{NP}$]] whose witnesses are in [[Class_FBQP|$\\text{FBQP}$]].  For example, the set of square-free numbers is in coRBQP using only the fact that factoring is in [[Class_FBQP|$\\text{FBQP}$]].  (Even without a proof that the factors are prime, the factorization proves that there is a square divisor.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_RP|$\\text{RP}$]] and [[Class_ZBQP|$\\text{ZBQP}$]], and is contained in [[Class_BQP|$\\text{BQP}$]] and [[Class_RQP|$\\text{RQP}$]].  Defined here to clarify [[Class_EQP|$\\text{EQP}$]]; see also [[Class_ZBQP|$\\text{ZBQP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RBQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RBQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RE - Recursively Enumerable Languages =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which a 'yes' answer can be verified by a Turing machine in a finite amount of time.  (If the answer is 'no,' on the other hand, the machine might never halt.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equivalently, the class of decision problems for which a Turing machine can list all the 'yes' instances, one by one (this is what 'enumerable' means).



A problem C is complete for [[Class_RE|$\\text{RE}$]] if (1) C is in [[Class_RE|$\\text{RE}$]] and (2) any problem in [[Class_RE|$\\text{RE}$]] can be reduced to C by a Turing machine.



Actually there are two types of reduction: M-reductions (for many-one), in which a single instance of the original problem is mapped to an instance of C, and T-reductions (for Turing), in which an algorithm for the original problem can make arbitrarily many calls to an oracle for C.



RE-complete sets are also called creative sets for some reason.



The canonical RE-complete problem is the halting problem: i.e., given a Turing machine, does it halt when started on a blank tape?



The famous unsolvability of the halting problem [[ZooRefs#Tur36|[Tur36] ]] implies that [[Class_R|$\\text{R}$]] does not equal [[Class_RE|$\\text{RE}$]].



Also, [[Class_RE|$\\text{RE}$]] does not equal [[Class_coRE|$\\text{coRE}$]].



[[Class_RE|$\\text{RE}$]] and [[Class_coRE|$\\text{coRE}$]] can be generalized to the arithmetic hierarchy [[Class_AH|$\\text{AH}$]].



There are problems in [[Class_RE|$\\text{RE}$]] that are neither RE-complete under T-reductions, nor in [[Class_R|$\\text{R}$]] [[ZooRefs#Fri57|[Fri57] ]] [[ZooRefs#Muc56|[Muc56] ]].  This is the resolution of Post's problem [[ZooRefs#Pos44|[Pos44] ]].



Indeed, [[Class_RE|$\\text{RE}$]] contains infinitely many nonequivalent 'T-degrees.'  (A T-degree is a class of problems, all of which can be T-reduced to one another.)  The structure of the T-degrees has been studied in more detail than you can possibly imagine [[ZooRefs#Sho99|[Sho99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_REG"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= REG - Regular Languages =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by deterministic finite automata (DFAs).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals the class solvable by nondeterministic finite automata (NDFAs).



Equals DSPACE(O(1)) [[ZooRefs#She59|[She59] ]], which equals DSPACE(o(log log n)) [[ZooRefs#HLS65|[HLS65] ]].



Includes, i.e., "Is the parity of the input odd?," but not "Are the majority of bits in the input 1's?"  This is sometimes expressed as "finite automata can't count."



Contained in [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]].



See e.g. [[ZooRefs#Koz97|[Koz97] ]], [[ZooRefs#Gur89|[Gur89] ]] for basic results on regular languages.



The class of decision problems solvable by deterministic finite automata (DFA's).



Equals the class solvable by nondeterministic finite automata (NDFA's).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_REG)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save REG because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RG"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RG - Refereed Games =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by a probabilistic polynomial-time verifier who can exchange a polynomial number of messages with two competing, computationally-unbounded provers -- one trying to convince the verifier that the answer is "yes," the other that the answer is "no."  Note that the verifier can hide information from the provers.  Public-coin [[Class_RG|$\\text{RG}$]] amounts to [[Class_SAPTIME|$\\text{SAPTIME}$]], which equals [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#Pap83|[Pap83] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_RG|$\\text{RG}$]] is in [[Class_EXP|$\\text{EXP}$]] relative to any oracle [[ZooRefs#KM92|[KM92] ]]; they are equal, unrelativized [FK97b].



See also PCD, GPCD.



Contains [[Class_RG[1]|$\\text{RG[1]}$]], and is contained in [[Class_QRG|$\\text{QRG}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RG)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RG because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RG(1)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RG(1) - One-turn Refereed Games =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems for which there exists a [[Class_BPP|$\\text{BPP}$]] machine M such that, on input x:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'yes,' then there exists a distribution Y such that for all distributions Z, M(x,Y,Z) accepts with probability at least 2/3.

If the answer is 'no,' then there exists a distribution Z such that for all distributions Y, M(x,Y,Z) rejects with probability at least 2/3.



In other words, it's the same as RG(k) for $k = 1$, the class of problems that admit interactive proofs with competing provers in which there's no communication from the verifier back to the provers.



RG(1) trivially contains [[Class_S2P|$\\text{S}_\\text{2}\\text{P}$]].  Indeed, RG(1) can be viewed as a randomized version of [[Class_S2P|$\\text{S}_\\text{2}\\text{P}$]].



RG(1) is trivially contained in RG(2) (and hence [[Class_PSPACE|$\\text{PSPACE}$]]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RG(1))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RG(1) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RG(2)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RG(2) - Two-turn (one-round) Refereed Games =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_RG|$\\text{RG}$]], except that now the verifier can exchange only two messages with each prover. Messages are exchanged in parallel, so the verifier cannot process the answer from one prover before preparing the question for the other.  See also RG(k).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



RG(2) is contained in [[Class_PSPACE|$\\text{PSPACE}$]], and they are equal, unrelativized [FK97b].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RG(2))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RG(2) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RG(k)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RG(k) - k-turn Refereed Games =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_RG|$\\text{RG}$]], except that now the verifier exchanges exactly k messages with each prover where k is a polynomial-bounded function of the input length. Messages are exchanged in parallel.  By definition, RG(poly) = [[Class_RG|$\\text{RG}$]]. See also RG(1) and RG(2).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Other than trivial bounds, very little is known of RG(k) for intermediate values of k. For example, does RG(k) = [[Class_PSPACE|$\\text{PSPACE}$]] for each constant $k\\geq 2$?
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RG(k))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RG(k) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RG[1]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RG[1] - One-Round Refereed Games =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_RG|$\\text{RG}$]], except that now the verifier can exchange only a single round of messages with the two provers.  A round consists of private messages from the verifier to the provers, followed by private responses from the provers to the verifier.  Since the queries are private, they may as well be parallel; likewise the responses.  This makes [[Class_RG[1]|$\\text{RG[1]}$]] a symmetric class, indeed a randomized analogue of [[Class_S2P|$\\text{S}_\\text{2}\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_RG[1]|$\\text{RG[1]}$]] is contained in [[Class_PSPACE|$\\text{PSPACE}$]], and they are equal, unrelativized [FK97b].



Contains [[Class_S2P|$\\text{S}_\\text{2}\\text{P}$]] and is contained in [[Class_SQG|$\\text{SQG}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RG[1])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RG[1] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RHL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= R,,H,,L - Randomized Halting Logarithmic-Space =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_RP|$\\text{RP}$]] does to [[Class_P|$\\text{P}$]].  The randomized machine must halt for every input and every setting of the random tape.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains undirected reachability (is there a path from vertex u to vertex v in an undirected graph?) [[ZooRefs#AKL+79|[AKL+79] ]].



Contained in [[Class_RL|$\\text{RL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RHL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RHL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RHSPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= R,,H,,SPACE(f(n)) - One-Sided Error Halting Probabilistic f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to BP,,H,,SPACE(f(n)) as [[Class_RP|$\\text{RP}$]] does to [[Class_BPP|$\\text{BPP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RHSPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RHSPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RL - Randomized Logarithmic-Space =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_RP|$\\text{RP}$]] does to [[Class_P|$\\text{P}$]].  The randomized machine must halt with probability 1 on any input.  It must also run in polynomial time (since otherwise we would just get}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==

[[Class_NL|$\\text{NL}$]]).



Contains [[Class_RHL|$\\text{R}_\\text{H}\\text{L}$]].



Contained in [[Class_SC|$\\text{SC}$]] [[ZooRefs#Nis92|[Nis92] ]].



[[ZooRefs#RTV05|[RTV05] ]] give strong evidence that [[Class_RL|$\\text{RL}$]] = [[Class_L|$\\text{L}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RNC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RNC - Randomized NC =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_NC|$\\text{NC}$]] as [[Class_RP|$\\text{RP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains the maximum matching problem for bipartite graphs [[ZooRefs#MVV87|[MVV87] ]].



Contained in [[Class_QNC|$\\text{QNC}$]].



See also: [[Class_coRNC|$\\text{coRNC}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RNC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RNC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RP - Randomized Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'yes,' at least 1/2 of computation paths accept.

If the answer is 'no,' all computation paths reject.



Defined in [[ZooRefs#Gil77|[Gil77] ]] (implicitly: the class VPP that is defined is equivalent to [[Class_RP|$\\text{RP}$]] by running the recognizer as many times as necessary to reach probability 1/2).



Contains the problem of testing whether an integer is prime [[ZooRefs#AH87|[AH87] ]], although this problem was subsequently shown to be in [[Class_P|$\\text{P}$]] [[ZooRefs#AKS02|[AKS02] ]].



For other problems in [[Class_RP|$\\text{RP}$]], see the standard text on randomized algorithms, [[ZooRefs#MR95|[MR95] ]].



Has the same p-measure as [[Class_ZPP|$\\text{ZPP}$]]. Moreover, this measure is either zero or one. If the measure is non-zero, then [[Class_ZPP|$\\text{ZPP}$]] = [[Class_BPP|$\\text{BPP}$]] = [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#IM03|[IM03] ]].



See also: [[Class_coRP|$\\text{coRP}$]], [[Class_ZPP|$\\text{ZPP}$]], [[Class_BPP|$\\text{BPP}$]].



Defined in [[ZooRefs#Gil77|[Gil77] ]].



Contains the problem of testing whether an integer is prime [[ZooRefs#AH87|[AH87] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RPP - Restricted Pseudo Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems (x,m) (where x is an input of length |x|=n and m is an integer parameter), that are solvable by a nondeterministic (i.e. [[Class_NP|$\\text{NP}$]]) machine in poly(n+m) time and O(m+log n) space simultaneously.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Mon80|[Mon80] ]].



See also [[Class_FPT|$\\text{FPT}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RPkcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RP,,k,,^cc^ - Randomized Pcc =

----
CategoryClassical 

== Description ==

{{{#!description

The class of functions $F$ which can be computed by $k$ players with access to shared random bits in the number-on-forehead (defined as in [[Class_Pkcc|$\\text{P}_\\text{k}\\text{}^\\text{cc}\\text{}$]]) model, subject to two constraints:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The communication cost (the sum of the number of random bits used and bits written to the shared blackboard) is O(\textrm{polylog}(n)).

 If F(X_1, \dots, X_k) = 1, then the players decide correctly with probably at least 2/3, whereas if F(X_1, \dots, X_k) = 0, the players always decide correctly.



[[Class_NPkcc|$\\text{NP}_\\text{k}\\text{}^\\text{cc}\\text{}$]] is not equal to [[Class_RPkcc|$\\text{RP}_\\text{k}\\text{}^\\text{cc}\\text{}$]] for $k\\le(1-\\delta)\\cdot\\log n$ players, for any constant $\\delta>0$ [[ZooRefs#DP08|[DP08] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RPkcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RPkcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RQP - One-sided Error Extension of EQP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of questions that can be answered by a QTM that accepts with probability 0 when the true answer is no, and accepts with probability at least 1/2 when the true answer is yes.  Since one of the probabilities has to vanish, [[Class_RQP|$\\text{RQP}$]] has the same technical caveats as [[Class_EQP|$\\text{EQP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_ZQP|$\\text{ZQP}$]] and [[Class_RBQP|$\\text{RBQP}$]], and is contained in [[Class_BQP|$\\text{BQP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RSPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RSPACE(f(n)) - Randomized f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_RL|$\\text{RL}$]], but for O(f(n))-space instead of logarithmic-space.  (Just as an [[Class_RL|$\\text{RL}$]] machine must run in polynomial time, so an RSPACE(f(n)) machine must run in 2^O(f(n))^ time.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in NSPACE(f(n)) and BPSPACE(f(n)).



Same as [[Class_RL|$\\text{RL}$]], but for O(f(n))-space instead of logarithmic-space.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RSPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RSPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RevSPACE(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RevSPACE(f(n)) - Reversible f(n)-Space =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable in space O(f(n)) by a reversible Turing machine (a deterministic Turing machine for which every configuration has at most one immediate predecessor).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Was shown to equal DSPACE(f(n)) [[ZooRefs#LMT97|[LMT97] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_RevSPACE(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RevSPACE(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_S2-EXP•PNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= S,,2,,-EXP•P^NP^ - Don't Ask =

----
CategoryClassical 

== Description ==

{{{#!description

One of the caged classes of the Complexity Zoo.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Has been implicated in a collapse scandal involving [[Class_AM[polylog]|$\\text{AM[polylog]}$]], [[Class_coNP|$\\text{coNP}$]], and [[Class_EH|$\\text{EH}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_S2-EXP•PNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save S2-EXP•PNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_S2P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= S,,2,,P - Second Level of the Symmetric Hierarchy =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

The class of decision problems for which there is a polynomial-time predicate [[Class_P|$\\text{P}$]] such that, on input x,}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'yes,' then there exists a y such that for all z, P(x,y,z) is true.

If the answer is 'no,' then there exists a z such that for all y, P(x,y,z) is false.



Note that this differs from [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] in that the quantifiers in the second condition are reversed.



Less formally, [[Class_S2P|$\\text{S}_\\text{2}\\text{P}$]] is the class of one-round games in which a prover and a disprover submit simultaneous moves to a deterministic, polynomial-time referee.  In [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]], the disprover moves first.



Defined in [[ZooRefs#RS98|[RS98] ]], where it was also shown that [[Class_S2P|$\\text{S}_\\text{2}\\text{P}$]] contains [[Class_MA|$\\text{MA}$]] and [[Class_Δ2P|$\\text{Δ}_\\text{2}\\text{P}$]].  Defined independently in [[ZooRefs#Can96|[Can96] ]].



Contained in ZPP^NP^ [[ZooRefs#Cai01|[Cai01] ]].



[[Class_S2-EXP•PNP|$\\text{S}_\\text{2}\\text{-EXP•P}^\\text{NP}\\text{}$]]: Don't Ask 

One of the caged classes of the Complexity Zoo.

Has been implicated in a collapse scandal involving [[Class_AM[polylog]|$\\text{AM[polylog]}$]], [[Class_coNP|$\\text{coNP}$]], and [[Class_EH|$\\text{EH}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_S2P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save S2P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SAC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SAC - Semi-Unbounded-Fanin AC =

----
CategoryClassical 

== Description ==

{{{#!description

SAC^k^ is the class of decision problems solvable by a family of depth-O(log^k^n) circuits with unbounded-fanin OR & bounded-fanin AND gates.  Negations are only allowed at the input level.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A uniformity condition may also be imposed.



Defined by [[ZooRefs#BCD+89|[BCD+89] ]], who also showed that SAC,,k,, is closed under complement for every k>0.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SAC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SAC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SAC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SAC^0^ - Semi-Unbounded-Fanin AC0 =

----
CategoryClassical 

== Description ==

{{{#!description

See [[Class_SAC|$\\text{SAC}$]] for definition.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Not closed under complement [[ZooRefs#BCD+89|[BCD+89] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SAC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SAC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SAC1"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SAC^1^ - Semi-Unbounded-Fanin AC1 =

----
CategoryClassical 

== Description ==

{{{#!description

See [[Class_SAC|$\\text{SAC}$]] for definition.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals LOGCFL/poly [[ZooRefs#Ven91|[Ven91] ]].



Contained in [[Class_⊕SAC1|$\\text{⊕SAC}^\\text{1}\\text{}$]] [[ZooRefs#GW96|[GW96] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SAC1)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SAC1 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SAPTIME"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SAPTIME - Stochastic Alternating Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by a polynomial-time Turing machine with three kinds of quantifiers: existential, universal, and randomized.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#Pap83|[Pap83] ]], where it was also observed that [[Class_SAPTIME|$\\text{SAPTIME}$]] = [[Class_PSPACE|$\\text{PSPACE}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SAPTIME)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SAPTIME because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SBP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SBP - Small Bounded-Error Probability =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which the following holds.  There exists a [[Class_SharpP|$\\text{#P}$]] function f and an [[Class_FP|$\\text{FP}$]] function g such that, for all inputs x,}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes" then f(x) > g(x).

If the answer is "no" then f(x) < g(x)/2.



Defined in [[ZooRefs#BGM02|[BGM02] ]], where the following was also shown:



[[Class_SBP|$\\text{SBP}$]] contains [[Class_MA|$\\text{MA}$]], [[Class_WAPP|$\\text{WAPP}$]], and [[Class_∃BPP|$\\text{∃BPP}$]].

[[Class_SBP|$\\text{SBP}$]] is contained in [[Class_AM|$\\text{AM}$]] and [[Class_BPPpath|$\\text{BPP}_\\text{path}\\text{}$]].

There exists an oracle relative to which [[Class_SBP|$\\text{SBP}$]] is not contained in [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]].

[[Class_SBP|$\\text{SBP}$]] is closed under union.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SBP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SBP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SBQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SBQP - Small Bounded-Error Quantum Polynomial-Time =

----
CategoryQuantum 

== Description ==

{{{#!description

The class of decision problems for which there exists a polynomial-time quantum algorithm that accepts with probability at least 2^−p(n)^ if the answer is "yes", and with probability at most 2^−p(n)−1^ if the answer is "no", for some polynomial p.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined by Kuperberg in [[ZooRefs#Kup09|[Kup09] ]], where he showed that [[Class_SBQP|$\\text{SBQP}$]] = [[Class_A0PP|$\\text{A}_\\text{0}\\text{PP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SBQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SBQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SC - Steve's Class =

----
CategoryClassical 

== Description ==

{{{#!description

(Named in honor of Stephen Cook.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of decision problems solvable by a Turing machine that simultaneously uses polynomial time and polylogarithmic space.



Note that [[Class_SC|$\\text{SC}$]] might be smaller than [[Class_P|$\\text{P}$]] ∩ [[Class_polyL|$\\text{polyL}$]], since for the latter, it suffices to have two separate algorithms: one polynomial-time and the other polylogarithmic-space.



Deterministic context-free languages (DCFLs) can be recognized in [[Class_SC|$\\text{SC}$]] [[ZooRefs#Coo79|[Coo79] ]].



[[Class_SC|$\\text{SC}$]] contains [[Class_RL|$\\text{RL}$]] and [[Class_BPL|$\\text{BPL}$]] [[ZooRefs#Nis92|[Nis92] ]].



[[Class_SC|$\\text{SC}$]] equals DTISP(poly,polylog) by definition.



Deterministic context-free languages (DCFL's) can be recognized in [[Class_SC|$\\text{SC}$]] [[ZooRefs#Coo79|[Coo79] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SE - Subexponentially-Solvable Search Problems =

----
CategoryClassical 

== Description ==

{{{#!description

The class of [[Class_FNP|$\\text{FNP}$]] search problems solvable in O(2^εn^) time for every ε>0.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#IPZ01|[IPZ01] ]], who also gave reductions showing that if any of k-SAT, k-colorability, k-set cover, clique, or vertex cover is in [[Class_SE|$\\text{SE}$]], then all of them are.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SEH"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SEH - Strong Exponential Hierarchy =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

The union of [[Class_NE|$\\text{NE}$]], NP^NE^, NP^NP^NE^, and so on.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Is called "strong" to contrast it with the ordinary Exponential Hierarchy [[Class_EH|$\\text{EH}$]].



Note that we would get the same class if we replaced [[Class_NE|$\\text{NE}$]] by [[Class_NEXP|$\\text{NEXP}$]].



[[Class_SEH|$\\text{SEH}$]] collapses to P^NE^ [[ZooRefs#Hem89|[Hem89] ]]



There exists an oracle relative to which [[Class_SEH|$\\text{SEH}$]] is not contained in [[Class_EH|$\\text{EH}$]] [[ZooRefs#Hem89|[Hem89] ]].

[[Class_EH|$\\text{EH}$]] and [[Class_SEH|$\\text{SEH}$]] are incomparable for all anyone knows.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SEH)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SEH because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SFk"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SF,,k,, - Width-k Bottleneck Turing Machines =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a k-bottleneck Turing machine. This is a machine that, after a polynomial amount of time, erases everything on the tape except for a single k-valued "safe-storage".  There's also a counter recording the number of erasings, which is in effect a non-deterministic witness.  For example, SF,,2,, contains both [[Class_⊕P|$\\text{⊕P}$]] and [[Class_NP|$\\text{NP}$]] by using the counter as a witness.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#CF91|[CF91] ]], where it was also shown that SF,,5,, = [[Class_PSPACE|$\\text{PSPACE}$]].



The complexity of SF,,2,,, SF,,3,,, and SF,,4,, was studied in [[ZooRefs#Ogi94|[Ogi94] ]] and [[ZooRefs#Her97|[Her97] ]].  The following result of those authors is among the caged beasts of the Complexity Zoo:



SF,,4,, is contained in BP ⊕P^Mod_3P ^ [[Class_⊕P|$\\text{⊕P}$]] ^ Mod_3P ^ [[Class_⊕P|$\\text{⊕P}\\text{}$]]



(Here the BP operator means that one makes the class into a bounded-error probabilistic class, the same way one makes [[Class_P|$\\text{P}$]] into [[Class_BPP|$\\text{BPP}$]] and [[Class_NP|$\\text{NP}$]] into [[Class_AM|$\\text{AM}$]].)
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SFk)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SFk because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SKC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SKC - Statistical Knowledge Complexity =

----
CategoryClassical 

== Description ==

{{{#!description

A hierarchy of generalizations of [[Class_SZK|$\\text{SZK}$]], in which Arthur is allowed to gain some information from his interaction with Merlin.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GP91|[GP91] ]].



There are several variants (which we only describe roughly), including:



SKC,,hint,,(k(n)): Hint sense.  The simulator can reproduce Arthur's view of the protocol if given a hint string of size k(n).

SKC,,hint,,(k(n)): Strict oracle sense.  The simulator can reproduce Arthur's view if allowed k(n) queries to an oracle O.

SKC,,avg,,(k(n)): Average oracle sense.  For each input, the expected number of queries the simulator makes to oracle O is at most k(n).

SKC,,ent,,(k(n)): Entropy sense.  Defined in [[ZooRefs#ABV95|[ABV95] ]]. For each input, the expectation (over Arthur's random coins) of -log(P) is at most k(n), where [[Class_P|$\\text{P}$]] is the probability that the view output by the simulator equals the view resulting from the actual protocol.



See also: [[Class_PKC|$\\text{PKC}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SKC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SKC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SL - Symmetric Logarithmic-Space =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by a nondeterministic Turing machine in logarithmic space, such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'yes,' one or more computation paths accept.

If the answer is 'no,' all paths reject.

If the machine can make a nondeterministic transition from configuration A to configuration B, then it can also transition from B to A.  (This is what 'symmetric' means.)



Defined in [[ZooRefs#LP82|[LP82] ]].



The undirected s-t connectivity problem (USTCON: is there a path from vertex s to vertex t in a given undirected graph?) is complete for [[Class_SL|$\\text{SL}$]], under L-reductions.



[[Class_SL|$\\text{SL}$]] contains [[Class_L|$\\text{L}$]], and is contained in [[Class_NL|$\\text{NL}$]].



It follows from [[ZooRefs#AKL+79|[AKL+79] ]] that [[Class_SL|$\\text{SL}$]] is contained in [[Class_L/poly|$\\text{L/poly}$]].



[[ZooRefs#KW93|[KW93] ]] showed that [[Class_SL|$\\text{SL}$]] is contained in [[Class_⊕L|$\\text{⊕L}$]], as well as [[Class_ModkL|$\\text{Mod}_\\text{k}\\text{L}$]] for every prime k.



[[Class_SL|$\\text{SL}$]] is also contained in DSPACE(log^3/2^n) [[ZooRefs#NSW92|[NSW92] ]], and indeed in DSPACE(log^4/3^n) [[ZooRefs#ATW+00|[ATW+00] ]].



[[ZooRefs#NT95|[NT95] ]] showed that [[Class_SL|$\\text{SL}$]] equals [[Class_coSL|$\\text{coSL}$]], and furthermore that SL^SL^ = [[Class_SL|$\\text{SL}$]] (that is, the symmetric logspace hierarchy collapses).



Reingold ultimately showed that [[Class_SL|$\\text{SL}$]] = [[Class_L|$\\text{L}$]] [[ZooRefs#Rei04|[Rei04] ]], even relative to an oracle. This subsumes many of the earlier results.



The reachability problem (is there a path from vertex s to vertex t?) for undirected graphs is complete for [[Class_SL|$\\text{SL}$]], under L-reduction.



The story ends with the remarkable result that [[Class_SL|$\\text{SL}$]] = [[Class_L|$\\text{L}$]] (even relative to an oracle)

[[ZooRefs#Rei04|[Rei04] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SLICEWISE PSPACE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SLICEWISE PSPACE - Parametrized PSPACE =

----
CategoryClassical 

== Description ==

{{{#!description

The parameterized version of [[Class_PSPACE|$\\text{PSPACE}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Same as [[Class_FPT|$\\text{FPT}$]], except that now on input (x,k) (k a parameter), the space used must be f(k)p(|x|), where p is a polynomial.



If [[Class_P|$\\text{P}$]] = [[Class_PSPACE|$\\text{PSPACE}$]], then [[Class_FPT|$\\text{FPT}$]] = SLICEWISE [[Class_PSPACE|$\\text{PSPACE}$]].



Defined in [[ZooRefs#DF99|[DF99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SLICEWISE PSPACE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SLICEWISE PSPACE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SNP - Strict NP =

----
CategoryClassical 

== Description ==

{{{#!description

[[ZooRefs#Fag74|[Fag74] ]] showed that [[Class_NP|$\\text{NP}$]] is precisely the class of decision problems reducible to a graph-theoretic property expressible in second-order existential logic.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Then [[Class_SNP|$\\text{SNP}$]] is the class of decision problems reducible to a graph-theoretic predicate with only universal quantifiers over vertices, no existential quantifiers.  As an example, k-SAT (CNF satisfiability with at most k literals per clause, for k a constant) is in [[Class_SNP|$\\text{SNP}$]].  But general SAT is not in [[Class_SNP|$\\text{SNP}$]], basically because we're not allowed to say, "There exists a literal in this clause that satisfies the clause."



Contains [[Class_MMSNP|$\\text{MMSNP}$]].



See also: [[Class_MaxSNP|$\\text{MaxSNP}$]].



[[ZooRefs#Fag74|[Fag74] ]]



[[Class_NP|$\\text{NP}$]]



[[ZooRefs#Pap94|[Pap94] ]]



There exists a relation P(u,v) on vertices of G, such that P(u,u) is false, and for all distinct u,v either P(u,v) or P(v,u), and P(u,v) and P(v,w) implies P(u,w), and if P(u,w) and there does not exist a v for which P(u,v) and P(v,w), then there is an edge from u to w.



total order
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SO"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SO - Second-Order logic =

----
CategoryClassical 

== Description ==

{{{#!description

We define second-order variable  has got an arity k and represent any proposition of arity $k$. They are usually written in upper-case.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Second order logic is the set of [[Class_FO|$\\text{FO}$]] formulae where we add quantification over second-order variables.



Every formuale is equivalent to a formulae in prenex normal form, where we first write quantification on variable on second order and then a FO-formulae in prenex normal form.



In Descriptive complexity we can see that [[Class_SO|$\\text{SO}$]] is equal to [[Class_PH|$\\text{PH}$]], more precisely we have that formulae in prenex normal form where existantial and universal of second order alternate k times are the kth level of the polynomial hierarchy.



This means that [[Class_SO|$\\text{SO}$]] with only existantial second-order quantification is equal to $\\Sigma^1$ which is [[Class_NP|$\\text{NP}$]], and with only universal quantification is equal to $\\Pi^1$ which is Co-NP.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SO)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SO because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SO(Horn)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SO(Horn) - Second-order in Horn form =

----
CategoryClassical 

== Description ==

{{{#!description

SO(horn) is the set of boolean queries definable with second-order formulae in normal form such that the quantifier-free part of the formula is in conjunctive normal form with at most one positive instance of a quantified relation per clause.  (Atomic queries to the database don't count.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



It was shown in [Grä92] that this class is equal to [[Class_P|$\\text{P}$]].



Those formulae can be made in prenex form where the second order is existential and the first order universal without loss of generality.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SO(Horn))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SO(Horn) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SO(Krom)"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SO(Krom) - Second-order in Krom form =

----
CategoryClassical 

== Description ==

{{{#!description

SO(krom) is the set of boolean queries definable with second-order formulae in normal form such that the quantifier-free part of the formula is in Krom form, wich means that in every clause there is at most two literals and the first-order portion contains no existential quantifiers.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



It was shown in [Grä92] that this class is equal to [[Class_NL|$\\text{NL}$]].



Those formulaes can be made in prenex form where the second order is existential and the first order universal without loss of generalities.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SO(Krom))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SO(Krom) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SO-E"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SO-E - Second Order Existential =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which a "yes" answer is expressible by a proposition with second-order existential quantifiers followed by a first-order formula.  See [[ZooRefs#Imm98|[Imm98] ]] for a full definition.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_SO-E|$\\text{SO-E}$]] = [[Class_NP|$\\text{NP}$]] [[ZooRefs#Fag74|[Fag74] ]].



Contains FO(poly(n)).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SO-E)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SO-E because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SO[LFP]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SO[LFP] - Second-Order logic with least fixed point =

----
CategoryClassical 

== Description ==

{{{#!description

[[Class_SO[LFP]|$\\text{SO[LFP]}$]] is to [[Class_SO|$\\text{SO}$]] what FO[LFP] is to [[Class_FO|$\\text{FO}$]]. The LFP operator can now also take second-order variable as argument.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



In Descriptive complexity we can see that 

[[Class_SO[LFP]|$\\text{SO[LFP]}$]] is  equal to EXPTIME.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SO[LFP])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SO[LFP] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SO[TC]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SO[TC] - Second-Order logic with transitive closure =

----
CategoryClassical 

== Description ==

{{{#!description

[[Class_SO[TC]|$\\text{SO[TC]}$]] is to [[Class_SO|$\\text{SO}$]] what FO[TC] is to [[Class_FO|$\\text{FO}$]]. The TC operator can now also take second-order variable as argument.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



In Descriptive complexity we can see that :

[[Class_SO[TC]|$\\text{SO[TC]}$]] is  equal to [[Class_PSPACE|$\\text{PSPACE}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SO[TC])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SO[TC] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SO[t(n)]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SO[$t(n)$] - Iterated Second-Order logic =

----
CategoryClassical 

== Description ==

{{{#!description

SO[$t(n)$] is to [[Class_SO|$\\text{SO}$]] what [[Class_FO[t(n)]|$\\text{FO[t(n)]}$]] is to [[Class_FO|$\\text{FO}$]]. But we now also have second-order quantifier in the quantifier block.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



In Descriptive complexity we can see that :



SO[n^{O(1)}] is  equal to [[Class_PSPACE|$\\text{PSPACE}$]] it is also another way to write SO(TC)

SO[2^{n^{O(1)}}] is equal to EXPTIME it is also another way to write SO(LFP)
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SO[t(n)])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SO[t(n)] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SP - Semi-Efficient Parallel =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems in [[Class_P|$\\text{P}$]] for which the best parallel algorithm (using a polynomial number of processors) is faster than the best serial algorithm by a factor of Ω(n^ε^) for some ε>0.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#KRS90|[KRS90] ]].



[[Class_SP|$\\text{SP}$]] is also an alternate name for [[Class_XPuniform|$\\text{XP}_\\text{uniform}\\text{}$]]
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SPARSE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SPARSE - Sparse Languages =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which the number of 'yes' instances of size n is upper-bounded by a polynomial in n.  If [[Class_SPARSE|$\\text{SPARSE}$]] intersects [[Class_NPC|$\\text{NPC}$]] then [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]] [[ZooRefs#Mah82|[Mah82] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_TALLY|$\\text{TALLY}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SPARSE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SPARSE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SPL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SPL - Stoic PL =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_PL|$\\text{PL}$]] as [[Class_SPP|$\\text{SPP}$]] does to [[Class_PP|$\\text{PP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains the maximum matching and perfect matching problems under a pseudorandom assumption [[ZooRefs#ARZ99|[ARZ99] ]].



Contains [[Class_UL|$\\text{UL}$]].



Contained in [[Class_C=L|$\\text{C}_\\text{=}\\text{L}$]] and [[Class_ModkL|$\\text{Mod}_\\text{k}\\text{L}$]].



Equals the set of problems low for [[Class_GapL|$\\text{GapL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SPL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SPL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SPP - Stoic PP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "no," then the number of accepting computation paths exactly equals the number of rejecting paths.

If the answer is "yes," then these numbers differ by 2.



(A technicality: If the total number of paths is even then the numbers can't differ by 1.)



Defined in [[ZooRefs#FFK94|[FFK94] ]], where it was also shown that [[Class_SPP|$\\text{SPP}$]] is low for [[Class_PP|$\\text{PP}$]], [[Class_C=P|$\\text{C}_\\text{=}\\text{P}$]], [[Class_ModkP|$\\text{Mod}_\\text{k}\\text{P}$]], and [[Class_SPP|$\\text{SPP}$]] itself.  (I.e. adding [[Class_SPP|$\\text{SPP}$]] as an oracle does not increase the power of these classes.)



Independently defined in [[ZooRefs#OH93|[OH93] ]], who called the class [[Class_XP|$\\text{XP}$]].



Contained in [[Class_LWPP|$\\text{LWPP}$]], [[Class_C=P|$\\text{C}_\\text{=}\\text{P}$]], and [[Class_WPP|$\\text{WPP}$]] among other classes.



Contains [[Class_FewP|$\\text{FewP}$]]; indeed, [[Class_FewP|$\\text{FewP}$]] is low for [[Class_SPP|$\\text{SPP}$]], so that SPP^FewP^ = [[Class_SPP|$\\text{SPP}$]] [[ZooRefs#FFK94|[FFK94] ]].



Contains the problem of deciding whether a graph has any nontrivial automorphisms [[ZooRefs#KST92|[KST92] ]].



Indeed, contains graph isomorphism [[ZooRefs#AK02|[AK02] ]].



Contains a whole gaggle of problems for solvable black-box groups: solvability testing, membership testing, subgroup testing, normality testing, order verification, nilpotetence testing, group isomorphism, and group intersection [[ZooRefs#Vin04|[Vin04] ]]



[[ZooRefs#AK02|[AK02] ]] also showed that the Hidden Subgroup Problem for permutation groups, of interest in quantum computing, is in FP^SPP^.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SQG"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SQG - Short Quantum Games =

----
CategoryQuantum 

== Description ==

{{{#!description

Same as QRG(2), except that now the verifier can process the yes-prover's answer before preparing the no-prover's question.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GW05|[GW05] ]], where it was also shown that [[Class_SQG|$\\text{SQG}$]] contains [[Class_QIP|$\\text{QIP}$]].



[[Class_SQG|$\\text{SQG}$]] is contained in [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#Gut05|[Gut05] ]].



[[Class_SQG|$\\text{SQG}$]] is trivially contained in QRG(4) (and hence [[Class_EXP|$\\text{EXP}$]]).



[[Class_SQG|$\\text{SQG}$]] trivially contains QRG(2) (and hence [[Class_PSPACE|$\\text{PSPACE}$]]).



[[Class_SQG|$\\text{SQG}$]] is contained in [[Class_PSPACE|$\\text{PSPACE}$]] [[ZooRefs#GW10|[GW10] ]].  Hence [[Class_SQG|$\\text{SQG}$]] = QRG(2) = RG(2) = [[Class_PSPACE|$\\text{PSPACE}$]] and the addition of quantum information, combined with the ability of the verifier to process the one prover's answer before preparing the other prover's question, has no effect on the complexity of two-turn (one-round) zero-sum games.



Same as [[Class_QRG|$\\text{QRG}$]], except that now the verifier can exchange only a single round of quantum messages with the two provers.  The verifier may process the yes-prover's response before sending a message to the no-prover (compare with [[Class_RG[1]|$\\text{RG[1]}$]], wherein the verifier's messages must be sent to the provers in parallel).



[[Class_SQG|$\\text{SQG}$]] is contained in [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#Gut05|[Gut05] ]], as well as in [[Class_QRG|$\\text{QRG}$]].



[[Class_SQG|$\\text{SQG}$]] trivially contains [[Class_QS2P|$\\text{QS}_\\text{2}\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SQG)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SQG because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SUBEXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SUBEXP - Deterministic Subexponential-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The intersection of DTIME(2^n^ε^) over all ε>0.  (Note that the algorithm used may vary with ε.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SUBEXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SUBEXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SZK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SZK - Statistical Zero Knowledge =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which a "yes" answer can be verified by a statistical zero-knowledge proof protocol.  In such an interactive proof}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==

(see [[Class_IP|$\\text{IP}$]]), we have a probabilistic polynomial-time verifier, and a prover who has unbounded computational resources.  By exchanging messages with the prover, the verifier must become convinced (with high probability) that the answer is "yes," without learning anything else about the problem (statistically).



What does that mean?  For each choice of random coins, the verifier has a "view" of his entire interaction with prover, consisting of his random coins as well as all messages sent back and forth.  Then the distribution over views resulting from interaction with the prover has to be statistically close to a distribution that the verifier could generate himself (in polynomial-time), without interacting with anyone.  (Here "statistically close" means that, say, the trace distance is at most 1/10.)



The most famous example of such a protocol is for graph nonisomorphism. Given two graphs G and H, the verifier picks at random one of the graphs (each with probability 1/2), permutes its vertices randomly, sends the resulting graph to the prover, and asks, "Which graph did I start with, G or H?"  If G and H are non-isomorphic, the prover can always answer correctly (since he can use exponential time), but if they're isomorphic, he can answer correctly with probability at most 1/2. Thus, if the prover always gives the correct answer, then the verifier becomes convinced the graphs are not isomorphic.  On the other hand, the verifier already knew which graph (G or H) he started with, so he could simulate his entire view of the interaction himself, without the prover's help.



If that sounds like a complicated definition, well, it is.  But it turns out that [[Class_SZK|$\\text{SZK}$]] has extremely nice properties. [[ZooRefs#Oka96|[Oka96] ]] showed that:



[[Class_SZK|$\\text{SZK}$]] is closed under complement.  E.g., a verifier can verify in zero-knowledge that two graphs are isomorphic, not only that they aren't. 

We can assume without loss of generality that the whole interaction consists of a constant number of messages.

Amazingly, we can also assume without loss of generality that the protocol is public-coin. That is, the verifier (often called Arthur) doesn't need to hide any of his random bits, as he did in the graph nonisomorphism protocol above, but can just send them all to the prover (called Merlin)!

Finally, we can assume without loss of generality that the verifier (Arthur) is honest. A dishonest verifier would be one that tries to learn something about the problem (violating the zero-knowledge requirement) by deviating from the protocol.



Subsequently, [[ZooRefs#SV97|[SV97] ]] showed that [[Class_SZK|$\\text{SZK}$]] has a natural complete promise problem, called Statistical Difference (SD).  Given two polynomial-size circuits, C,,0,, and C,,1,,, let D,,0,, and D,,1,, be the distributions over their respective outputs when they're given as input a uniformly random n-bit string.  We're promised that D,,0,, and D,,1,, have trace distance either at most 1/3 or at least 2/3; the problem is to decide which is the case.



Note: The constants 1/3 and 2/3 can be amplified to 2^-poly(n)^ and 1-2^-poly(n)^ respectively.  But it is crucial that (2/3)^2^ > 1/3.



Another complete promise problem for [[Class_SZK|$\\text{SZK}$]] is Entropy Difference (ED) [[ZooRefs#GV99|[GV99] ]].  Here we're promised that either H(D,,0,,)>H(D,,1,,)+1 or H(D,,1,,)>H(D,,0,,)+1, where the distributions D,,0,, and D,,1,, are as above, and H denotes Shannon entropy.  The problem is to determine which is the case.



If any hard-on-average language is in [[Class_SZK|$\\text{SZK}$]], then one-way functions exist [[ZooRefs#Ost91|[Ost91] ]].



See general zero-knowledge ([[Class_ZK|$\\text{ZK}$]]).



Contains [[Class_PZK|$\\text{PZK}$]] and [[Class_NISZK|$\\text{NISZK}$]], and is contained in [[Class_AM|$\\text{AM}$]] ∩ [[Class_coAM|$\\text{coAM}$]], as well as [[Class_CZK|$\\text{CZK}$]] and [[Class_QSZK|$\\text{QSZK}$]].



There exists an oracle relative to which [[Class_SZK|$\\text{SZK}$]] is not in [[Class_BQP|$\\text{BQP}$]] [[ZooRefs#Aar02|[Aar02] ]].



Contained in [[Class_DQP|$\\text{DQP}$]] [Aar02b].



The class of decision problems for which a "yes" answer can be verified by a statistical zero-knowledge proof protocol.  In such a protocol, we have a [[Class_BPP|$\\text{BPP}$]] (i.e. probabilistic polynomial-time) verifier, Arthur, and a prover, Merlin, who has unbounded computational resources.  By sending messages back and forth with Merlin, Arthur must become convinced (with high probability) that the answer is "yes," without learning anything else about the problem (statistically).



What does that mean?  For each choice of random coins, Arthur has a "view" of his entire interaction with Merlin, consisting of his random coins as well as all messages sent back and forth.  Then the distribution over views resulting from interaction with Merlin has to be statistically close to a distribution that Arthur could generate himself (in polynomial-time), without interacting with Merlin.  (Here "statistically close" means that, say, the trace distance is at most 1/10.)



The most famous example of such a protocol is for graph nonisomorphism. Given two graphs G and H, Arthur can pick one of the graphs (each with probability 1/2), permute its vertices randomly, send the resulting graph to Merlin, and ask, "Which graph did I start with, G or H?"  If G and H are non-isomorphic, Merlin can always answer correctly (since he can use exponential time), but if they're isomorphic, he can answer correctly with probability at most 1/2. Thus, if Merlin always gives the correct answer, Arthur becomes convinced the graphs are not isomorphic.  On the other hand, Arthur already knew which graph (G or H) he started with, so he could simulate his entire view of the interaction himself, without Merlin's help.



[[Class_SZK|$\\text{SZK}$]] is closed under complement.  I.e. Arthur can verify in zero-knowledge that two graphs are isomorphic, not only that they aren't. We can assume without loss of generality that the whole interaction consists of a constant number of messages.

Amazingly, we can also assume without loss of generality that the protocol is public-coin. I.e. Arthur doesn't need to hide any of his random bits, as he did in the graph nonisomorphism protocol above, but can just send them all to Merlin!

Finally, we can assume without loss of generality that the verifier (Arthur) is honest. A dishonest verifier would be one that tries to learn something about the problem (violating the zero-knowledge requirement) by deviating from the protocol.



Zero-knowledge proofs were first studied in [[ZooRefs#GMW91|[GMW91] ]], [[ZooRefs#GMR89|[GMR89] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SZK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SZK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SZKh"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SZK,,h,, - SZK With Limited Help =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which a "yes" answer can be verified by a statistical zero-knowledge proof protocol, and the prover and verifier both have access to a string computed by a trusted probabilistic polynomial-time third party with access to the input.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#BG03|[BG03] ]], where it was also shown that [[Class_SZKh|$\\text{SZK}_\\text{h}\\text{}$]] = [[Class_SZK|$\\text{SZK}$]].



Contains [[Class_NISZKh|$\\text{NISZK}_\\text{h}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SZKh)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SZKh because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SelfNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SelfNP - Self-Witnessing NP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of languages [[Class_L|$\\text{L}$]] in [[Class_NP|$\\text{NP}$]] such that the union, over all x in [[Class_L|$\\text{L}$]], of the set of valid witnesses for x equals [[Class_L|$\\text{L}$]] itself.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#HT03|[HT03] ]], where it was shown that the closure of [[Class_SelfNP|$\\text{SelfNP}$]] under polynomial-time many-one reductions is [[Class_NP|$\\text{NP}$]].



They also show that if [[Class_SelfNP|$\\text{SelfNP}$]] = [[Class_NP|$\\text{NP}$]], then [[Class_E|$\\text{E}$]] = [[Class_NE|$\\text{NE}$]]; and that SAT is contained in [[Class_SelfNP|$\\text{SelfNP}$]].



See also: [[Class_PermUP|$\\text{PermUP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_SelfNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SelfNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_TALLY"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= TALLY - Tally Languages =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which every 'yes' instance has the form 0^n^ (i.e. inputs are encoded in unary).  If [[Class_TALLY|$\\text{TALLY}$]] intersects [[Class_NPC|$\\text{NPC}$]] then [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]] [[ZooRefs#Mah82|[Mah82] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_SPARSE|$\\text{SPARSE}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_TALLY)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save TALLY because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_TC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= TC^0^ - Constant-Depth Threshold Circuits =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by polynomial-size, constant-depth circuits with unbounded fanin, which can use AND, OR, and NOT gates (as in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]]) as well as threshold gates.  A threshold gate returns 1 if at least half of its inputs are 1, and 0 otherwise.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A uniformity requirement is sometimes also placed.



[[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] contains [[Class_ACC0|$\\text{ACC}^\\text{0}\\text{}$]], and is contained in [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]].



[[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] circuits of depth 3 are strictly more powerful than [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] circuits of depth 2 [[ZooRefs#HMP+93|[HMP+93] ]].



[[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] circuits of depth 3 and quasipolynomial size can simulate all of [[Class_ACC0|$\\text{ACC}^\\text{0}\\text{}$]] [[ZooRefs#Yao90|[Yao90] ]].



There is a function in [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] (explicitly given in [[ZooRefs#She08|[She08] ]]), whose computation with [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]]  circuits of depth 2 requires an exponential number of gates.



[[ZooRefs#NR97|[NR97] ]] give a candidate pseudorandom function family computable in [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]], that is secure assuming a subexponential lower bound on the hardness of factoring.  (See also [[ZooRefs#NRR01|[NRR01] ]] for an improvement of this construction, as well as [[ZooRefs#Kha93|[Kha93] ]].)



One implication is that, assuming such a bound, there is no natural proof in the sense of [[ZooRefs#RR97|[RR97] ]] separating [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] from [[Class_P/poly|$\\text{P/poly}$]].  (It is important for this that a function family, and not just a candidate pseudorandom generator, is computable in [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]].)  Another implication is that functions in [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] are likely to be difficult to learn.



The permanent of a 0-1 matrix cannot be computed in uniform [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] [[ZooRefs#All99|[All99] ]].



In a breakthrough result [[ZooRefs#Hes01|[Hes01] ]] (building on [[ZooRefs#BCH86|[BCH86] ]] and [[ZooRefs#CDL01|[CDL01] ]]), integer division was shown to be in U,,D,,-uniform [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]].  Indeed division is complete for this class under [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] reductions.



In a breakthrough result [[ZooRefs#Hes01|[Hes01] ]] (building on [[ZooRefs#BCH86|[BCH86] ]] and [[ZooRefs#CDL01|[CDL01] ]]), integer division was shown to be in L-uniform [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]].  Indeed division is complete for this class under [[Class_AC0|$\\text{AC}^\\text{0}\\text{}$]] reductions.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_TC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save TC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_TFNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= TFNP - Total Function NP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of function problems of the following form:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Given an input x and a polynomial-time predicate F(x,y), output any y satisfying F(x,y).  (Such a y is promised to exist.)



Can be considered as the functional analogue of [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]]. Defined in [[ZooRefs#MP91|[MP91] ]].



Contained in [[Class_FNP|$\\text{FNP}$]].



Subclasses include [[Class_PPA|$\\text{PPA}$]], [[Class_PPP|$\\text{PPP}$]], and [[Class_PLS|$\\text{PLS}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_TFNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save TFNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_TREE-REGULAR"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= TREE-REGULAR - Regular Tree-Valued Languages =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_REG|$\\text{REG}$]], except that now the inputs are trees (say, binary trees) instead of strings.  Each vertex is labeled with a symbol from a fixed alphabet.  Evaluation begins at the leaves and proceeds to the root.  The state of the finite automaton at each vertex v is a function of (1) the states at v's children (if any), and (2) the symbol at v.  The tree is in the language if and only if the automaton is in an 'accept' state at the root.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



See [[ZooRefs#Koz92|[Koz92] ]] for example.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_TREE-REGULAR)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save TREE-REGULAR because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_TreeBQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= TreeBQP - BQP Restricted To Tree States =

----
CategoryClassical 

== Description ==

{{{#!description

The class of languages accepted by a [[Class_BQP|$\\text{BQP}$]] machine subject to the constraint that at every time step t, the machine's state is exponentially close to a tree state -- that is, a state expressible by a polynomial-size tree of additions and tensor products (together with complex constants and |0> and |1> leaf nodes).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



More formally, a uniform classical polynomial-time algorithm generates a sequence of gates g^(1)^, ... ,g^(p(n))^.  Each g^(t)^ can be either be selected from some finite universal basis of unitary gates (the choice turns out not to matter), or can be a 1-qubit measurement.  When we perform a measurement, the state evolves to one of two possible pure states, with the usual probabilities, rather than to a mixed state.  We require that the final gate g^(p(n))^ is a measurement of the first qubit.  If at least one intermediate state was more than distance 2^-Ω(n)^ away from the nearest state of tree size at most p(n), then the outcome of the final measurement is chosen adversarially; otherwise it is given by the usual Born probabilities.  The measurement must return 1 with probability at least 2/3 if the input is in the language, and with probability at most 1/3 otherwise.



Contains [[Class_BPP|$\\text{BPP}$]], and is contained in [[Class_BQP|$\\text{BQP}$]].



Defined in [Aar03b], where it was also shown that [[Class_TreeBQP|$\\text{TreeBQP}$]] is

contained in the third level of [[Class_PH|$\\text{PH}$]], which might provide weak evidence that

[[Class_TreeBQP|$\\text{TreeBQP}$]] does not equal [[Class_BQP|$\\text{BQP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_TreeBQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save TreeBQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_UAP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= UAP - Unambiguous Alternating Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_AP|$\\text{AP}$]], except we are promised that each existential quantifier has at most one 'yes' path, and each universal quantifier has at most one 'no' path.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_UP|$\\text{UP}$]].



Defined in [[ZooRefs#NR98|[NR98] ]], where it was also shown that, even though [[Class_AP|$\\text{AP}$]] = [[Class_PSPACE|$\\text{PSPACE}$]], it is unlikely that the same is true for [[Class_UAP|$\\text{UAP}$]], since [[Class_UAP|$\\text{UAP}$]] is contained in [[Class_SPP|$\\text{SPP}$]].



[[ZooRefs#CGR+04|[CGR+04] ]] have also shown that UAP^UAP^ = [[Class_UAP|$\\text{UAP}$]], and that [[Class_UAP|$\\text{UAP}$]] contains Graph Isomorphism problem.



[[ZooRefs#CGR+04|[CGR+04] ]] have also shown that UAP^UAP^ = [[Class_UAP|$\\text{UAP}$]], and that [[Class_UAP|$\\text{UAP}$]] contains the Graph Isomorphism problem.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_UAP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save UAP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_UCC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= UCC - Unique Connected Component =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems reducible in [[Class_L|$\\text{L}$]] to the problem of whether an undirected graph has a unique connected component.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



See [[ZooRefs#AG00|[AG00] ]] for more information.



Contained in [[Class_SL|$\\text{SL}$]].



See also [[Class_coUCC|$\\text{coUCC}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_UCC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save UCC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_UCFL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= UCFL - Unambiguous CFL =

----
CategoryClassical 

== Description ==

{{{#!description

The class of context-free languages which can be represented by grammars where each word in the language has exactly one leftmost derivation.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Strictly contains Deterministic [[Class_CFL|$\\text{CFL}$]].  Strictly contained in [[Class_CFL|$\\text{CFL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_UCFL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save UCFL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_UE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= UE - Unambiguous Exponential-Time With Linear Exponent =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_E|$\\text{E}$]] as [[Class_UP|$\\text{UP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_UE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save UE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_UL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= UL - Unambiguous L =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_UP|$\\text{UP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If [[Class_UL|$\\text{UL}$]] = [[Class_NL|$\\text{NL}$]], then [[Class_FNL|$\\text{FNL}$]] is contained in [[Class_SharpL|$\\text{#L}$]] [[ZooRefs#AJ93|[AJ93] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_UL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save UL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_UL/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= UL/poly - Nonuniform UL =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_UL|$\\text{UL}$]] as [[Class_P/poly|$\\text{P/poly}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Equals [[Class_NL/poly|$\\text{NL/poly}$]] [[ZooRefs#RA00|[RA00] ]]. (A corollary is that [[Class_UL/poly|$\\text{UL/poly}$]] is closed under complement).



Note that in [[Class_UL/poly|$\\text{UL/poly}$]], the witness must be unique even for bad advice. UL/mpoly (as in [[Class_BQP/mpoly|$\\text{BQP/mpoly}$]]) is a more natural definition, but this is a moot distinction here because [[ZooRefs#RA00|[RA00] ]] show that they both equal [[Class_NL/poly|$\\text{NL/poly}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_UL/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save UL/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_UP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= UP - Unambiguous Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'yes,' exactly one computation path accepts.

If the answer is 'no,' all computation paths reject.



Defined by [[ZooRefs#Val76|[Val76] ]].



"Worst-case" one-way functions exist if and only if [[Class_P|$\\text{P}$]] does not equal [[Class_UP|$\\text{UP}$]] ([[ZooRefs#GS88|[GS88] ]] and independently [[ZooRefs#Ko85|[Ko85] ]]).  "Worst-case" one-way permutations exist if and only if [[Class_P|$\\text{P}$]] does not equal [[Class_UP|$\\text{UP}$]] ∩ [[Class_coUP|$\\text{coUP}$]] [[ZooRefs#HT03|[HT03] ]].  Note that these are weaker than the one-way functions and permutations that are needed for cryptographic applications.



There exists an oracle relative to which [[Class_P|$\\text{P}$]] is strictly contained in [[Class_UP|$\\text{UP}$]] is strictly contained in [[Class_NP|$\\text{NP}$]] [[ZooRefs#Rac82|[Rac82] ]]; indeed, these classes are distinct with probability 1 relative to a random oracle [[ZooRefs#Bei89|[Bei89] ]].



[[Class_NP|$\\text{NP}$]] is contained in RP^PromiseUP^ [[ZooRefs#VV86|[VV86] ]].  On the other hand, [[ZooRefs#BBF98|[BBF98] ]] give an oracle relative to which [[Class_P|$\\text{P}$]] = [[Class_UP|$\\text{UP}$]] but still [[Class_P|$\\text{P}$]] does not equal [[Class_NP|$\\text{NP}$]].



[[Class_UP|$\\text{UP}$]] is not known or believed to contain complete problems.  [[ZooRefs#Sip82|[Sip82] ]], [[ZooRefs#HH86|[HH86] ]] give oracles relative to which [[Class_UP|$\\text{UP}$]] has no complete problems.



[[Class_NP|$\\text{NP}$]] is contained in RP^Promise-UP^ [[ZooRefs#VV86|[VV86] ]].  On the other hand, [[ZooRefs#BBF98|[BBF98] ]] give an oracle relative to which [[Class_P|$\\text{P}$]] = [[Class_UP|$\\text{UP}$]] but still [[Class_P|$\\text{P}$]] does not equal [[Class_NP|$\\text{NP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_UP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save UP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_UPPcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= UPP^cc^ - Unrestricted Communication Analogue of PP =

----
CategoryClassical 

== Description ==

{{{#!description

Defined by [[ZooRefs#BFS86|[BFS86] ]], [[Class_UPPcc|$\\text{UPP}^\\text{cc}\\text{}$]] is one of two communication complexity analogues of [[Class_PP|$\\text{PP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==

[[Class_UPPcc|$\\text{UPP}^\\text{cc}\\text{}$]] is the class of all languages defined by functions $f : \\{0,1\\}^n \\times \\{0,1\\}^n \\to \\{0,1\\}$ which are computable by polylogarithmic protocols that accept with probability strictly greater than 1/2 when $f(x,y) = 1$ and accept with probably strictly less than 1/2 otherwise. No accounting is made for how many random bits are consulted during the protocol.



See also: [[Class_PPcc|$\\text{PP}^\\text{cc}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_UPPcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save UPPcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_US"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= US - Unique Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The all-American counting class.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that the answer is 'yes' if and only if exactly one computation path accepts.



In contrast to [[Class_UP|$\\text{UP}$]], a machine can legally have more than one accepting path - that just means that the corresponding input is not in the language.



Defined in [[ZooRefs#BG82|[BG82] ]].



Contains [[Class_coNP|$\\text{coNP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_US)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save US because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_VCk"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= VC,,k,, - Verification Class With A Circuit of Depth K =

----
CategoryClassical 

== Description ==

{{{#!description

For k = 0, VC,,0,, is the class of compressible languages.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==

 For k = 1, VC,,1,, is the class of languages that have local verification: they can be verified by testing only a small part of the instance. (Small means polynomial in the witness length and the log of the instance length.)

 For k ≥ 2, [[Class_VCk|$\\text{VC}_\\text{k}\\text{}$]] is the class of languages that can be verified by a circuit of depth k, with size polynomial in the witness length and instance length.



VC,,0,, ⊆ VC,,OR,, ⊆ VC,,1,, ⊆ VC,,2,, ⊆ VC,,3,, ...



Introduced in [[ZooRefs#HN06|[HN06] ]]; see there for formal definitions.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_VCk)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save VCk because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_VCor"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= VC,,or,, - Verification Class With OR =

----
CategoryClassical 

== Description ==

{{{#!description

The class of languages that have verification presentable as the OR of m instances of SAT, each of size n. (m is the witness length of an instance and n is the instance length.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Introduced in [[ZooRefs#HN06|[HN06] ]].



See also [[Class_VCk|$\\text{VC}_\\text{k}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_VCor)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save VCor because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_VNCk"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= VNC,,k,, - Valiant NC Over Field k =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]] as [[Class_NC|$\\text{NC}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



More formally, the class of [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]] problems computable by a straight-line program of depth polylogarithmic in n.



Surprisingly, [[Class_VNCk|$\\text{VNC}_\\text{k}\\text{}$]] = [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]] for any k [[ZooRefs#VSB+83|[VSB+83] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_VNCk)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save VNCk because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_VNPk"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= VNP,,k,, - Valiant NP Over Field k =

----
CategoryClassical 

== Description ==

{{{#!description

A superclass of [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]] in Valiant's algebraic complexity theory, but not quite the analogue of [[Class_NP|$\\text{NP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A problem is in [[Class_VNPk|$\\text{VNP}_\\text{k}\\text{}$]] if there exists a polynomial p with the following properties:



p is computable in [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]]; that is, by a polynomial-size straight-line program.

The inputs to p are constants c,,1,,,...,c,,m,,,e,,1,,,...,e,,h,, and indeterminates X,,1,,,...,X,,n,, over the base field k.

When p is summed over all 2^h^ possible assignments of {0,1} to each of e,,1,,,...,e,,h,,, the result is some specified polynomial q.



Originated in [Val79b].



If the field k has characteristic greater than 2, then the permanent of an n-by-n matrix of indeterminates is VNP,,k,,-complete under a type of reduction called p-projections ([Val79b]; see also [[ZooRefs#Bur00|[Bur00] ]]).



A central conjecture is that for all k, [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]] is not equal to [[Class_VNPk|$\\text{VNP}_\\text{k}\\text{}$]].  Bürgisser [[ZooRefs#Bur00|[Bur00] ]] shows that if this were false then:



If k is finite, NC^2^/poly = [[Class_P/poly|$\\text{P/poly}$]] = [[Class_NP/poly|$\\text{NP/poly}$]] = PH/poly.

If k has characteristic 0, then assuming the Generalized Riemann Hypothesis (GRH), NC^3^/poly = [[Class_P/poly|$\\text{P/poly}$]] = [[Class_NP/poly|$\\text{NP/poly}$]] = PH/poly, and #P/poly = FP/poly.



In both cases, [[Class_PH|$\\text{PH}$]] collapses to [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_VNPk)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save VNPk because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_VPL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= VPL - Visibly pushdown languages =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems that can be decided by a visibly pushdown automaton. In a visibly pushdown automaton, all push and pop transitions have to be triggered by special alphabet symbols, and thus are visible in the input word. Nondeterminism does not add to the expressive power of this automaton model, and the complexity class is closed under all Boolean operations.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Originated in [[ZooRefs#AM04|[AM04] ]]. See also [[ZooRefs#AM09|[AM09] ]].



Properly contains [[Class_REG|$\\text{REG}$]]. Properly contained in [[Class_DCFL|$\\text{DCFL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_VPL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save VPL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_VPk"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= VP,,k,, - Valiant P Over Field k =

----
CategoryClassical 

== Description ==

{{{#!description

The class of efficiently-solvable problems in Valiant's algebraic complexity theory.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



More formally, the input consists of constants c,,1,,,...,c,,m,, and indeterminates X,,1,,,...,X,,n,, over a base field k (for instance, the complex numbers or Z,,2,,).  The desired output is a collection of polynomials over the X,,i,,'s.  The complexity is the minimum number of pairwise additions, subtractions, and multiplications needed by a straight-line program to produce these polynomials.  [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]] is the class of problems whose complexity is polynomial in n.  (Hence, [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]] is a nonuniform class, in contrast to [[Class_PC|$\\text{P}_\\text{C}\\text{}$]] and [[Class_PR|$\\text{P}_\\text{R}\\text{}$]].)



Originated in [Val79b]; see [[ZooRefs#Bur00|[Bur00] ]] for more information.



Contained in [[Class_VNPk|$\\text{VNP}_\\text{k}\\text{}$]] and [[Class_VQPk|$\\text{VQP}_\\text{k}\\text{}$]], and contains [[Class_VNCk|$\\text{VNC}_\\text{k}\\text{}$]].



More formally, the input consists of constants c,,1,,,...,c,,m,, and indeterminates X^1^,...,X,,n,, over a base field k (for instance, the complex numbers or Z,,2,,).  The desired output is a collection of polynomials over the X,,i,,'s.  The complexity is the minimum number of pairwise additions, subtractions, and multiplications needed by a straight-line program to produce these polynomials.  [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]] is the class of problems whose complexity is polynomial in n.  (Hence, [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]] is a nonuniform class, in contrast to [[Class_PC|$\\text{P}_\\text{C}\\text{}$]] and [[Class_PR|$\\text{P}_\\text{R}\\text{}$]].)
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_VPk)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save VPk because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_VQPk"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= VQP,,k,, - Valiant QP Over Field k =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_VPk|$\\text{VP}_\\text{k}\\text{}$]] as [[Class_QP|$\\text{QP}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Originated in [Val79b].



The determinant of an n-by-n matrix of indeterminates is VQP,,k,,-complete under a type of reduction called qp-projections (see [[ZooRefs#Bur00|[Bur00] ]] for example).  It is an open problem whether the determinant is VP,,k,,-complete.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_VQPk)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save VQPk because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_W*[t]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= W^*^[t] - W[t] With Parameter-Dependent Depth =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_W[t]|$\\text{W[t]}$]], except that now the circuit depth can depend on the parameter k rather than being constant.  (The number of unbounded-fanin gates along any path to the root is still at most t.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



W^*^[1] = [[Class_W[1]|$\\text{W[1]}$]] [[ZooRefs#DFT96|[DFT96] ]], and W^*^[2] = W[2] [[ZooRefs#DF97|[DF97] ]], but the problem is open for larger t.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_W*[t])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save W*[t] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_WAPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= WAPP - Weak Almost-Wide PP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which there exists a [[Class_SharpP|$\\text{#P}$]] function f, a polynomial p, and an ε > 0, such that for all inputs x,}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes" then 2^p(|x|)^ ≥ f(x) > (1+ε) 2^p(|x|)-1^.

If the answer is "no" then 0 ≤ f(x) < (1-ε) 2^p(|x|)-1^.



Defined in [[ZooRefs#BGM02|[BGM02] ]], where it is also shown that [[Class_WAPP|$\\text{WAPP}$]] is contained in [[Class_AWPP|$\\text{AWPP}$]] and [[Class_SBP|$\\text{SBP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_WAPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save WAPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_WHILE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= WHILE - While programs and some restrictions =

----
CategoryClassical 

== Description ==

{{{#!description

While is a theorical programing language defined in [[ZooRefs#jon98|[jon98] ]],  is a way to define syntacticaly [[Class_P|$\\text{P}$]] and a syntactic resctriction of [[Class_WHILE|$\\text{WHILE}$]] is exactly [[Class_L|$\\text{L}$]]. The important point is that those two languages are powerful enough to simulate all of [[Class_P|$\\text{P}$]] (and [[Class_L|$\\text{L}$]]) and when we write a program in this language we never need to prove his time (space) complexity, since the language garantee it !}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



In While, input are composed only of lists (in a lisp-way where a list is either an empty list or a pair of his first element and his tail) and the elements of the list and variables are only pointers to list.



A program contains global variables and procedures.



Every procedure are composed of a name, a list of argument and local variables and a list of command. The procedure doesn't return any value, they only affect global variables.

The command are: variable affectation, while loop, if/then/else and procedure call.

The empty list is considered as false and everything else as true, this is the only way to do while/if test.



There are three primitives function, tail, head, and cons(h,t), who give the first value of a list, the tail of the list and who return a list whose first element is h and the rest of the list is t and we can call defined procedure.



We can then define WHILE^/cons-rec^ which is [[Class_WHILE|$\\text{WHILE}$]] without "cons" primitive and procedure call[#]. It is equivalent to [[Class_L|$\\text{L}$]]. The trick to do the computation in logspace is that without recursion we only need to save a fixed number of variables who are only pointers to part of the input, so they only take logspace. Since any logspace TM can avoid having a work tape by having a fixed number of reading head on his input, we can simulate logspace TM by using a variable for every reading head. (The binary string is coded as a list of () for 0 and (()) for 1, so equality can be checked trivially)



[#] in fact we only need to forbid recursive call, hence the name, but when we lose recursion we can assume there is no procedure call w.l.o.g, in fact in [[ZooRefs#jon98|[jon98] ]] [[Class_WHILE|$\\text{WHILE}$]] is first defined without procedure call and procedure are defined later, but this presentation may be more easy to understand and at least more general.



We can then also define WHILE^rec/cons^ which is [[Class_WHILE|$\\text{WHILE}$]] without "cons" primitive but with procedure calls, and hence recursion. It is equivalent to [[Class_P|$\\text{P}$]]. 

The trick to do a computation of a WHILE^rec/cons^ in [[Class_P|$\\text{P}$]] is to memoize the couple (global variables, input) when a procedure is called and the value of the globals variable when the procedure end, since we don't have cons, only a polynomial number of call will really be executed and we can detect loop.

Simulating [[Class_P|$\\text{P}$]] in WHILE^rec/cons^ is quite more subtle, [[Class_P|$\\text{P}$]] TM are equivalent to some counter machine wich can easily be simulated by [[Class_WHILE|$\\text{WHILE}$]] programs with cons, and then we can simulate the cons thanks to the call stack.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_WHILE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save WHILE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_WPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= WPP - Wide PP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "no," then the number of accepting computation paths exactly equals the number of rejecting paths.

If the answer is "yes," then their difference exactly equals a function f(x) computable in polynomial time (i.e. [[Class_FP|$\\text{FP}$]]).



Defined in [[ZooRefs#FFK94|[FFK94] ]].



Contained in [[Class_C=P|$\\text{C}_\\text{=}\\text{P}$]] ∩ [[Class_coC=P|$\\text{coC}_\\text{=}\\text{P}$]], as well as [[Class_AWPP|$\\text{AWPP}$]].



Contains [[Class_SPP|$\\text{SPP}$]] and [[Class_LWPP|$\\text{LWPP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_WPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save WPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_W[*]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= W[*] - Union of W[t]'s =

----
CategoryClassical 

== Description ==

{{{#!description

The union of [[Class_W[t]|$\\text{W[t]}$]] over all t.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_W[*])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save W[*] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_W[1]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= W[1] - Weighted Analog of NP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems of the form (x,k) (k a parameter), that are fixed-parameter reducible to the following:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Weighted 3SAT: Given a 3SAT formula, does it have a satisfying assignment of Hamming weight k?



A fixed-parameter reduction is a Turing reduction that takes time at most f(k)p(|x|), where f is an arbitrary function and p is a polynomial.  Also, if the input is (x,k), then all Weighted 3SAT instances the algorithm queries about must have the form <x',k'> where k' is at most k.



Contains [[Class_FPT|$\\text{FPT}$]].



Defined in [[ZooRefs#DF99|[DF99] ]], where the following is also shown:



If [[Class_FPT|$\\text{FPT}$]] = [[Class_W[1]|$\\text{W[1]}$]] then [[Class_NP|$\\text{NP}$]] is contained in DTIME(2^o(n)^).



[[Class_W[1]|$\\text{W[1]}$]] can be generalized to [[Class_W[t]|$\\text{W[t]}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_W[1])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save W[1] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_W[P]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= W[P] - Weighted Circuit Satisfiability =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems of the form (x,k) (k a parameter), that are fixed-parameter reducible to the following problem, for some constant h:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Weighted Circuit-SAT: Given a Boolean circuit C (with no restriction on depth), does C have a satisfying assignment of Hamming weight k?



See [[Class_W[1]|$\\text{W[1]}$]] for the definition of fixed-parameter reducibility.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contains [[Class_W[SAT]|$\\text{W[SAT]}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_W[P])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save W[P] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_W[SAT]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= W[SAT] - Weighted Satisfiability =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems of the form (x,k) (k a parameter), that are fixed-parameter reducible to the following problem, for some constant h:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Weighted SAT: Given a Boolean formula F (with no restriction on depth), does F have a satisfying assignment of Hamming weight k?



See [[Class_W[1]|$\\text{W[1]}$]] for the definition of fixed-parameter reducibility.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contains [[Class_W[t]|$\\text{W[t]}$]] for every t, and is contained in [[Class_W[P]|$\\text{W[P]}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_W[SAT])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save W[SAT] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_W[t]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= W[t] - Nondeterministic Fixed-Parameter Hierarchy =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

A generalization of [[Class_W[1]|$\\text{W[1]}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The class of decision problems of the form (x,k) (k a parameter), that are fixed-parameter reducible to the following problem, for some constant h:



Weighted Weft-t Depth-h Circuit-SAT: Given a Boolean circuit C, with a mixture of fanin-2 and unbounded-fanin gates.  The number unbounded-fanin gates along any path to the root is at most t, and the total depth (fanin-2 and unbounded-fanin) is at most h.  Does C have a satisfying assignment of Hamming weight k?



See [[Class_W[1]|$\\text{W[1]}$]] for the definition of fixed-parameter reducibility.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contained in [[Class_W[SAT]|$\\text{W[SAT]}$]] and in [[Class_W*[t]|$\\text{W}^\\text{*}\\text{[t]}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_W[t])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save W[t] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_XOR-MIP*[2,1]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= XOR-MIP*[2,1] - MIP*[2,1] With 1-Bit Proofs =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_MIP*[2,1]|$\\text{MIP*[2,1]}$]], but with the further restriction that both provers send only a single bit to the verifier, and the verifier's output is a function of the exclusive-OR of those bits.  There should exist 0<a<b<1 such that if the answer is "yes", then for some responses of the provers the verifier accepts with probability at least b, while if the answer is "no", then for all responses of the provers the verifier accepts with probability at most a.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined by [[ZooRefs#CHT+04|[CHT+04] ]], whose motivation was a connection to the Bell and CHSH inequalities of quantum physics.



[[Class_XOR-MIP*[2,1]|$\\text{XOR-MIP*[2,1]}$]] is contained in [[Class_NEXP|$\\text{NEXP}$]] [[ZooRefs#CHT+04|[CHT+04] ]].



[[Class_XOR-MIP*[2,1]|$\\text{XOR-MIP*[2,1]}$]] is contained in [[Class_QIP[2]|$\\text{QIP[2]}$]] [[ZooRefs#Weh06|[Weh06] ]]
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_XOR-MIP*[2,1])>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save XOR-MIP*[2,1] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_XP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= XP - Fixed-Parameter Tractable for Each Parameter =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems of the form (x,k) (k a parameter) that are solvable in time O(|x|^f(k)^) for some function f.  The algorithm used may depend on k.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#DF99|[DF99] ]].



Contains [[Class_XPuniform|$\\text{XP}_\\text{uniform}\\text{}$]].



Strictly contains [[Class_FPT|$\\text{FPT}$]] (by diagonalization).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_XP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save XP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_XPuniform"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= XP,,uniform,, - Uniform XP =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_XP|$\\text{XP}$]] except that the algorithm used must be the same for each k (though it can take k as input).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#DF99|[DF99] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_XPuniform)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save XPuniform because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_YACC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= YACC - Yet Another Complexity Class =

----
CategoryClassical 

== Description ==

{{{#!description

A term of derision, used against a complexity class.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_YACC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save YACC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_YP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= YP - Your Polynomial-Time or Yaroslav-Percival =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which there exists a polynomial-time machine M such that:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



For all input sizes n, there exists a polynomial-size advice string s,,n,, such that M(x,s,,n,,) outputs the correct answer for all inputs x of size n.

For all inputs x and advice strings s, M(x,s) outputs either the correct answer or "I don't know."



Defined in a recent post of the blog Shtetl-Optimized.  See there for an explanation of the class's name.



Contains [[Class_ZPP|$\\text{ZPP}$]] by the same argument that places [[Class_BPP|$\\text{BPP}$]] in [[Class_P/poly|$\\text{P/poly}$]].



Also contains [[Class_P|$\\text{P}$]] with [[Class_TALLY|$\\text{TALLY}$]] ∩ [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]] oracle.



Is contained in [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]] and [[Class_YPP|$\\text{YPP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_YP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save YP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_YPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= YPP - Yaroslav BPP =

----
CategoryClassical 

== Description ==

{{{#!description

The probabilistic analogue of [[Class_YP|$\\text{YP}$]]; it is to [[Class_YP|$\\text{YP}$]] what [[Class_MA|$\\text{MA}$]] is to [[Class_NP|$\\text{NP}$]].  Formally, the class of decision problems for which there exists a syntactic [[Class_BPP|$\\text{BPP}$]] machine M such that:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



For all input sizes n, there exists a polynomial-size advice string a,,n,, such that for all inputs x of size n, M(x,a,,n,,) outputs the correct answer with probability at least 2/3.

For all inputs x and advice strings a, the probability that M(x,a) outputs the incorrect answer is at most 1/3.  In other words, the sum of the probabilities of the correct answer and "I don't know" is at least 2/3.



To amplify a [[Class_YPP|$\\text{YPP}$]] machine, one can run it multiple times, then accept if a majority of runs accept, reject if a majority reject, and otherwise output "I don't know."



Contains [[Class_BPP|$\\text{BPP}$]] and [[Class_YP|$\\text{YP}$]], and is contained in [[Class_MA|$\\text{MA}$]] and [[Class_P/poly|$\\text{P/poly}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_YPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save YPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_YQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= YQP - Yaroslav BQP =

----
CategoryClassical 

== Description ==

{{{#!description

Is to [[Class_YPP|$\\text{YPP}$]] as [[Class_BQP|$\\text{BQP}$]] is to [[Class_BPP|$\\text{BPP}$]], and [[Class_QMA|$\\text{QMA}$]] is to [[Class_MA|$\\text{MA}$]].  The machine is now a quantum computer and the advice is a quantum state |ψ_n>.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_BQP|$\\text{BQP}$]] and [[Class_YPP|$\\text{YPP}$]], and is contained in [[Class_QMA|$\\text{QMA}$]] and [[Class_BQP/qpoly|$\\text{BQP/qpoly}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_YQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save YQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ZBQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ZBQP - Strict Quantum ZPP =

----
CategoryQuantum 

== Description ==

{{{#!description

Defined as [[Class_RBQP|$\\text{RBQP}$]] ∩ coRBQP.  Equivalently, the class of problems in [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]] such that both positive and negative witnesses are in [[Class_FBQP|$\\text{FBQP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



For example, the language of square-free numbers is in [[Class_ZBQP|$\\text{ZBQP}$]], because factoring is in [[Class_FBQP|$\\text{FBQP}$]] and a factorization can be certified in [[Class_ZPP|$\\text{ZPP}$]] (indeed in [[Class_P|$\\text{P}$]], by [[ZooRefs#AKS02|[AKS02] ]]).



Unlike [[Class_EQP|$\\text{EQP}$]] or [[Class_ZQP|$\\text{ZQP}$]], [[Class_ZBQP|$\\text{ZBQP}$]] would generalize [[Class_ZPP|$\\text{ZPP}$]] in practice if quantum computers existed, in the sense that it provides proven answers.



Contains [[Class_ZPP|$\\text{ZPP}$]] and is contained in [[Class_RBQP|$\\text{RBQP}$]] and [[Class_ZQP|$\\text{ZQP}$]].  Also, ZBQP^ZBQP^ = [[Class_ZBQP|$\\text{ZBQP}$]].  Defined here to clarify [[Class_EQP|$\\text{EQP}$]] and [[Class_ZQP|$\\text{ZQP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ZBQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ZBQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ZK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ZK - Zero-Knowledge (see CZK) =

----
CategoryClassical 

== Description ==

{{{#!description

Often used as a shorthand for (computational zero-knowledge) [[Class_CZK|$\\text{CZK}$]], but may also be used as a general paradigm encomposing various classes ranging from perfect and statistical zero-knowledge ([[Class_SZK|$\\text{SZK}$]]) to computational ones ([[Class_CZK|$\\text{CZK}$]]), and also various forms of non-interactive zero-knowledge proof systems.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Zero-knowledge proofs were introduced in [[ZooRefs#GMR89|[GMR89] ]], and further studied in [[ZooRefs#GMW91|[GMW91] ]], which demonstrated the wide applicability of the concept.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ZK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ZK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ZPE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ZPE - Zero-Error Probabilistic E =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_ZPP|$\\text{ZPP}$]], but with 2^O(n)^-time instead of polynomial-time.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_ZPE|$\\text{ZPE}$]] = [[Class_EE|$\\text{EE}$]] if and only if [[Class_ZPP|$\\text{ZPP}$]] = [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#IKW01|[IKW01] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ZPE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ZPE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ZPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ZPP - Zero-Error Probabilistic Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Defined as [[Class_RP|$\\text{RP}$]] ∩ [[Class_coRP|$\\text{coRP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined as the class of problems solvable by randomized algorithms that always return the correct answer, and whose expected running time (on any input) is polynomial, in [[ZooRefs#Gil77|[Gil77] ]].  (Proposition 5.5(iii) in this paper shows that the two definitions above are equivalent.)



Contains the problem of testing whether an integer is prime [[ZooRefs#SS77|[SS77] ]] [[ZooRefs#AH87|[AH87] ]].



In contrast to [[Class_BPP|$\\text{BPP}$]] and [[Class_RP|$\\text{RP}$]], it is not known whether showing [[Class_ZPP|$\\text{ZPP}$]] = [[Class_P|$\\text{P}$]] requires proving superpolynomial circuit lower bounds [[ZooRefs#KI02|[KI02] ]].



There exists an oracle relative to which [[Class_ZPP|$\\text{ZPP}$]] = [[Class_EXP|$\\text{EXP}$]] [Hel84a], [Hel84b], [[ZooRefs#Kur85|[Kur85] ]], [[ZooRefs#Hel86|[Hel86] ]].



Has the same p-measure as [[Class_RP|$\\text{RP}$]]. Moreover, this measure is either zero or one. If the measure is non-zero, then [[Class_ZPP|$\\text{ZPP}$]] = [[Class_BPP|$\\text{BPP}$]] = [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#IM03|[IM03] ]].



The class of problems solvable by randomized algorithms that always return the correct answer, and whose expected running time (on any input) is polynomial.



Defined in [[ZooRefs#Gil77|[Gil77] ]].



There exists an oracle relative to which [[Class_ZPP|$\\text{ZPP}$]] = [[Class_EXP|$\\text{EXP}$]] [[ZooRefs#Hel84|[Hel84] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ZPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ZPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ZPTIME(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ZPTIME(f(n)) - Zero-Error Probabilistic f(n)-Time =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_ZPP|$\\text{ZPP}$]], but with O(f(n))-time instead of polynomial-time.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



For any constructible superpolynomial f, ZPTIME(f(n)) with [[Class_NP|$\\text{NP}$]] oracle is not contained in [[Class_P/poly|$\\text{P/poly}$]] [[ZooRefs#KW98|[KW98] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ZPTIME(f(n)))>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ZPTIME(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_ZQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ZQP - Zero-Error Extension Of EQP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of questions that can be answered by a QTM that answers yes, no, or "maybe".  If the correct answer is yes, then P[no] = 0, and vice-versa; and the probability of maybe is at most 1/2.  Since some of the probabilities have to vanish, [[Class_ZQP|$\\text{ZQP}$]] has the same technical caveats as [[Class_EQP|$\\text{EQP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined independently in [[ZooRefs#BW03|[BW03] ]] and in [[ZooRefs#Nis02|[Nis02] ]].



Contains [[Class_EQP|$\\text{EQP}$]] and [[Class_ZBQP|$\\text{ZBQP}$]] and is contained in [[Class_BQP|$\\text{BQP}$]].  Equals [[Class_RQP|$\\text{RQP}$]] ∩ coRQP.  There is an oracle such that ZQP^ZQP^ is larger than [[Class_ZQP|$\\text{ZQP}$]] [[ZooRefs#BW03|[BW03] ]]; c.f. with [[Class_ZBQP|$\\text{ZBQP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_ZQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ZQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coAM"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coAM - Complement of AM =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coAM)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coAM because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coC=P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coC,,=,,P - Complement of C=P =

----
CategoryClassical 

== Description ==

{{{#!description

Equals [[Class_NQP|$\\text{NQP}$]] [[ZooRefs#FGH+98|[FGH+98] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coC=P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coC=P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coMA"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coMA - Complement of MA =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coMA)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coMA because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coModkP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coMod,,k,,P - Complement of ModkP =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coModkP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coModkP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coNE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coNE - Complement of NE =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coNE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coNE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coNEXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coNEXP - Complement of NEXP =

----
CategoryClassical 

== Description ==

{{{#!description

Contained in [[Class_NEXP/poly|$\\text{NEXP/poly}$]] (folklore result reported in [Fortnow's weblog]).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contained in [[Class_NEXP/poly|$\\text{NEXP/poly}$]] (folklore result reported in [weblog]).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coNEXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coNEXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coNL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coNL - Complement of NL =

----
CategoryClassical 

== Description ==

{{{#!description

Equals [[Class_NL|$\\text{NL}$]] [[ZooRefs#Imm88|[Imm88] ]] [[ZooRefs#Sze87|[Sze87] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coNL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coNL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coNP - Complement of NP =

----
CategoryClassical 

== Description ==

{{{#!description

If [[Class_NP|$\\text{NP}$]] = [[Class_coNP|$\\text{coNP}$]], then any inconsistent Boolean formula of size n has a proof of inconsistency of size polynomial in n.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If [[Class_NP|$\\text{NP}$]] does not equal [[Class_coNP|$\\text{coNP}$]], then [[Class_P|$\\text{P}$]] does not equal [[Class_NP|$\\text{NP}$]].  But the other direction is not known.



See also: [[Class_NP|$\\text{NP}$]] ∩ [[Class_coNP|$\\text{coNP}$]].



Every problem in [[Class_coNP|$\\text{coNP}$]] has an [[Class_IP|$\\text{IP}$]] (interactive proof) system, where moreover the prover can be restricted to BPP^#P^. If every problem in [[Class_coNP|$\\text{coNP}$]] has an interactive protocol whose rounds are bounded by a polylogarithmic function, then [[Class_EH|$\\text{EH}$]] collapses to the third level [[ZooRefs#SS04|[SS04] ]].



Co-NP is equal to SO-A, the second-order queries where the second-order quantifiers are only universals.



Every problem in [[Class_coNP|$\\text{coNP}$]] has an [[Class_IP|$\\text{IP}$]] (interactive proof) system, where moreover the prover can be restricted to BPP^#P^.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coNP/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coNP/poly - Complement of NP/poly =

----
CategoryClassical 

== Description ==

{{{#!description

If [[Class_NP|$\\text{NP}$]] is contained in [[Class_coNP/poly|$\\text{coNP/poly}$]] then [[Class_PH|$\\text{PH}$]] collapses to S,,2,,P^NP^ [[ZooRefs#CCH+01|[CCH+01] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



NP^NP^NP^(coNP/poly ∩ NP)^ = NP^NP^NP^ [[ZooRefs#HNO+96|[HNO+96] ]]



Note: At the suggestion of Luis Antuñes, the above specimen of the Complexity Zoo has been locked in a cage.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coNP/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coNP/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coNPcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coNP^cc^ - Complement of NPcc =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coNPcc)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coNPcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coNQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coNQP - Complement of NQP =

----
CategoryClassical 

== Description ==

{{{#!description

Equals [[Class_C=P|$\\text{C}_\\text{=}\\text{P}$]] [[ZooRefs#FGH+98|[FGH+98] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coNQP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coNQP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coRE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coRE - Complement of RE =

----
CategoryClassical 

== Description ==

{{{#!description

Does not equal [[Class_RE|$\\text{RE}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The problem "given a computable predicate [[Class_P|$\\text{P}$]], is [[Class_P|$\\text{P}$]] true of all positive integers?" is coRE-complete.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coRE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coRE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coRNC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coRNC - Complement of RNC =

----
CategoryClassical 

== Description ==

{{{#!description

Contains the problem of whether a bipartite graph has a perfect matching [[ZooRefs#Kar86|[Kar86] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coRNC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coRNC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coRP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coRP - Complement of RP =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#Gil77|[Gil77] ]].  (This paper does not actually discuss [[Class_coRP|$\\text{coRP}$]], other than implicitly mentioning that [[Class_ZPP|$\\text{ZPP}$]] = [[Class_RP|$\\text{RP}$]] ∩ co-RP.  Is there a better reference?)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains the problem of testing whether an integer is prime [[ZooRefs#SS77|[SS77] ]].



Defined in [[ZooRefs#Gil77|[Gil77] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coRP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coRP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coSL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coSL - Complement of SL =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coSL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coSL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coSPARSE"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coSPARSE - Complement of SPARSE =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coSPARSE)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coSPARSE because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coUCC"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coUCC - Complement of UCC =

----
CategoryClassical 

== Description ==

{{{#!description

[[ZooRefs#Tor00|[Tor00] ]] showed the following problem complete for [[Class_coUCC|$\\text{coUCC}$]] under [[Class_L|$\\text{L}$]] reductions:}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Given a colored graph G with at most two vertices having any given color, does G have any nontrivial automorphisms?
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coUCC)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coUCC because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_coUP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= coUP - Complement of UP =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_coUP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save coUP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_cofrIP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= cofrIP - Complement of frIP =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_cofrIP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save cofrIP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_compIP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= compIP - Competitive IP Proof System =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_compNP|$\\text{compNP}$]] but for interactive ([[Class_IP|$\\text{IP}$]]) proofs instead of [[Class_NP|$\\text{NP}$]] proofs.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



More formally, [[Class_compIP|$\\text{compIP}$]] is the class of decision problems [[Class_L|$\\text{L}$]] in [[Class_IP|$\\text{IP}$]] = [[Class_PSPACE|$\\text{PSPACE}$]] such that, if the answer is "yes," then that can be proven by an interactive protocol between a [[Class_BPP|$\\text{BPP}$]] verifier and a prover, a [[Class_BPP|$\\text{BPP}$]] machine with access only to an oracle for [[Class_L|$\\text{L}$]].



Assuming [[Class_NEE|$\\text{NEE}$]] is not contained in [[Class_BPEE|$\\text{BPEE}$]], [[Class_NP|$\\text{NP}$]] (and indeed [[Class_NP|$\\text{NP}$]] ∩ [[Class_Coh|$\\text{Coh}$]]) is not contained in [[Class_compIP|$\\text{compIP}$]] [[ZooRefs#BG94|[BG94] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_compIP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save compIP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_compNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= compNP - Competitive NP Proof System =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems [[Class_L|$\\text{L}$]] in [[Class_NP|$\\text{NP}$]] such that, if the answer is "yes," then a proof can be constructed in polynomial time given access only to an oracle for [[Class_L|$\\text{L}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_NPC|$\\text{NPC}$]].



[[ZooRefs#BG94|[BG94] ]] show that [[Class_compNP|$\\text{compNP}$]] is contained in [[Class_frIP|$\\text{frIP}$]], and that assuming [[Class_NEE|$\\text{NEE}$]] is not contained in [[Class_BPEE|$\\text{BPEE}$]], [[Class_compNP|$\\text{compNP}$]] does not equal [[Class_NP|$\\text{NP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_compNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save compNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_frIP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= frIP - Function-Restricted IP Proof Systems =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems [[Class_L|$\\text{L}$]] that have a decider in the following sense.  There exists a [[Class_BPP|$\\text{BPP}$]] machine D such that for all inputs x,}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes" then D^L^(x) (D with oracle for [[Class_L|$\\text{L}$]]) accepts with probability at least 2/3.

If the answer is "no" then D^A^(x) accepts with probability at most 1/3 for all oracles A.



Contains [[Class_compIP|$\\text{compIP}$]] [[ZooRefs#BG94|[BG94] ]] and [[Class_Check|$\\text{Check}$]] [[ZooRefs#BK89|[BK89] ]].



Contained in [[Class_MIP|$\\text{MIP}$]] = [[Class_NEXP|$\\text{NEXP}$]] [[ZooRefs#FRS88|[FRS88] ]].



Assuming [[Class_NEE|$\\text{NEE}$]] is not contained in [[Class_BPEE|$\\text{BPEE}$]], [[Class_NP|$\\text{NP}$]] (and indeed [[Class_NP|$\\text{NP}$]] ∩ [[Class_Coh|$\\text{Coh}$]]) is not contained in [[Class_frIP|$\\text{frIP}$]] [[ZooRefs#BG94|[BG94] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_frIP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save frIP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_k-BWBP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= k-BWBP - Bounded-Width Branching Program =

----
CategoryClassical 

== Description ==

{{{#!description

Alternate name for [[Class_k-PBP|$\\text{k-PBP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_k-BWBP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save k-BWBP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_k-EQBP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= k-EQBP - Width-k Polynomial-Time Exact Quantum Branching Programs =

----
CategoryQuantum 

== Description ==

{{{#!description

See [[Class_k-PBP|$\\text{k-PBP}$]] for the definition of a classical branching program.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A quantum branching program is the natural quantum generalization: we have a quantum state in a Hilbert space of dimension k.  Each step t consists of applying a unitary matrix U^(t)^(x,,i,,): that is, U^(t)^ depends on a single bit x,,i,, of the input.  (So these are the quantum analogues of so-called oblivious branching programs.)  In the end we measure to decide whether to accept; there must be zero probability of error.



Defined in [[ZooRefs#AMP02|[AMP02] ]], where it was also shown that [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] is contained in 2-EQBP.



k-BQBP can be defined similarly.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_k-EQBP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save k-EQBP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_k-PBP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= k-PBP - Polynomial-Size Width-k Branching Program =

----
CategoryClassical 

== Description ==

{{{#!description

A branching program is a directed acyclic graph with a designated start vertex.  Each (non-sink) vertex is labeled by the name of an input bit, and has two outgoing edges, one of which is followed if that input bit is 0, the other if the bit is 1.  A sink vertex can be either an 'accept' or a 'reject' vertex.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



The size of the branching program is the number of vertices.  The branching program has width k if the vertices can be sorted into levels, each with at most k vertices, such that each edge goes from a level to the one immediately after it.



Then [[Class_k-PBP|$\\text{k-PBP}$]] is the class of decision problems solvable by a family of polynomial-size, width-k branching programs.  (A uniformity condition may also be imposed.)



[[Class_k-PBP|$\\text{k-PBP}$]] equals (nonuniform) [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] for constant k at least 5 [[ZooRefs#Bar89|[Bar89] ]].  On the other hand, 4-PBP is in [[Class_ACC0|$\\text{ACC}^\\text{0}\\text{}$]] [[ZooRefs#BT88|[BT88] ]].



Contained in [[Class_k-EQBP|$\\text{k-EQBP}$]], as well as [[Class_PBP|$\\text{PBP}$]].



See also BP,,d,,(P).
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_k-PBP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save k-PBP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_mAL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= mAL - Monotone AL =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#GS90|[GS90] ]].  Equals [[Class_mP|$\\text{mP}$]] by definition.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_mAL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save mAL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_mL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= mL - Monotone L =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a family of monotone log-width polynomial-size leveled circuits.  (A leveled circuit is one where gates on each level can depend only on the level immediately below it.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GS90|[GS90] ]], who raise as an open problem to define a uniform version of [[Class_mL|$\\text{mL}$]].



Strictly contains [[Class_mNC1|$\\text{mNC}^\\text{1}\\text{}$]] [[ZooRefs#GS91|[GS91] ]].



Contained in (nonuniform versions of) [[Class_mNL|$\\text{mNL}$]] and [[Class_mcoNL|$\\text{mcoNL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_mL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save mL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_mNC1"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= mNC^1^ - Monotone NC1 =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a family of monotone [[Class_NC1|$\\text{NC}^\\text{1}\\text{}$]] circuits (i.e. AND and OR gates only).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A uniformity condition could also be imposed.



Defined in [[ZooRefs#GS90|[GS90] ]].



Strictly contained in [[Class_mNL|$\\text{mNL}$]] [[ZooRefs#KW88|[KW88] ]], and indeed in [[Class_mL|$\\text{mL}$]] [[ZooRefs#GS91|[GS91] ]].



Strictly contains [[Class_mTC0|$\\text{mTC}^\\text{0}\\text{}$]] [[ZooRefs#Yao89|[Yao89] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_mNC1)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save mNC1 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_mNL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= mNL - Monotone NL =

----
CategoryClassical 

== Description ==

{{{#!description

See [[Class_mP|$\\text{mP}$]] for the definition of a monotone nondeterministic Turing machine, due to [[ZooRefs#GS90|[GS90] ]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



[[Class_mNL|$\\text{mNL}$]] is the class of decision problems solvable by a monotone nondeterministic log-space Turing machine.



[[Class_mNL|$\\text{mNL}$]] does not equal [[Class_mcoNL|$\\text{mcoNL}$]] [[ZooRefs#GS90|[GS90] ]], in contrast to the case for [[Class_NL|$\\text{NL}$]] and [[Class_coNL|$\\text{coNL}$]].



Also, [[Class_mNL|$\\text{mNL}$]] strictly contains [[Class_mNC1|$\\text{mNC}^\\text{1}\\text{}$]] [[ZooRefs#KW88|[KW88] ]].



See also: [[Class_mL|$\\text{mL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_mNL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save mNL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_mNP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= mNP - Monotone NP =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems for which a 'yes' answer can be verified in [[Class_mP|$\\text{mP}$]] (that is, monotone polynomial-time).  The monotonicity requirement applies only to the input bits, not to the bits that are guessed nondeterministically. So, in the corresponding circuit, one can have NOT gates so long as they depend only on the nondeterministic guess bits.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GS90|[GS90] ]], where it was also shown that [[Class_mNP|$\\text{mNP}$]] is 'trivial': that is, it contains exactly the monotone problems in [[Class_NP|$\\text{NP}$]].



Strictly contains [[Class_mP|$\\text{mP}$]] [[ZooRefs#Raz85|[Raz85] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_mNP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save mNP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_mP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= mP - Monotone P =

----
CategoryClassical 

== Description ==

{{{#!description

The definition of this class, due to [[ZooRefs#GS90|[GS90] ]], is not obvious.  First, a monotone nondeterministic Turing machine is one such that, whenever it can make a transition with a 0 on its input tape, it can also make that same transition with a 1 on its input tape. (This restriction does not apply to the work tape.)  A monotone alternating Turing machine is subject to the restriction that it can only reference an input bit x by, "there exists a z at most x," or "for all z at least x."}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Then applying the result of [[ZooRefs#CKS81|[CKS81] ]] that [[Class_P|$\\text{P}$]] = [[Class_AL|$\\text{AL}$]], [[Class_mP|$\\text{mP}$]] is defined to be [[Class_mAL|$\\text{mAL}$]]: the class of decision problems solvable by a monotone alternating log-space Turing machine.



Actually there's a caveat: A monotone Turing machine or circuit can first negate the entire input, then perform a monotone computation.  That way it becomes meaningful to talk about whether a monotone complexity class is closed under complement.



Strictly contained in [[Class_mNP|$\\text{mNP}$]] [[ZooRefs#Raz85|[Raz85] ]].



Deciding whether a bipartite graph has a perfect matching, despite being both a monotone problem and in [[Class_P|$\\text{P}$]], requires monotone circuits of superpolynomial size [Raz85b].  Letting MONO be the class of monotone problems, it follows that [[Class_mP|$\\text{mP}$]] is strictly contained in MONO ∩ [[Class_P|$\\text{P}$]].



See also: [[Class_mNC1|$\\text{mNC}^\\text{1}\\text{}$]], [[Class_mL|$\\text{mL}$]], [[Class_mNL|$\\text{mNL}$]], [[Class_mcoNL|$\\text{mcoNL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_mP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save mP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_mP/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= mP/poly - Monotone P/poly =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a nonuniform family of polynomial-size Boolean circuits with only AND and OR gates, no NOT gates.  (Or rather, following the definitions of [[ZooRefs#GS90|[GS90] ]], the entire input can be negated as long as there are no other negations.)}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



More straightforward to define than [[Class_mP|$\\text{mP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_mP/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save mP/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_mTC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= mTC^0^ - Monotone TC0 =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by a family of monotone [[Class_TC0|$\\text{TC}^\\text{0}\\text{}$]] circuits (i.e. constant-depth, polynomial-size, AND, OR, and threshold gates, but no NOT gates).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



A uniformity condition could also be imposed.



Defined in [[ZooRefs#GS90|[GS90] ]].



Strictly contained in [[Class_mNC1|$\\text{mNC}^\\text{1}\\text{}$]] [[ZooRefs#Yao89|[Yao89] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_mTC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save mTC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_mcoNL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= mcoNL - Complement of mNL =

----
CategoryClassical 

== Description ==

{{{#!description

Defined in [[ZooRefs#GS90|[GS90] ]], where it was also shown that [[Class_mcoNL|$\\text{mcoNL}$]] does not equal [[Class_mNL|$\\text{mNL}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



See also: [[Class_mL|$\\text{mL}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_mcoNL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save mcoNL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_polyL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= polyL - Polylogarithmic Space =

----
CategoryClassical 

== Description ==

{{{#!description

Equals DSPACE((log n)^c^).}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



In contrast to [[Class_L|$\\text{L}$]], which is contained in [[Class_P|$\\text{P}$]], it is not known if [[Class_polyL|$\\text{polyL}$]] is contained in [[Class_P|$\\text{P}$]] or vice versa.  On the other hand, we do know that [[Class_polyL|$\\text{polyL}$]] does not equal [[Class_P|$\\text{P}$]], since (for example) [[Class_polyL|$\\text{polyL}$]] does not have complete problems under many-to-one logspace reductions.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_polyL)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save polyL because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_span-P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= span-P - Span Polynomial-Time =

----
CategoryClassical 

== Description ==

{{{#!description

The class of functions computable as |S|, where S is the set of output values returned by the accepting paths of an [[Class_NP|$\\text{NP}$]] machine.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#KST+89|[KST+89] ]], where it is also shown that [[Class_span-P|$\\text{span-P}$]] contains [[Class_SharpP|$\\text{#P}$]] and [[Class_OptP|$\\text{OptP}$]]; and that [[Class_span-P|$\\text{span-P}$]] = [[Class_SharpP|$\\text{#P}$]] if and only if [[Class_UP|$\\text{UP}$]] = [[Class_NP|$\\text{NP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_span-P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save span-P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_symP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= symP - Alternate Name for S2P =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_symP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save symP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Δ2P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Δ,,2,,P - P With NP Oracle =

----
CategoryClassical 

== Description ==

{{{#!description

A level of [[Class_PH|$\\text{PH}$]], the polynomial hierarchy.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_BH|$\\text{BH}$]].



There exists an oracle relative to which [[Class_Δ2P|$\\text{Δ}_\\text{2}\\text{P}$]] is not contained in [[Class_PP|$\\text{PP}$]] [[ZooRefs#Bei94|[Bei94] ]].



There exists another oracle relative to which [[Class_Δ2P|$\\text{Δ}_\\text{2}\\text{P}$]] is contained in [[Class_P/poly|$\\text{P/poly}$]] [[ZooRefs#BGS75|[BGS75] ]], and indeed has linear-size circuits [[ZooRefs#Wil85|[Wil85] ]].



There exists an oracle B for which BPP^B^ is exponentially more powerful than Δ,,2,,P^B^ [[ZooRefs#KV96|[KV96] ]].



If [[Class_P|$\\text{P}$]] = [[Class_NP|$\\text{NP}$]], then any polynomial-size circuit C can be learned in [[Class_Δ2P|$\\text{Δ}_\\text{2}\\text{P}$]] with C oracle [[ZooRefs#Aar06|[Aar06] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Δ2P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Δ2P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Θ2P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Θ,,2,,P - Alternate name for PNP[log] =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Θ2P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Θ2P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Π2P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Π,,2,,P - coNP With NP Oracle =

----
CategoryClassical 

== Description ==

{{{#!description

Complement of [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Along with [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]], comprises the second level of [[Class_PH|$\\text{PH}$]], the polynomial hierarchy. For any fixed k, there is a problem in [[Class_Π2P|$\\text{Π}_\\text{2}\\text{P}$]] ∩ [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] that cannot be solved by circuits of size n^k^ [[ZooRefs#Kan82|[Kan82] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Π2P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Π2P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Σ2P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Σ,,2,,P - NP With NP Oracle =

----
CategoryClassical 

== Description ==

{{{#!description

Complement of [[Class_Π2P|$\\text{Π}_\\text{2}\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Along with [[Class_Π2P|$\\text{Π}_\\text{2}\\text{P}$]], comprises the second level of [[Class_PH|$\\text{PH}$]], the polynomial hierarchy.



[[ZooRefs#Uma98|[Uma98] ]] has shown that the following problems are complete for [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]]:



Minimum equivalent DNF.  Given a DNF formula F and integer k, is there a DNF formula equivalent to F with k or fewer occurences of literals?

Shortest implicant.  Given a formula F and integer k, is there a conjunction of k or fewer literals that implies F?  (Note that this problem cannot be Σ,,2,,P-complete for DNF formulas unless [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] equals βP^NP^.)



For any fixed k, there is a problem in [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] ∩ [[Class_Π2P|$\\text{Π}_\\text{2}\\text{P}$]] that cannot be solved by circuits of size n^k^ [[ZooRefs#Kan82|[Kan82] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Σ2P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Σ2P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_Φ2P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= Φ,,2,,P - Second Level of the Symmetric Hierarchy, Alternative Definition =

----
CategoryClassical CategoryHierarchy 

== Description ==

{{{#!description

The class of problems for which there exists a polynomial-time predicate P(x,y,z) such that for all x, if the answer on input x is "yes," then}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



For all y, there exists a z for which P(x,y,z).

For all z, there exists a y for which P(x,y,z).



Contained in [[Class_Σ2P|$\\text{Σ}_\\text{2}\\text{P}$]] and [[Class_Π2P|$\\text{Π}_\\text{2}\\text{P}$]].



Defined in [[ZooRefs#Can96|[Can96] ]], where it was also observed that [[Class_Φ2P|$\\text{Φ}_\\text{2}\\text{P}$]] = [[Class_S2P|$\\text{S}_\\text{2}\\text{P}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_Φ2P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save Φ2P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_βP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= βP - Limited-Nondeterminism NP =

----
CategoryClassical 

== Description ==

{{{#!description

β,,k,,P is the class of decision problems solvable by a polynomial-time Turing machine that makes O(log^k^n) nondeterministic transitions, with the same acceptance mechanism as [[Class_NP|$\\text{NP}$]].  Equivalently, the machine receives a purported proof of size O(log^k^n) that the answer is 'yes.'}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Then [[Class_βP|$\\text{βP}$]] is the union of β,,k,,P over all constant k.



Defined in [[ZooRefs#KF84|[KF84] ]].  See also the survey [[ZooRefs#GLM96|[GLM96] ]].



There exist oracles relative to which basically any consistent inclusion structure among the β,,k,,P's can be realized [[ZooRefs#BG98|[BG98] ]].



β,,2,,P contains [[Class_LOGNP|$\\text{LOGNP}$]] and [[Class_LOGSNP|$\\text{LOGSNP}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_βP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save βP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_δ-BPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= δ-BPP - δ-Semi-Random BPP =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_BPP|$\\text{BPP}$]], except that the random bit source is biased as follows.  Each bit could depend on all the previous bits in arbitrarily complicated ways; the only promise is that the bit is 1 with probability in the range [δ,1-δ], conditioned on all previous bits.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



So clearly 0-BPP = [[Class_P|$\\text{P}$]] and 1/2-BPP = [[Class_BPP|$\\text{BPP}$]].



It turns out that, for any δ>0, [[Class_δ-BPP|$\\text{δ-BPP}$]] = [[Class_BPP|$\\text{BPP}$]] [[ZooRefs#VV85|[VV85] ]], [[ZooRefs#Zuc91|[Zuc91] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_δ-BPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save δ-BPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_δ-RP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= δ-RP - δ-Semi-Random RP =

----
CategoryClassical 

== Description ==

{{{#!description

Same as [[Class_δ-BPP|$\\text{δ-BPP}$]], but for [[Class_RP|$\\text{RP}$]] instead of [[Class_BPP|$\\text{BPP}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



For any δ>0, [[Class_δ-RP|$\\text{δ-RP}$]] = [[Class_RP|$\\text{RP}$]] [[ZooRefs#VV85|[VV85] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_δ-RP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save δ-RP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_∃BPP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ∃BPP - BPP With Existential Operator =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems for which there exists a [[Class_BPP|$\\text{BPP}$]] machine M such that, for all inputs x,}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is "yes" then there exists a y such that M(x,y) accepts.

If the answer is "no" then for all y, M(x,y) rejects.



Alternatively defined as NP^BPP^.



Contains [[Class_NP|$\\text{NP}$]] and [[Class_BPP|$\\text{BPP}$]], and is contained in [[Class_MA|$\\text{MA}$]] and [[Class_SBP|$\\text{SBP}$]].



[[Class_∃BPP|$\\text{∃BPP}$]] seems obviously equal to [[Class_MA|$\\text{MA}$]], yet [[ZooRefs#FFK+93|[FFK+93] ]] constructed an oracle relative to which they're unequal!  Here is the difference: if the answer is "yes," [[Class_MA|$\\text{MA}$]] requires only that there exist a y such that for at least 2/3 of random strings r, M(x,y,r) accepts (where M is a [[Class_P|$\\text{P}$]] predicate).  For all other y's, the proportion of r's such that M(x,y,r) accepts can be arbitrary (say, 1/2).  For [[Class_∃BPP|$\\text{∃BPP}$]], by contrast, the probability that M(x,y) accepts must always be either at most 1/3 or at least 2/3, for all y's.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_∃BPP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ∃BPP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_∃NISZK"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ∃NISZK - NISZK With Existential Operator =

----
CategoryClassical 

== Description ==

{{{#!description

Contains [[Class_NP|$\\text{NP}$]] and [[Class_NISZK|$\\text{NISZK}$]], and is contained in the third level of [[Class_PH|$\\text{PH}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_∃NISZK)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ∃NISZK because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_⊕EXP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ⊕EXP - Parity EXP =

----
CategoryClassical 

== Description ==

{{{#!description

The exponential-time analogue of [[Class_⊕P|$\\text{⊕P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



There exists an oracle relative to which [[Class_⊕EXP|$\\text{⊕EXP}$]] = [[Class_ZPP|$\\text{ZPP}$]] [[ZooRefs#BBF98|[BBF98] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_⊕EXP)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ⊕EXP because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_⊕L"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ⊕L - Parity L =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_L|$\\text{L}$]] as [[Class_⊕P|$\\text{⊕P}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_SL|$\\text{SL}$]] [[ZooRefs#KW93|[KW93] ]].



Solving a linear system over Z,,2,, is complete for [[Class_⊕L|$\\text{⊕L}$]] [[ZooRefs#Dam90|[Dam90] ]].



⊕L^⊕L^ = [[Class_⊕L|$\\text{⊕L}$]] [[ZooRefs#HRV00|[HRV00] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_⊕L)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ⊕L because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_⊕L/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ⊕L/poly - Nonuniform ⊕L =

----
CategoryClassical 

== Description ==

{{{#!description

Has the same relation to [[Class_⊕L|$\\text{⊕L}$]] as [[Class_P/poly|$\\text{P/poly}$]] does to [[Class_P|$\\text{P}$]].}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Contains [[Class_NL/poly|$\\text{NL/poly}$]] [[ZooRefs#GW96|[GW96] ]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_⊕L/poly)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ⊕L/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_⊕P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ⊕P - Parity P =

----
CategoryClassical 

== Description ==

{{{#!description

The class of decision problems solvable by an [[Class_NP|$\\text{NP}$]] machine such that}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



If the answer is 'yes,' then the number of accepting paths is odd.

If the answer is 'no,' then the number of accepting paths is even.



Defined in [[ZooRefs#PZ83|[PZ83] ]].



Contains graph isomorphism; indeed, graph isomorphism is low for [[Class_⊕P|$\\text{⊕P}$]] [[ZooRefs#AK02|[AK02] ]].



Contains [[Class_FewP|$\\text{FewP}$]] [[ZooRefs#CH89|[CH89] ]].



There exists an oracle relative to which [[Class_P|$\\text{P}$]] = [[Class_⊕P|$\\text{⊕P}$]] but [[Class_P|$\\text{P}$]] is not equal to [[Class_NP|$\\text{NP}$]] (and indeed [[Class_NP|$\\text{NP}$]] = [[Class_EXP|$\\text{EXP}$]]) [[ZooRefs#BBF98|[BBF98] ]].



Equals Mod,,2^m,,P for every positive integer m.
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_⊕P)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ⊕P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_⊕SAC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ⊕SAC^0^ - AC0 With Unbounded Parity Gates =

----
CategoryClassical 

== Description ==

{{{#!description

}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==


== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_⊕SAC0)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ⊕SAC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_⊕SAC1"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= ⊕SAC^1^ - AC1 With Unbounded Parity Gates =

----
CategoryClassical 

== Description ==

{{{#!description

The class of problems solvable by a nonuniform family of polynomial-size, polylog-depth circuits with unbounded-fanin XOR and bounded-fanin AND gates.}}}

== Complete Problem ==

{{{#!complete_problem

}}}

== Comments ==



Defined in [[ZooRefs#GW96|[GW96] ]], where it was also shown that [[Class_⊕SAC1|$\\text{⊕SAC}^\\text{1}\\text{}$]] contains [[Class_SAC1|$\\text{SAC}^\\text{1}\\text{}$]].
== Relations ==

{{{#!class_relations

}}}


== See Also ==

<<FullSearch(linkto:Class_⊕SAC1)>>
'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save ⊕SAC1 because")
    print (e)

if p:
    assert p.exists()

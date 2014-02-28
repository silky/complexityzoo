# coding: utf-8
import py

from MoinMoin import wikiutil

import urllib

from MoinMoin.PageEditor import PageEditor
from MoinMoin.web.contexts import ScriptContext
from MoinMoin.Page import Page

pagename = u"Class_#AC0"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #AC^0^ - Sharp-AC0 =

== Comments ==

The class of functions from {0,1}^n^ to nonnegative integers computed by polynomial-size constant-depth arithmetic circuits, using addition and multiplication gates and the constants 0 and 1.



Contained in [[Class_GapAC0|GapAC0]].
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save #AC0 because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_#GA"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #GA - Graph Automorphism =

== Comments ==

The class of problems (Karp-)reducible to counting the number of automorphisms of a graph.



Counterpart of [[Class_GI|GI]].
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save #GA because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_#L"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #L - Sharp-L =

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_#P|#P]] does to [[Class_P|P]].



[[Class_#L|#L]] is contained in [[Class_DET|DET]] [[ZooRefs#AJ93|[AJ93] ]].
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save #L because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_#L/poly"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #L/poly - Nonuniform #L =

== Comments ==

Has the same relation to [[Class_#L|#L]] as [[Class_P/poly|P/poly]] does to [[Class_P|P]].
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save #L/poly because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_#P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #P - Sharp-P =

== Comments ==

The class of function problems of the form "compute f(x)," where f is the number of accepting paths of an [[Class_NP|NP]] machine.



The canonical #P-complete problem is #SAT: given a Boolean formula, compute how many satisfying assignments it has.



Defined in [[ZooRefs#Val79|[Val79] ]], where it was also shown that the problem of counting the number of perfect matchings in a bipartite graph (or equivalently, computing the permanent of a 0-1 matrix) is #P-complete.



What makes that interesting is that the associated decision problem (whether a bipartite graph has a perfect matching) is in [[Class_P|P]].



[[Class_PH|PH]] is in [[Class_P#P|P#P]] [[ZooRefs#Tod89|[Tod89] ]].



Any function in [[Class_#P|#P]] can be approximated to within a polynomial factor in [[Class_BPP|BPP]] with [[Class_NP|NP]] oracle [[ZooRefs#Sto85|[Sto85] ]].
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save #P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_#W[t]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= #W[t] - Sharp-W[t] =

== Comments ==

Roughly, the analogue of [[Class_#P|#P]] for parameterized complexity.  I.e. the class of parameterized counting problems that are fixed-parameter parsimonious reducible to the following problem:



#WSAT: Given a Boolean formula, count the number of satisfying assignments of Hamming weight k (where k is the parameter).



Defined in [[ZooRefs#FG02|[FG02] ]], which should be consulted for the full definition.  [[ZooRefs#FG02|[FG02] ]] also showed that there exist #W[1]-complete problems whose corresponding decision problems are fixed-parameter tractable (i.e. in FPT).
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save #W[t] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_(Mk)P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= (M,,k,,)P - Acceptance Mechanism by Monoid Mk =

== Comments ==

A monoid is a set with an associative operation and an identity element (so it's like a group, except that it need not have inverses).



Then [[Class_(Mk)P|(Mk)P]] is the class of decision problems solvable by an [[Class_NP|NP]] machine with the following acceptance mechanism.  The i^th^ computation path (under some lexicographic ordering) outputs an element m,,i,, of M,,k,,.  Then the machine accepts if and only if m,,1,,m,,2,,...m,,s,, is the identity (where s is the number of paths).



Defined by Hertrampf [[ZooRefs#Her97|[Her97] ]], who also showed the following (in the special case M is a group):



If G is any nonsolvable group (for example S,,5,,, the symmetric group on 5 elements), then (G)P = [[Class_PSPACE|PSPACE]].

(Z,,k,,)P = [[Class_coModkP|coModkP]], where Z,,k,, is the cyclic group on k elements.

If |G|=k, then (G)P contains [[Class_coModkP|coModkP]].
== Relations ==


== See Also ==

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

== Comments ==

Together with [[Class_NP/poly|NP/poly]] ∩ [[Class_coNP/poly|coNP/poly]], has the same relation to [[Class_NP|NP]] ∩ [[Class_coNP|coNP]] as [[Class_P/poly|P/poly]] has to [[Class_P|P]].  A language in (NP ∩ coNP)/poly is defined by a single language in [[Class_NP|NP]] ∩ [[Class_coNP|coNP]] which is then modified by advice.  A language in [[Class_NP/poly|NP/poly]] ∩ [[Class_coNP/poly|coNP/poly]] comes from two possibly different languages in [[Class_NP|NP]] and [[Class_coNP|coNP]] which become the same with good advice.



There is an oracle relative to which [[Class_NP/poly|NP/poly]] ∩ [[Class_coNP/poly|coNP/poly]], indeed NP/1 ∩ coNP/1, is not contained in (NP ∩ coNP)/poly [[ZooRefs#FFK+93|[FFK+93] ]].  Recently they improved this to NP/1 ∩ [[Class_coNP|coNP]] [FF..].



If [[Class_NP|NP]] is contained in (NP ∩ coNP)/poly, then [[Class_PH|PH]] collapses to S,,2,,P^NP ∩ [[Class_coNP|coNP]] [[ZooRefs#CCH+01|[CCH+01] ]].
== Relations ==


== See Also ==

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

== Comments ==

See [[Class_AvgP|AvgP]] for basic notions of average-case complexity.



[[Class_(NP,P-samplable)|(NP,P-samplable)]] is the same as [[Class_DistNP|DistNP]], except that the distribution μ only needs to be samplable in polynomial time.  μ's cumulative density function does not need to be computable in polynomial time.



Any problem complete for [[Class_DistNP|DistNP]] is also complete for [[Class_(NP,P-samplable)|(NP,P-samplable)]] [[ZooRefs#IL90|[IL90] ]].
== Relations ==


== See Also ==

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

== Comments ==

The intersection of [[Class_NPC|NPC]] with {0,1}^*^ (i.e. the set of binary strings).



Contains [[Class_NP|NP]].



Is contained in [[Class_PSPACE|PSPACE]], and in [[Class_AM|AM]] assuming the Extended Riemann Hypothesis [[ZooRefs#Koi96|[Koi96] ]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#Bra77|[Bra77] ]], where it was also shown that [[Class_1NAuxPDAp|1NAuxPDAp]] strictly contains [[Class_CFL|CFL]] and is strictly contained in [[Class_LOGCFL|LOGCFL]]. The class corresponds to the closure of [[Class_CFL|CFL]] under one-way log-space reductions.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_SBP|SBP]], except that f is a nonnegative-valued [[Class_GapP|GapP]] function rather than a [[Class_#P|#P]] function.



Defined in [[ZooRefs#Vya03|[Vya03] ]], where the following was also shown:



[[Class_A0PP|A0PP]] contains [[Class_QMA|QMA]], [[Class_AWPP|AWPP]], and [[Class_coC=P|coC=P]].

[[Class_A0PP|A0PP]] is contained in [[Class_PP|PP]].

If [[Class_A0PP|A0PP]] = [[Class_PP|PP]] then [[Class_PH|PH]] is contained in [[Class_PP|PP]].



Kuperberg ([[ZooRefs#Kup09|[Kup09] ]]) showed that [[Class_A0PP|A0PP]] = [[Class_SBQP|SBQP]].



Same as [[Class_SBP|SBP]], except that f is a [[Class_GapP|GapP]] rather than [[Class_#P|#P]] function.
== Relations ==


== See Also ==

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

== Comments ==

AC^i^ is the class of decision problems solvable by a nonuniform family of Boolean circuits, with polynomial size, depth O(log^i^(n)), and unbounded fanin.  The gates allowed are AND, OR, and NOT.



Then [[Class_AC|AC]] is the union of AC^i^ over all nonnegative i.



AC^i^ is contained in NC^i+1^; thus, [[Class_AC|AC]] = [[Class_NC|NC]].



Contains [[Class_NL|NL]].



For a random oracle A, (AC^i^)^A^ is strictly contained in (AC^i+1^)^A^, and (uniform) AC^A^ is strictly contained in P^A^, with probability 1 [[ZooRefs#Mil92|[Mil92] ]].



fo-uniform [[Class_AC|AC]] with depth  is equal to [[Class_FO[]|FO[]]]
== Relations ==


== See Also ==

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

== Comments ==

An especially important subclass of [[Class_AC|AC]], corresponding to constant-depth, unbounded-fanin, polynomial-size circuits with AND, OR, and NOT gates.



Computing the Parity or Majority of n bits is not in [[Class_AC0|AC0]] [[ZooRefs#FSS84|[FSS84] ]].



There are functions in [[Class_AC0|AC0]] that are pseudorandom for all statistical tests in [[Class_AC0|AC0]] [[ZooRefs#NW94|[NW94] ]].  But there are no functions in [[Class_AC0|AC0]] that are pseudorandom for all statistical tests in [[Class_QP|QP]] (quasipolynomial time) [[ZooRefs#LMN93|[LMN93] ]].



[[ZooRefs#LMN93|[LMN93] ]] showed furthermore that functions with [[Class_AC0|AC0]] circuits of depth d are learnable in [[Class_QP|QP]], given their outputs on O(2^log(n)^O(d)^) randomly chosen inputs.  On the other hand, this learning algorithm is essentially optimal, unless there is a 2^n^o(1)^ algorithm for factoring [[ZooRefs#Kha93|[Kha93] ]].



Although there are no good pseudorandom functions in [[Class_AC0|AC0]], [[ZooRefs#IN96|[IN96] ]] showed that there are pseudorandom generators that stretch n bits to n+Θ(log n), assuming the hardness of a problem based on subset sum.



[[Class_AC0|AC0]] contains [[Class_NC0|NC0]], and is contained in [[Class_QACf0|QACf0]] and [[Class_MAC0|MAC0]].



In descriptive complexity, uniform [[Class_AC0|AC0]] can be characterized as the class of problems expressible by first-order predicates with addition and multiplication operators - or indeed, with ordering and multiplication, or ordering and division (see [[ZooRefs#Lee02|[Lee02] ]]). So it's equivalent to the class [[Class_FO|FO]] and to [[Class_AL|AL]] the alternating logtime hierarchy.



[[ZooRefs#BLM+98|[BLM+98] ]] showed the following problem is complete for depth-k [[Class_AC0|AC0]] circuits (with a uniformity condition):



Given a grid graph of polynomial length and width k, decide whether there is a path between vertices s and t (which can be given as part of the input).



Computing the parity or majority of n bits is not in [[Class_AC0|AC0]] [[ZooRefs#FSS84|[FSS84] ]].



Although there are no good pseudorandom functions in [[Class_AC0|AC0]], [[ZooRefs#IN96|[IN96] ]] showed that there are pseudorandom generators in [[Class_AC0|AC0]] that stretch n bits to n+Θ(log n), assuming the hardness of a problem based on subset sum. Work of [[ZooRefs#AIK04|[AIK04] ]] shows pseudorandom generators in [[Class_NC0|NC0]] under more relaxed assumptions.



[[Class_AC0|AC0]] contains [[Class_NC0|NC0]], and is contained in [[Class_QAC0|QAC0]] and [[Class_MAC0|MAC0]].



In descriptive complexity, uniform [[Class_AC0|AC0]] can be characterized as the class of problems expressible by first-order predicates with addition and multiplication operators - or indeed, with ordering and multiplication, or ordering and division (see [[ZooRefs#Lee02|[Lee02] ]]).
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_AC0|AC0]], but now "MOD m" gates (for a specific m) are allowed in addition to AND, OR, and NOT gates.  (A MOD m gate outputs 0 if the sum of its inputs is congruent to 0 modulo m, and 1 otherwise.)



If m is a power of a prime p, then for any prime q not equal to p, deciding whether the sum of n bits is congruent to 0 modulo q is not in [[Class_AC0[m]|AC0[m]]] [[ZooRefs#Raz87|[Raz87] ]] [[ZooRefs#Smo87|[Smo87] ]].  It follows that, for any such m, [[Class_AC0[m]|AC0[m]]] is strictly contained in [[Class_NC1|NC1]].



However, if m is a product of distinct primes (e.g. 6), then it is not even known whether [[Class_AC0[m]|AC0[m]]] = NP!



See also: [[Class_QAC0[m]|QAC0[m]]].



However, if m is a product of distinct primes (i.e. 6), then it is not even known whether [[Class_AC0[m]|AC0[m]]] = NP!
== Relations ==


== See Also ==

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

== Comments ==

See [[Class_AC|AC]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_AC0[m]|AC0[m]]], but now the constant-depth circuit can contain MOD m gates for any m.



Contained in [[Class_TC0|TC0]].



Indeed, can be simulated by depth-3 threshold circuits of quasipolynomial size [[ZooRefs#Yao90|[Yao90] ]].



According to [[ZooRefs#All96|[All96] ]], there is no good evidence for the existence of cryptographically secure functions in [[Class_ACC0|ACC0]].



There is no non-uniform [[Class_ACC0|ACC0]] circuits of polynomial size for NTIMES[2^n^] and no [[Class_ACC0|ACC0]] circuit of size 2^n^O(1)^^ for E^NP^ (The class [[Class_E|E]] with an [[Class_NP|NP]] oracle). These are the only two known nontrivial lower bounds against [[Class_ACC0|ACC0]] and were recently discovered by [[ZooRefs#Wil11|[Wil11] ]].



Contains 4-PBP [[ZooRefs#BT88|[BT88] ]].



See also: [[Class_QACC0|QACC0]].



In 1996, [[ZooRefs#All96|[All96] ]] suggested the existence of cryptographically secure functions in [[Class_ACC0|ACC0]] as an important open question. In 2004, work of [[ZooRefs#AIK04|[AIK04] ]] showed pseudorandom generators in [[Class_NC0|NC0]] based on widely-believed assumptions.
== Relations ==


== See Also ==

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

== Comments ==

The analog of [[Class_PH|PH]] in computability theory.



Let Δ,,0,, = Σ,,0,, = Π,,0,, = [[Class_R|R]].  Then for i>0, let



Δ,,i,, = [[Class_R|R]] with Σ,,i-1,, oracle.

Σ,,i,, = [[Class_RE|RE]] with Σ,,i-1,, oracle.

Π,,i,, = [[Class_coRE|coRE]] with Σ,,i-1,, oracle.



Then [[Class_AH|AH]] is the union of these classes for all nonnegative constant i.



Each level of [[Class_AH|AH]] strictly contains the levels below it.



An equivalent definition is:  is the set of numbers decided by formula with one free variable and bounded quantifier, where the primitives are + and . A bounded quantifier is of the form  or  where   is considered to be free in . Then  is the sets of number validating a formula of the form  with .  is the set of formula who are negation of  formula.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_AP|AP]], but for logarithmic-space instead of polynomial-time.



[[Class_AL|AL]] = [[Class_P|P]] [[ZooRefs#CKS81|[CKS81] ]].
== Relations ==


== See Also ==

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

== Comments ==

Literally, the class of [[Class_ALL|ALL]] languages.



[[Class_ALL|ALL]] is a gargantuan beast that's been wreaking havoc in the Zoo of late.



First [Aar04b] observed that PP/rpoly (PP with polynomial-size randomized advice) equals [[Class_ALL|ALL]], as does PostBQP/qpoly (PostBQP with polynomial-size quantum advice).



Then [[ZooRefs#Raz05|[Raz05] ]] showed that QIP/qpoly, and even IP(2)/rpoly, equal [[Class_ALL|ALL]].



Nor is it hard to show that MA,,EXP,,/rpoly = [[Class_ALL|ALL]].



On the other hand, even though [[Class_PSPACE|PSPACE]] contains [[Class_PP|PP]], and [[Class_EXPSPACE|EXPSPACE]] contains [[Class_MAEXP|MAEXP]], it's easy to see that PSPACE/rpoly = [[Class_PSPACE/poly|PSPACE/poly]] and EXPSPACE/rpoly = EXPSPACE/poly are not [[Class_ALL|ALL]].



So does [[Class_ALL|ALL]] have no respect for complexity class inclusions at ALL?  (Sorry.)



It is not as contradictory as it first seems.  The deterministic base class in all of these examples is modified by computational non-determinism after it is modified by advice.  For example, MA,,EXP,,/rpoly means M(A,,EXP,,/rpoly), while (MA,,EXP,,)/rpoly equals MA,,EXP,,/poly by a standard argument.  In other words, it's only the verifier, not the prover or post-selector, who receives the randomized or quantum advice. The prover knows a description of the advice state, but not its measured values.  Modification by /rpoly does preserve class inclusions when it is applied after other changes.
== Relations ==


== See Also ==

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

== Comments ==

[[Class_ALOGTIME|ALOGTIME]] is the class of languages decidable in logarithmic time by a random access alternating Turing machine.



Known to be equal to U,,E^*^,,-uniform [[Class_NC1|NC1]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a "yes" answer can be verified by an Arthur-Merlin protocol, as follows.



Arthur, a [[Class_BPP|BPP]] (i.e. probabilistic polynomial-time) verifier, generates a "challenge" based on the input, and sends it together with his random coins to Merlin.  Merlin sends back a response, and then Arthur decides whether to accept.  Given an algorithm for Arthur, we require that



If the answer is "yes," then Merlin can act in such a way that Arthur accepts with probability at least 2/3 (over the choice of Arthur's random bits).

If the answer is "no," then however Merlin acts, Arthur will reject with probability at least 2/3.



Surprisingly, it turns out that such a system is just as powerful as a private-coin one, in which Arthur does not need to send his random coins to Merlin [[ZooRefs#GS86|[GS86] ]].  So, Arthur never needs to hide information from Merlin.



Furthermore, define AM[k] similarly to [[Class_AM|AM]], except that Arthur and Merlin have k rounds of interaction.  Then for all constant k>2, AM[k] = AM[2] = [[Class_AM|AM]] [[ZooRefs#BM88|[BM88] ]].  Also, the result of [[ZooRefs#GS86|[GS86] ]] can then be stated as follows: IP[k] is contained in AM[k+2] for every k (constant or non-constant).



[[Class_AM|AM]] contains graph nonisomorphism.



Contains [[Class_NP|NP]], [[Class_BPP|BPP]], and [[Class_SZK|SZK]], and is contained in [[Class_Π2P|Π2P]] and [[Class_NP/poly|NP/poly]].



If [[Class_AM|AM]] contains [[Class_coNP|coNP]] then [[Class_PH|PH]] collapses to [[Class_Σ2P|Σ2P]] ∩ [[Class_Π2P|Π2P]] [[ZooRefs#BHZ87|[BHZ87] ]].



There exists an oracle relative to which [[Class_AM|AM]] is not contained in [[Class_PP|PP]] [[ZooRefs#Ver92|[Ver92] ]].



[[Class_AM|AM]] = [[Class_NP|NP]] under a strong derandomization assumption: namely that some language in [[Class_NE|NE]] ∩ [[Class_coNE|coNE]] requires nondeterministic circuits of size 2^Ω(n)^ ([[ZooRefs#MV99|[MV99] ]], improving [[ZooRefs#KM99|[KM99] ]]).  (A nondeterministic circuit C has two inputs, x and y, and accepts on x if there exists a y such that C(x,y)=1.)
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which both "yes" and "no" answers can be verified by an [[Class_AM|AM]] protocol.



If [[Class_EXP|EXP]] requires exponential time even for [[Class_AM|AM]] protocols, then [[Class_AM|AM]] ∩ [[Class_coAM|coAM]] = [[Class_NP|NP]] ∩ [[Class_coNP|coNP]] [[ZooRefs#GST03|[GST03] ]].



There exists an oracle relative to which [[Class_AM|AM]] ∩ [[Class_coAM|coAM]] is not contained in [[Class_PP|PP]] [[ZooRefs#Ver95|[Ver95] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_AM|AM]], except that Arthur is exponential-time and can exchange exponentially long messages with Merlin.



Contains [[Class_MAEXP|MAEXP]], and is contained in [[Class_EH|EH]] and indeed [[Class_S2-EXP•PNP|S2-EXP•PNP]].



If [[Class_coNP|coNP]] is contained in [[Class_AM[polylog]|AM[polylog]]] then [[Class_EH|EH]] collapses to [[Class_AMEXP|AMEXP]] [[ZooRefs#PV04|[PV04] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_AM|AM]], except that we allow polylog(n) rounds of interaction between Arthur and Merlin instead of a constant number.



Not much is known about [[Class_AM[polylog]|AM[polylog]]] -- for example, whether it sits in [[Class_PH|PH]].  However, [[ZooRefs#SS04|[SS04] ]] show that if [[Class_AM[polylog]|AM[polylog]]] contains [[Class_coNP|coNP]], then [[Class_EH|EH]] collapses to [[Class_S2-EXP•PNP|S2-EXP•PNP]].  ([[ZooRefs#PV04|[PV04] ]] improved the collapse to AM,,EXP,,.)
== Relations ==


== See Also ==

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

== Comments ==

An alternating Turing machine is a nondeterministic machine with two kinds of states, AND states and OR states.  It accepts if and only if the tree of all computation paths, considered as an AND-OR tree, evaluates to 1.  (Here 'Accept' corresponds to 1 and 'Reject' to 0.)



Then [[Class_AP|AP]] is the class of decision problems solvable in polynomial time by an alternating Turing machine.



[[Class_AP|AP]] = [[Class_PSPACE|PSPACE]] [[ZooRefs#CKS81|[CKS81] ]].



The abbreviation [[Class_AP|AP]] is also used for Approximable in Polynomial Time, see [[Class_AxP|AxP]].
== Relations ==


== See Also ==

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

== Comments ==

Roughly, the class of decision problems for which the following holds.  For all polynomials p(n), there exist [[Class_GapP|GapP]] functions f and g such that for all inputs x with n=|x|,



If the answer is "yes" then 1 > f(x)/g(1^n^) > 1-2^-p(n)^.

If the answer is "no" then 0 < f(x)/g(1^n^) < 2^-p(n)^.



Defined in [[ZooRefs#Li93|[Li93] ]], where the following was also shown:



[[Class_APP|APP]] is contained in [[Class_PP|PP]], and indeed is low for [[Class_PP|PP]].

[[Class_APP|APP]] is closed under intersection, union, and complement.



[[Class_APP|APP]] contains [[Class_AWPP|AWPP]] [[ZooRefs#Fen02|[Fen02] ]].



The abbreviation [[Class_APP|APP]] is also used for Approximable in Probabilistic Polynomial Time, see [[Class_AxPP|AxPP]].
== Relations ==


== See Also ==

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

== Comments ==

The subclass of [[Class_NPO|NPO]] problems that admit constant-factor approximation algorithms.  (I.e., there is a polynomial-time algorithm that is guaranteed to find a solution within a constant factor of the optimum cost.)



Contains [[Class_PTAS|PTAS]].



Equals the closure of [[Class_MaxSNP|MaxSNP]] and of [[Class_MaxNP|MaxNP]] under [[Class_PTAS|PTAS]] reduction [[ZooRefs#KMS+99|[KMS+99] ]], [[ZooRefs#CT94|[CT94] ]].



Defined in [[ZooRefs#ACG+99|[ACG+99] ]].
== Relations ==


== See Also ==

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

== Comments ==

ATIME(f(n)) is the class of problems for which there are alternating Turing machines (see AP) which decide the problem in time bounded by f(n).



In particular, [[Class_AP|AP]] = ATIME(poly(n)).
== Relations ==


== See Also ==

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

== Comments ==

The class of problems decidable by an O(f(n))-space Turing machine with three kinds of quantifiers: existential, universal, and randomized.



Contains [[Class_GAN-SPACE(f(n))|GAN-SPACE(f(n))]].



AUC-SPACE(poly(n)) = [[Class_SAPTIME|SAPTIME]] = [[Class_PSPACE|PSPACE]] [[ZooRefs#Pap83|[Pap83] ]].



[[ZooRefs#Con92|[Con92] ]] shows that AUC-SPACE(log n) has a natural complete problem, and is contained in [[Class_NP|NP]] ∩ [[Class_coNP|coNP]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#OW93|[OW93] ]] to be the class of decision problems that have a good average-case [[Class_BPP|BPP]] algorithm, whenever the input is chosen from an efficiently samplable distribution.



Note that this is not the same as the [[Class_BPP|BPP]] version of [[Class_AvgP|AvgP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that for some polynomial-time computable (i.e. FP) function f,



If the answer is "no," then the difference between the number of accepting and rejecting paths is non-negative and at most 2^-poly(n)^f(x).

If the answer is "yes," then the difference is between (1-2^-poly(n)^)f(x) and f(x).



Defined in [[ZooRefs#FFK94|[FFK94] ]].



Contains [[Class_BQP|BQP]] [[ZooRefs#FR98|[FR98] ]], [[Class_WAPP|WAPP]] [[ZooRefs#BGM02|[BGM02] ]], [[Class_LWPP|LWPP]], and [[Class_WPP|WPP]].



Contained in [[Class_APP|APP]] [[ZooRefs#Fen02|[Fen02] ]].
== Relations ==


== See Also ==

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

== Comments ==

The union of [[Class_AW[t]|AW[t]]] over all t.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_AW[SAT]|AW[SAT]]] but with 'circuit' instead of 'formula.'



Has the same relation to [[Class_AW[SAT]|AW[SAT]]] as [[Class_W[P]|W[P]]] has to [[Class_W[SAT]|W[SAT]]].



Defined in [[ZooRefs#DF99|[DF99] ]].
== Relations ==


== See Also ==

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

== Comments ==

Basically has the same relation to [[Class_W[SAT]|W[SAT]]] as [[Class_PSPACE|PSPACE]] does to [[Class_NP|NP]].



The class of decision problems of the form (x,r,k,,1,,,...,k,,r,,) (r,k,,1,,,...,k,,r,, parameters), that are fixed-parameter reducible to the following problem, for some constant h:



Parameterized QBFSAT: Given a Boolean formula F (with no restriction on depth), over disjoint variable sets S,,1,,,...,S,,r,,.  Does there exist an assignment to S,,1,, of Hamming weight k,,1,,, such that for all assignments to S,,2,, of Hamming weight k,,2,,, etc. (alternating 'there exists' and 'for all'), F is satisfied?



See [[Class_W[1]|W[1]]] for the definition of fixed-parameter reducibility.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contains [[Class_AW[*]|AW[*]]], and is contained in [[Class_AW[P]|AW[P]]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_W[t]|W[t]]] as [[Class_PSPACE|PSPACE]] does to [[Class_NP|NP]].



Same as [[Class_AW[SAT]|AW[SAT]]], except that the formula F can have depth at most t.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contained in [[Class_AW[*]|AW[*]]].
== Relations ==


== See Also ==

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

== Comments ==

The class of multivariate polynomials over the integers that can be evaluated using a polynomial (in the input size n) number of additions, subtractions, and multiplications, together with the constants -1 and 1.  The class is nonuniform, in the sense that the polynomial for each input size n can be completely different.



Named in [[ZooRefs#Imp02|[Imp02] ]], though it has been considered since the 1970's.



If [[Class_P|P]] = [[Class_BPP|BPP]] (or even [[Class_BPP|BPP]] is contained in NE), then either [[Class_NEXP|NEXP]] is not in [[Class_P/poly|P/poly]], or else the permanent polynomial of a matrix is not in [[Class_AlgP/poly|AlgP/poly]] [[ZooRefs#KI02|[KI02] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems that are in NP^A^ with probability 1, where A is an oracle chosen uniformly at random.



Equals [[Class_AM|AM]] [[ZooRefs#NW94|[NW94] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems that are in P^A^ with probability 1, where A is an oracle chosen uniformly at random.



Equals [[Class_BPP|BPP]] [[ZooRefs#BG81|[BG81] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems that are in PSPACE^A^ with probability 1, where A is an oracle chosen uniformly at random.



[[Class_Almost-PSPACE|Almost-PSPACE]] is not known to equal [[Class_PSPACE|PSPACE]] -- rather surprisingly, given the fact that [[Class_PSPACE|PSPACE]] equals BPPSPACE and even [[Class_PPSPACE|PPSPACE]].



What's known is that [[Class_Almost-PSPACE|Almost-PSPACE]] = BP^exp^•PSPACE, where BP^exp^• is like the BP• operator but with exponentially-long strings [[ZooRefs#BVW98|[BVW98] ]].  It follows that [[Class_Almost-PSPACE|Almost-PSPACE]] is contained in NEXP^NP^ ∩ coNEXP^NP^.



Whereas both BP^exp^•PSPACE and BPPSPACE machines are allowed exponentially many random bits, the former has a reusable record of all of these bits on a witness tape, while the latter can only preserve a fraction of them on the work tape.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems such that for some [[Class_#P|#P]] function f(x,0^m^),



The answer on input x is 'yes' if and only if the middle bit of f(x) is 1.

The m bits of f(x) to the left and right of the middle bit are all 0.



Defined in [[ZooRefs#GKR+95|[GKR+95] ]].



Contains [[Class_PH|PH]] and Contained in [[Class_MP|MP]].
== Relations ==


== See Also ==

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

== Comments ==

Similar to [[Class_TreeBQP|TreeBQP]] except that the quantum computer's state at each time step is restricted to being exponentially close to a state in AmpP (that is, a state for which the amplitudes are computable by a classical polynomial-size circuit).



Defined in [Aar03b], where it was also observed that [[Class_AmpP-BQP|AmpP-BQP]] is contained in the third level of [[Class_PH|PH]], just as [[Class_TreeBQP|TreeBQP]] is.
== Relations ==


== See Also ==

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

== Comments ==

Equivalent to [[Class_NAuxPDAp|NAuxPDAp]] without the running-time restriction.



Equals [[Class_P|P]] [Coo71b].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_E|E]] as [[Class_AvgP|AvgP]] does to [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

A distributional problem consists of a decision problem A, and a probability distribution μ over problem instances.



A function f, from strings to integers, is polynomial on μ-average if there exists a constant ε>0 such that the expectation of f^ε^(x) is finite, when x is drawn from μ.



Then (A,μ) is in [[Class_AvgP|AvgP]] if there is an algorithm for A whose running time is polynomial on μ-average.



This convoluted definition is due to Levin [[ZooRefs#Lev86|[Lev86] ]], who realized that simpler definitions lead to classes that fail to satisfy basic closure properties.  Also see [[ZooRefs#Gol97|[Gol97] ]] for more information.



If [[Class_AvgP|AvgP]] = [[Class_DistNP|DistNP]] then [[Class_EXP|EXP]] = [[Class_NEXP|NEXP]] [[ZooRefs#BCG+92|[BCG+92] ]].



Strictly contained in [[Class_HeurP|HeurP]] [[ZooRefs#NS05|[NS05] ]].



See also: [[Class_(NP,P-samplable)|(NP,P-samplable)]].
== Relations ==


== See Also ==

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

== Comments ==

Usually called [[Class_AP|AP]] in the literature.  I've renamed it [[Class_AxP|AxP]] to distinguish it from the "other" [[Class_AP|AP]].



The class of real-valued functions from {0,1}^n^ to [0,1] that can be approximated within any ε>0 by a deterministic Turing machine in time polynomial in n and 1/ε.



Defined by [[ZooRefs#KRC00|[KRC00] ]], who also showed that the set of [[Class_AxP|AxP]] machines is in [[Class_RE|RE]].
== Relations ==


== See Also ==

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

== Comments ==

Usually called [[Class_APP|APP]].  I've renamed it [[Class_AxPP|AxPP]] to distinguish it from the "other" [[Class_APP|APP]].



The class of real-valued functions from {0,1}^n^ to [0,1] that can be approximated within any ε>0 by a probabilistic Turing machine in time polynomial in n and 1/ε.



Defined by [[ZooRefs#KRC00|[KRC00] ]], who also show the following:



Approximating the acceptance probability of a Boolean circuit is AxPP-complete.  The authors argue that this makes [[Class_AxPP|AxPP]] a more natural class than [[Class_BPP|BPP]], since the latter is not believed to have complete problems.

If [[Class_AxPP|AxPP]] = [[Class_AxP|AxP]], then [[Class_BPP|BPP]] = [[Class_P|P]].

On the other hand, there exists an oracle relative to which [[Class_BPP|BPP]] = [[Class_P|P]] but [[Class_AxPP|AxPP]] does not equal [[Class_AxP|AxP]].



[[Class_AxPP|AxPP]] is recursively enumerable [Jeř07].



Interestingly, it is unclear whether the set of [[Class_AxPP|AxPP]] machines is in [[Class_RE|RE]].
== Relations ==


== See Also ==

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

== Comments ==

The smallest class that contains [[Class_NP|NP]] and is closed under union, intersection, and complement.



The levels are defined as follows:



BH,,1,, = [[Class_NP|NP]].

BH,,2i,, is the class of languages that are the intersection of a BH,,2i-1,, language with a [[Class_coNP|coNP]] language.

BH,,2i+1,, is the class of languages that are the union of a BH,,2i,, language with an [[Class_NP|NP]] language.



Then [[Class_BH|BH]] is the union over all i of BH,,i,,.



Defined in [[ZooRefs#WW85|[WW85] ]].



For more detail see [[ZooRefs#CGH+88|[CGH+88] ]].



Contained in [[Class_Δ2P|Δ2P]] and indeed in [[Class_PNP[log]|PNP[log]]].



If [[Class_BH|BH]] collapses at any level, then [[Class_PH|PH]] collapses to Σ,,3,,P [[ZooRefs#Kad88|[Kad88] ]].



See also: [[Class_DP|DP]], [[Class_QH|QH]].



See also: [[Class_QH|QH]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_E|E]] as [[Class_BPP|BPP]] does to [[Class_P|P]].



[[Class_EE|EE]] = [[Class_BPE|BPE]] if and only if [[Class_EXP|EXP]] = [[Class_BPP|BPP]] [[ZooRefs#IKW01|[IKW01] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_EE|EE]] as [[Class_BPP|BPP]] does to [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable in O(f(n))-space with error probability at most 1/3, by a Turing machine that halts on every input and every random tape setting.



Contains [[Class_RHSPACE(f(n))|RHSPACE(f(n))]].



Is contained in DSPACE(f(n)^3/2^) [[ZooRefs#SZ95|[SZ95] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_BPP|BPP]] does to [[Class_P|P]].  The Turing machine has to halt with probability 1 on every input.



Contained in [[Class_SC|SC]] [[ZooRefs#Nis92|[Nis92] ]] and in [[Class_PL|PL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is 'yes' then at least 2/3 of the computation paths accept.

If the answer is 'no' then at most 1/3 of the computation paths accept.



(Here all computation paths have the same length.)



Often identified as the class of feasible problems for a computer with access to a genuine random-number source.



Defined in [[ZooRefs#Gil77|[Gil77] ]].



Contained in [[Class_Σ2P|Σ2P]] ∩ [[Class_Π2P|Π2P]] [[ZooRefs#Lau83|[Lau83] ]], and indeed in ZPP^NP^ [[ZooRefs#GZ97|[GZ97] ]].



If [[Class_BPP|BPP]] contains [[Class_NP|NP]], then [[Class_RP|RP]] = [[Class_NP|NP]] [Ko82,Gil77] and [[Class_PH|PH]] is contained in [[Class_BPP|BPP]] [[ZooRefs#Zac88|[Zac88] ]].



If any problem in [[Class_E|E]] requires circuits of size 2^Ω(n)^, then [[Class_BPP|BPP]] = [[Class_P|P]] [[ZooRefs#IW97|[IW97] ]] (in other words, [[Class_BPP|BPP]] can be derandomized).



Indeed, any proof that [[Class_BPP|BPP]] = [[Class_P|P]] requires showing either that [[Class_NEXP|NEXP]] is not in [[Class_P/poly|P/poly]], or else that [[Class_#P|#P]] requires superpolynomial-size arithmetic circuits [[ZooRefs#KI02|[KI02] ]].



[[Class_BPP|BPP]] is not known to contain complete problems.  [[ZooRefs#Sip82|[Sip82] ]], [[ZooRefs#HH86|[HH86] ]] give oracles relative to which [[Class_BPP|BPP]] has no complete problems.



There exist oracles relative to which [[Class_P|P]] = [[Class_RP|RP]] but still [[Class_P|P]] is not equal to [[Class_BPP|BPP]] [[ZooRefs#BF99|[BF99] ]].



In contrast to the case of [[Class_P|P]], it is unknown whether [[Class_BPP|BPP]] collapses to BPTIME(n^c^) for some fixed constant c.  However, [[ZooRefs#Bar02|[Bar02] ]] and [[ZooRefs#FS04|[FS04] ]] have shown hierarchy theorems for [[Class_BPP|BPP]] with a small amount of advice.



A zero-one law exists stating that [[Class_BPP|BPP]] has p-measure zero unless [[Class_BPP|BPP]] = [[Class_EXP|EXP]] [[ZooRefs#Mel00|[Mel00] ]].



Equals [[Class_Almost-P|Almost-P]].



See also: [[Class_BPPpath|BPPpath]].



If [[Class_BPP|BPP]] contains [[Class_NP|NP]], then [[Class_RP|RP]] = [[Class_NP|NP]] [[ZooRefs#Ko82|[Ko82] ]] and [[Class_PH|PH]] is contained in [[Class_BPP|BPP]] [[ZooRefs#Zac88|[Zac88] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_P-OBDD|P-OBDD]], except that probabilistic transitions are allowed and the OBDD need only accept with probability at least 2/3.



Does not contain the integer multiplication problem [[ZooRefs#AK96|[AK96] ]].



Strictly contained in [[Class_BQP-OBDD|BQP-OBDD]] [[ZooRefs#NHK00|[NHK00] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a [[Class_BPP|BPP]] machine that is given O(log n) advice bits, which can depend on both the machine's random coin flips and the input length n, but not on the input itself.



Defined in [[ZooRefs#TV02|[TV02] ]], where it was also shown that if [[Class_EXP|EXP]] is in [[Class_BPP//log|BPP//log]] then

[[Class_EXP|EXP]] = [[Class_BPP|BPP]], and if [[Class_PSPACE|PSPACE]] is in [[Class_BPP//log|BPP//log]] then [[Class_PSPACE|PSPACE]] = [[Class_BPP|BPP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a semantic [[Class_BPP|BPP]] machine with O(log n) advice bits that depend only on the input length n.  If the advice is good, the output must be correct with probability at least 2/3.  If it is bad, the machine must provide some answer with probability at least 2/3.  See the discussion for [[Class_BQP/poly|BQP/poly]].



Contained in [[Class_BPP/mlog|BPP/mlog]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a syntactic [[Class_BPP|BPP]] machine with O(log n) advice bits that depend only on the input length n.  If the advice is good, the output must be correct with probability at least 2/3.  If it is bad, it need not be.



Contained in [[Class_BPP/rlog|BPP/rlog]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a syntactic [[Class_BPP|BPP]] machine with O(log n) random advice bits whose probability distribution depends only on the input length n.  For each n, there exists good advice such that the output is correct with probability at least 2/3.



Contains [[Class_BPP/mlog|BPP/mlog]].  The inclusion is strict, because [[Class_BPP/rlog|BPP/rlog]] contains any finitely sparse language by fingerprinting; see the discussion for [[Class_ALL|ALL]].



Contained in [[Class_BPP//log|BPP//log]].
== Relations ==


== See Also ==

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

== Comments ==

[[Class_BPP|BPP]] with an oracle that, given a string x, returns the minimum over all programs [[Class_P|P]] that output x,,i,, on input i, of the length of [[Class_P|P]] plus the maximum time taken by [[Class_P|P]] on any input.



A similar class was defined in [[ZooRefs#ABK+02|[ABK+02] ]], where it was also shown that in [[Class_BPPKT|BPPKT]] one can factor, compute discrete logarithms, and more generally invert any one-way function on a non-negligible fraction of inputs.



See also: [[Class_PK|PK]].
== Relations ==


== See Also ==

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

== Comments ==

The analogue of [[Class_Pcc|Pcc]] for bounded-error probabilistic communication complexity.



Does not equal [[Class_Pcc|Pcc]], and is not contained in [[Class_NPcc|NPcc]], because of the EQUALITY problem.



Defined in [[ZooRefs#BFS86|[BFS86] ]].



Has the same relation to [[Class_BPPcc|BPPcc]] and [[Class_BPP|BPP]] as [[Class_Pcc|Pcc]] does to [[Class_Pcc|Pcc]] and [[Class_P|P]].



[[Class_NPcc|NPcc]] is not contained in [[Class_BPPcc|BPPcc]] for  players, for any constant  [[ZooRefs#DP08|[DP08] ]].
== Relations ==


== See Also ==

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

pagename = u"Class_BPPpath"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= BPP,,path,, - Threshold BPP =

== Comments ==

Same as [[Class_BPP|BPP]], except that now the computation paths need not all have the same length.



Defined in [[ZooRefs#HHT97|[HHT97] ]], where the following was also shown:



[[Class_BPPpath|BPPpath]] contains [[Class_MA|MA]] and [[Class_PNP[log]|PNP[log]]], and is contained in [[Class_PP|PP]] and BPP^NP^.

[[Class_BPPpath|BPPpath]] is closed under complementation, intersection, and union.

If [[Class_BPPpath|BPPpath]] = BPP,,path,,^BPP,,path,,^, then [[Class_PH|PH]] collapses to [[Class_BPPpath|BPPpath]].

If [[Class_BPPpath|BPPpath]] contains [[Class_Σ2P|Σ2P]], then [[Class_PH|PH]] collapses to BPP^NP^.



There exists an oracle relative to which [[Class_BPPpath|BPPpath]] is not contained in [[Class_Σ2P|Σ2P]] [[ZooRefs#BGM02|[BGM02] ]].



An alternate characterization of [[Class_BPPpath|BPPpath]] uses the idea of post-selection. That is, [[Class_BPPpath|BPPpath]] is the class of languages  for which there exists a pair of polynomial-time Turing machines  and  such that the following conditions hold for all :



If , .

 If , .

 .



We say that  is the post-selector. Intuitively, this characterization allows a [[Class_BPP|BPP]] machine to require that its random bits have some special but easily verifiable property. This characterization makes the inclusion [[Class_NP|NP]] ⊆ [[Class_BPPpath|BPPpath]] nearly trivial.



See Also: [[Class_PostBQP|PostBQP]] (quantum analogue).



[[Class_BPPpath|BPPpath]] contains [[Class_MA|MA]] and [[Class_PNP[log]|PNP[log]]], and is contained in [[Class_PP|PP]] and BPP^NP^.

[[Class_BPPpath|BPPpath]] is closed under complementation, intersection, and union.

If [[Class_BPPpath|BPPpath]] = BPP,,path,,^BPPpath^, then [[Class_PH|PH]] collapses to [[Class_BPPpath|BPPpath]].

If [[Class_BPPpath|BPPpath]] contains [[Class_Σ2P|Σ2P]], then [[Class_PH|PH]] collapses to BPP^NP^.
== Relations ==


== See Also ==

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

== Comments ==

Equals BPTIME(2^O((log n)^k)^); that is, the class of problems solvable in quasipolynomial-time on a bounded-error machine.



Defined in [[ZooRefs#CNS99|[CNS99] ]], where the following was also shown:



If either (1) [[Class_#P|#P]] does not have a subexponential-time bounded-error algorithm, or (2) [[Class_EXP|EXP]] does not have subexponential-size circuits, then the [[Class_BPQP|BPQP]] hierarchy is strict -- that is, for all a < b at least 1, BPTIME(2^(log n)^a^) is strictly contained in BPTIME(2^(log n)^b^).
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable in O(f(n))-space with error probability at most 1/3, by a Turing machine that halts with probability 1 on every input.



Contains [[Class_RSPACE(f(n))|RSPACE(f(n))]] and [[Class_BPHSPACE(f(n))|BPHSPACE(f(n))]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_BPP|BPP]], but with f(n)-time (for some constructible function f) rather than polynomial-time machines.



Defined in [[ZooRefs#Gil77|[Gil77] ]].



BPTIME(n^log n^) does not equal BPTIME(2^n^ε^) for any ε>0 [[ZooRefs#KV88|[KV88] ]].  Proving a stronger time hierarchy theorem for BPTIME is a longstanding open problem; see [[ZooRefs#BH97|[BH97] ]] for details.



[[ZooRefs#Bar02|[Bar02] ]] has shown the following:



If we allow a small number of advice bits (say log n), then there is a strict hierarchy: for every d at least 1, BPTIME(n^d^)/(log n) does not equal BPTIME(n^d+1^)/(log n).

In the uniform setting, if [[Class_BPP|BPP]] has complete problems then BPTIME(n^d^) does not equal BPTIME(n^d+1^).

BPTIME(n) does not equal [[Class_NP|NP]].



Subsequently, [[ZooRefs#FS04|[FS04] ]] managed to reduce the number of advice bits to only 1: BPTIME(n^d^)/1 does not equal BPTIME(n^d+1^)/1.  They also proved a hierarchy theorem for HeurBPTIME.



For another bounded-error hierarchy result, see [[Class_BPQP|BPQP]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#Weg88|[Weg88] ]].



The class of decision problems solvable by a family of polynomial size branching programs, with the additional condition that each bit of the input is tested at most d times.



[[Class_BPd(P)|BPd(P)]] strictly contains BP,,d-1,,(P), for every d > 1 [[ZooRefs#Tha98|[Tha98] ]].



Contained in [[Class_PBP|PBP]].



See also: [[Class_P-OBDD|P-OBDD]], [[Class_k-PBP|k-PBP]].
== Relations ==


== See Also ==

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

== Comments ==

Equals [[Class_AM|AM]].
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable in polynomial time by a quantum Turing machine, with at most 1/3 probability of error.



One can equivalently define [[Class_BQP|BQP]] as the class of decision problems solvable by a uniform family of polynomial-size quantum circuits, with at most 1/3 probability of error [[ZooRefs#Yao93|[Yao93] ]].  Any universal gate set can be used as a basis; however, a technicality is that the transition amplitudes must be efficiently computable, since otherwise one could use them to encode the solutions to hard problems (see [[ZooRefs#ADH97|[ADH97] ]]).



[[Class_BQP|BQP]] is often identified as the class of feasible problems for quantum computers.



Contains the factoring and discrete logarithm problems [[ZooRefs#Sho97|[Sho97] ]], the hidden Legendre symbol problem [[ZooRefs#DHI02|[DHI02] ]], the Pell's equation and principal ideal problems [[ZooRefs#Hal02|[Hal02] ]], and some other problems not thought to be in [[Class_BPP|BPP]].



Defined in [[ZooRefs#BV97|[BV97] ]], where it is also shown that [[Class_BQP|BQP]] contains [[Class_BPP|BPP]] and is contained in [[Class_P|P]] with a [[Class_#P|#P]] oracle.



BQP^BQP^ = [[Class_BQP|BQP]] [[ZooRefs#BV97|[BV97] ]].



[[ZooRefs#ADH97|[ADH97] ]] showed that [[Class_BQP|BQP]] is contained in [[Class_PP|PP]], and [[ZooRefs#FR98|[FR98] ]] showed that [[Class_BQP|BQP]] is contained in [[Class_AWPP|AWPP]].



There exist oracles relative to which:



[[Class_BQP|BQP]] does not equal to [[Class_BPP|BPP]] [[ZooRefs#BV97|[BV97] ]] (and by similar arguments, is not in P/poly).

[[Class_BQP|BQP]] is not contained in [[Class_MA|MA]] [[ZooRefs#Wat00|[Wat00] ]].

[[Class_BQP|BQP]] is not contained in Mod,,p,,P for prime p [[ZooRefs#GV02|[GV02] ]].

[[Class_NP|NP]], and indeed [[Class_NP|NP]] ∩ [[Class_coNP|coNP]], are not contained in [[Class_BQP|BQP]]  with probability 1 relative to a random oracle and a random permutation oracle, respectively [[ZooRefs#BBB+97|[BBB+97] ]].

[[Class_SZK|SZK]] is not contained in [[Class_BQP|BQP]] [[ZooRefs#Aar02|[Aar02] ]].

[[Class_BQP|BQP]] is not contained in [[Class_SZK|SZK]] (follows easily using the quantum walk problem in [[ZooRefs#CCD+03|[CCD+03] ]]).

[[Class_PPAD|PPAD]] is not contained in [[Class_BQP|BQP]] [[ZooRefs#Li11|[Li11] ]].



[[Class_BQP|BQP]] does not equal [[Class_BPP|BPP]] [[ZooRefs#BV97|[BV97] ]] (and by similar arguments, is not in P/poly).

[[Class_BQP|BQP]] is not contained in [[Class_MA|MA]] [[ZooRefs#Wat00|[Wat00] ]].

[[Class_BQP|BQP]] is not contained in Mod,,p,,P for prime p [[ZooRefs#GV02|[GV02] ]].

[[Class_NP|NP]], and indeed [[Class_NP|NP]] ∩ [[Class_coNP|coNP]], are not contained in [[Class_BQP|BQP]] (in fact, this holds with probability 1 relative to a random oracle and a random permutation oracle, respectively) [[ZooRefs#BBB+97|[BBB+97] ]].

[[Class_SZK|SZK]] is not contained in [[Class_BQP|BQP]] [[ZooRefs#Aar02|[Aar02] ]].

[[Class_BQP|BQP]] is not contained in [[Class_SZK|SZK]] (follows easily using the quantum walk problem in [[ZooRefs#CCD+03|[CCD+03] ]]).
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_P-OBDD|P-OBDD]], except that unitary (quantum) transitions are allowed and the OBDD need only accept with probability at least 2/3.



Strictly contains [[Class_BPP-OBDD|BPP-OBDD]] [[ZooRefs#NHK00|[NHK00] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_BQP/poly|BQP/poly]] except that the advice is O(log n) bits instead of a polynomial number.



Contained in [[Class_BQP/mlog|BQP/mlog]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_BQP/mpoly|BQP/mpoly]] except that the advice is O(log n) bits instead of a polynomial number.



Strictly contained in [[Class_BQP/qlog|BQP/qlog]] [[ZooRefs#NY03|[NY03] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of languages recognized by a syntactic [[Class_BQP|BQP]] machine with deterministic polynomial advice that depends only on the input length, such that the output is correct with probability 2/3 when the advice is good.



Can also be defined as the class of problems solvable by a nonuniform family of polynomial-size quantum circuits, just as [[Class_P/poly|P/poly]] is the class solvable by a nonuniform family of polynomial-size classical circuits.



Referred to with a variety of other ad hoc names, including [[Class_BQP/poly|BQP/poly]] on occassion.



Contains [[Class_BQP/qlog|BQP/qlog]], and is contained in [[Class_BQP/qpoly|BQP/qpoly]].



Does not contain [[Class_ESPACE|ESPACE]] [[ZooRefs#NY03|[NY03] ]].
== Relations ==


== See Also ==

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

== Comments ==

Is to [[Class_BQP/mpoly|BQP/mpoly]] as [[Class_∃BPP|∃BPP]] is to [[Class_MA|MA]].  Namely, the [[Class_BQP|BQP]] machine is required to give some answer with probability at least 2/3 even if the advice is bad.  Even though [[Class_BQP/mpoly|BQP/mpoly]] is a more natural class, [[Class_BQP/poly|BQP/poly]] follows the standard definition of advice as a class operator [[ZooRefs#KL82|[KL82] ]].



Contained in [[Class_BQP/mpoly|BQP/mpoly]] and contains [[Class_BQP/log|BQP/log]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_BQP/mlog|BQP/mlog]] except that the advice is quantum instead of classical.



Strictly contains [[Class_BQP/mlog|BQP/mlog]] [[ZooRefs#NY03|[NY03] ]].



Contained in [[Class_BQP/mpoly|BQP/mpoly]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a [[Class_BQP|BQP]] machine that receives a quantum state ψ,,n,, as advice, which depends only on the input length n.



As with [[Class_BQP/mpoly|BQP/mpoly]], the acceptance probability does not need to be bounded away from 1/2 if the machine is given bad advice. (Thus, we are discussing the class that [[ZooRefs#NY03|[NY03] ]] call BQP/*Qpoly.) Indeed, such a condition would make quantum advice unusable, by a continuity argument.



Does not contain [[Class_EESPACE|EESPACE]] [[ZooRefs#NY03|[NY03] ]].



[Aar04b] shows the following:



There exists an oracle relative to which [[Class_BQP/qpoly|BQP/qpoly]] does not contain [[Class_NP|NP]].

[[Class_BQP/qpoly|BQP/qpoly]] is contained in [[Class_PP/poly|PP/poly]].



A classical oracle separation between [[Class_BQP/qpoly|BQP/qpoly]] and [[Class_BQP/mpoly|BQP/mpoly]] is presently unknown, but there is a quantum oracle separation [[ZooRefs#AK06|[AK06] ]].  An unrelativized separation is too much to hope for, since it would imply that [[Class_PP|PP]] is not contained in [[Class_P/poly|P/poly]].



Contains [[Class_BQP/mpoly|BQP/mpoly]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_BQP|BQP]] with access to two sets of qubits: causality-respecting qubits and CTC qubits.



Defined in [Aar05c], where it was shown that [[Class_PSPACE|PSPACE]] is contained in [[Class_BQPCTC|BQPCTC]], which in turn is contained in [[Class_SQG|SQG]].



See also [[Class_PCTC|PCTC]].
== Relations ==


== See Also ==

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

== Comments ==

Equals [[Class_PSPACE|PSPACE]] and [[Class_PPSPACE|PPSPACE]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_BQP/mpoly|BQP/mpoly]], except that the machine only gets to make nonadaptive queries to whatever oracle it might have.



Defined in [NY03b], where it was also shown that [[Class_P|P]] is not contained in [[Class_BQPtt/poly|BQPtt/poly]] relative to an oracle.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_BQP|BQP]], but with f(n)-time (for some constructible function f) rather than polynomial-time machines.



Defined in [[ZooRefs#BV97|[BV97] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems for which there exists a [[Class_DiffAC0|DiffAC0]] function f such that the answer is "yes" on input x if and only if f(x)=0.



Equals [[Class_TC0|TC0]] and [[Class_PAC0|PAC0]] under logspace uniformity [[ZooRefs#ABL98|[ABL98] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_C=P|C=P]] does to [[Class_P|P]].



C,,=,,L^C=L^ = L^C=L^ [[ZooRefs#ABO99|[ABO99] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that the number of accepting paths exactly equals the number of rejecting paths, if and only if the answer is 'yes.'



Equals [[Class_coNQP|coNQP]] [[ZooRefs#FGH+98|[FGH+98] ]].
== Relations ==


== See Also ==

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

== Comments ==

A comparator gate consists of two inputs and outputs the minimum of its two inputs on its first output wire and outputs the maximum of its two inputs on its second output wire. One important restriction is that each output of a comparator gate has fanout at most one. The Comparator Circuit Value Problem (CCVP) is defined as following. Given a circuit composed of comparator gates, the inputs to the circuit, and one output of the circuit, calculate the value of this output.



[[Class_CC|CC]] is defined as the class of problems log-space many-one reducible to CCVP [[ZooRefs#MS89|[MS89] ]]. At present it is only known that NLCCP [[ZooRefs#MS89|[MS89] ]]. [[Class_CC|CC]] is an example of a complexity class neither known to be in [[Class_NC|NC]] nor P-complete.



Natural complete problems for the [[Class_CC|CC]] class include Stable Marriage Problem, Stable Roommate Problem, Lex-first Maximal Matching [[ZooRefs#Sub94|[Sub94] ]].
== Relations ==


== See Also ==

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

== Comments ==

The set of problems solvable by by constant-depth circuits having only MOD,,m,, gates for constant .



This complexity class entry is a stub. If you feel so inclined, please help out!
== Relations ==


== See Also ==

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

== Comments ==

Does not equal [[Class_QCFL|QCFL]] [[ZooRefs#MC00|[MC00] ]].



Contained in [[Class_LOGCFL|LOGCFL]].



Strictly contains [[Class_DCFL|DCFL]] [[ZooRefs#Bra77|[Bra77] ]] and indeed [[Class_UCFL|UCFL]].



Strictly contains [[Class_DCFL|DCFL]] [[ZooRefs#Bra77|[Bra77] ]].
== Relations ==


== See Also ==

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

== Comments ==

The union of the C,,k,,P's over all constant k.



Contained in [[Class_PSPACE|PSPACE]].



Strictly contains DLOGTIME-uniform [[Class_NC1|NC1]] [[ZooRefs#CMTV98|[CMTV98] ]].



It is an open problem whether there exists an oracle relative to which [[Class_CH|CH]] is infinite, or even unequal to [[Class_PSPACE|PSPACE]].  This is closely related to the problem of whether [[Class_TC0|TC0]] = [[Class_NC1|NC1]], since a padding argument shows that [[Class_TC0|TC0]] = [[Class_NC1|NC1]] implies [[Class_CH|CH]] = [[Class_PSPACE|PSPACE]].



It is an open problem whether there exists an oracle relative to which [[Class_CH|CH]] is infinite, or even unequal to [[Class_PSPACE|PSPACE]].  This is closely related to the problem of whether [[Class_TC0|TC0]] = [[Class_NC1|NC1]].
== Relations ==


== See Also ==

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

pagename = u"Class_CL#P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CL#P - Cluster Sharp-P =

== Comments ==

The class of [[Class_#P|#P]] function problems such that some underlying [[Class_NP|NP]] machine  witnessing membership in [[Class_#P|#P]] has

"clustered" accepting paths. That is:



There exists a polynomial  such that each computation path of  on each input  is exactly  bits long.

There is a length-respecting total order  having polynomial-time computable adjacency checks on the computation paths of .

The accepting paths of  on any input  are contiguous with respect to .



Defined in [[ZooRefs#HHK+05|[HHK+05] ]].
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save CL#P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_CLOG"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= CLOG - Continuous Logarithmic-Time =

== Comments ==

Roughly, the class of continuous problems solvable by an ordinary differential equation (ODE) with convergence time logarithmic in the size of the input.  The vector field of the ODE is specified by an [[Class_NC1|NC1]] formula, with n parameters that represent the input.  The point to which the ODE converges (assuming it does) is the output.



Defined in [[ZooRefs#BSF02|[BSF02] ]], which should be consulted for more details.



[[ZooRefs#BSF02|[BSF02] ]] show that finding the maximum of n integers is in [[Class_CLOG|CLOG]].  Thus, [[Class_CLOG|CLOG]] is best thought of as the continuous-time analog of [[Class_NC1|NC1]], not of DTIME(log n).



Contained in [[Class_CP|CP]].
== Relations ==


== See Also ==

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

== Comments ==

A nondeterministic analog of [[Class_CP|CP]].  Defined in [[ZooRefs#SF98|[SF98] ]], which should be consulted for the definition (it has something to do with strange attractors, I think).



The authors raise the question of whether [[Class_CP|CP]] equals [[Class_CNP|CNP]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_CLOG|CLOG]], except that the convergence time can be polynomial rather than logarithmic in the input size.



Defined in [[ZooRefs#BSF02|[BSF02] ]] and [[ZooRefs#SF98|[SF98] ]].



Finding a maximum flow, which is P-complete, can be done in [[Class_CP|CP]] [[ZooRefs#BSF02|[BSF02] ]].  Based on this the authors argue that "P is contained in CP," but this seems hard to formalize, since [[Class_CP|CP]] is not a complexity class in the usual sense.  They also conjecture that "CP is contained in P" (i.e. the class of ODE's they consider can be integrated efficiently on a standard Turing machine), but this is open.



Contained in [[Class_CNP|CNP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a (nonuniform) family of Boolean circuits of size O(f(n)).



So for example, CSIZE(poly(n)) (the union of CSIZE(n^k^) over all k) equals [[Class_P/poly|P/poly]].



Defined in [[ZooRefs#SM02|[SM02] ]] among other places.
== Relations ==


== See Also ==

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

== Comments ==

The class of languages generated by context-sensitive grammars.



Equals NSPACE(n) [[ZooRefs#Kur64|[Kur64] ]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#FV93|[FV93] ]] as the class of languages corresponding to fixed templates (where a template is a set of allowed constraints on values and variables) in the general Constraint Satisfaction Problem. Under this construction, 3SAT may be expressed as the fixed template (over the alphabet ) containing :



For example, a 3SAT clause  is represented in the [[Class_CSP|CSP]] construction as . By similar constructions, any k-SAT problem can be seen to be in [[Class_CSP|CSP]]. The class also includes Graph k-Coloring (for ), Graph H-Coloring (for some graph ) and Linear Programming mod .



In [[ZooRefs#FV93|[FV93] ]], where the class is defined, the authors show that every problem in [[Class_MMSNP|MMSNP]] is reducible under randomized polynomial-time reductions to a problem in [[Class_CSP|CSP]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_SZK|SZK]], except that now the two distributions are merely required to be computationally indistinguishable by any [[Class_BPP|BPP]] algorithm; they don't have to be statistically close.  (The "two distributions" are (1) the distribution over the verifier's view of their interaction with the prover, conditioned on the verifier's random coins, and (2) the distribution over views that the verifier can simulate without the prover's help.)



Unlike [[Class_SZK|SZK]], it is not known if [[Class_CZK|CZK]] is closed under complement.  [[Class_CZK|CZK]] is now known to share other properties with [[Class_SZK|SZK]]: the verifier may as well be honest and may as well show their coins, and [[Class_CZK|CZK]] is closed under unions [[ZooRefs#Vad06|[Vad06] ]].  (Previously, these properties were only established in the presence of one-way functions [[ZooRefs#GMW91|[GMW91] ]].)



Assuming the existence of one-way functions, [[Class_CZK|CZK]] contains [[Class_NP|NP]] [[ZooRefs#GMW91|[GMW91] ]], and actually equals IP=PSPACE [[ZooRefs#BGG+90|[BGG+90] ]].  However, none of these implications of one-way functions relativize (Impagliazzo, unpublished).



On the other hand, if one-way functions do not exist then [[Class_CZK|CZK]] = [[Class_AVBPP|AVBPP]] [[ZooRefs#OW93|[OW93] ]].



Contains [[Class_PZK|PZK]] and [[Class_SZK|SZK]].



Same as [[Class_SZK|SZK]], except that now the two distributions are merely required to be computationally indistinguishable by any [[Class_BPP|BPP]] algorithm; they don't have to be statistically close.  (The "two distributions" are (1) the distribution over Arthur's view of his interaction with Merlin, conditioned on Arthur's random coins, and (2) the distribution over views that Arthur can simulate without Merlin's help.)



Unlike [[Class_SZK|SZK]], it is not known if [[Class_CZK|CZK]] is closed under complement.  [[Class_CZK|CZK]] is now known to share other properties with [[Class_SZK|SZK]]: the verifier may as well be honest and may as well show his coins, and [[Class_CZK|CZK]] is closed under unions [[ZooRefs#Vad06|[Vad06] ]].  (Previously, these properties were only established in the presence of one-way functions.)



Assuming the existence of one-way functions, [[Class_CZK|CZK]] contains [[Class_NP|NP]] [[ZooRefs#GMW91|[GMW91] ]], and indeed equals IP=PSPACE [[ZooRefs#BGG+90|[BGG+90] ]].  However, none of these implications of one-way functions relativize (Impagliazzo, unpublished).
== Relations ==


== See Also ==

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

== Comments ==

The class of problems such that a polynomial-time program [[Class_P|P]] that allegedly solves them can be checked efficiently.  That is, f is in [[Class_Check|Check]] if there exists a [[Class_BPP|BPP]] algorithm C such that for all programs [[Class_P|P]] and inputs x,



If P(y)=f(y) for all inputs y, then C^P^(x) (C with oracle access to P) accepts with probability at least 2/3.

If P(x) is not equal to f(x) then C^P^(x) accepts with probability at most 1/3.



Introduced in [[ZooRefs#BK89|[BK89] ]], where it was also shown that [[Class_Check|Check]] equals [[Class_frIP|frIP]] ∩ [[Class_cofrIP|cofrIP]].



[[Class_Check|Check]] is contained in [[Class_NEXP|NEXP]] ∩ [[Class_coNEXP|coNEXP]] [[ZooRefs#FRS88|[FRS88] ]].



[[ZooRefs#BG94|[BG94] ]] show that if [[Class_NEE|NEE]] is not contained in [[Class_BPEE|BPEE]] then [[Class_NP|NP]] is not contained in [[Class_Check|Check]].
== Relations ==


== See Also ==

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

== Comments ==

Defined as follows:



C,,0,,P = [[Class_P|P]]

C,,1,,P = [[Class_PP|PP]]

C,,2,,P = PP^PP^

In general, C,,k+1,,P is [[Class_PP|PP]] with [[Class_CkP|CkP]] oracle



The union of the C,,k,,P's is called the counting hierarchy, [[Class_CH|CH]].



Defined in [[ZooRefs#Wag86|[Wag86] ]].



See [[ZooRefs#Tor91|[Tor91] ]] or [[ZooRefs#AW90|[AW90] ]] for more information.
== Relations ==


== See Also ==

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

== Comments ==

The class of problems [[Class_L|L]] that are efficiently autoreducible, in the sense that given an input x and access to an oracle for [[Class_L|L]], a [[Class_BPP|BPP]] machine can compute L(x) by querying [[Class_L|L]] only on points that differ from x.



Defined in [Yao90b].



[[ZooRefs#BG94|[BG94] ]] show that, assuming [[Class_NEE|NEE]] is not contained in [[Class_BPEE|BPEE]], [[Class_Coh|Coh]] ∩ [[Class_NP|NP]] is not contained in any of [[Class_compNP|compNP]], [[Class_Check|Check]], or [[Class_frIP|frIP]].
== Relations ==


== See Also ==

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

pagename = u"Class_D#P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= D#P - Alternate Name for P#P =

== Comments ==


== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save D#P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_DCFL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= DCFL - Deterministic CFL =

== Comments ==

The class of languages accepted by deterministic pushdown automata.



Defined in [[ZooRefs#GG66|[GG66] ]], where it was also shown that [[Class_DCFL|DCFL]] is strictly contained in [[Class_CFL|CFL]], contained in [[Class_UCFL|UCFL]], and strictly contains [[Class_REG|REG]].  The inclusion in [[Class_UCFL|UCFL]] is also strict.



Defined in [[ZooRefs#GG66|[GG66] ]], where it was also shown that [[Class_DCFL|DCFL]] is strictly contained in [[Class_CFL|CFL]] and strictly contains [[Class_REG|REG]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems reducible in [[Class_L|L]] to the problem of computing the determinant of an n-by-n matrix of n-bit integers.



Defined in [[ZooRefs#Coo85|[Coo85] ]].



Contained in [[Class_NC2|NC2]], and contains [[Class_NL|NL]] and [[Class_PL|PL]] [[ZooRefs#BCP83|[BCP83] ]].



Graph isomorphism is hard for [[Class_DET|DET]] under L-reductions [[ZooRefs#Tor00|[Tor00] ]].
== Relations ==


== See Also ==

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

== Comments ==

[[Class_DP|DP]] = BH,,2,,, the second level of the Boolean hierarchy.



Defined in [[ZooRefs#PY84|[PY84] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a [[Class_BQP|BQP]] machine with oracle access to a dynamical simulator. When given a polynomial-size quantum circuit, the simulator returns a sample from the distribution over "classical histories" induced by the circuit. The simulator can adversarially choose any history distribution that satisfies the axioms of "symmetry" and "locality" -- so that the [[Class_DQP|DQP]] algorithm has to work for any distribution satisfying these axioms.



See [[ZooRefs#Aar05|[Aar05] ]] for a full definition.



There it is also shown that [[Class_SZK|SZK]] is contained in [[Class_DQP|DQP]].



Contains [[Class_BQP|BQP]], and is contained in [[Class_EXP|EXP]] [[ZooRefs#Aar05|[Aar05] ]].



There exists an oracle relative to which [[Class_DQP|DQP]] does not contain [[Class_NP|NP]] [[ZooRefs#Aar05|[Aar05] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a Turing machine in space O(f(n)).



The Space Hierarchy Theorem: For constructible f(n) greater than log

n, [[Class_DSPACE(f(n))|DSPACE(f(n))]] is strictly contained in DSPACE(f(n) log(f(n))) [[ZooRefs#HLS65|[HLS65] ]].



For space constructible f(n), strictly contains [[Class_DTIME(f(n))|DTIME(f(n))]] [[ZooRefs#HPV77|[HPV77] ]].



DSPACE(n) does not equal [[Class_NP|NP]] (though we have no idea if one contains the other)!



See also: [[Class_NSPACE(f(n))|NSPACE(f(n))]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a Turing machine in time . Note that some authors choose to call this class TIME.



Of great relevance to DTIME is the Time Hierarchy Theorem: For any constructible function  greater than , DTIME() is strictly contained in DTIME() [[ZooRefs#HS65|[HS65] ]]. As a corollary, [[Class_P|P]] ⊂ [[Class_EXP|EXP]].



For any space constructible , DTIME() is strictly contained in DSPACE() [[ZooRefs#HPV77|[HPV77] ]].



Also, DTIME() is strictly contained in NTIME() [[ZooRefs#PPS+83|[PPS+83] ]] (this result does not work for arbitrary ).



For any constructible superpolynomial , DTIME() with [[Class_PP|PP]] oracle is not in [[Class_P/poly|P/poly]] (see [[ZooRefs#All96|[All96] ]]).



The class of decision problems solvable by a Turing machine in time O(f(n)).



The Time Hierarchy Theorem: For constructible f(n) greater than n, [[Class_DTIME(f(n))|DTIME(f(n))]] is strictly contained in DTIME(f(n) log(f(n)) loglog(f(n))) [[ZooRefs#HS65|[HS65] ]].



For any space constructible f(n), [[Class_DTIME(f(n))|DTIME(f(n))]] is strictly contained in [[Class_DSPACE(f(n))|DSPACE(f(n))]] [[ZooRefs#HPV77|[HPV77] ]].



Also, DTIME(n) is strictly contained in NTIME(n) [[ZooRefs#PPS+83|[PPS+83] ]] (this result does not work for arbitrary f(n)).



For any constructible superpolynomial f(n), [[Class_DTIME(f(n))|DTIME(f(n))]] with [[Class_PP|PP]] oracle is not in [[Class_P/poly|P/poly]] (see [[ZooRefs#All96|[All96] ]]).
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a Turing machine that uses time O(t(n)) and space O(s(n)) simultaneously.



Thus [[Class_SC|SC]] = DTISP(poly,polylog) for example.



Defined in [[ZooRefs#Nis92|[Nis92] ]], where it was also shown that for all space-constructible s(n)=Ω(log n), BPSPACE(s(n)) is contained in DTISP(2^O(s(n))^,s^2^(n)).
== Relations ==


== See Also ==

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

== Comments ==

The class of functions from {0,1}^n^ to integers expressible as the difference of two [[Class_#AC0|#AC0]] functions.



Equals [[Class_GapAC0|GapAC0]] under logspace uniformity [[ZooRefs#ABL98|[ABL98] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of pairs (A,B), where A and B are [[Class_NP|NP]] problems whose sets of "yes" instances are nonempty and disjoint.



If there exists an optimal propositional proof system, then [[Class_DisNP|DisNP]] has a complete pair [[ZooRefs#Raz94|[Raz94] ]].  On the other hand, there exists an oracle relative to which [[Class_DisNP|DisNP]] does not have a complete pair [[ZooRefs#GSS+03|[GSS+03] ]].



If [[Class_P|P]] does not equal [[Class_UP|UP]], then [[Class_DisNP|DisNP]] contains pairs not separated by any set in [[Class_P|P]] [[ZooRefs#GS88|[GS88] ]].  On the other hand, there exists an oracle relative to which [[Class_P|P]] does not equal [[Class_NP|NP]] but still [[Class_DisNP|DisNP]] does not contain any P-inseparable pairs [[ZooRefs#HS92|[HS92] ]].
== Relations ==


== See Also ==

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

== Comments ==

(also called (NP,P-computable) or RNP)



A distributional problem consists of a decision problem A, and a probability distribution μ over problem instances.



(A,μ) is in [[Class_DistNP|DistNP]] if A is in [[Class_NP|NP]], and μ is P-computable (meaning that its cumulative density function can be evaluated in polynomial time).



[[Class_DistNP|DistNP]] has complete problems [[ZooRefs#Lev86|[Lev86] ]] (see also [[ZooRefs#Gur87|[Gur87] ]]), although unlike for [[Class_NP|NP]] this is not immediate.



Any DistNP-complete problem is also complete for [[Class_(NP,P-samplable)|(NP,P-samplable)]] [[ZooRefs#IL90|[IL90] ]].



[[Class_DistNP|DistNP]] has complete problems [[ZooRefs#Gur87|[Gur87] ]], although unlike for [[Class_NP|NP]] this is not immediate.
== Relations ==


== See Also ==

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

== Comments ==

The class of dynamic problems solvable using first-order predicates.



Basically what this means is that an algorithm maintains some polynomial-size data structure (say a graph), and receives a sequence of updates (add this edge, delete that one, etc.).  For each update, it computes a new value for the data structure in [[Class_FO|FO]] -- that is, for each bit of the data structure, there is an [[Class_FO|FO]] function representing the new value of that bit, which takes as input both the update and the previous value of the data structure.  At the end the algorithm needs to answer some question (i.e. is the graph connected?).



See [[ZooRefs#HI02|[HI02] ]] for more information, and a complete problem for [[Class_Dyn-FO|Dyn-FO]].



See also [[Class_Dyn-ThC0|Dyn-ThC0]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_Dyn-FO|Dyn-FO]], except that now updates are computed via constant-depth predicates that have "COUNT" available, in addition to AND, OR, and NOT -- so it's a uniform version of [[Class_TC0|TC0]] rather than of [[Class_AC0|AC0]].



See [[ZooRefs#HI02|[HI02] ]] for more information.
== Relations ==


== See Also ==

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

== Comments ==

Equals DTIME(2^O(n)^).



Does not equal [[Class_NP|NP]] [[ZooRefs#Boo72|[Boo72] ]] or [[Class_PSPACE|PSPACE]] [[ZooRefs#Boo74|[Boo74] ]] relative to any oracle.  However, there is an oracle relative to which [[Class_E|E]] is contained in [[Class_NP|NP]] (see ZPP), and an oracle relative to [[Class_PSPACE|PSPACE]] is contained in [[Class_E|E]] (by equating the former with P).



There exists a problem that is complete for [[Class_E|E]] under polynomial-time Turing reductions but not polynomial-time truth-table reductions [[ZooRefs#Wat87|[Wat87] ]].



Problems hard for [[Class_BPP|BPP]] under Turing reductions have measure 1 in [[Class_E|E]] [[ZooRefs#AS94|[AS94] ]].



It follows that, if the problems complete for [[Class_E|E]] under Turing reductions do not have measure 1 in [[Class_E|E]], then [[Class_BPP|BPP]] does not equal [[Class_EXP|EXP]].



[[ZooRefs#IT89|[IT89] ]] gave an oracle relative to which [[Class_E|E]] = [[Class_NE|NE]] but still there is an exponential-time binary predicate whose corresponding search problem is not in [[Class_E|E]].



[[ZooRefs#BF03|[BF03] ]] gave a proof that if [[Class_E|E]] = [[Class_NE|NE]], then no sparse set is collapsing, where they defined a set  to be collapsing if  and if for all  such that  and  are Turing reducible to each other,  and  are many-to-one reducible to each other.



Contrast with [[Class_EXP|EXP]].
== Relations ==


== See Also ==

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

== Comments ==

Equals DTIME(2^2^O(n)^^) (though some authors alternatively define it as being equal to DTIME(2^O(2^n^)^)).



[[Class_EE|EE]] = [[Class_BPE|BPE]] if and only if [[Class_EXP|EXP]] = [[Class_BPP|BPP]] [[ZooRefs#IKW01|[IKW01] ]].



Contained in [[Class_EEXP|EEXP]] and [[Class_NEE|NEE]].



Equals DTIME(2^2^O(n)^) (though some authors alternatively define it as being equal to DTIME(2^O(2^n)^)).
== Relations ==


== See Also ==

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

== Comments ==

Equals DTIME(2^2^2^O(n)^^^).



In contrast to the case of [[Class_EE|EE]], it is not known whether [[Class_EEE|EEE]] = [[Class_BPEE|BPEE]] implies [[Class_EE|EE]] = [[Class_BPE|BPE]] [[ZooRefs#IKW01|[IKW01] ]].



Equals DTIME(2^2^2^O(n)^).
== Relations ==


== See Also ==

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

== Comments ==

Equals DSPACE(2^2^O(n)^^).



Is not contained in [[Class_BQP/qpoly|BQP/qpoly]] [[ZooRefs#NY03|[NY03] ]].



Equals DSPACE(2^2^O(n)^).
== Relations ==


== See Also ==

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

== Comments ==

Equals DTIME(2^2^p(n)^^) for p a polynomial.



Also known as 2-EXP.



Contains [[Class_EE|EE]], and is contained in [[Class_NEEXP|NEEXP]].



Equals DTIME(2^2^p(n)^) for p a polynomial.
== Relations ==


== See Also ==

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

== Comments ==

Has roughly the same relationship to [[Class_E|E]] as [[Class_PH|PH]] does to [[Class_P|P]].



More formally, [[Class_EH|EH]] is defined as the union of [[Class_E|E]], [[Class_NE|NE]], NE^NP^, [[Class_NE|NE]] with [[Class_Σ2P|Σ2P]] oracle, and so on.



See [[ZooRefs#Har87|[Har87] ]] for more information.



If [[Class_coNP|coNP]] is contained in [[Class_AM[polylog]|AM[polylog]]], then [[Class_EH|EH]] collapses to [[Class_S2-EXP•PNP|S2-EXP•PNP]] [[ZooRefs#SS04|[SS04] ]] and indeed [[Class_AMEXP|AMEXP]] [[ZooRefs#PV04|[PV04] ]].



On the other hand, [[Class_coNE|coNE]] is contained in [[Class_NE/poly|NE/poly]], so perhaps it wouldn't be so surprising if [[Class_NE|NE]] collapses.



There exists an oracle relative to which [[Class_EH|EH]] does not contain [[Class_SEH|SEH]] [[ZooRefs#Hem89|[Hem89] ]]. [[Class_EH|EH]] and [[Class_SEH|SEH]] are incomparable for all anyone knows.
== Relations ==


== See Also ==

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

== Comments ==

Equals the union of DTIME(2^n^), DTIME(2^2^n^^), DTIME(2^2^2^n^^^), and so on.



Contained in [[Class_PR|PR]].



Equals the union of DTIME(2^n^), DTIME(2^2^n^), DTIME(2^2^2^n^), and so on.
== Relations ==


== See Also ==

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

== Comments ==

An extension of [[Class_LkP|LkP]].



The class of problems A such that Σ,,k,,P^A^ is contained in Σ,,k-1,,P^A,NP^.



Defined in [[ZooRefs#BBS86|[BBS86] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is 'no,' then all computation paths reject.

If the answer is 'yes,' then the number of accepting paths is a power of two.



Contained in [[Class_C=P|C=P]], and in [[Class_ModkP|ModkP]] for any odd k.  Contains [[Class_UP|UP]].



Defined in [[ZooRefs#BHR00|[BHR00] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of optimization problems such that, given an instance of length n, we can find a solution within a factor 1+ε of the optimum in time f(ε)p(n), where p is a polynomial and f is arbitrary.



Contains [[Class_FPTAS|FPTAS]] and is contained in [[Class_PTAS|PTAS]].



Defined in [[ZooRefs#CT97|[CT97] ]], where the following was also shown:



If [[Class_FPT|FPT]] = [[Class_XPuniform|XPuniform]] then [[Class_EPTAS|EPTAS]] = [[Class_PTAS|PTAS]].

If [[Class_EPTAS|EPTAS]] = [[Class_PTAS|PTAS]] then [[Class_FPT|FPT]] = [[Class_W[P]|W[P]]].

If [[Class_FPT|FPT]] is strictly contained in [[Class_W[1]|W[1]]], then there is a natural problem that is in [[Class_PTAS|PTAS]] but not in [[Class_EPTAS|EPTAS]].  (See [[ZooRefs#CT97|[CT97] ]] for the statement of the problem, since it's not that natural.)
== Relations ==


== See Also ==

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

== Comments ==

The same as [[Class_BQP|BQP]], except that the quantum algorithm must return the correct answer with probability 1, and run in polynomial time with probability 1.  Unlike bounded-error quantum computing, there is no theory of universal QTMs for exact quantum computing models.  In the original definition in [[ZooRefs#BV97|[BV97] ]], each language in [[Class_EQP|EQP]] is computed by a single QTM, equivalently to a uniform family of quantum circuits with a finite gate set [[Class_K|K]] whose amplitudes can be computed in polynomial time. See [[Class_EQPK|EQPK]].  However, some results require an infinite gate set.  The official definition here is that the gate set should be finite.



Without loss of generality, the amplitudes in the gate set [[Class_K|K]] are algebraic numbers [[ZooRefs#ADH97|[ADH97] ]].



There is an oracle that separates [[Class_EQP|EQP]] from [[Class_NP|NP]] [[ZooRefs#BV97|[BV97] ]], indeed from [[Class_Δ2P|Δ2P]] [[ZooRefs#GP01|[GP01] ]].  There is also an oracle relative to which [[Class_EQP|EQP]] is not in Mod,,p,,P where p is prime [[ZooRefs#GV02|[GV02] ]].  On the other hand, [[Class_EQP|EQP]] is in [[Class_LWPP|LWPP]] [[ZooRefs#FR98|[FR98] ]].



P^||NP[2k]^ is contained in EQP^||NP[k]^, where "||NP[k]" denotes k nonadaptive oracle queries to [[Class_NP|NP]] (queries that cannot depend on the results of previous queries) [[ZooRefs#BD99|[BD99] ]].



See also [[Class_ZBQP|ZBQP]].
== Relations ==


== See Also ==

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

== Comments ==

The set of problems that can be answered by a uniform family of polynomial-sized quantum circuits whose gates are drawn from a set [[Class_K|K]], and that return the correct answer with probability 1, and run in polynomial time with probability 1, and the allowed gates are drawn from a set [[Class_K|K]].  [[Class_K|K]] may be either finite or countable and enumerated.  If S is a ring, the union of [[Class_EQPK|EQPK]] over all finite gate sets [[Class_K|K]] whose amplitudes are in the ring [[Class_R|R]] can be written EQP,,S,,.



Defined in [[ZooRefs#ADH97|[ADH97] ]] in the special case of a finite set of 1-qubit gates controlled by a second qubit.  It was shown there that transcendental gates may be replaced by algebraic gates without decreasing the size of [[Class_EQPK|EQPK]].



[[ZooRefs#FR98|[FR98] ]] show that EQP,,Q,, is in [[Class_LWPP|LWPP]].  The proof can be generalized to any finite, algebraic gate set [[Class_K|K]].



The hidden shift problem for a vector space over Z/2 is in EQP,,Q,, by Simon's algorithm.  The discrete logarithm problem over Z/p is in EQP,,Q-bar,, using infinitely many gates [[ZooRefs#MZ03|[MZ03] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_EQP|EQP]], but with f(n)-time (for some constructible function f) rather than polynomial-time machines.



Defined in [[ZooRefs#BV97|[BV97] ]].
== Relations ==


== See Also ==

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

== Comments ==

Equals DSPACE(2^O(n)^).



If [[Class_E|E]] = [[Class_ESPACE|ESPACE]] then [[Class_P|P]] = [[Class_BPP|BPP]] [[ZooRefs#HY84|[HY84] ]].



Indeed if [[Class_E|E]] has nonzero measure in [[Class_ESPACE|ESPACE]] then [[Class_P|P]] = [[Class_BPP|BPP]] [[ZooRefs#Lut91|[Lut91] ]].



[[Class_ESPACE|ESPACE]] is not contained in [[Class_P/poly|P/poly]] [[ZooRefs#Kan82|[Kan82] ]].



Is not contained in [[Class_BQP/mpoly|BQP/mpoly]] [[ZooRefs#NY03|[NY03] ]].



See also: [[Class_EXPSPACE|EXPSPACE]].
== Relations ==


== See Also ==

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

== Comments ==

Equals the union of DTIME(2^p(n)^) over all polynomials p.



Also equals [[Class_P|P]] with [[Class_E|E]] oracle.



If [[Class_L|L]] = [[Class_P|P]] then [[Class_PSPACE|PSPACE]] = [[Class_EXP|EXP]].



If [[Class_EXP|EXP]] is in [[Class_P/poly|P/poly]] then [[Class_EXP|EXP]] = [[Class_MA|MA]] [[ZooRefs#BFL91|[BFL91] ]].



Problems complete for [[Class_EXP|EXP]] under many-one reductions have measure 0 in [[Class_EXP|EXP]] [[ZooRefs#May94|[May94] ]], [[ZooRefs#JL95|[JL95] ]].



There exist oracles relative to which



[[Class_EXP|EXP]] = [[Class_NP|NP]] = [[Class_ZPP|ZPP]] [Hel84a], [Hel84b], [[ZooRefs#Kur85|[Kur85] ]], [[ZooRefs#Hel86|[Hel86] ]],

[[Class_EXP|EXP]] = [[Class_NEXP|NEXP]] but still [[Class_P|P]] does not equal [[Class_NP|NP]] [[ZooRefs#Dek76|[Dek76] ]],

[[Class_EXP|EXP]] does not equal [[Class_PSPACE|PSPACE]] [[ZooRefs#Dek76|[Dek76] ]].



[[ZooRefs#BT04|[BT04] ]] show the following rather striking result: let A be many-one complete for [[Class_EXP|EXP]], and let S be any set in [[Class_P|P]] of subexponential density.  Then A-S is Turing-complete for [[Class_EXP|EXP]].



[[ZooRefs#SM03|[SM03] ]] show that if [[Class_EXP|EXP]] has circuits of polynomial size, then [[Class_P|P]] can be simulated in [[Class_MAPOLYLOG|MAPOLYLOG]] such that no deterministic polynomial-time adversary can generate a list of inputs for a [[Class_P|P]] problem that includes one which fails to be simulated. As a result, [[Class_EXP|EXP]] ⊆ [[Class_MA|MA]] if [[Class_EXP|EXP]] has circuits of polynomial size.



[[ZooRefs#SU05|[SU05] ]] show that [[Class_EXP|EXP]]  [[Class_NP/poly|NP/poly]] implies [[Class_EXP|EXP]]  P^||NP^/poly.



In descriptive complexity EXPTIME can be defined as SO() which is also SO(LFP)



[[Class_EXP|EXP]] = [[Class_NP|NP]] = [[Class_ZPP|ZPP]] [[ZooRefs#Hel84|[Hel84] ]],

[[Class_EXP|EXP]] = [[Class_NEXP|NEXP]] but still [[Class_P|P]] does not equal [[Class_NP|NP]] [[ZooRefs#Dek76|[Dek76] ]],

[[Class_EXP|EXP]] does not equal [[Class_PSPACE|PSPACE]] [[ZooRefs#Dek76|[Dek76] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable in [[Class_EXP|EXP]] with the help of a polynomial-length advice string that depends only on the input length.



Contains [[Class_BQP/qpoly|BQP/qpoly]] [Aar04b].
== Relations ==


== See Also ==

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

== Comments ==

Equals the union of DSPACE(2^p(n)^) over all polynomials p.



See also: [[Class_ESPACE|ESPACE]].



Given a first-order statement about real numbers, involving only addition and comparison (no multiplication), we can decide in [[Class_EXPSPACE|EXPSPACE]] whether it's true or not [[ZooRefs#Ber80|[Ber80] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems that can be proven to be solvable in O(f(n)) space on a deterministic Turing machine, from the axioms of formal system F.



Defined in [[ZooRefs#Har78|[Har78] ]].



See also [[Class_F-TIME(f(n))|F-TIME(f(n))]].  The results about F-TAPE mirror those about F-TIME, but in some cases are sharper.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems that can be proven to be solvable in O(f(n)) time on a deterministic Turing machine, from the axioms of formal system F.



Defined in [[ZooRefs#Har78|[Har78] ]], where the following was also shown:



If [[Class_F-TIME(f(n))|F-TIME(f(n))]] = [[Class_DTIME(f(n))|DTIME(f(n))]], then [[Class_DTIME(f(n))|DTIME(f(n))]] is strictly contained in DTIME(f(n)g(n)) for any nondecreasing, unbounded, recursive g(n).

There exist recursive, monotonically increasing f(n) such that [[Class_F-TIME(f(n))|F-TIME(f(n))]] is strictly contained in [[Class_DTIME(f(n))|DTIME(f(n))]].



See also [[Class_F-TAPE(f(n))|F-TAPE(f(n))]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_BQP|BQP]] as [[Class_FNP|FNP]] does to [[Class_NP|NP]].



There exists an oracle relative to which [[Class_PLS|PLS]] is not contained in [[Class_FBQP|FBQP]] [[ZooRefs#Aar03|[Aar03] ]].
== Relations ==


== See Also ==

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

== Comments ==

FH,,k,, is the class of problems solvable by a uniform family of polynomial-size quantum circuits, with k levels of Hadamard gates and all other gates preserving the computational basis.  (Conditional phase flip gates are fine, for example.)  Thus



FH,,0,, = [[Class_P|P]]

FH,,1,, = [[Class_BPP|BPP]]

FH,,2,, contains factoring because of Kitaev's phase estimation algorithm



It is an open problem to show that the Fourier hierarchy is infinite relative to an oracle (that is, FH,,k,, is strictly contained in FH,,k+1,,).



Defined in [[ZooRefs#Shi03|[Shi03] ]].



FH,,0,, = [[Class_P|P]]

FH,,1,, = [[Class_BPP|BPP]]

FH,,2,, contains factoring, because of Kitaev's phase estimation algorithm
== Relations ==


== See Also ==

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

== Comments ==

The class of fixed point problems. In the framework of fixed point problems, an instance I is associated with a (continuous) function F,,I,,, and a solution of I is a fixed point of F,,I,,.



Properties of [[Class_FIXP|FIXP]] problems:



the function F,,I,, is represented by an algebraic circuit over {+, -, *, /, max, min} with rational constants

 there is a polynomial time algorithm that computes the circuit from I.



Every [[Class_FIXP|FIXP]] problem has Partial Computation, Decision, (Strong) Approximation, and Existence counterparts; these can all be solved in [[Class_PSPACE|PSPACE]].



The Nash equilibrium problem for 3 or more players is FIXP-complete.



Linear-FIXP = [[Class_PPAD|PPAD]].



Defined in [[ZooRefs#EY07|[EY07] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_NL|NL]] as [[Class_FNP|FNP]] does to [[Class_NP|NP]].



Defined by [[ZooRefs#AJ93|[AJ93] ]], who also showed that if [[Class_NL|NL]] = [[Class_UL|UL]], then [[Class_FNL|FNL]] is contained in [[Class_#L|#L]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_FNL|FNL]] as [[Class_P/poly|P/poly]] does to [[Class_P|P]].



Contained in [[Class_#L/poly|#L/poly]] [[ZooRefs#RA00|[RA00] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of function problems of the following form:



Given an input x and a polynomial-time predicate F(x,y), if there exists a y satisfying F(x,y) then output any such y, otherwise output 'no.'



[[Class_FNP|FNP]] generalizes [[Class_NP|NP]], which is defined in terms of decision problems only.



Actually the word "function" is misleading, since there could be many valid outputs y.  That's unavoidable, since given a predicate F there's no "syntactic" criterion ensuring that y is unique.



[[Class_FP|FP]] = [[Class_FNP|FNP]] if and only if [[Class_P|P]] = [[Class_NP|NP]].



Contains [[Class_TFNP|TFNP]].



A basic question about [[Class_FNP|FNP]] problems is whether they're self-reducible; that is, whether they reduce to the corresponding [[Class_NP|NP]] decision problems.  Although this is true for all [[Class_NPC|NPC]] problems, [[ZooRefs#BG94|[BG94] ]] shows that if [[Class_EE|EE]] does not equal [[Class_NEE|NEE]], then there is a problem in [[Class_NP|NP]] such that no corresponding [[Class_FNP|FNP]] problem can be reduced to it.  [[ZooRefs#BG94|[BG94] ]] cites Impagliazzo and Sudan as giving the same conclusion under the assumption that [[Class_NE|NE]] does not equal [[Class_coNE|coNE]].
== Relations ==


== See Also ==

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

== Comments ==

First order logic is the smallest logical class of logic language. It is the base of Descriptive complexity and equal to the class [[Class_AC0|AC0]] and to [[Class_AH|AH]], the alternating logtime hierarchy.



When we use logic formalism, the input is a structure, usually it is either strings (of bits or over an alphabet) whose elements are position of the strings, or graphs whose elements are vertices. The mesure of the input will there be the size of the structure.

Whatever the structure is, we can suppose that there are relation that you can test, by example  is true iff there is an edge from  to  if the structure is a graph, and  is true iff the nth letter of the string is 1. We also have constant, who are special elements of the structure, by example if we want to check reachability in a graph, we will have to choose two constant s and t.



In descriptive complexity we almost always suppose that there is a total order over the elements and that we can check equality between elements. This let us consider elements as number,  is the number  iff there is  elements  such that . Thanks to this we also want the primitive "bit", where  is true if only the th bith of  is 1. (We can replace  by plus and time, ternary relation such that  is true iff  and  is true iff ).



Since in a computer elements are only pointers or string of bit, thoses assumptions make sens, and those primitive function can be calculated in most of the small complexity classes. We can also imagine [[Class_FO|FO]] without those primitives, which gives us smaller complexity classes.



The language [[Class_FO|FO]] is then defined as the closure by conjunction ( ), negation () and universal quantification () over element of the structures. We also often use existantial quantification () and disjunction () but those can be defined thanks to the 3 first symbols.



The semantics of the formulae in [[Class_FO|FO]] is straightforward,  is true iff  is false,  is true iff  is true and  is true, and () is true iff whatever element we decide that  is we can choose,  is true.



A querie in [[Class_FO|FO]] will then be to check if a [[Class_FO|FO]] formulae is true over a given structure, this structure is the input of the problem. One should not confuse this kind of problem with checking if a quantified boolean formula is true, which is the definition of QBF, which is Pspace-complete. The difference between those two problem is that in QBF the size of the problem is the size of the formula and elements are just boolean value, whereas in [[Class_FO|FO]] the size of the problem is the size of the structure and the formula is fixed.



Every formulae is equivalent to a formulae in prenexe normal form where we put recursively every quantifier and then a quantifier-free formulae.
== Relations ==


== See Also ==

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

== Comments ==

[[Class_FO(DTC)|FO(DTC)]] is defined as FO(tc) where the transitive closure operator is deterministic, which means that when we apply DTC(), we know that for all , there exist at most one  such that phi(u,v).



We can suppose that DTC() is syntactic sugar for TC() where .



It was shown in [[ZooRefs#Imm99|[Imm99] ]] page 144 that this class is equal to [[Class_L|L]].
== Relations ==


== See Also ==

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

== Comments ==

[[Class_FO(LFP)|FO(LFP)]] is the set of boolean queries definable with first-order fixed-point formulae where the partial fixed point is limited to be monotone, which means that if the second order variable is , then  always implies .



We can obtain the monotony by restricting the formula  to have only positive occurrences of  (i.e. there is an even number of negations before every occurrence of ). We can also describe LFP() as syntactic sugar of PFP() where .



Thanks to monotonicity we only add and never remove vectors to the truth table of , and since there is only  possible vectors we always find a fixed point before  iterations. Hence it was shown in [[ZooRefs#Imm82|[Imm82] ]] that FO(LFP)=P. This definition is equivalent to FO().
== Relations ==


== See Also ==

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

== Comments ==

FO(pfp) is the set of boolean queries definable with first-order formulae with a partial fixed point operator.



Let  be an integer,   vectors of  variables,  a second-order variable of arity , and  a [[Class_FO(PFP)|FO(PFP)]] function using  and  as variables, then we can define iteratively  such that  and  which means that the property  is true on the input  if  is true on input , and when the variable  is replaced by . Then, either there is a fixed point, or the list of  is looping.



PFP( is defined as the value of the fixed point of  on y if there is a fixed point, else as false.



Since s are property of arity , there is at most  values for the s, so with a poly-space counter we can check if there is a loop or not.



It was proved in [[ZooRefs#Imm98|[Imm98] ]] that FO(pfp) is equal to [[Class_PSPACE|PSPACE]].
== Relations ==


== See Also ==

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

== Comments ==

[[Class_FO(TC)|FO(TC)]] is the set of boolean queries definable with first-order formulae with a transitive closure (TC) operator.



TC is defined this way: let  be a positiver integer and  be vectors of  variables, then TC( is true if there exist  variables  such that  and for all  . Here,  is a formula over  written in [[Class_FO(TC)|FO(TC)]] and  means that the variables  and  are replaced by  and .



Every formula of TC can be written in a normal form FO( where  is a [[Class_FO|FO]] formula and we suppose that there is an order on the model where variables are quantified, so we can choose the minimum and maximum element.



It was shown in [[ZooRefs#Imm98|[Imm98] ]] page 150 that this class is equal to [[Class_NL|NL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a "yes" answer can be expressed by a first-order logic predicate, with a block of restricted quantifiers repeated t(n) times.  See [[ZooRefs#Imm98|[Imm98] ]] for a full definition.



FO(poly(n)) = [[Class_P|P]] (see [[ZooRefs#Var82|[Var82] ]] for example).



FO(poly(n)) is contained in [[Class_SO-E|SO-E]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a uniform family of polynomial-size, unbounded-fanin, depth O(log log n) circuits with AND, OR, and NOT gates. Equals FO(log log n).



Defined in [[ZooRefs#BKL+00|[BKL+00] ]], where it was also shown that many problems on finite groups are in [[Class_FOLL|FOLL]].



Contains uniform [[Class_AC0|AC0]], and is contained in uniform [[Class_AC1|AC1]].



Is not known to be comparable to [[Class_L|L]] or [[Class_NL|NL]].



The class of decision problems solvable by a nonuniform family of polynomial-size, unbounded-fanin, depth O(loglog n) circuits with AND, OR, and NOT gates.



Contains [[Class_AC0|AC0]], and is contained in [[Class_AC1|AC1]].



Is not known to be comparable to [[Class_L/poly|L/poly]] or [[Class_NL/poly|NL/poly]].
== Relations ==


== See Also ==

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

pagename = u"Class_FO[]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FO[] - Iterated First-Order logic =

== Comments ==

Let  be a function from integers to integers.

 abbreviates  and  abbreviates .



A quantifier block is a list  where the s are quantifier free FO-formulae and each s is either  or .

If  is a quantifier block then  is the block consisting of  iterated copies of . 

Note that there are  quantifiers in the list, but only k variables; each variable is used  times.



[[Class_FO[]|FO[]]] consists of the FO-formulae with quantifier blocks that are iterated  times.



In Descriptive complexity we can see that :



[[Class_FO[]|FO[]]] is equal to fo-uniform AC^i^, and in fact [[Class_FO[]|FO[]]] is fo-uniform [[Class_AC|AC]] of depth 

[[Class_FO[]|FO[]]] is equal to [[Class_NC|NC]]

[[Class_FO[]|FO[]]] is equal to [[Class_P|P]] and [[Class_FO(LFP)|FO(LFP)]]

[[Class_FO[]|FO[]]] is equal to [[Class_PSPACE|PSPACE]] and [[Class_FO(PFP)|FO(PFP)]]
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save FO[] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_FP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= FP - Function Polynomial-Time =

== Comments ==

Sometimes defined as the class of functions computable in polynomial time by a Turing machine.  (Generalizes [[Class_P|P]], which is defined in terms of decision problems only.)



However, if we want to compare [[Class_FP|FP]] to [[Class_FNP|FNP]], we should instead define it as the class of [[Class_FNP|FNP]] problems (that is, polynomial-time predicates P(x,y)) for which there exists a polynomial-time algorithm that, given x, outputs any y such that P(x,y).  That is, there could be more than one valid output, even though any given algorithm only returns one of them.



[[Class_FP|FP]] = [[Class_FNP|FNP]] if and only if [[Class_P|P]] = [[Class_NP|NP]].



If FP^NP^ = [[Class_FPNP[log]|FPNP[log]]] (that is, allowed only a logarithmic number of queries), then [[Class_P|P]] = [[Class_NP|NP]] [[ZooRefs#Kre88|[Kre88] ]].  The corresponding result for [[Class_PNP|PNP]] versus [[Class_PNP[log]|PNP[log]]] is not known, and indeed fails relative to some oracles (see [Har87b]).
== Relations ==


== See Also ==

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

== Comments ==

Given a graph, the problem of outputting the size of its maximum clique is complete for [[Class_FPNP[log]|FPNP[log]]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_FPT|FPT]] as [[Class_RP|RP]] does to [[Class_P|P]].



Defined in [[ZooRefs#AR01|[AR01] ]], where it was shown that, if the Resolution proof system is automatizable (that is, if a refutation can always be found in time polynomial in the length of the shortest refutation), then [[Class_W[P]|W[P]]] is contained in [[Class_FPR|FPR]].



Has the same relation to [[Class_FPT|FPT]] as [[Class_R|R]] does to [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

The subclass of [[Class_#P|#P]] counting problems whose answer, y, is approximable in the following sense.  There exists a randomized algorithm that, with probability at least 1-δ, approximates y to within an ε multiplicative factor in time polynomial in n (the input size), 1/ε, and log(1/δ).



The permanent of a nonnegative matrix is in [[Class_FPRAS|FPRAS]] [[ZooRefs#JSV01|[JSV01] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems of the form (x,k), k a parameter, that are solvable in time f(k)p(|x|), where f is arbitrary and p is a polynomial.



The basic class of the theory of fixed-parameter tractability, as described by Downey and Fellows [[ZooRefs#DF99|[DF99] ]].



To separate [[Class_FPT|FPT]] and W[2], one could show there is no proof system for CNF formulae that admits proofs of size f(k)n^O(1)^, where f is a computable function and n is the size of the formula.



Contained in [[Class_FPTnu|FPTnu]], [[Class_W[1]|W[1]]], and [[Class_FPR|FPR]].



Contains [[Class_FPTAS|FPTAS]] [[ZooRefs#CC97|[CC97] ]], as well as [[Class_FPTsu|FPTsu]].



Contains [[Class_EPTAS|EPTAS]] unless [[Class_FPT|FPT]] = [[Class_W[1]|W[1]]] [[ZooRefs#Baz95|[Baz95] ]].
== Relations ==


== See Also ==

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

== Comments ==

The subclass of [[Class_NPO|NPO]] problems that admit an approximation scheme in the following sense.  For any ε>0, there is an algorithm that is guaranteed to find a solution whose cost is within a 1+ε factor of the optimum cost.  Furthermore, the running time of the algorithm is polynomial in n (the size of the problem) and in 1/ε.



Contained in [[Class_PTAS|PTAS]].



Defined in [[ZooRefs#ACG+99|[ACG+99] ]].



Contained in [[Class_FPT|FPT]] [[ZooRefs#CC97|[CC97] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_FPT|FPT]] except that the algorithm can vary with the parameter k (though its running time must always be O(p(|x|)), for a fixed polynomial p).



An alternate view is that a single algorithm can take a polynomial-length advice string, depending on k.



Defined in [[ZooRefs#DF99|[DF99] ]] (though they did not use our notation).
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_FPT|FPT]] except that f has to be recursive.



Defined in [[ZooRefs#DF99|[DF99] ]] (though they did not use our notation).
== Relations ==


== See Also ==

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

== Comments ==

The class of problems for which the task is to output a quantum certificate for a [[Class_QMA|QMA]] problem, when such a certificate exists.  Thus, the desired output is a quantum state.



Defined in [[ZooRefs#JWB03|[JWB03] ]], where it is also shown that state preparation for 3-local Hamiltonians is FQMA-complete.  The authors also observe that, in contrast to the case of [[Class_FNP|FNP]] versus [[Class_NP|NP]], there is no obvious reduction of [[Class_FQMA|FQMA]] problems to [[Class_QMA|QMA]] problems.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



The number of accepting paths a is bounded by a polynomial in the size of the input x.

For some polynomial-time predicate [[Class_Q|Q]], Q(x,a) is true if and only if the answer is 'yes.'



Also called FewPaths.



Defined in [[ZooRefs#CH89|[CH89] ]].



Contains [[Class_FewP|FewP]], and is contained in P^FewP^ [[ZooRefs#Kob89|[Kob89] ]] and in [[Class_SPP|SPP]] [[ZooRefs#FFK94|[FFK94] ]].



See also the survey [[ZooRefs#Tor90|[Tor90] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NEXP|NEXP]] machine such that, given a "yes" instance, no more than an exponential number of computation paths accept.



Contained in MIP[NP^FewEXP^] (MIP where provers are not unbounded in computational power, but are limited to NP^FewEXP^) [[ZooRefs#AKS+94|[AKS+94] ]].



Alternatively, [[Class_FewEXP|FewEXP]] can refer to the sparsity of accepting paths in a given instance. In [[ZooRefs#AKR+03|[AKR+03] ]], the authors show that the conjectures "FewEXP search instances are EXP-solvable" and "FewEXP decision instances are EXP/poly-solvable" are equivalent. That is, for all [[Class_NEXP|NEXP]] machines , the following conditions are equivalent:



There exists an [[Class_EXP|EXP]] machine  such that if given a string ,  accepts and has exponentially bounded accepting paths, then  produces one such path.

 There exists an [[Class_EXP/poly|EXP/poly]] machine  which accepts a string  if and only  accepts.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is 'no,' then all computation paths reject.

If the answer is 'yes,' then at least one path accepts; furthermore, the number of accepting paths is upper-bounded by a polynomial in n, the size of the input.



Defined in [[ZooRefs#AR88|[AR88] ]].



Is contained in [[Class_⊕P|⊕P]] [[ZooRefs#CH89|[CH89] ]].



There exists an oracle relative to which [[Class_P|P]], [[Class_UP|UP]], [[Class_FewP|FewP]], and [[Class_NP|NP]] are all distinct [[ZooRefs#Rub88|[Rub88] ]].



Also, there exists an oracle relative to which [[Class_FewP|FewP]] does not have a Turing-complete set [[ZooRefs#HJV93|[HJV93] ]].



Contained in [[Class_Few|Few]].



See also the survey [[ZooRefs#Tor90|[Tor90] ]].
== Relations ==


== See Also ==

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

== Comments ==

Can be defined as the class of problems polynomial-time Turing reducible to the Graph Automorphism problem.



Contains [[Class_P|P]] and is contained in [[Class_GI|GI]].



See [[ZooRefs#KST93|[KST93] ]] for much more information about [[Class_GA|GA]].



Can be defined as the class of problems polynomial-time Turing reducible to the problem of deciding whether a given graph has any nontrivial automorphisms.
== Relations ==


== See Also ==

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

== Comments ==

The class of problems decidable by an O(f(n))-space Turing machine with two kinds of quantifiers: existential and randomized.



Contains [[Class_NSPACE(f(n))|NSPACE(f(n))]] and [[Class_BPSPACE(f(n))|BPSPACE(f(n))]], and is contained in [[Class_AUC-SPACE(f(n))|AUC-SPACE(f(n))]].



By linear programming, GAN-SPACE(log n) is contained in [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a "yes" answer can be verified by



guessing s(n) bits, then

verifying the answer in complexity class C.



For example, GC(p(n),P) = [[Class_NP|NP]] where p is a polynomial.



Defined in [[ZooRefs#CC93|[CC93] ]].



Umans [[ZooRefs#Uma98|[Uma98] ]] has shown that given a DNF expression Φ, the Shortest Implicant problem is GC(log^2^n, coNP)-complete.



Umans [[ZooRefs#Uma98|[Uma98] ]] has shown that given a DNF expression Φ, the Shortest Implicant problem (is there a conjunction of at most k negated or non-negated literals that implies Φ?) is GC(log^2^n, coNP)-complete.
== Relations ==


== See Also ==

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

== Comments ==

The class of languages generated by context-sensitive grammars in which the right-hand side of each transformation is either strictly longer than the left-hand side or the left-hand side consists of the start symbol.



Defined in [[ZooRefs#DW86|[DW86] ]] and shown to be contained in [[Class_LOGCFL|LOGCFL]] (and therefore in [[Class_P|P]] among others).



Shown to be equivalent to Acyclic [[Class_CSL|CSL]] in [[ZooRefs#Nie02|[Nie02] ]].



The class of languages generated by context-sensitive grammars in which the right-hand side of each transformation is strictly longer than the left-hand side.



Defined in [[ZooRefs#DW86|[DW86] ]].
== Relations ==


== See Also ==

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

== Comments ==

Can be defined as the class of problems polynomial-time Turing reducible to the Graph Isomorphism problem.



Contains [[Class_GA|GA]] and is contained in [[Class_Δ2P|Δ2P]].



The Graph Isomorphism problem itself (as opposed to the set of problems Turing reducible to Graph Isomorphism) is contained in [[Class_NP|NP]] as well as [[Class_coAM|coAM]] (and indeed SZK).  So in particular, if Graph Isomorphism is NP-complete, then [[Class_PH|PH]] collapses.



See [[ZooRefs#KST93|[KST93] ]] for much more information about [[Class_GI|GI]].



Can be defined as the class of problems polynomial-time Turing reducible to the problem of deciding whether two graphs are isomorphic.



The [[Class_GI|GI]] problem itself (as opposed to the set of problems Turing reducible to GI) is contained in [[Class_NP|NP]] as well as [[Class_coAM|coAM]] (and indeed SZK).  So in particular, if graph isomorphism is NP-complete, then [[Class_PH|PH]] collapses.
== Relations ==


== See Also ==

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

== Comments ==

The class of [[Class_NPO|NPO]] problems which have the property that for all locally optimal solutions, the ratio between the values of the local and global optima is upper-bounded by a constant.



Defined in [[ZooRefs#AP95|[AP95] ]], where it was also shown that [[Class_GLO|GLO]] is strictly contained in [[Class_APX|APX]].



[[ZooRefs#KMS+99|[KMS+99] ]] showed that [[Class_MaxSNP|MaxSNP]] is not contained in [[Class_GLO|GLO]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_PCD(r(n),q(n))|PCD(r(n),q(n))]], except that now the verifier is allowed nonadaptively to query O(q(n)) rounds of the debate, with no restriction on the number of bits it looks at within each round.



Defined in [[ZooRefs#CFL+93|[CFL+93] ]], who also showed that PCD(log n, q(n)) = GPCD(log n, q(n)) for every q(n).
== Relations ==


== See Also ==

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

== Comments ==

(Basically) the class of decision problems of the form (x,k) (k a parameter), that are solvable by a parameterized family of circuits with unbounded fanin and depth t.  A uniformity condition may also be imposed.



Defined in [[ZooRefs#DF99|[DF99] ]], which should be consulted for the full definition.



Uniform G[P] (i.e. with no restriction on depth) is equal to [[Class_FPT|FPT]].
== Relations ==


== See Also ==

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

== Comments ==

The class of functions from {0,1}^n^ to integers computable by constant-depth, polynomial-size arithmetic circuits with addition and multiplication gates and the constants 0, 1, and -1.  (The only difference from [[Class_#AC0|#AC0]] is the ability to subtract, using the constant -1.)



Equals [[Class_DiffAC0|DiffAC0]] under logspace uniformity [[ZooRefs#ABL98|[ABL98] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_GapP|GapP]] does to [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

The class of functions f(x) such that for some [[Class_NP|NP]] machine, f(x) is the number of accepting paths minus the number of rejecting paths.



Equivalently, the closure of the [[Class_#P|#P]] functions under subtraction.



Defined in [[ZooRefs#FFK94|[FFK94] ]] and independently [[ZooRefs#Gup95|[Gup95] ]].
== Relations ==


== See Also ==

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

== Comments ==

High order logic is an extension of Second order, First order where we add quantification over higher order variables.



We define a relation of order  and arity  to be a subset of -tuple of relation of order  and arity . When  it is by extension a first order variable. The quantification of formula in [[Class_HO|HO]] is over a given order (which is a straightforward extension of [[Class_SO|SO]] where we add quantification over constant (first-order variable) and relation (second-order variables). The atomic predicates now can be general application of relation of order  and arity  to  relations of order  and arity  and  test of equality between two relations of the same order and arity.



is the set of formulae with quantification up to order O. (resp. ) is defined as the set of formula in  beginning by an existantial (resp universal) quantifier followed by at most  alternation of quantifiers.



This class was define in [[ZooRefs#HT06|[HT06] ]], and it was proved that  where  is the th level of the polynomial hierarchy.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems that have [[Class_SZK|SZK]] protocols assuming an honest verifier (i.e. one who doesn't try to learn more about the problem by deviating from the protocol).



Equals [[Class_SZK|SZK]] [[ZooRefs#Oka96|[Oka96] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is 'yes,' exactly 1/2 of computation paths accept.

If the answer is 'no,' all computation paths reject.



Significantly, the number of candidate witnesses is restricted to be a power of 2.  (This is implicit if they are binary strings.)



Contained in [[Class_RP|RP]], [[Class_EP|EP]], and [[Class_ModkP|ModkP]] for every odd k.  Contained in [[Class_EQP|EQP]] by the Deutsch-Jozsa algorithm.



Defined in [[ZooRefs#BB92|[BB92] ]], where it was called C,,==,,P[half].  The name used here is from [[ZooRefs#BS00|[BS00] ]].  There it was shown that [[Class_HalfP|HalfP]] is contained in every similar class in which 1/2 is replaced by some other dyadic fraction.
== Relations ==


== See Also ==

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

== Comments ==

The class of problems for which a 1-1/poly(n) fraction of instances are solvable by a [[Class_BPP|BPP]] machine.



[[ZooRefs#FS04|[FS04] ]] showed a strict hierarchy theorem for [[Class_HeurBPP|HeurBPP]]; thus, [[Class_HeurBPP|HeurBPP]] does not equal HeurBPTIME(n^c^) for any fixed c.
== Relations ==


== See Also ==

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

== Comments ==

The class of problems for which a 1-1/poly(n) fraction of instances are solvable by a [[Class_BPTIME(f(n))|BPTIME(f(n))]] machine. Thus, [[Class_HeurBPTIME(f(n))|HeurBPTIME(f(n))]] has the same relationship with BPTIME as HeurDTIME.



Thus [[Class_HeurBPP|HeurBPP]] is the union of HeurBPTIME(n^c^) over all c.



The class of problems for which a 1-1/poly(n) fraction of instances are solvable by a [[Class_BPTIME(f(n))|BPTIME(f(n))]] machine.
== Relations ==


== See Also ==

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

pagename = u"Class_HeurDTIME(f(n))"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HeurDTIME,,,,(f(n)) - Heuristic DTIME =

== Comments ==

For functions  and , we say that tuple , where  is a language and  is a distribution of problem instances, if there exists a heuristic deterministic algorithm  such that for all  in the support of ,  runs in time bounded by  and with failure probability bounded by  [[ZooRefs#BT06|[BT06] ]].
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HeurDTIME(f(n)) because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HeurNTIME"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HeurNTIME,,,, - Heuristic NTIME =

== Comments ==

Defined as Heur,,,,DTIME, but for non-deterministic heuristic algorithms.



[[Class_NP|NP]] is not contained in HeurNTIME,,,,() for any constants  [[ZooRefs#Per07|[Per07] ]].
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save HeurNTIME because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_HeurP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= HeurP - Heuristic P =

== Comments ==

The class of distributional problems solvable by a [[Class_P|P]] machine. Defined in [[ZooRefs#Imp95|[Imp95] ]], though he calls the class HP.



Alternately, [[ZooRefs#BT06|[BT06] ]] define [[Class_HeurP|HeurP]] as being the set of tuples , where  is a language and  is a distribution of problem instances, such that there exists an algorithm  satisfying two properties:



For every , for every  in the support of , and for every ,  runs in time bounded by .

 For every ,  is a heuristic algorithm for  whose error probability is bounded by .
== Relations ==


== See Also ==

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

== Comments ==

The class of distributional problems solvable by a [[Class_PP|PP]] machine. Defined in [[ZooRefs#Ill95|[Ill95] ]], though he calls the class HPP.
== Relations ==


== See Also ==

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

== Comments ==

The class of problems A in [[Class_NP|NP]] such that Σ,,k,,P^A^ = Σ,,k+1,,P; that is, adding A as an oracle increases the power of the k^th^ level of the polynomial hierarchy by a maximum amount.



For all k, H,,k,, is contained in H,,k+1,,.



H,,0,, consists exactly of the problems complete for [[Class_NP|NP]] under Cook reductions.



H,,1,, consists exactly of the problems complete for [[Class_NP|NP]] under strong non-deterministic Turing reductions [[ZooRefs#Sch83|[Sch83] ]].



Defined in [[ZooRefs#Sch83|[Sch83] ]].



See also [[Class_LkP|LkP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems such that, for every n-bit string x, there exists a program A of size O(log n) that, given x as input, "correctly decides" the answer on x in time polynomial in n.  This means:



There exists a polynomial p such that for any input y, A returns either "yes", "no", or "I don't know" in time p(|y|).

Whenever A returns "yes" or "no", it is correct.

A returns either "yes" or "no" on x.



Defined in [[ZooRefs#OKS+94|[OKS+94] ]]; see also [[ZooRefs#LV97|[LV97] ]].



If [[Class_NP|NP]] is contained in [[Class_IC[log,poly]|IC[log,poly]]], then [[Class_P|P]] = [[Class_NP|NP]] [[ZooRefs#OKS+94|[OKS+94] ]].  Indeed, any self-reducible problem in [[Class_IC[log,poly]|IC[log,poly]]] is also in [[Class_P|P]].



Strictly contains [[Class_P/log|P/log]], and is strictly contained in [[Class_P/poly|P/poly]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a "yes" answer can be verified by an interactive proof.  Here a probabilistic polynomial-time verifier sends messages back and forth with an all-powerful prover.  They can have polynomially many rounds of interaction. Given the verifier's algorithm, at the end:



If the answer is "yes," the prover must be able to behave in such a way that the verifier accepts with probability at least 2/3 (over the choice of the verifier's random bits).

If the answer is "no," then however the prover behaves the verifier must reject with probability at least 2/3.



Defined in [[ZooRefs#GMR89|[GMR89] ]], with the motivation of providing a framework for the introduction of zero-knowledge proofs (see the class ZK). Interestingly, the power of general interactive proof systems is not decreased if the verifier is only allowed random queries (i.e., it merely tosses coins and sends any outcome to the prover). The latter model, known as the Arthur-Merlin (or public-coin) model was introduced independently (but later) in [[ZooRefs#Bab85|[Bab85] ]], and a strong equivalent (which preserves the number of rounds) is proved in [[ZooRefs#GS86|[GS86] ]]. 

Often, it is required that the prover can convince the verifier to accept correct assertions with probability 1; this is called perfect completeness.

However, the definitions with one-sided and two-sided error can be shown to be equivalent (see [[ZooRefs#FGM+89|[FGM+89] ]]).



First demonstration to the power of interactive proofs was given by showing that for graph nonisomorphism (a problem not known in NP) has such proofs [[ZooRefs#GMW91|[GMW91] ]]. Five years later is was shown that

[[Class_IP|IP]] contains [[Class_PH|PH]] [[ZooRefs#LFK+90|[LFK+90] ]], and indeed (this was discovered only a few weeks later) equals [[Class_PSPACE|PSPACE]] [[ZooRefs#Sha90|[Sha90] ]].  On the other hand, [[Class_coNP|coNP]] is not contained in [[Class_IP|IP]] relative to a random oracle [[ZooRefs#CCG+94|[CCG+94] ]].



See also: [[Class_MIP|MIP]], [[Class_QIP|QIP]], [[Class_MA|MA]], [[Class_AM|AM]].



The class of decision problems for which a "yes" answer can be verified by an interactive proof.  Here a [[Class_BPP|BPP]] (i.e. probabilistic polynomial-time) verifier sends messages back and forth with an all-powerful prover.  They can have polynomially many rounds of interaction. Given the verifier's algorithm, at the end:



[[Class_IP|IP]] contains [[Class_PH|PH]] [[ZooRefs#LFK+90|[LFK+90] ]], and indeed (this was discovered only a few days later) equals [[Class_PSPACE|PSPACE]] [[ZooRefs#Sha90|[Sha90] ]].  On the other hand, [[Class_coNP|coNP]] is not contained in [[Class_IP|IP]] relative to a random oracle [[ZooRefs#CCG+94|[CCG+94] ]].



See also: [[Class_MIP|MIP]], [[Class_QIP|QIP]], [[Class_MA|MA]], [[Class_AM|AM]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_IP|IP]], except that if the answer is "yes," there need only be a prover strategy that causes the verifier to accept with probability greater than 1/2, while if the answer is "no," then for all prover strategies the verifier accepts with probability less than 1/2.



Defined in [[ZooRefs#CCG+94|[CCG+94] ]], where it was also shown that [[Class_IPP|IPP]] = [[Class_PSPACE|PSPACE]] relative to all oracles.  Since [[Class_IP|IP]] is strictly contained in [[Class_PSPACE|PSPACE]] relative to a random oracle, the authors interpreted this as evidence against the Random Oracle Hypothesis (a slight change in definition can cause the behavior of a class relative to a random oracle to change drastically).



See also: [[Class_PPSPACE|PPSPACE]].
== Relations ==


== See Also ==

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

== Comments ==

Alternate name for [[Class_AM[polylog]|AM[polylog]]].
== Relations ==


== See Also ==

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

== Comments ==

A class of number-theoretic functions, defined as the closure of basic integer arithmetic operations (, as well as constants 0, 1, and projections) under composition and polynomially long sums and products. Defined by [[ZooRefs#Con73|[Con73] ]], who mistakenly claimed it coincides with [[Class_FP|FP]].



Equals U,,D,,-uniform FTC^0^ by [[ZooRefs#Hes01|[Hes01] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a Turing machine restricted to use an amount of memory logarithmic in the size of the input, n.  (The input itself is not counted as part of the memory.)



[[Class_L|L]] is contained in [[Class_P|P]].  [[Class_L|L]] contains [[Class_NC1|NC1]] [[ZooRefs#Bor77|[Bor77] ]], and is contained in generalizations including [[Class_NL|NL]], [[Class_L/poly|L/poly]], [[Class_SL|SL]], [[Class_RL|RL]], [[Class_⊕L|⊕L]], and [[Class_ModkL|ModkL]].



Reingold [[ZooRefs#Rei04|[Rei04] ]] showed that, remarkably, [[Class_L|L]] = [[Class_SL|SL]].  In other words, undirected graph connectivity is solvable in deterministic logarithmic space.



Immerman [[ZooRefs#Imm83|[Imm83] ]] showed that [[Class_L|L]] is the class FO(dtc) of first-order expressible queries with a deterministic transitive closure.



[[Class_L|L]] queries are exactly the one that can be written in a syntactic restriction of  While languages.



[[Class_L|L]] contains [[Class_NC1|NC1]] [[ZooRefs#Bor77|[Bor77] ]], and is contained in generalizations including [[Class_NL|NL]], [[Class_L/poly|L/poly]], [[Class_SL|SL]], [[Class_RL|RL]], [[Class_⊕L|⊕L]], and [[Class_ModkL|ModkL]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_P/poly|P/poly]] does to [[Class_P|P]].



Equals [[Class_PBP|PBP]] [[ZooRefs#Cob66|[Cob66] ]].



Contains [[Class_SL|SL]] [[ZooRefs#AKL+79|[AKL+79] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a nonuniform family of Boolean circuits, with linear size, constant depth and unbounded fanin.



It is equivalent to [[Class_AC0|AC0]] with bounded fanout and it is properly contained in [[Class_AC0|AC0]] [[ZooRefs#CR96|[CR96] ]].
== Relations ==


== See Also ==

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

== Comments ==

A Turing machine with random access owns a special tape where it can write a binary number , and it can query the value of the th bit of the input. Hence any bit of the input can be read in only logtime.



The th level of the Logarithmic Time Hierarchy is the set of languages recognised by alternating Turing machine in logtime with random access and  alternation, begining with existantial state. [[Class_LH|LH]] is the union of all levels and is equal to tothe class [[Class_AC0|AC0]] and to [[Class_FO|FO]] Descriptive complexity.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a deterministic Turing machine in linear time.



Strictly Contained in [[Class_NLIN|NLIN]]. [[ZooRefs#PPS+83|[PPS+83] ]].



Contained in [[Class_NLIN|NLIN]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems reducible in [[Class_L|L]] to the problem of deciding membership in a context-free language.



Equivalently, [[Class_LOGCFL|LOGCFL]] is the class of decision problems solvable by a uniform family of [[Class_AC1|AC1]] circuits, in which no AND gate has fan-in exceeding 2 (see e.g. [[ZooRefs#Joh90|[Joh90] ]], p. 137).



[[Class_LOGCFL|LOGCFL]] is closed under complement [[ZooRefs#BCD+89|[BCD+89] ]].



Contains [[Class_NL|NL]] [[ZooRefs#Sud78|[Sud78] ]].
== Relations ==


== See Also ==

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

== Comments ==

There are several possible definitions of this class; the most common is the class of languages which can be computed in space O(log log n) by a deterministic Turing machine with two-way access to the input. A typical nonregular language in this class has a form such as 00..00a00..01b00..10b00..11a..., with the successive numbers having logarithmic length. It is the smallest of a collection of sublogarithmically bounded space classes, since any smaller space class contains only the regular languages. These and related classes are studied extensively in [[ZooRefs#Szep94|[Szep94] ]] and [[ZooRefs#LiRe93|[LiRe93] ]]. The alternation hierarchy for this class is infinite ([[ZooRefs#BGR93|[BGR93] ]]), and the  and  levels are incomparable unless ; however, the nondeterministic version of the class is closed under complement ([[ZooRefs#Geff91|[Geff91] ]]).



Sublogarithmically-bounded Turing reductions are equivalent to "regular" (constant-bounded) reductions, however ([[ZooRefs#Agr01|[Agr01] ]]).



Note that while there are no decision problems that can be tested in one-way loglog space, there are promise problems which can be so tested, such as Balanced Monotone Boolean Sentence Value [[ZooRefs#Buss91|[Buss91] ]]. Also, the alternation hierarchy over 1-way loglog space still does not collapse.



Obviously contained in [[Class_L|L]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems expressible in logical form as



The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists y such that for all j in S, the predicate φ(I,s,,j,,,x,y,j) holds.  Here x and y are logarithmic-length strings, or equivalently polynomially bounded numbers, and φ is computable in [[Class_P|P]].



LOGNP,,0,, is the subclass in which φ is a first-order predicate without quantifiers and x and y are bounded lists of indices of input bits.  [[Class_LOGNP|LOGNP]] is also the closure of LOGNP,,0,, under many-one reduction.



The motivation is that the analogue of LOGNP,,0,, without the logarithmic bound on |S| is [[Class_SO-E|SO-E]], which by Fagin's theorem equals [[Class_NP|NP]] [[ZooRefs#Fag74|[Fag74] ]].



Defined in [[ZooRefs#PY96|[PY96] ]], where it was also shown that the following problem is complete for [[Class_LOGNP|LOGNP]] under many-one reductions:



Vapnik-Chervonenkis (V-C) Dimension.  Given a family F of subsets of a set U, find a subset of S of U of maximum cardinality, such that every subset of S can be written as the intersection of S with some set in F.



Contains [[Class_LOGSNP|LOGSNP]], and is contained in [[Class_βP|βP]] (indeed β,,2,,P).



The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists y such that for all j, the predicate φ(I,s,,j,,,x,y,j) holds.  Here x and y are logarithmic-length strings, or equivalently polynomially bounded numbers, and φ is computable in [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems expressible in logical form as



The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists j in S such that the predicate φ(I,s,,j,,,x,j) holds.  Here x is a logarithmic-length string, or equivalently a polynomially bounded number, and φ is computable in [[Class_P|P]].



LOGSNP,,0,, is the subclass in which φ is a first-order predicate without quantifiers and x is a bounded lists of indices of input bits.  [[Class_LOGSNP|LOGSNP]] is also the closure of LOGSNP,,0,, under many-one reduction.  See [[Class_LOGNP|LOGNP]] and [[Class_SNP|SNP]] for the motivation.



Defined in [[ZooRefs#PY96|[PY96] ]].



Contained in [[Class_LOGNP|LOGNP]], and therefore [[Class_QPLIN|QPLIN]].



If [[Class_P|P]] = [[Class_LOGSNP|LOGSNP]], then for every constructible f(n) > n, [[Class_NTIME(f(n))|NTIME(f(n))]] is contained in DTIME(g(n)^sqrt(g(n))^), where g(n) = O(f(n) logf(n)) [[ZooRefs#FK97|[FK97] ]].



The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists j such that the predicate φ(I,s,,j,,,x,j) holds.  Here x and y are logarithmic-length strings, or equivalently polynomially bounded numbers, and φ is computable in [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is "no," then the number of accepting computation paths exactly equals the number of rejecting paths.

If the answer is "yes," then the difference of these numbers equals a function f(|x|) computable in polynomial time (i.e. FP).  Here |x| is the length of the input x, and ``polynomial time means polynomial in |x|, the length of x, rather than the length of |x|.



Defined in [[ZooRefs#FFK94|[FFK94] ]], where it was also shown that [[Class_LWPP|LWPP]] is low for [[Class_PP|PP]] and [[Class_C=P|C=P]].  (I.e. adding [[Class_LWPP|LWPP]] as an oracle does not increase the power of these classes.)



Contained in [[Class_WPP|WPP]] and [[Class_AWPP|AWPP]].



Contains [[Class_SPP|SPP]].



Also, contains the graph isomorphism problem [[ZooRefs#KST92|[KST92] ]].



Contains a whole litter of problems for solvable black-box groups: group intersection, group factorization, coset intersection, and double-coset membership [[ZooRefs#Vin04|[Vin04] ]].



Contains a whole litter of problems for solvable black-box groups: group intersection, group factorization, coset intersection, and double-coset membership [[ZooRefs#Vin04|[Vin04] ]]
== Relations ==


== See Also ==

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

== Comments ==

The class of problems A such that Σ,,k,,P^A^ = Σ,,k,,P; that is, adding A as an oracle does not increase the power of the k^th^ level of the polynomial hierarchy.



L,,1,,P = [[Class_NP|NP]] ∩ [[Class_coNP|coNP]].



For all k, L,,k,, is contained in L,,k+1,, and in [[Class_NP|NP]].



Defined in [[ZooRefs#Sch83|[Sch83] ]].



See also [[Class_HkP|HkP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NL|NL]] machine such that



The number of accepting paths on input x is f(x), and

The answer is 'yes' if and only if R(x,f(x))=1, where [[Class_R|R]] is some predicate computable in [[Class_L|L]].



Defined in [[ZooRefs#BDH+92|[BDH+92] ]], where it was also shown that [[Class_LogFew|LogFew]] is contained in [[Class_ModkL|ModkL]] for all k>1.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_FewP|FewP]] but for logspace-bounded (i.e. NL) machines.



Defined in [[ZooRefs#BDH+92|[BDH+92] ]], where it was also shown that [[Class_LogFewNL|LogFewNL]] is contained in [[Class_ModZkL|ModZkL]] for all k>1.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a Merlin-Arthur protocol, which goes as follows.  Merlin, who has unbounded computational resources, sends Arthur a polynomial-size purported proof that the answer to the problem is "yes."  Arthur must verify the proof in [[Class_BPP|BPP]] (i.e. probabilistic polynomial-time), so that



If the answer is "yes," then there exists a proof such that Arthur accepts with probability at least 2/3.

If the answer is "no," then for all proofs Arthur accepts with probability at most 1/3.



An alternative definition requires that if the answer is "yes," then there exists a proof such that Arthur accepts with certainty.  However, the definitions with one-sided and two-sided error can be shown to be equivalent (see [[ZooRefs#FGM+89|[FGM+89] ]]).



Contains [[Class_NP|NP]] and [[Class_BPP|BPP]] 

(in fact also ∃BPP), and is contained in [[Class_AM|AM]] and in [[Class_QMA|QMA]].



Also contained in [[Class_Σ2P|Σ2P]] ∩ [[Class_Π2P|Π2P]].



There exists an oracle relative to which [[Class_BQP|BQP]] is not in [[Class_MA|MA]] [[ZooRefs#Wat00|[Wat00] ]].



Equals [[Class_NP|NP]] under a derandomization assumption: if [[Class_E|E]] requires exponentially-sized circuits, then [[Class_PromiseBPP|PromiseBPP]] = [[Class_PromiseP|PromiseP]], implying that [[Class_MA|MA]] = [[Class_NP|NP]] [[ZooRefs#IW97|[IW97] ]].



Shown in [[ZooRefs#San07|[San07] ]] that MA/1 does not have circuits of size  for any . In the same paper, the result was used to show that MA/1 cannot be solved on more than a  fraction of inputs having length  by any circuit of size . Finally, it was shown that [[Class_MA|MA]] does not have arithmetic circuits of size .



See also: [[Class_MAE|MAE]], [[Class_MAEXP|MAEXP]].



An alternative definition requires that if the answer is "yes," then there exists a proof such that Arthur accepts with certainty.  However, the definitions with one-sided and two-sided error can be shown to be equivalent (exercise for the Zoo visitor).



Contains [[Class_NP|NP]] and [[Class_∃BPP|∃BPP]], and is contained in [[Class_AM|AM]] and in [[Class_QMA|QMA]].



Equals [[Class_NP|NP]] under a derandomization assumption.
== Relations ==


== See Also ==

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

== Comments ==

The subclass of [[Class_MA|MA]] such that for each input size n, there is a sparse set S,,n,, that Merlin's proof string always belongs to (no matter what the input is).



Defined in [[ZooRefs#KST93|[KST93] ]], where it is also observed that if graph isomorphism is in [[Class_P/poly|P/poly]], then the complement of graph isomorphism is in [[Class_MA'|MA']].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_AC0|AC0]], except now we're allowed a single unbounded-fanin majority gate at the root.



Defined in [[ZooRefs#JKS02|[JKS02] ]].



[[Class_MAC0|MAC0]] is strictly contained in [[Class_TC0|TC0]] [[ZooRefs#ABF+94|[ABF+94] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_MA|MA]], except now Arthur is [[Class_E|E]] instead of polynomial-time.



If [[Class_MAE|MAE]] = [[Class_NEE|NEE]] then [[Class_MA|MA]] = [[Class_NEXP|NEXP]] ∩ [[Class_coNEXP|coNEXP]] [[ZooRefs#IKW01|[IKW01] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_MA|MA]], except now Arthur is [[Class_EXP|EXP]] instead of polynomial-time, and the message from Merlin can be exponentially long.



There is a problem in [[Class_MAEXP|MAEXP]] that does not have polynomial-size circuits [[ZooRefs#BFT98|[BFT98] ]].  On the other hand, there is an oracle relative to which every problem in [[Class_MAEXP|MAEXP]] does have polynomial-size circuits.



[[ZooRefs#MVW99|[MVW99] ]] considered the best circuit lower bound obtainable for a problem in [[Class_MAEXP|MAEXP]], using current techniques.  They found that this bound is half-exponential: i.e. a function f such that f(f(n))=2^n^.  Such functions exist, but are not expressible using standard asymptotic notation.
== Relations ==


== See Also ==

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

== Comments ==

Identical to [[Class_MA|MA]] except for that Arthur (the verifier) has random access to the proof string given by Merlin, and is limited to running times of order .



This class was used by [[ZooRefs#SM03|[SM03] ]] to show that if [[Class_EXP|EXP]] has circuits of polynomial size, then [[Class_EXP|EXP]] = [[Class_MA|MA]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_IP|IP]], except that now the verifier can exchange messages with many provers, not just one.  The provers cannot communicate with each other during the execution of the protocol, so the verifier can "cross-check" their assertions (as with suspects in separate interrogation rooms).



Defined in [[ZooRefs#BGK+88|[BGK+88] ]].



Let MIP[k] be the class of decision problems for which a "yes" answer can be verified with k provers.  Then for all k>2, MIP[k] = MIP[2] = [[Class_MIP|MIP]] [[ZooRefs#BGK+88|[BGK+88] ]].



[[Class_MIP|MIP]] equals [[Class_NEXP|NEXP]] [[ZooRefs#BFL91|[BFL91] ]]; this is a famous non-relativizing result.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_MIP|MIP]], except that the provers can share arbitrarily many entangled qubits.  The verifier is classical, as are all messages between the provers and verifier.



Defined in [[ZooRefs#CHT+04|[CHT+04] ]], where evidence was given suggesting that [[Class_MIP*|MIP*]] does not "obviously" equal [[Class_NEXP|NEXP]].



[[Class_MIP*|MIP*]] contains [[Class_NEXP|NEXP]] [[ZooRefs#IV12|[IV12] ]]. By contrast, [[Class_MIP|MIP]], the corresponding class without entanglement, equals [[Class_NEXP|NEXP]] (and even MIP[2,1] with two provers and one round equals NEXP).



Even MIP*[4,poly] and MIP[5,1] contain [[Class_NEXP|NEXP]] [[ZooRefs#IV12|[IV12] ]].



[[Class_MIP*[2,1]|MIP*[2,1]]] contains [[Class_XOR-MIP*[2,1]|XOR-MIP*[2,1]]].



In 2012 it was shown that [[Class_QMIP|QMIP]] = [[Class_MIP*|MIP*]] [[ZooRefs#RUV12|[RUV12] ]]
== Relations ==


== See Also ==

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

== Comments ==

Same as MIP[2], except that now only one round is allowed, and the two provers can share arbitrarily many entangled qubits.  The verifier is classical, as are all messages between the provers and verifier.



Defined in [[ZooRefs#CHT+04|[CHT+04] ]], where evidence was given suggesting that [[Class_MIP*|MIP*]] does not "obviously" equal [[Class_NEXP|NEXP]].  By contrast, MIP[2,1], the corresponding class without entanglement, equals [[Class_NEXP|NEXP]].



Indeed, the relationship between [[Class_MIP*|MIP*]] and [[Class_MIP|MIP]] = [[Class_NEXP|NEXP]] is completely unknown -- either could contain the other, or they could be incomparable.



It is also unknown whether increasing the number of provers or rounds changes [[Class_MIP*[2,1]|MIP*[2,1]]].



Contains [[Class_XOR-MIP*[2,1]|XOR-MIP*[2,1]]].
== Relations ==


== See Also ==

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

== Comments ==

The exponential-time analogue of [[Class_MIP|MIP]].



In the unrelativized world, equals [[Class_NEEXP|NEEXP]].



There exists an oracle relative to which [[Class_MIPEXP|MIPEXP]] equals the intersection of [[Class_P/poly|P/poly]], [[Class_PNP|PNP]], and [[Class_⊕P|⊕P]] [[ZooRefs#BFT98|[BFT98] ]].
== Relations ==


== See Also ==

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

== Comments ==

The set of all problems reducible to matrix multiplication. That is, the set of problems  that can be reduced to the multiplication of two square matrices can be reduced to  in linear time.



Currently, the best known algorithm for multiplying two  matrices is the Coppersmith–Winograd_algorithm, which has a time complexity of  [[ZooRefs#CW90|[CW90] ]]. Note that for the general problem, a lower bound of  is trivial from the number of elements being considered.
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#FV93|[FV93] ]] as a subclass of [[Class_SNP|SNP]].  There are three syntactic restrictions defining the subclass [[Class_MMSNP|MMSNP]], based on the form of the [[Class_SNP|SNP]] formula defining the language:



The second order existentially quantified variables, known as the proof relations, are restricted to be monadic.  (Monadic relations can be treated as sets.)

 Any relations in the formula other than the proof relations must occur only negated (the formula is monotone).

 No inequality relations can occur in the formula.



[[Class_MMSNP|MMSNP]] seems to obey dichotomy, by excluding languages that are NP-intermediate.  This is still open but widely believed.  Dropping any of the restrictions monotone/monadic/without inequalities allows NP-intermediate languages unless [[Class_P|P]] = [[Class_NP|NP]], since any problem in [[Class_NP|NP]] is polynomial time equivalent to a problem in each of these broader classes.  [[Class_MMSNP|MMSNP]] therefore seems to be a maximal fragment of [[Class_NP|NP]] where NP-intermediate languages are excluded.



Every constraint satisfaction problem with a fixed target structure is expressible in [[Class_MMSNP|MMSNP]], and there is a polynomial time Turing reduction from every [[Class_MMSNP|MMSNP]] query to finitely many constraint satisfaction problems.  [[Class_MMSNP|MMSNP]] therefore seems to capture the class of constraint satisfaction problems with fixed templates, [[Class_CSP|CSP]].



Defined in [[ZooRefs#FV93|[FV93] ]] as a subclass of [[Class_SNP|SNP]], where the second order existentially quantified variables are sets (monadic) and any relations in the first-order part occur negated (monotone).  Further, no inequalities can occur in the first-order part.



[[Class_MMSNP|MMSNP]] seems to obey dichotomy, by excluding Ladner languages.  This is still open but widely believed.  Dropping any of the restrictions monotone/monadic/without inequalities          allows Ladner languages unless [[Class_P|P]] = [[Class_NP|NP]], since any problem in [[Class_NP|NP]] is polynomial time equivalent to a problem in each of these broader classes.  [[Class_MMSNP|MMSNP]] therefore seems to be a maximal fragment of [[Class_NP|NP]] where Ladner languages are excluded.



Every constraint satisfaction problem is expressible in [[Class_MMSNP|MMSNP]], and there is a polynomial time Turing reduction from every [[Class_MMSNP|MMSNP]] query to finitely many constraint satisfaction problems.  [[Class_MMSNP|MMSNP]] therefore seems to capture the class of constraint satisfaction problems.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems such that for some [[Class_#P|#P]] function f, the answer on input x is 'yes' if and only if the middle bit of f(x) is 1.



Defined in [[ZooRefs#GKR+95|[GKR+95] ]].



Contains [[Class_AmpMP|AmpMP]] and [[Class_PH|PH]].



[[Class_MP|MP]] with [[Class_ModP|ModP]] oracle equals [[Class_MP|MP]] with [[Class_#P|#P]] oracle [[ZooRefs#KT96|[KT96] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a family of monotone stratified planar circuits (a uniformity condition may also be imposed).



Such a circuit can contain only AND and OR gates of bounded fanin.  It must be embeddable in the plane with no wires crossing.  Furthermore, the input bits can only be accessed at the bottom level, where they are listed in order (x,,1,,,...,x,,n,,).



Defined in [[ZooRefs#DC89|[DC89] ]].



[[ZooRefs#BLM+99|[BLM+99] ]] showed that we can assume without loss of generality that the circuit has width n and depth n^3^.
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_NP|NP]] as [[Class_MaxSNP|MaxSNP]] does to [[Class_SNP|SNP]].



Contains [[Class_MaxPB|MaxPB]].



The closure of [[Class_MaxNP|MaxNP]] under [[Class_PTAS|PTAS]] reduction is [[Class_APX|APX]] [[ZooRefs#KMS+99|[KMS+99] ]], [[ZooRefs#CT94|[CT94] ]].
== Relations ==


== See Also ==

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

== Comments ==

The subclass of [[Class_MaxNP|MaxNP]] problems for which the cost function is guaranteed always to be bounded by a polynomial.



[[Class_MinPB|MinPB]] can be defined similarly.



Defined in [[ZooRefs#KT94|[KT94] ]].



The closure of [[Class_MaxPB|MaxPB]] under [[Class_PTAS|PTAS]] reductions equals [[Class_NPOPB|NPOPB]] [[ZooRefs#CKS+99|[CKS+99] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of optimization problems reducible by an "L-reduction" to a problem in [[Class_MaxSNP0|MaxSNP0]].  (Note: 'L' stands for linear -- this is not the same as an [[Class_L|L]] reduction!  For more details see [[ZooRefs#PY88|[PY88] ]].)



Defined in [[ZooRefs#PY88|[PY88] ]], where the following was also shown:



Max3SAT is MaxSNP-complete.  (Max3SAT is the problem of finding an assignment that maximizes the number of satisfied clauses in a CNF formula with at most 3 literals per clause.)

Any problem in [[Class_MaxSNP|MaxSNP]] can be approximated to within a fixed ratio.



The closure of [[Class_MaxSNP|MaxSNP]] under [[Class_PTAS|PTAS]] reduction is [[Class_APX|APX]] [[ZooRefs#KMS+99|[KMS+99] ]], [[ZooRefs#CT94|[CT94] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of function problems expressible as "find a relation such that the set of k-tuples for which a given [[Class_SNP|SNP]] predicate holds has maximum cardinality."



For example (see [[ZooRefs#Pap94|[Pap94] ]]), the Max-Cut problem can be expressed as follows:



Given a graph G, find a subset S of vertices that maximizes the number of pairs (u,v) of vertices such that u is in S, and v is not in S, and G has an edge from u to v.



Defined in [[ZooRefs#PY88|[PY88] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_MaxPB|MaxPB]] but for minimization instead of maximization problems.
== Relations ==


== See Also ==

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

== Comments ==

A language  if there are functions  and  such that for all strings :



There exists a prime  and a natural number  such that .

  if and only if .



Thus, for any prime  and natural number , . Moreover, FL^ModL^ = FL^GapL^ [[ZooRefs#AV04|[AV04] ]].



Defined in [[ZooRefs#AV04|[AV04] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a [[Class_ModkP|ModkP]] machine where k can vary depending on the input.  The only requirement is that 0^k^ be computable in polynomial time.



Defined in [[ZooRefs#KT96|[KT96] ]], where it was also shown that [[Class_ModP|ModP]] is contained in [[Class_AmpMP|AmpMP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a nondeterministic logspace Turing machine, such that



If the answer is "yes," then the number of accepting paths is not congruent to 0 mod k.

If the answer is "no," then there are no accepting paths.



Defined in [[ZooRefs#BDH+92|[BDH+92] ]], where it was also shown that [[Class_ModZkL|ModZkL]] contains [[Class_LogFewNL|LogFewNL]] for all k>1.



Contained in [[Class_ModkL|ModkL]] and in [[Class_NL|NL]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_ModkP|ModkP]] does to [[Class_P|P]].



For any prime k, [[Class_ModkL|ModkL]] contains [[Class_SL|SL]] [[ZooRefs#KW93|[KW93] ]].



For any prime k, Mod,,k,,L^ModkL^ = [[Class_ModkL|ModkL]] [[ZooRefs#HRV00|[HRV00] ]].



For any k>1, contains [[Class_LogFew|LogFew]] [[ZooRefs#BDH+92|[BDH+92] ]].
== Relations ==


== See Also ==

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

== Comments ==

For any k>1: The class of decision problems solvable by an [[Class_NP|NP]] machine such that the number of accepting paths is divisible by k, if and only if the answer is "no."



Mod,,2,,P is more commonly known as [[Class_⊕P|⊕P]] "parity-P."



For every k, [[Class_ModkP|ModkP]] contains graph isomorphism [[ZooRefs#AK02|[AK02] ]].



Defined in [[ZooRefs#CH89|[CH89] ]], [[ZooRefs#Her90|[Her90] ]].



[[ZooRefs#Her90|[Her90] ]] and [[ZooRefs#BG92|[BG92] ]] showed that [[Class_ModkP|ModkP]] is the set of unions of languages in Mod,,p,,P for each prime p that divides k.  In particular, if p is prime, then Mod,,p,,P = Mod,,p^m,,P for all positive integers m.  A further fact is that Mod,,p,,P is closed under union, intersection, and complement for p prime.



On the other hand, if k is not a prime power, then there exists an oracle relative to which [[Class_ModkP|ModkP]] is not closed under intersection or complement [[ZooRefs#BBR94|[BBR94] ]].



For prime p, there exists an oracle relative to which Mod,,p,,P does not contain [[Class_EQP|EQP]] [[ZooRefs#GV02|[GV02] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by nondeterministic logarithmic-space and polynomial-time Turing machines with auxiliary pushdown.



Equals [[Class_LOGCFL|LOGCFL]] [[ZooRefs#Sud78|[Sud78] ]].
== Relations ==


== See Also ==

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

== Comments ==

(Named in honor of Nick Pippenger.)



NC^i^ is the class of decision problems solvable by a uniform family of Boolean circuits, with polynomial size, depth O(log^i^(n)), and fan-in 2.



Then [[Class_NC|NC]] is the union of NC^i^ over all nonnegative i.



Also, [[Class_NC|NC]] equals the union of PT/WK(log^k^n, n^k^)/poly over all constants k.



NC^i^ is contained in AC^i^; thus, [[Class_NC|NC]] = [[Class_AC|AC]].



Contains [[Class_NL|NL]].



Generalizations include [[Class_RNC|RNC]] and [[Class_QNC|QNC]].



[[ZooRefs#IN96|[IN96] ]] construct a candidate pseudorandom generator in [[Class_NC|NC]] based on the subset sum problem.



For a random oracle A, (NC^i^)^A^ is strictly contained in (NC^i+1^)^A^, and uniform NC^A^ is strictly contained in P^A^, with probability 1 [[ZooRefs#Mil92|[Mil92] ]].



In descriptive complexity, [[Class_NC|NC]] can be defined by [[Class_FO[]|FO[]]]



NC^i^ is the class of decision problems solvable by a nonuniform family of Boolean circuits, with polynomial size, depth O(log^i^(n)), and fan-in 2.
== Relations ==


== See Also ==

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

== Comments ==

By definition, a decision problem in [[Class_NC0|NC0]] can depend on only a constant number of bits of the input.  Thus, [[Class_NC0|NC0]] usually refers to functions computable by constant-depth, bounded-fanin circuits.



There is a family of permutations computable by a uniform family of [[Class_NC0|NC0]] circuits that is P-hard to invert [[ZooRefs#Has88|[Has88] ]].



Recently [[ZooRefs#AIK04|[AIK04] ]] solved a longstanding open problem by showing that there exist pseudorandom generators and one-way functions in [[Class_NC0|NC0]], based on (for example) the hardness of factoring.  Specifically, in these generators every bit of the output depends on only 4 input bits.  Whether the dependence can be reduced to 3 bits under the same cryptographic assumptions is open, but [[ZooRefs#AIK04|[AIK04] ]] have some partial results in this direction.  It is known that the dependence cannot be reduced to 2 bits.
== Relations ==


== See Also ==

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

== Comments ==

See [[Class_NC|NC]] for definition.



[[ZooRefs#KV94|[KV94] ]] give a family of functions that is computable in [[Class_NC1|NC1]], but not efficiently learnable unless there exists an efficient algorithm for factoring Blum integers.



Was shown to equal 5-PBP [[ZooRefs#Bar89|[Bar89] ]].  On the other hand, width 5 is necessary unless [[Class_NC1|NC1]] = [[Class_ACC0|ACC0]] [[ZooRefs#BT88|[BT88] ]].



As an application of this result, [[Class_NC1|NC1]] can be simulated on a quantum computer with three qubits, one initialized to a pure state and the remaining two in the maximally mixed state [[ZooRefs#ASV00|[ASV00] ]].  Surprisingly, [[ZooRefs#AMP02|[AMP02] ]] showed that only a single qubit is needed to simulate [[Class_NC1|NC1]] - i.e. that [[Class_NC1|NC1]] is contained in 2-EQBP.  (Complex amplitudes are needed for this result.)



Is contained in [[Class_L|L]] [[ZooRefs#Bor77|[Bor77] ]].



Contains [[Class_TC0|TC0]].



[[Class_NC1|NC1]] contains the integer division problem [[ZooRefs#BCH86|[BCH86] ]], even if an L-uniformity condition is imposed [[ZooRefs#CDL01|[CDL01] ]].



U,,E^*^,,-uniform [[Class_NC1|NC1]] is equal to [[Class_ALOGTIME|ALOGTIME]] [[ZooRefs#RUZ81|[RUZ81] ]].
== Relations ==


== See Also ==

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

== Comments ==

See [[Class_NC|NC]] for definition.



Contains [[Class_NL|NL]].
== Relations ==


== See Also ==

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

== Comments ==

Nondeterministic exponential time with linear exponent (i.e. NTIME(2^O(n)^)).



P^NE^ = NP^NE^ [[ZooRefs#Hem89|[Hem89] ]].



Contained in [[Class_NEXP|NEXP]].
== Relations ==


== See Also ==

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

== Comments ==

Contains [[Class_coNE|coNE]], just as [[Class_NEXP/poly|NEXP/poly]] contains [[Class_coNEXP|coNEXP]].
== Relations ==


== See Also ==

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

== Comments ==

Nondeterministic double-exponential time with linear exponent (i.e. NTIME(2^2^O(n)^^)).



If [[Class_MAE|MAE]] = [[Class_NEE|NEE]] then [[Class_MA|MA]] = [[Class_NEXP|NEXP]] ∩ [[Class_coNEXP|coNEXP]] [[ZooRefs#IKW01|[IKW01] ]].



Contained in [[Class_NEEXP|NEEXP]].



Nondeterministic double-exponential time with linear exponent (i.e. NTIME(2^2^O(n)^)).
== Relations ==


== See Also ==

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

== Comments ==

Nondeterministic triple-exponential time with linear exponent.
== Relations ==


== See Also ==

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

== Comments ==

Nondeterministic double-exponential time (i.e. NTIME(2^2^p(n)^^) for p a polynomial).



Equals [[Class_MIPEXP|MIPEXP]] (unrelativized).



Nondeterministic double-exponential time (i.e. NTIME(2^2^p(n)^) for p a polynomial).
== Relations ==


== See Also ==

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

== Comments ==

Nondeterministic exponential time (i.e. NTIME(2^p(n)^) for p a polynomial).



Equals [[Class_MIP|MIP]] [[ZooRefs#BFL91|[BFL91] ]] (but not relative to all oracles).



[[Class_NEXP|NEXP]] is in [[Class_MIP*|MIP*]] [[ZooRefs#IV12|[IV12] ]].



[[Class_NEXP|NEXP]] is in [[Class_P/poly|P/poly]] if and only if [[Class_NEXP|NEXP]] = [[Class_MA|MA]] [[ZooRefs#IKW01|[IKW01] ]].



[[ZooRefs#KI02|[KI02] ]] show the following:



If [[Class_P|P]] = [[Class_RP|RP]], then [[Class_NEXP|NEXP]] is not computable by polynomial-size arithmetic circuits.

If [[Class_P|P]] = [[Class_BPP|BPP]] and if checking whether a Boolean circuit computes a function that is close to a low-degree polynomial over a finite field is in [[Class_P|P]], then [[Class_NEXP|NEXP]] is not in [[Class_P/poly|P/poly]].

If [[Class_NEXP|NEXP]] is in [[Class_P/poly|P/poly]], then matrix permanent is NEXP-complete.



Does not equal [[Class_NP|NP]] [[ZooRefs#SFM78|[SFM78] ]].



Does not equal [[Class_EXP|EXP]] if and only if there is a sparse set in [[Class_NP|NP]] that is not in [[Class_P|P]].



There exists an oracle relative to which [[Class_EXP|EXP]] = [[Class_NEXP|NEXP]] but still [[Class_P|P]] does not equal [[Class_NP|NP]] [[ZooRefs#Dek76|[Dek76] ]].



The theory of reals with addition (see EXPSPACE) is hard for [[Class_NEXP|NEXP]] [[ZooRefs#FR74|[FR74] ]].
== Relations ==


== See Also ==

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

== Comments ==

Contains [[Class_coNEXP|coNEXP]] (folklore result reported in [weblog]).
== Relations ==


== See Also ==

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

== Comments ==

Defined in [M08] based on [[ZooRefs#DDPY98|[DDPY98] ]],[[ZooRefs#BFM88|[BFM88] ]].



Contained in [[Class_PZK|PZK]].



[M08] showed a complete promise-problem for [[Class_NIPZK|NIPZK]], called Unifrom (UN). Instances 

in UN are circuits with n+1 output bits. The first n bits represent the uniform distribution, and the last bit is 1 with probability at least 2/3. For instances not in UN, when the last bit is 1, at most 1/3 of the strings of length n can appear as the output of the circuit. The problem is to decide which is the case.
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_QSZK|QSZK]] as [[Class_NISZK|NISZK]] does to [[Class_SZK|SZK]].



Defined in [[ZooRefs#Kob02|[Kob02] ]], where it was also shown that the following promise problem is complete for [[Class_NIQSZK|NIQSZK]].  Given a quantum circuit, we are promised that the state it prepares (when run on the all-0 state, and tracing out non-output qubits) has trace distance either at most 1/3 or at least 2/3 from the maximally mixed state. The problem is to output "no" in the former case and "yes" in the latter.



NIQPZK can be defined similarly.
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#DDP+98|[DDP+98] ]].



Contained in [[Class_SZK|SZK]].



[[ZooRefs#GSV99|[GSV99] ]] showed the following:



If [[Class_SZK|SZK]] does not equal [[Class_BPP|BPP]] then [[Class_NISZK|NISZK]] does not equal [[Class_BPP|BPP]].

[[Class_NISZK|NISZK]] equals [[Class_SZK|SZK]] if and only if [[Class_NISZK|NISZK]] is closed under complement.

[[Class_NISZK|NISZK]] has natural complete promise problems:

  

    Statistical Distance from Uniform (SDU): Given a circuit, consider the distribution over outputs when the circuit is given a uniformly random n-bit string.  We're promised that the trace distance between this distribution and the uniform distribution is either at most 1/3 or at least 2/3.  The problem is to output "yes" in the former case and "no" in the latter.

    Entropy Approximation (EA): Now we're promised that the entropy of the circuit's output distribution is either at least k+1 or at most k-1.  The problem is to output "yes" in the former case and "no" in the latter.



[[Class_NIPZK|NIPZK]] can be defined similarly.
== Relations ==


== See Also ==

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

== Comments ==

The non-interactive analogue of [[Class_SZKh|SZKh]].



Defined in [[ZooRefs#BG03|[BG03] ]], where the following was also shown:



[[Class_NISZKh|NISZKh]] contains [[Class_NISZK|NISZK]] and is contained in [[Class_SZK|SZK]].

Graph Isomorphism is in [[Class_NISZKh|NISZKh]].

The following problem is complete for [[Class_NISZKh|NISZKh]]: Given two functions from {0,1}^n^ to {0,1}^n^ (specified by circuits), decide whether their ranges are almost equal or almost disjoint, given that one of these is the case.



The quantum lower bound for the set comparison problem in [[ZooRefs#Aar02|[Aar02] ]] implies an oracle relative to which [[Class_NISZKh|NISZKh]] is not in [[Class_BQP|BQP]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_NP|NP]] does to [[Class_P|P]].



In a breakthrough result, was shown to equal [[Class_coNL|coNL]] [[ZooRefs#Imm88|[Imm88] ]] [[ZooRefs#Sze87|[Sze87] ]].  (Though contrast to mNL.)



Is contained in [[Class_LOGCFL|LOGCFL]] [[ZooRefs#Sud78|[Sud78] ]], as well as [[Class_NC2|NC2]].



Is contained in [[Class_UL/poly|UL/poly]] [[ZooRefs#RA00|[RA00] ]].



Deciding whether a bipartite graph has a perfect matching is hard for [[Class_NL|NL]] [[ZooRefs#KUW86|[KUW86] ]].



[[Class_NL|NL]] can be defined in a logical formalism as SO(krom) and also as FO(tc), reachability in directed graph is NL-Complete under FO-reduction.
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_NL|NL]] as [[Class_P/poly|P/poly]] does to [[Class_P|P]].



Is contained in [[Class_⊕L/poly|⊕L/poly]] [[ZooRefs#GW96|[GW96] ]], as well as [[Class_SAC1|SAC1]].



Equals [[Class_UL/poly|UL/poly]] [[ZooRefs#RA00|[RA00] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_LIN|LIN]] as [[Class_NP|NP]] does to [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_NL|NL]] -- but if there's an oracle, then [[Class_NLOG|NLOG]] can make queries nondeterministically on a polynomial-size, one-way oracle tape.  (NL, by contrast, can use nondeterministic transitions only on the worktape; oracle queries have to be deterministic.)



See [[ZooRefs#LL76|[LL76] ]] or [[ZooRefs#HCK+88|[HCK+88] ]] for more information.



Although [[Class_NLOG|NLOG]] is contained in [[Class_P|P]], there exists an oracle relative to which that is not the case.  This illustrates that care is needed when defining oracle access mechanisms.
== Relations ==


== See Also ==

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

== Comments ==

Class of functions computable in nearly linear time n(log n)^O(1)^ on deterministic random access machines.



Defined in [[ZooRefs#GS89|[GS89] ]].



See also [[Class_QL|QL]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_NC|NC]], but with O(f(n)) nondeterministic gates. A nondeterministic gate has no inputs and a single output bit.



Defined in [[ZooRefs#Wol94|[Wol94] ]], where the author proves various inclusions, including but not limited to NNC(poly(n))=NP, NNC(log(n))=NC, and NNC(polylog)⊆DSPACE(polylog).
== Relations ==


== See Also ==

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

== Comments ==

Class of functions computable in nearly linear time n(log n)^O(1)^ on nondeterministic random access machines.  Equals [[Class_NQL|NQL]] [[ZooRefs#GS89|[GS89] ]].



Defined in [[ZooRefs#GS89|[GS89] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class that does not contain any languages.  (It might not surprise you that I put this one in at the suggestion of a mathematician...)



Is the opposite of [[Class_ALL|ALL]], but does not equal the complement coALL = [[Class_ALL|ALL]].



Is closed under polynomial-time Turing reductions :-).



Equals [[Class_SPARSE|SPARSE]] ∩ [[Class_coSPARSE|coSPARSE]] and [[Class_TALLY|TALLY]] ∩ coTALLY.
== Relations ==


== See Also ==

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

== Comments ==

The class of dashed hopes and idle dreams.



More formally: an "NP machine" is a nondeterministic polynomial-time Turing machine.



Then [[Class_NP|NP]] is the class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is "yes," at least one computation path accepts.

If the answer is "no," all computation paths reject.



Equivalently, [[Class_NP|NP]] is the class of decision problems such that, if the answer is "yes," then there is a proof of this fact, of length polynomial in the size of the input, that can be verified in [[Class_P|P]] (i.e. by a deterministic polynomial-time algorithm).  On the other hand, if the answer is "no," then the algorithm must declare invalid any purported proof that the answer is "yes."



For example, the SAT problem is to decide whether a given Boolean formula has any satisfying truth assignments. SAT is in [[Class_NP|NP]], since a "yes" answer can be proved by just exhibiting a satisfying assignment.



A decision problem is NP-complete if (1) it is in [[Class_NP|NP]], and (2) any problem in [[Class_NP|NP]] can be reduced to it (under some notion of reduction).  The class of NP-complete problems is sometimes called [[Class_NPC|NPC]].



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



[[Class_NP|NP]] contains [[Class_P|P]].  I've discovered a marvelous proof that [[Class_NP|NP]] and [[Class_P|P]] are unequal, but this web page is too small to contain it.  Too bad, since otherwise I'd be eligible for $1,000,000 [[ZooRefs#CMI00|[CMI00] ]].



There exists an oracle relative to which [[Class_P|P]] and [[Class_NP|NP]] are unequal [[ZooRefs#BGS75|[BGS75] ]].  Indeed, [[Class_P|P]] and [[Class_NP|NP]] are unequal relative to a random oracle with probability 1 [[ZooRefs#BG81|[BG81] ]] (see [[ZooRefs#AFM01|[AFM01] ]] for a novel take on this result).  Though random oracle results are not always indicative about the unrelativized case [[ZooRefs#CCG+94|[CCG+94] ]].



There even exists an oracle relative to which the [[Class_P|P]] versus [[Class_NP|NP]] problem is outside the usual axioms of set theory [[ZooRefs#HH76|[HH76] ]].



If we restrict to monotone classes, [[Class_mP|mP]] is strictly contained in [[Class_mNP|mNP]] [[ZooRefs#Raz85|[Raz85] ]].



Perhaps the most important insight anyone has had into [[Class_P|P]] versus [[Class_NP|NP]] is to be found in [[ZooRefs#RR97|[RR97] ]].  There the authors show that no 'natural proof' can separate [[Class_P|P]] from [[Class_NP|NP]] (or more precisely, place [[Class_NP|NP]] outside of P/poly), unless secure pseudorandom generators do not exist.  A proof is 'natural' if it satisfies two conditions called constructivity and largeness; essentially all lower bound techniques known to date satisfy these conditions.  To obtain unnatural proof techniques, some people suspect we need to relate [[Class_P|P]] versus [[Class_NP|NP]] to heavy-duty 'traditional' mathematics, for instance algebraic geometry.  See [[ZooRefs#MS02|[MS02] ]] (and the survey article [[ZooRefs#Reg02|[Reg02] ]]) for a development of this point of view.



For more on [[Class_P|P]] versus [[Class_NP|NP]] (circa 1992) see [[ZooRefs#Sip92|[Sip92] ]].  For an opinion poll, see [[ZooRefs#Gas02|[Gas02] ]].



If [[Class_P|P]] equals [[Class_NP|NP]], then [[Class_NP|NP]] equals its complement [[Class_coNP|coNP]].  Whether [[Class_NP|NP]] equals [[Class_coNP|coNP]] is also open.  [[Class_NP|NP]] and [[Class_coNP|coNP]] can be extended to the polynomial hierarchy [[Class_PH|PH]].



The set of decision problems in [[Class_NP|NP]], but not in [[Class_P|P]] or [[Class_NPC|NPC]], is sometimes called [[Class_NPI|NPI]].  If [[Class_P|P]] does not equal [[Class_NP|NP]] then [[Class_NPI|NPI]] is nonempty [[ZooRefs#Lad75|[Lad75] ]].



Probabilistic generalizations of [[Class_NP|NP]] include [[Class_MA|MA]] and [[Class_AM|AM]].  If [[Class_NP|NP]] is in [[Class_coAM|coAM]] (or BPP) then [[Class_PH|PH]] collapses to [[Class_Σ2P|Σ2P]] [[ZooRefs#BHZ87|[BHZ87] ]].



[[Class_PH|PH]] also collapses to [[Class_Σ2P|Σ2P]] if [[Class_NP|NP]] is in [[Class_P/poly|P/poly]] [[ZooRefs#KL82|[KL82] ]].



There exist oracles relative to which [[Class_NP|NP]] is not in [[Class_BQP|BQP]] [[ZooRefs#BBB+97|[BBB+97] ]].



An alternate characterization is [[Class_NP|NP]] = PCP(log n, O(1)) [[ZooRefs#ALM+98|[ALM+98] ]].



Also, [[ZooRefs#Fag74|[Fag74] ]] showed that [[Class_NP|NP]] is precisely the class of decision problems reducible to a graph-theoretic property expressible in second-order existential logic. This leads to the subclass [[Class_SNP|SNP]].



It is known that if any NP-complete language is sparse (contains no more than a polynomial number of strings of length ), then [[Class_P|P]] = [[Class_NP|NP]]. [[ZooRefs#BH08|[BH08] ]] improved this result, showing that if any language in [[Class_NP|NP]] has an NP-hard set of subexponential density, then [[Class_coNP|coNP]] is contained in [[Class_NP/poly|NP/poly]] and thus, by [[ZooRefs#Yap82|[Yap82] ]], [[Class_PH|PH]] collapses to the third level.



[[Class_NP|NP]] is equal to [[Class_SO-E|SO-E]], the second-order queries where the second-order quantifiers are only existantials.



For example, the SAT problem is to decide whether a given Boolean formula has any satisfying truth assignments.  SAT is in [[Class_NP|NP]], since a "yes" answer can be proved by just exhibiting a satisfying assignment.



Also, [[ZooRefs#Fag74|[Fag74] ]] gave a logical characterization of [[Class_NP|NP]], which leads to the subclass [[Class_SNP|SNP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems in both [[Class_NP|NP]] and [[Class_coNP|coNP]].



Contains factoring [[ZooRefs#Pra75|[Pra75] ]].



Contains graph isomorphism under the assumption that some language in [[Class_NE|NE]] ∩ [[Class_coNE|coNE]] requires nondeterministic circuits of size 2^Ω(n)^ ([[ZooRefs#MV99|[MV99] ]], improving [[ZooRefs#KM99|[KM99] ]]).  (A nondeterministic circuit C has two inputs, x and y, and accepts on x if there exists a y such that C(x,y)=1.)



Equals [[Class_PNP|PNP]] ∩ [[Class_coNP|coNP]] [[ZooRefs#Bra79|[Bra79] ]].  In particular, if a problem in [[Class_NP|NP]] ∩ [[Class_coNP|coNP]] is NP-hard with Turing reduction, then [[Class_NP|NP]] = [[Class_coNP|coNP]].



Is not believed to contain complete problems.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_NP/poly|NP/poly]], except that now the advice string is logarithmic-size.



Shown in [[ZooRefs#FK05|[FK05] ]] that [[Class_EXP|EXP]] ⊆ [[Class_NP/log|NP/log]] if and only if [[Class_EXP|EXP]] = [[Class_P||NP|P||NP]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_NP|NP]] as [[Class_P/poly|P/poly]] does to [[Class_P|P]].



Contains [[Class_AM|AM]].  On the other hand, if [[Class_NP/poly|NP/poly]] contains [[Class_coNP|coNP]] then [[Class_PH|PH]] collapses to the third level.



NP/poly-natural proofs cannot show that circuit families are outside [[Class_P/poly|P/poly]], under a pseudorandomness assumption [[ZooRefs#Rud97|[Rud97] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems such that (1) they're in [[Class_NP|NP]] and (2) every problem in [[Class_NP|NP]] is reducible to them (under some notion of reduction).  In other words, the hardest problems in [[Class_NP|NP]].



Two notions of reduction from problem A to problem B are usually considered:



Karp or many-one reductions.  Here a polynomial-time algorithm is given as input an instance of problem A, and must produce as output an instance of problem B.

Turing reductions, in this context also called Cook reductions.  Here the algorithm for problem B can make arbitrarily many calls to an oracle for problem A.



Some examples of NP-complete problems are discussed under the entry for [[Class_NP|NP]].



The classic reference on [[Class_NPC|NPC]] is [[ZooRefs#GJ79|[GJ79] ]].



Unless [[Class_P|P]] = [[Class_NP|NP]], [[Class_NPC|NPC]] does not contain any sparse problems: that is, problems such that the number of 'yes' instances of size n is upper-bounded by a polynomial in n [[ZooRefs#Mah82|[Mah82] ]].



A famous conjecture [[ZooRefs#BH77|[BH77] ]] asserts that all NP-complete problems are polynomial-time isomorphic -- i.e. between any two problems, there is a one-to-one and onto Karp reduction. If that's true, the NP-complete problems could be interpreted as mere "relabelings" of one another.



NP-complete problems are p-superterse unless [[Class_P|P]] = [[Class_NP|NP]] [[ZooRefs#BKS95|[BKS95] ]].  This means that, given k Boolean formulas F,,1,,,...,F,,k,,, if you can rule out even one of the 2^k^ possibilities in polynomial time (e.g., "if F,,1,,,...,F,,k-1,, are all unsatisfiable then F,,k,, is satisfiable"), then [[Class_P|P]] = [[Class_NP|NP]].



An analog of [[Class_NP|NP]] for Turing machines over a complex number field.



Defined in [[ZooRefs#BCS+97|[BCS+97] ]].



It is unknown whether [[Class_PC|PC]] = [[Class_NPC|NPC]], nor are implications known among this question, [[Class_PR|PR]] versus [[Class_NPR|NPR]], and [[Class_P|P]] versus [[Class_NP|NP]].



However, [[ZooRefs#CKK+95|[CKK+95] ]] show that if [[Class_P/poly|P/poly]] does not equal [[Class_NP/poly|NP/poly]] then [[Class_PC|PC]] does not equal [[Class_NPC|NPC]].



[[ZooRefs#BCS+97|[BCS+97] ]] show the following striking result.  For a positive integer n, let t(n) denote the minimum number of additions, subtractions, and multiplications needed to construct n, starting from 1.  If for every sequence {n,,k,,} of positive integers, t(n,,k,, k!) grows faster than polylogarithmically in k, then [[Class_PC|PC]] does not equal [[Class_NPC|NPC]].



See also [[Class_VNPk|VNPk]].
== Relations ==


== See Also ==

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

== Comments ==

Sometimes used to denote the set of decision problems in [[Class_NP|NP]] that are neither NP-complete (that is, in NPC) nor in [[Class_P|P]].



Is thought to contain (for example) decision versions of factoring and graph isomorphism.



Is nonempty if [[Class_P|P]] does not equal [[Class_NP|NP]] [[ZooRefs#Lad75|[Lad75] ]].  Indeed, under this assumption, it contains an infinite number of distinct polynomial-time equivalence classes.
== Relations ==


== See Also ==

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

== Comments ==

The class of all (possibly partial, possibly multivalued) functions computed by an [[Class_NP|NP]] machine as follows: ignore the rejecting paths, and consider any output of an accepting path to be "one of the outputs."



Contains [[Class_NPSV|NPSV]] and [[Class_NPMVt|NPMVt]].



Defined in [[ZooRefs#BLS84|[BLS84] ]].



Contrast with [[Class_FNP|FNP]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_NPMV|NPMV]] as [[Class_P-Sel|P-Sel]] does to [[Class_P|P]].



Defined in [[ZooRefs#HHN+95|[HHN+95] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of all (possibly multivalued) [[Class_NPMV|NPMV]] functions that are total (that is, defined for every input).
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_NPMVt|NPMVt]] as [[Class_P-Sel|P-Sel]] does to [[Class_P|P]].



Defined in [[ZooRefs#HHN+95|[HHN+95] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of function problems of the form, "Find any n-bit string x that maximizes a cost function C(x), where C is computable in [[Class_FP|FP]] (i.e. polynomial-time)."



Defined in [[ZooRefs#ACG+99|[ACG+99] ]].



Contains [[Class_APX|APX]] and [[Class_NPOPB|NPOPB]].
== Relations ==


== See Also ==

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

== Comments ==

The subclass of [[Class_NPO|NPO]] problems for which the cost function is guaranteed always to be bounded by a polynomial in n (the input size).



See [[ZooRefs#ACG+99|[ACG+99] ]].



[[Class_NPOPB|NPOPB]] equals the closure of [[Class_MaxPB|MaxPB]] under [[Class_PTAS|PTAS]] reductions [[ZooRefs#CKS+99|[CKS+99] ]].
== Relations ==


== See Also ==

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

== Comments ==

An analog of [[Class_NP|NP]] for Turing machines over a real number field.



Defined in [[ZooRefs#BCS+97|[BCS+97] ]].



It is unknown whether [[Class_PR|PR]] = [[Class_NPR|NPR]], nor are implications known among this question, [[Class_PC|PC]] versus [[Class_NPC|NPC]], and [[Class_P|P]] versus [[Class_NP|NP]].



Also, in contrast to the case of [[Class_NPC|NPC]], it is an open problem to show that [[Class_P/poly|P/poly]] distinct from [[Class_NP/poly|NP/poly]] implies [[Class_PR|PR]] distinct from [[Class_NPR|NPR]].  The difference is that in the real case, a comparison (or greater-than) operator is available, and it is not known how much power this yields in comparison to the complex case.



See also [[Class_VNPk|VNPk]].
== Relations ==


== See Also ==

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

== Comments ==

Equals [[Class_PSPACE|PSPACE]] [[ZooRefs#Sav70|[Sav70] ]].



On the other hand, this result does not relativize if we allow strings of unbounded length to be written to the oracle tape.  In particular, there exists an oracle relative to which [[Class_NPSPACE|NPSPACE]] is not contained in [[Class_EXP|EXP]] [[ZooRefs#GTW+91|[GTW+91] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of [[Class_NPMV|NPMV]] functions that are single-valued (i.e., such that every accepting path outputs the same value).



Defined in [[ZooRefs#BLS84|[BLS84] ]].



Contains [[Class_NPSVt|NPSVt]].



[[Class_P|P]] = [[Class_NP|NP]] if and only if [[Class_FP|FP]] = [[Class_NPSV|NPSV]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_NPSV|NPSV]] as [[Class_P-Sel|P-Sel]] does to [[Class_P|P]].



Defined in [[ZooRefs#HHN+95|[HHN+95] ]].



Has the same relation to href="#npsv">NPSV as [[Class_P-Sel|P-Sel]] does to [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

The class of all [[Class_NPSV|NPSV]] functions that are total (that is, defined on every input).



Contained in [[Class_NPMVt|NPMVt]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_NPSVt|NPSVt]] as [[Class_P-Sel|P-Sel]] does to [[Class_P|P]].



Also known as NP-sel.



Defined in [[ZooRefs#HHN+95|[HHN+95] ]].
== Relations ==


== See Also ==

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

== Comments ==

The analogue of [[Class_Pcc|Pcc]] for nondeterministic communication complexity.  Both communication bits and nondeterministic guess bits count toward the complexity.



Does not equal [[Class_Pcc|Pcc]] or [[Class_coNPcc|coNPcc]] because of the EQUALITY problem.  Also, does not contain [[Class_BPPcc|BPPcc]] because of that problem.



Defined in [[ZooRefs#BFS86|[BFS86] ]].



Contained in [[Class_PHcc|PHcc]].



Has the same relation to [[Class_NPcc|NPcc]] and [[Class_NP|NP]] as [[Class_Pcc|Pcc]] does to [[Class_Pcc|Pcc]] and [[Class_P|P]].



[[Class_NPcc|NPcc]] is not contained in [[Class_BPPcc|BPPcc]] for  players, for any constant . As a result, [[Class_NPcc|NPcc]] is not equal to [[Class_RPcc|RPcc]] under the same conditions [[ZooRefs#DP08|[DP08] ]].
== Relations ==


== See Also ==

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

pagename = u"Class_NQL"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= NQL - Nondet Quasi-Linear =

== Comments ==

The class of problems that can be decided in quasi-linear time by a multitape nondeterministic Turing machine.  Quasi-linear here means n(log n)^k^ + k, for some k.



Equals [[Class_NNLT|NNLT]].



SAT is NQL-complete under quasi-linear-time reductions (which can be computed in deterministic quasi-linear time) [[ZooRefs#Sch78|[Sch78] ]].



Defined in [[ZooRefs#Sch78|[Sch78] ]].



See also: [[Class_NLT|NLT]], [[Class_Q|Q]], [[Class_QL|QL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a QTM in polynomial time such that a particular '|Accept>' state has nonzero amplitude at the end of the computation, if and only if the answer is 'yes.'  Since it has an exact amplitude condition, [[Class_NQP|NQP]] has the same technical caveats as [[Class_EQP|EQP]].  Or it would, except that it turns out to equal [[Class_coC=P|coC=P]] [[ZooRefs#FGH+98|[FGH+98] ]].



Defined in [[ZooRefs#ADH97|[ADH97] ]].



Contrast with [[Class_QMA|QMA]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_NPSPACE|NPSPACE]], but with f(n)-space (for some constructible function f) rather than polynomial-space machines.



Contained in DSPACE(f(n)^2^) [[ZooRefs#Sav70|[Sav70] ]], and indeed RevSPACE(f(n)^2^) 95|[[ZooRefs#CP95|[CP95] ]].



NSPACE(n^k^) is strictly contained in NSPACE(n^k+ε^) for ε>0 [[ZooRefs#Iba72|[Iba72] ]] (actually the hierarchy theorem is stronger than this, but pretty technical to state).



Contained in DSPACE(f(n)^2^) [[ZooRefs#Sav70|[Sav70] ]], and indeed RevSPACE(f(n)^2^) [[ZooRefs#CP95|[CP95] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems such that whether the answer on input x agrees with the answer on input x-1 (that is, the lexicographic predecessor of x) is solvable in polynomial time.  The Turing machine has to decide agreement or disagreement without access to the answer for x-1.



Is contained in [[Class_E|E]], [[Class_NT*|NT*]], and [[Class_⊕P|⊕P]].  Defined in [[ZooRefs#GHJ+91|[GHJ+91] ]] to study ⊕P-complete problems.  They show  that [[Class_P|P]], [[Class_NT|NT]], [[Class_NT*|NT*]], and [[Class_⊕P|⊕P]] are either all equal or strictly nested.  In particular, they differ with probability 1 relative to a random oracle.
== Relations ==


== See Also ==

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

== Comments ==

Defined like [[Class_NT|NT]], but with a more general ordering on inputs.  A problem [[Class_L|L]] is in [[Class_NT*|NT*]] if, first, there is a partially defined predecessor function pred(x) in [[Class_FP|FP]] that organizes the space of inputs into a forest.  The size of the lineage of each x must also be bounded by 2^poly(|x|)^.  Second, if L(x) is the Boolean answer to [[Class_L|L]] on input x, then L(x)+L(pred(x)) is computable in polynomial time; or if pred(x) does not exist, L(x) is computable in polynomial time.



Defined in [[ZooRefs#GHJ+91|[GHJ+91] ]].



Contains [[Class_NT|NT]] and is contained in [[Class_⊕P|⊕P]].  The inclusions are either both strict or both equalities (whence [[Class_⊕P|⊕P]] = [[Class_P|P]] as well).
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_NP|NP]], but with f(n)-time (for some constructible function f) rather than polynomial-time machines.



The Nondeterministic Time Hierarchy Theorem: If f and g are time-constructible and f(n+1)=o(g), then [[Class_NTIME(f(n))|NTIME(f(n))]] does not equal NTIME(g(n)) [[ZooRefs#SFM78|[SFM78] ]] (this is actually stronger than the hierarchy theorem for DTIME).



NTIME(n) strictly contains DTIME(n) [[ZooRefs#PPS+83|[PPS+83] ]] (this result does not work for arbitrary f(n)).



For any constructible superpolynomial f, [[Class_NTIME(f(n))|NTIME(f(n))]] with [[Class_NP|NP]] oracle is not in [[Class_P/poly|P/poly]] [[ZooRefs#Kan82|[Kan82] ]].
== Relations ==


== See Also ==

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

== Comments ==

The set of languages [[Class_L|L]] such that for every k, there is a language L_k in [[Class_P|P]] that differs from [[Class_L|L]] on at most 2^n^/n^k^ inputs of length n.  Discussed in [[ZooRefs#NS05|[NS05] ]] and implicitly defined in [[ZooRefs#Yam99|[Yam99] ]].



The set of languages [[Class_L|L]] such that for every k, there is a language L_k in [[Class_P|P]] that differs from [[Class_L|L]] on at most 2^n/n^k inputs of length n.  Discussed in [[ZooRefs#NS05|[NS05] ]] and implicitly defined in [[ZooRefs#Yam99|[Yam99] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a [[Class_BQP|BQP]] machine in which a single qubit is initialized to the '0' state, and the remaining qubits are initialized to the maximally mixed state.  (This definition is not known to be robust, so one also needs to specify a gate set.)



We also need to stipulate that there are no "strong measurements" -- intermediate measurements on which later operations are conditioned -- since otherwise we can do all of [[Class_BQP|BQP]] by first initializing the computer to the all-0 state.  Parker and Plenio [[ZooRefs#PP00|[PP00] ]] failed to appreciate this point.



Defined by [[ZooRefs#ASV00|[ASV00] ]] (though they didn't use the name OCQ), who also showed that if [[Class_OCQ|OCQ]] = [[Class_BQP|BQP]], something other than gate-by-gate simulation will be needed to show this.
== Relations ==


== See Also ==

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

== Comments ==

The class of functions computable by taking the maximum of the output values over all accepting paths of an [[Class_NP|NP]] machine.



Defined in [[ZooRefs#Kre88|[Kre88] ]].



Contrast with [[Class_FNP|FNP]].
== Relations ==


== See Also ==

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

== Comments ==

The class that started it all.



The class of decision problems solvable in polynomial time by a Turing machine.  (See also [[Class_FP|FP]], for function problems.)



Defined in [[ZooRefs#Edm65|[Edm65] ]], [[ZooRefs#Cob64|[Cob64] ]], [[ZooRefs#Rab60|[Rab60] ]], and other seminal early papers.



Contains some highly nontrivial problems, including linear programming [[ZooRefs#Kha79|[Kha79] ]] and finding a maximum matching in a general graph [[ZooRefs#Edm65|[Edm65] ]].



Contains the problem of testing whether an integer is prime [[ZooRefs#AKS02|[AKS02] ]], an important result that improved on a proof requiring an assumption of the generalized Riemann hypothesis [[ZooRefs#Mil76|[Mil76] ]].



A decision problem is P-complete if it is in [[Class_P|P]], and if every problem in [[Class_P|P]] can be reduced to it in [[Class_L|L]] (logarithmic space).  The canonical P-complete problem is circuit evaluation: given a Boolean circuit and an input, decide what the circuit outputs when given the input.



Important subclasses of [[Class_P|P]] include [[Class_L|L]], [[Class_NL|NL]], [[Class_NC|NC]], and [[Class_SC|SC]].



[[Class_P|P]] is contained in [[Class_NP|NP]], but whether they're equal seemed to be an open problem when I last checked.



Efforts to generalize [[Class_P|P]] resulted in [[Class_BPP|BPP]] and [[Class_BQP|BQP]].



The nonuniform version is [[Class_P/poly|P/poly]], the monotone version is [[Class_mP|mP]], and versions over the real and complex number fields are [[Class_PR|PR]] and [[Class_PC|PC]] respectively.



In descriptive complexity, [[Class_P|P]] can be defined by three different kind of formulae, FO(lfp) which is also FO()], and also as [[Class_SO(Horn)|SO(Horn)]]



[[Class_P|P]] queries are exactly the one that can be written in the While^/cons^ languages.
== Relations ==


== See Also ==

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

pagename = u"Class_P#P"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^#P^ - P With #P Oracle =

== Comments ==

I decided this class is so important that it deserves an entry of its own, apart from [[Class_#P|#P]].



Contains [[Class_PH|PH]] [[ZooRefs#Tod89|[Tod89] ]], and is contained in [[Class_PSPACE|PSPACE]].



Equals [[Class_PPP|PPP]] (exercise for the visitor).
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save P#P because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_P#P[1]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P^#P[1]^ - P With Single Query To #P Oracle =

== Comments ==

Contains [[Class_PH|PH]] [[ZooRefs#Tod89|[Tod89] ]].
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save P#P[1] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_P-Close"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= P-Close - Problems Close to P =

== Comments ==

The class of decision problems solvable by a polynomial-time algorithm that outputs the wrong answer on only a sparse (that is, polynomially-bounded) set of instances.



Defined in [[ZooRefs#Yes83|[Yes83] ]].



Contains [[Class_Almost-P|Almost-P]] and is contained in [[Class_P/poly|P/poly]] [[ZooRefs#Sch86|[Sch86] ]].
== Relations ==


== See Also ==

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

== Comments ==

An ordered binary decision diagram (OBDD) is a branching program (see k-PBP), with the additional constraint that if x,,i,, is queried before x,,j,, on any path, then i<j.



Then [[Class_P-OBDD|P-OBDD]] is the class of decision problems solvable by polynomial-size OBDD's.



Contained in [[Class_PBP|PBP]], as well as [[Class_BPP-OBDD|BPP-OBDD]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which there's a polynomial-time algorithm with the following property.  Whenever it's given two instances, a "yes" and a "no" instance, the algorithm can always decide which is the "yes" instance.



Defined in [[ZooRefs#Sel79|[Sel79] ]], where it was also shown that if [[Class_NP|NP]] is contained in [[Class_P-Sel|P-Sel]] then [[Class_P|P]] = [[Class_NP|NP]].



There exist P-selective sets that are not recursive (i.e. not in R).
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_P/poly|P/poly]], except that the advice string for input size n can have length at most logarithmic in n, rather than polynomial.



Strictly contained in [[Class_IC[log,poly]|IC[log,poly]]].



If [[Class_NP|NP]] is contained in [[Class_P/log|P/log]] then [[Class_P|P]] = [[Class_NP|NP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a family of polynomial-size Boolean circuits.  The family can be nonuniform; that is, there could be a completely different circuit for each input length.



Equivalently, [[Class_P/poly|P/poly]] is the class of decision problems solvable by a polynomial-time Turing machine that receives an 'advice string,' that depends only on the size n of the input, and that itself has size upper-bounded by a polynomial in n.



Contains [[Class_BPP|BPP]] by the progenitor of derandomization arguments [[ZooRefs#Adl78|[Adl78] ]] [[ZooRefs#KL82|[KL82] ]].  By extension, BPP/poly, BPP/mpoly, and BPP/rpoly all equal [[Class_P/poly|P/poly]]. (By contrast, there is an oracle relative to which [[Class_BPP/log|BPP/log]] does not equal [[Class_BPP/mlog|BPP/mlog]], while [[Class_BPP/mlog|BPP/mlog]] and [[Class_BPP/rlog|BPP/rlog]] are not equal relative to any oracle.)



[[ZooRefs#KL82|[KL82] ]] showed that, if [[Class_P/poly|P/poly]] contains [[Class_NP|NP]], then [[Class_PH|PH]] collapses to the second level, [[Class_Σ2P|Σ2P]].



They also showed:



If [[Class_PSPACE|PSPACE]] is in [[Class_P/poly|P/poly]] then [[Class_PSPACE|PSPACE]] equals [[Class_Σ2P|Σ2P]] ∩ [[Class_Π2P|Π2P]].

If [[Class_EXP|EXP]] is in [[Class_P/poly|P/poly]] then [[Class_EXP|EXP]] = [[Class_Σ2P|Σ2P]].



It was later shown that, if [[Class_NP|NP]] is contained in [[Class_P/poly|P/poly]], then [[Class_PH|PH]] collapses to ZPP^NP^ [[ZooRefs#KW98|[KW98] ]] and indeed [[Class_S2P|S2P]] [[ZooRefs#Cai01|[Cai01] ]]. This seems close to optimal, since there exists an oracle relative to which the collapse cannot be improved to [[Class_Δ2P|Δ2P]] [[ZooRefs#Wil85|[Wil85] ]].



If [[Class_NP|NP]] is not contained in [[Class_P/poly|P/poly]], then [[Class_P|P]] does not equal [[Class_NP|NP]].  Much of the effort toward separating [[Class_P|P]] from [[Class_NP|NP]] is based on this observation.  However, a 'natural proof' as defined by [[ZooRefs#RR97|[RR97] ]] cannot be used to show [[Class_NP|NP]] is outside [[Class_P/poly|P/poly]], if there is any pseudorandom generator in [[Class_P/poly|P/poly]] that has hardness 2^Ω(n^ε)^ for some ε>0.



If [[Class_NP|NP]] is contained in [[Class_P/poly|P/poly]], then [[Class_MA|MA]] = [[Class_AM|AM]] [[ZooRefs#AKS+95|[AKS+95] ]]



The monotone version of [[Class_P/poly|P/poly]] is [[Class_mP/poly|mP/poly]].



[[Class_P/poly|P/poly]] has measure 0 in [[Class_E|E]] with [[Class_Σ2P|Σ2P]] oracle [May94b].



Strictly contains [[Class_IC[log,poly]|IC[log,poly]]] and [[Class_P/log|P/log]].
== Relations ==


== See Also ==

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

== Comments ==

The Political Action Committee for computational complexity research.



The class of problems for which there exists a [[Class_DiffAC0|DiffAC0]] function f such that the answer is "yes" on input x if and only if f(x)>0.



Equals [[Class_TC0|TC0]] and [[Class_C=AC0|C=AC0]] under logspace uniformity [[ZooRefs#ABL98|[ABL98] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_k-PBP|k-PBP]] but with no width restriction.



Equals [[Class_L/poly|L/poly]] [[ZooRefs#Cob66|[Cob66] ]].



Contains [[Class_P-OBDD|P-OBDD]], [[Class_BPd(P)|BPd(P)]].
== Relations ==


== See Also ==

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

== Comments ==

An analog of [[Class_P|P]] for Turing machines over a complex number field.



Defined in [[ZooRefs#BCS+97|[BCS+97] ]].



See also [[Class_PR|PR]], [[Class_NPC|NPC]], [[Class_NPR|NPR]], [[Class_VPk|VPk]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems decidable by a probabilistically checkable debate system, as follows.



Two debaters B and C alternate writing strings on a "debate tape," with B arguing that the answer is "yes" and C arguing the answer is "no."  Then a polynomial-time verifier flips O(r(n)) random coins and makes O(q(n)) nonadaptive queries to the debate tape (meaning that they depend only on the input and the random coins, not the results of previous queries).  The verifier then outputs an answer, which should be correct with high probability.



Defined in [[ZooRefs#CFL+93|[CFL+93] ]], who also showed that PCD(log n, 1) = [[Class_PSPACE|PSPACE]].  This result was used to show that certain problems are PSPACE-hard even to approximate.



Contained in [[Class_GPCD(r(n),q(n))|GPCD(r(n),q(n))]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems such that a "yes" answer can be verified by a probabilistically checkable proof, as follows.



The verifier is a polynomial-time Turing machine with access to O(r(n)) uniformly random bits.  It has random access to a proof (which might be exponentially long), but can query only O(q(n)) bits of the proof.



Then we require the following:



If the answer is "yes," there exists a proof such that the verifier accepts with certainty.

If the answer is "no," then for all proofs the verifier rejects with probability at least 1/2 (over the choice of the O(r(n)) random bits).



Defined in [[ZooRefs#AS98|[AS98] ]].



By definition [[Class_NP|NP]] = PCP(0,poly(n)).



[[Class_MIP|MIP]] = PCP(poly(n),poly(n)).



[[Class_PCP(r(n),q(n))|PCP(r(n),q(n))]] is contained in NTIME(2^O(r(n))^q(n) + poly(n)).



[[Class_NP|NP]] = PCP(log n, log n) [[ZooRefs#AS98|[AS98] ]].



In fact, [[Class_NP|NP]] = PCP(log n, 1) [[ZooRefs#ALM+98|[ALM+98] ]]!



On the other hand, if [[Class_NP|NP]] is contained in PCP(o(log n), o(log n)), then [[Class_P|P]] = [[Class_NP|NP]] [[ZooRefs#FGL+91|[FGL+91] ]].



Also, even though there exists an oracle relative to which [[Class_NP|NP]] = [[Class_EXP|EXP]] [[ZooRefs#Hel84|[Hel84] ]], if we could show there exists an oracle relative to which PCP(log n, 1) = [[Class_EXP|EXP]], then we'd have proved [[Class_P|P]] not equal to [[Class_NP|NP]] [[ZooRefs#For94|[For94] ]].



Another weird oracle fact: since [[Class_NP|NP]] does not equal [[Class_NEXP|NEXP]] [[ZooRefs#SFM78|[SFM78] ]], PCP(0,log n) does not equal PCP(0,poly(n)).  However, there exist oracles relative to which the latter inequality is false [[ZooRefs#HCC+92|[HCC+92] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_P|P]] with access to bits along a closed time curve.



Implicitly defined in [Aar05c], where it was shown that [[Class_PSPACE|PSPACE]] = [[Class_PCTC|PCTC]].



See also [[Class_BQPCTC|BQPCTC]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_EXP|EXP]] as [[Class_PP|PP]] does to [[Class_P|P]].



Is not contained in [[Class_P/poly|P/poly]] [[ZooRefs#BFT98|[BFT98] ]].
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable in time O(t(n)) by a nondeterministic Turing machine, as follows.  The machine is given oracle access to a proof string of unbounded length.



If the answer is "yes," then there exists a value of the proof string such that all computation paths accept.

If the answer is "no," then for all values of the proof string, there exists a computation path that rejects.



Credited in [[ZooRefs#For94|[For94] ]] to S. Arora, [[Class_R|R]]. Impagliazzo, and U. Vazirani.



An interesting question is whether [[Class_NP|NP]] = PFCHK(log n) relative to all possible oracles.  Fortnow [[ZooRefs#For94|[For94] ]] observes that the answer depends on what oracle access mechanism is used.
== Relations ==


== See Also ==

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

== Comments ==

Let Δ,,0,,P = Σ,,0,,P = Π,,0,,P = [[Class_P|P]].  Then for i>0, let



Δ,,i,,P = [[Class_P|P]] with Σ,,i-1,,P oracle.

Σ,,i,,P = [[Class_NP|NP]] with Σ,,i-1,,P oracle.

Π,,i,,P = [[Class_coNP|coNP]] with Σ,,i-1,,P oracle.



Then [[Class_PH|PH]] is the union of these classes for all nonnegative constant i.



[[Class_PH|PH]] can also be defined using alternating quantifiers: it's the class of problems of the form, "given an input x, does there exist a y such that for all z, there exists a w ... such that φ(x,y,z,w,...)," where y,z,w,... are polynomial-size strings and φ is a polynomial-time computable predicate.  It's not totally obvious that this is equivalent to the first definition, since the first one involves adaptive [[Class_NP|NP]] oracle queries and the second one doesn't, but it is.



Defined in [[ZooRefs#Sto76|[Sto76] ]].



Contained in [[Class_P|P]] with a [[Class_PP|PP]] oracle [[ZooRefs#Tod89|[Tod89] ]].



Contains [[Class_BPP|BPP]] [[ZooRefs#Lau83|[Lau83] ]].



Relative to a random oracle, [[Class_PH|PH]] is strictly contained in [[Class_PSPACE|PSPACE]] with probability 1 [[ZooRefs#Cai86|[Cai86] ]].



Furthermore, there exist oracles separating any Σ,,i,,P from Σ,,i+1,,P.  On the other hand, it is unknown whether Σ,,i,,P is strictly contained in Σ,,i+1,,P relative to a random oracle with probability 1 (see [[ZooRefs#Has87|[Has87] ]]).  Book [[ZooRefs#Boo94|[Boo94] ]] shows that if [[Class_PH|PH]] collapses relative to a random oracle with probability 1, then it collapses unrelativized.



It was shown in [CPO7] that if the [[Class_NP|NP]] Machine Hypothesis holds, then

.



For a compendium of problems complete for different classes of the Polynomial Hierarchy see [Sch02a] and [Sch02b].



[[Class_PH|PH]] is equal to the set of boolean queries recognizable by a concurent random acess machine using exponentially many processors and constant time[[ZooRefs#Imm89|[Imm89] ]].



Since [[Class_NP|NP]] is the class of query expressible in second-order existantial logic, [[Class_PH|PH]] can also be defined as the query expressible in second-order logic.
== Relations ==


== See Also ==

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

== Comments ==

The obvious generalization of [[Class_NPcc|NPcc]] and [[Class_coNPcc|coNPcc]] to a nondeterministic hierarchy.



It is unknown whether Σ,,2,,^cc^ equals Π,,2,,^cc^.



Defined in [[ZooRefs#BFS86|[BFS86] ]], where it was also shown (among other things) that [[Class_BPPcc|BPPcc]] is contained in Σ,,2,,^cc^ ∩ Π,,2,,^cc^.
== Relations ==


== See Also ==

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

== Comments ==

(Actually, I've since been informed that [[Class_PINC|PINC]] means "Incremental Polynomial-Time.")



The class of function problems, f:{0,1}^n^->{0,1}^m^, such that the k^th^ output bit is computable in time polynomial in n and k.



Defined in [[ZooRefs#JY88|[JY88] ]].



Contained in [[Class_PIO|PIO]].  This containment is strict, since if m=2^n^ (say), then computing the first bit of f(x) might be EXP-complete.
== Relations ==


== See Also ==

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

== Comments ==

The class of function problems, f:{0,1}^n^->{0,1}^m^, such that f(x) is computable in time polynomial in n and m.  Allows us to discuss whether a function is "efficiently computable" or not, even if the output is too long to write down in polynomial time.



Defined in [[ZooRefs#Yan81|[Yan81] ]].



Strictly contains [[Class_PINC|PINC]].
== Relations ==


== See Also ==

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

== Comments ==

[[Class_P|P]] equipped with an oracle that, given a string x, returns the length of the shortest program that outputs x.



A similar class was defined in [[ZooRefs#ABK+02|[ABK+02] ]], where it was also shown that [[Class_PK|PK]] contains [[Class_PSPACE|PSPACE]].  It is not known whether [[Class_PK|PK]] contains all of [[Class_R|R]], or even any recursive problem not in [[Class_PSPACE|PSPACE]].



See also: [[Class_BPPKT|BPPKT]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_PZK|PZK]] as [[Class_SKC|SKC]] does to [[Class_SZK|SZK]].



Defined in [[ZooRefs#GP91|[GP91] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] that [[Class_PP|PP]] has to [[Class_P|P]].



Contains [[Class_BPL|BPL]].



PL^PL^ = [[Class_PL|PL]] (see [[ZooRefs#HO02|[HO02] ]]).
== Relations ==


== See Also ==

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

== Comments ==

The class of Boolean functions f:{-1,1}^n^->{-1,1} such that the sum of absolute values of Fourier coefficients of f is bounded by a polynomial in n.



Defined in [[ZooRefs#BS90|[BS90] ]], where it was also shown that [[Class_PL1|PL1]] is contained in [[Class_PT1|PT1]] (and this inclusion is strict).
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#Pap90|[Pap90] ]].



I believe it's the same as [[Class_PPA|PPA]].
== Relations ==


== See Also ==

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

== Comments ==

The class of [[Class_TFNP|TFNP]] function problems that are guaranteed to have a solution because of the Lovász Local Lemma.  Defined in [Pap94b].
== Relations ==


== See Also ==

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

== Comments ==

The subclass of [[Class_TFNP|TFNP]] function problems that are guaranteed to have a solution because of the lemma that "every finite directed acyclic graph has a sink."



More precisely, for each input, there's a finite set of solutions (i.e. strings), and a polynomial-time algorithm that computes a cost for each solution, and a neighboring solution of lower cost provided that one exists.  Then the problem is to return any solution that has cost less than or equal to all of its neighbors.  (In other words, a local optimum.)



(Note: In the Zookeeper's humble opinion, [[Class_PLS|PLS]] should have been defined as follows: there exist polynomial-time algorithms that compute the cost of a solution, and the set of all neighbors of a given solution, not just a single solution of lower cost. Of course we'd require that every solution has only polynomially many neighbors.  The two definitions are not obviously equivalent, and it's conceivable that knowing all the neighbors would be helpful -- for example, in simulated annealing one sometimes makes uphill moves.)



(Note to Note: The equivalance of these classes was shown (though not stated explicitly) in Theorem 1 of [[ZooRefs#JPY88|[JPY88] ]].)



Defined in [[ZooRefs#JPY88|[JPY88] ]], [[ZooRefs#PY88|[PY88] ]].



There exists an oracle relative to which [[Class_PLS|PLS]] is not contained in [[Class_FBQP|FBQP]] [[ZooRefs#Aar03|[Aar03] ]].



Also, there exist oracles relative to which [[Class_PLS|PLS]] is not contained in [[Class_PPA|PPA]] [[ZooRefs#BM04|[BM04] ]], and [[Class_PPA|PPA]] and [[Class_PPP|PPP]] are not contained in [[Class_PLS|PLS]] [[ZooRefs#Mor01|[Mor01] ]].



Whether [[Class_PLS|PLS]] is not in [[Class_PPP|PPP]] relative to some oracle remains open.



[[ZooRefs#CT07|[CT07] ]] conjecture that if [[Class_PPAD|PPAD]] is in [[Class_P|P]], then [[Class_PLS|PLS]] is in [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

The class of Boolean functions f:{-1,1}^n^->{-1,1} such that the maximum of |α|^-1^, over all Fourier coefficients α of f, is upper-bounded by a polynomial in n.



Defined in [[ZooRefs#BS90|[BS90] ]], where it was also shown that [[Class_PL∞|PL∞]] contains [[Class_PT1|PT1]] (and this inclusion is strict).
== Relations ==


== See Also ==

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

== Comments ==

See [[Class_Δ2P|Δ2P]].
== Relations ==


== See Also ==

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

== Comments ==

Equals [[Class_P|P]] with 2^k^-1 parallel queries to [[Class_NP|NP]] (i.e. queries that do not depend on the outcomes of previous queries) ([[ZooRefs#BH91|[BH91] ]] and [[ZooRefs#Hem89|[Hem89] ]] independently).



If P^NP[1]^ = P^NP[2]^, then P^NP[1]^ = [[Class_PNP[log]|PNP[log]]] and indeed [[Class_PH|PH]] collapses to Δ,,3,,P (attributed in [Har87b] to J. Kadin).
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a [[Class_P|P]] machine, that can make O(log n) queries to an [[Class_NP|NP]] oracle (where n is the length of the input).



Equals [[Class_P||NP|P||NP]], the class of decision problems solvable by a [[Class_P|P]] machine that can make polynomially many nonadaptive queries to an [[Class_NP|NP]] oracle (i.e. queries that do not depend on the outcomes of previous queries) ([[ZooRefs#BH91|[BH91] ]] and [[ZooRefs#Hem89|[Hem89] ]] independently).



[[Class_PNP[log]|PNP[log]]] is contained in [[Class_PP|PP]] [[ZooRefs#BHW89|[BHW89] ]].



Determining the winner in an election system proposed in 1876 by Charles Dodgson (a.k.a. Lewis Carroll) has been shown to be complete for [[Class_PNP[log]|PNP[log]]] [[ZooRefs#HHR97|[HHR97] ]].



Contains [[Class_PNP[k]|PNP[k]]] for all constants k.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_PNP[log]|PNP[log]]], except that now log^2^ queries can be made.



The model-checking problem for a certain temporal logic is P^NP[log^2]^-complete [[ZooRefs#Sch03|[Sch03] ]].



For all k, [[Class_P|P]] with log^k^ adaptive queries to [[Class_NP|NP]] coincides with [[Class_P|P]] with log^k+1^ nonadaptive queries [[ZooRefs#CS92|[CS92] ]].
== Relations ==


== See Also ==

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

== Comments ==

The subclass of [[Class_TFNP|TFNP]] function problems that are guaranteed to have a solution because of the lemma that "every finite graph has an even number of odd-degree nodes."



Equals [[Class_PPA|PPA]] [[ZooRefs#Pap90|[Pap90] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is 'yes' then at least 1/2 of computation paths accept.

If the answer is 'no' then less than 1/2 of computation paths accept.



Defined in [[ZooRefs#Gil77|[Gil77] ]].



[[Class_PP|PP]] is closed under union and intersection [[ZooRefs#BRS91|[BRS91] ]] (this was an open problem for 14 years).



Contains [[Class_PNP[log]|PNP[log]]] [[ZooRefs#BHW89|[BHW89] ]].



Equals PP^BPP^ [KST+89b] as well as [[Class_PostBQP|PostBQP]] [Aar05b].



However, there exists an oracle relative to which [[Class_PP|PP]] does not contain [[Class_Δ2P|Δ2P]] [[ZooRefs#Bei94|[Bei94] ]].



[[Class_PH|PH]] is in [[Class_PPP|PPP]] [[ZooRefs#Tod89|[Tod89] ]].



[[Class_BQP|BQP]] is low for [[Class_PP|PP]]; i.e. PP^BQP^ = [[Class_PP|PP]] [[ZooRefs#FR98|[FR98] ]].



For a random oracle A, [[Class_PPA|PPA]] is strictly contained in PSPACE^A^ with probability 1 [[ZooRefs#ABF+94|[ABF+94] ]].



For any fixed k, there exists a language in [[Class_PP|PP]] that does not have circuits of size n^k^ [Vin04b].  Indeed, there exists a language in [[Class_PP|PP]] that does not even have quantum circuits of size n^k^ with quantum advice [[ZooRefs#Aar06|[Aar06] ]].



By contrast, there exists an oracle relative to which [[Class_PP|PP]] has linear-size circuits [[ZooRefs#Aar06|[Aar06] ]].



[[Class_PP|PP]] can be generalized to the counting hierarchy [[Class_CH|CH]].
== Relations ==


== See Also ==

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

== Comments ==

Contains [[Class_BQP/qpoly|BQP/qpoly]] [Aar04b].



If [[Class_PP/poly|PP/poly]] = [[Class_P/poly|P/poly]] then [[Class_PP|PP]] is contained in [[Class_P/poly|P/poly]].  Indeed this is true with any syntactically defined class in place of [[Class_PP|PP]].  An implication is that any unrelativized separation of [[Class_BQP/qpoly|BQP/qpoly]] from [[Class_BQP/mpoly|BQP/mpoly]] would imply that [[Class_PP|PP]] does not have polynomial-size circuits.
== Relations ==


== See Also ==

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

== Comments ==

Defined in [Pap94b]; see also [[ZooRefs#BCE+95|[BCE+95] ]].



The subclass of [[Class_TFNP|TFNP]] function problems that are guaranteed to have a solution because of the lemma that "all graphs of maximum degree 2

have an even number of leaves."



More precisely, there's a polynomial-time algorithm that, given any string, computes its 'neighbor' strings (of which there are at most two). Then given a leaf string (i.e. one with only one neighbor), the problem is to output another leaf string.



As an example, suppose you're given a cubic graph (one where every vertex has degree 3), and a Hamiltonian cycle H on that graph.  Then by making a sequence of modifications to H (albeit possibly exponentially many), it is always possible to find a second Hamilton cycle (see [[ZooRefs#Pap94|[Pap94] ]]).  So this problem is in [[Class_PPA|PPA]].



Another problem in [[Class_PPA|PPA]] is finding an Arrow-Debreu equilibrium, given the goods and utility functions of traders in a marketplace.



Contained in [[Class_TFNP|TFNP]].



Contains [[Class_PPAD|PPAD]].



There exist oracles relative to which [[Class_PPA|PPA]] does not contain [[Class_PLS|PLS]] [[ZooRefs#BM04|[BM04] ]] and [[Class_PPP|PPP]] [[ZooRefs#BCE+95|[BCE+95] ]].  There also exists an oracle relative to which [[Class_PPA|PPA]] is not contained in [[Class_PPP|PPP]] [[ZooRefs#BCE+95|[BCE+95] ]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [Pap94b]; see also [[ZooRefs#BCE+95|[BCE+95] ]].



Same as [[Class_PPA|PPA]], except now the graph is directed, and we're asked to find either a source or a sink.



Contained in [[Class_PPA|PPA]] and [[Class_PPADS|PPADS]].



NASH, the problem of finding a Nash equilibrium in a normal form game of two or more players with specified utilities, is in [[Class_PPAD|PPAD]] [Pap94b], and proved to be complete for [[Class_PPAD|PPAD]] with four players in [[ZooRefs#DGP05|[DGP05] ]], and shortly after extended to the case of three players [[ZooRefs#DP05|[DP05] ]] and independently [[ZooRefs#CD05|[CD05] ]].



There exists an oracle relative to which [[Class_PPP|PPP]] is not contained in [[Class_PPAD|PPAD]] [[ZooRefs#BCE+95|[BCE+95] ]].

There exists an oracle relative to which [[Class_PPAD|PPAD]] is not contained in [[Class_BQP|BQP]] [[ZooRefs#Li11|[Li11] ]].



There exists an oracle relative to which [[Class_PPP|PPP]] is not contained in [[Class_PPAD|PPAD]] [[ZooRefs#BCE+95|[BCE+95] ]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [Pap94b]; see also [[ZooRefs#BCE+95|[BCE+95] ]].



Same as [[Class_PPA|PPA]], except now the graph is directed, and we're asked to find a sink.



Contained in [[Class_PPP|PPP]].



Contains [[Class_PPAD|PPAD]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [Pap94b]; see also [[ZooRefs#BCE+95|[BCE+95] ]].



The subclass of [[Class_TFNP|TFNP]] function problems that are guaranteed to have a solution because of the Pigeonhole Principle.



More precisely, we're given a Boolean circuit, that maps n-bit strings to n-bit strings.  The problem is to return either an input that maps to 0^n^, or two inputs that map to the same output.



Contained in [[Class_TFNP|TFNP]].



Contains [[Class_PPADS|PPADS]].



[[ZooRefs#BCE+95|[BCE+95] ]] give oracles relative to which [[Class_PPP|PPP]] is not contained in [[Class_PPA|PPA]] and [[Class_PPAD|PPAD]], and [[Class_PPA|PPA]] is not contained in [[Class_PPP|PPP]].



[[ZooRefs#Mor01|[Mor01] ]] gives an oracle relative to which [[Class_PPP|PPP]] is not contained in [[Class_PLS|PLS]].



Whether [[Class_PLS|PLS]] is not contained in [[Class_PPP|PPP]] relative to some oracle remains open.



A level of the counting hierarchy [[Class_CH|CH]].



It is not known whether there exists an oracle relative to which [[Class_PPP|PPP]] does not equal [[Class_PSPACE|PSPACE]].



Contains PP^PH^ [[ZooRefs#Tod89|[Tod89] ]].



Equals [[Class_P#P|P#P]] (exercise for the visitor).



Since the permanent of a matrix is #P-complete [[ZooRefs#Val79|[Val79] ]], Toda's theorem implies that any problem in the polynomial hierarchy can be solved by computing a sequence of permanents.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_IPP|IPP]], except that [[Class_IPP|IPP]] uses private coins while [[Class_PPSPACE|PPSPACE]] uses public coins.



Can also be defined as a probabilistic version of [[Class_PSPACE|PSPACE]].



Equals [[Class_PSPACE|PSPACE]].



Defined in [[ZooRefs#Pap83|[Pap83] ]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#BFS86|[BFS86] ]], [[Class_PPcc|PPcc]] is one of two ways to define a communication complexity analogue of [[Class_PP|PP]]. In [[Class_PPcc|PPcc]], we note that in an algorithm that uses an amount of random bits bounded by , the bias between the accept and reject probabilities can be no smaller than . Thus, in [[Class_PPcc|PPcc]], the communication complexity is defined as the sum of the traditional communication complexity (the number of exchanged bits) and the log of the reciprocal of the worst-case (smallest) bias.



The difference between this class and [[Class_UPPcc|UPPcc]] is discussed further in [[ZooRefs#BVW07|[BVW07] ]], where it is shown that [[Class_PPcc|PPcc]] ⊂ [[Class_UPPcc|UPPcc]].



See Also: [[Class_UPPcc|UPPcc]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable in polynomial space using at most a polynomial number of queries to the oracle.



Thus, [[Class_PQUERY|PQUERY]] = [[Class_PSPACE|PSPACE]], but PQUERY^A^ does not equal PSPACE^A^ for some oracles A.



Defined in [[ZooRefs#Kur83|[Kur83] ]], where it was actually put forward as a serious argument (!!) against believing relativization results.
== Relations ==


== See Also ==

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

== Comments ==

Basically, the class of functions definable by recursively building up arithmetic functions: addition, multiplication, exponentiation, tetration, etc.  What's not allowed is to "diagonalize" a whole series of such functions to produce an even faster-growing one.  Thus, the Ackermann function was proposed in 1928 as an example of a recursive function that's not primitive recursive, showing that [[Class_PR|PR]] is strictly contained in [[Class_R|R]].



Alternatively, the [[Class_PR|PR]] functions are exactly those functions that can be computed via programs in any reasonable, idealized ALGOL-like programming language where only definite loops are allowed, that is, loops where the number of iterations is specified before the loop starts (so FOR-loops are okay but not WHILE- or REPEAT-loops), and recursive calls are not allowed.



An interesting difference is that [[Class_PR|PR]] functions can be explicitly enumerated, whereas functions in [[Class_R|R]] cannot be (since otherwise the halting problem would be decidable).  That is, [[Class_PR|PR]] is a "syntactic" class whereas [[Class_R|R]] is "semantic."



On the other hand, we can "enumerate" any [[Class_RE|RE]] set by a [[Class_PR|PR]] function in the following sense: given an input (M,k), where M is a Turing machine and k is an integer, if M halts within k steps then output M; otherwise output nothing.  Then the union of the outputs, over all possible inputs (M,k), is exactly the set of M that halt.



[[Class_PR|PR]] strictly contains [[Class_ELEMENTARY|ELEMENTARY]].



An analog of [[Class_P|P]] for Turing machines over a real number field.



Defined in [[ZooRefs#BCS+97|[BCS+97] ]].



See also [[Class_PC|PC]], [[Class_NPC|NPC]], [[Class_NPR|NPR]], [[Class_VPk|VPk]].
== Relations ==


== See Also ==

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

== Comments ==

Yeah, I'm told that's what the S and [[Class_K|K]] stand for.  Go figure.



The class of total function problems definable as follows: given a directed graph of indegree and outdegree at most 1, and given a source, find a sink.



Defined in [[ZooRefs#Pap90|[Pap90] ]].



Equals [[Class_PPADS|PPADS]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a Turing machine in polynomial space.



Equals [[Class_NPSPACE|NPSPACE]] [[ZooRefs#Sav70|[Sav70] ]], [[Class_AP|AP]] [[ZooRefs#CKS81|[CKS81] ]], [[Class_IP|IP]] [[ZooRefs#Sha90|[Sha90] ]], and, assuming the existence of one-way functions, [[Class_CZK|CZK]] [[ZooRefs#BGG+90|[BGG+90] ]].



Contains [[Class_P|P]] with [[Class_#P|#P]] oracle.



A canonical PSPACE-complete problem is QBF.



Relative to a random oracle, [[Class_PSPACE|PSPACE]] strictly contains [[Class_PH|PH]] with probability 1 [[ZooRefs#Cai86|[Cai86] ]].



[[Class_PSPACE|PSPACE]] has a complete problem that is both downward self-reducible and random self-reducible [[ZooRefs#TV02|[TV02] ]].  It is the largest class with such a complete problem.



Contained in [[Class_EXP|EXP]].  There exists an oracle relative to which this containment is proper [[ZooRefs#Dek76|[Dek76] ]].



In descriptive complexity, [[Class_PSPACE|PSPACE]] can be defined with 4 differents kind of formulae, FO() which is also [[Class_FO(PFP)|FO(PFP)]] and SO() which is also SO(TC).



A canonical PSPACE-complete problem is Quantified Boolean Formula (QBF): Given a Boolean formula with universal and existential quantifiers, decide whether it's true or false.
== Relations ==


== See Also ==

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

== Comments ==

Contains [[Class_QMA/qpoly|QMA/qpoly]] [Aar06b].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a uniform family of Boolean circuits with depth upper-bounded by f(n) and size (number of gates) upper-bounded by g(n).



The union of PT/WK(log^k^n, n^k^) over all constants k equals [[Class_NC|NC]].
== Relations ==


== See Also ==

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

== Comments ==

The class of Boolean functions f:{-1,1}^n^->{-1,1} such that f(x)=sgn(p(x)), where p is a polynomial having a number of terms polynomial in n.



Defined in [[ZooRefs#BS90|[BS90] ]], where it was also shown that [[Class_PT1|PT1]] contains [[Class_PL1|PL1]] (and this inclusion is strict), and that [[Class_PT1|PT1]] is contained in [[Class_PL∞|PL∞]] (and this inclusion is strict).
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

The subclass of [[Class_NPO|NPO]] problems that admit an approximation scheme in the following sense.  For any ε>0, there is a polynomial-time algorithm that is guaranteed to find a solution whose cost is within a 1+ε factor of the optimum cost.  (However, the exponent of the polynomial might depend strongly on ε.)



Contains [[Class_FPTAS|FPTAS]], and is contained in [[Class_APX|APX]].



As an example, the Traveling Salesman Problem in the Euclidean plane is in [[Class_PTAS|PTAS]] [[ZooRefs#Aro96|[Aro96] ]].



Defined in [[ZooRefs#ACG+99|[ACG+99] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_SZK|SZK]], but now the two distributions must be identical, not merely statistically close.  (The "two distributions" are (1) the distribution over the verifier's view of his interaction with the prover, conditioned on the verifier's random coins, and (2) the distribution over views that the verifier can simulate without the prover's help.)



Contained in [[Class_SZK|SZK]].



See also: [[Class_CZK|CZK]].



Same as [[Class_SZK|SZK]], but now the two distributions must be identical, not merely statistically close.  (The "two distributions" are (1) the distribution over Arthur's view of his interaction with Merlin, conditioned on Arthur's random coins, and (2) the distribution over views that Arthur can simulate without Merlin's help.)
== Relations ==


== See Also ==

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

== Comments ==

In a two-party communication complexity problem, Alice and Bob have n-bit strings x and y respectively, and they wish to evaluate some Boolean function f(x,y) using as few bits of communication as possible.  [[Class_Pcc|Pcc]] is the class of (infinite families of) f's, such that the amount of communication needed is only O(polylog(n)), even if Alice and Bob are restricted to a deterministic protocol.



Note that all functions of the form above are solvable given  bits of communication, since no bounds are placed on the computational abilities of Alice and Bob. Thus, when discussing this class, "polynomially" is sometimes used in place of "polylogarithmically."



Is strictly contained in [[Class_NPcc|NPcc]] and in [[Class_BPPcc|BPPcc]] because of the EQUALITY problem.



Equals [[Class_NPcc|NPcc]] ∩ [[Class_coNPcc|coNPcc]].



Defined in [[ZooRefs#BFS86|[BFS86] ]].



Like [[Class_Pcc|Pcc]], but with  players, where each player can see all of the other player's bits, but not their own. Intuitively, each player has their bits written on their forehead.



More formally, [[Class_Pcc|Pcc]] is the class of functions  where for all , , such that  is solvable in a deterministic sense by  players, each of which is aware of all inputs  other than his own, and such that  bits of communication are used.



[[Class_Pcc|Pcc]] is trivially contained in [[Class_BPPcc|BPPcc]], [[Class_RPcc|RPcc]] and [[Class_NPcc|NPcc]].
== Relations ==


== See Also ==

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

== Comments ==

The class of languages [[Class_L|L]] in [[Class_UP|UP]] such that the mapping from an input x to the unique witness for x is a permutation of [[Class_L|L]].



Contains [[Class_P|P]].



Defined in [[ZooRefs#HT03|[HT03] ]], where it was also shown that the closure of [[Class_PermUP|PermUP]] under polynomial-time one-to-one reductions is [[Class_UP|UP]].



On the other hand, they show that if [[Class_PermUP|PermUP]] = [[Class_UP|UP]] then [[Class_E|E]] = [[Class_UE|UE]].



See also: [[Class_SelfNP|SelfNP]].
== Relations ==


== See Also ==

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

== Comments ==

Defined by Valiant [[ZooRefs#Val03|[Val03] ]] to be "the class of physically constructible polynomial resource computers" (characterizing what "can be computed in the physical world in practice").  There he says that [[Class_PhP|PhP]] contains [[Class_P|P]] and [[Class_BPP|BPP]], but that it is open whether [[Class_PhP|PhP]] contains [[Class_BQP|BQP]], since no scalable quantum computing proposal has been demonstrated beyond reasonable doubt.



For what it's worth, the present zookeeper has more qualms about admitting DTIME(n^1000^) into [[Class_PhP|PhP]] than BQTIME(n^2^).  It is very possible that the total number of bits or bit tranisitions that can be witnessed by any one observer in the universe is finite.  (Recent observations of the cosmological constant combined with plausible fundamental physics yields a bound of 10^k^ with k in the low hundreds.)  In practice, less than 10^50^ bits and less than 10^80^ bit transitions are available for human use.  (This is combining the number of atoms in the Earth with the number of signals that they can exchange in a millenium.)



The present veterinarian concurs that [[Class_PhP|PhP]] is an unhealthy animal, although it is valid to ask whether [[Class_BQP|BQP]] is a realistic class.
== Relations ==


== See Also ==

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

pagename = u"Class_PostBQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= PostBQP - BQP With Postselection =

== Comments ==

A class inspired by the proverb, "if at first you don't succeed, try, try again."



Formally, the class of decision problems solvable by a [[Class_BQP|BQP]] machine such that



If the answer is 'yes' then the second qubit has at least 2/3 probability of being measured 1, conditioned on the first qubit having been measured 1.

If the answer is 'no' then the second qubit has at most 1/3 probability of being measured 1, conditioned on the first qubit having been measured 1.

On any input, the first qubit has a nonzero probability of being measured 1.



Defined in [Aar05b], where it is also shown that [[Class_PostBQP|PostBQP]] equals [[Class_PP|PP]].



[Aar05b] also gives the following alternate characterizations of [[Class_PostBQP|PostBQP]] (and therefore of PP):



The quantum analogue of [[Class_BPPpath|BPPpath]].

The class of problems solvable in quantum polynomial time if we allow arbitrary linear operations (not just unitary ones). Before measuring, we divide all amplitudes by a normalizing factor to make the probabilities sum to 1.

The class of problems solvable in quantum polynomial time if we take the probability of measuring a basis state with amplitude α to be not |α|^2^ but |α|^p^, where p is an even integer greater than 2.  (Again we need to divide all amplitudes by a normalizing factor to make the probabilities sum to 1.)
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_DSPACE(f(n))|DSPACE(f(n))]] as [[Class_PP|PP]] does to [[Class_P|P]].  The Turing machine has to halt on every input and every setting of the random tape.



Equals [[Class_PrSPACE(f(n))|PrSPACE(f(n))]] [[ZooRefs#Jun85|[Jun85] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_DSPACE(f(n))|DSPACE(f(n))]] as [[Class_PP|PP]] does to [[Class_P|P]].  The Turing machine has to halt with probability 1 on every input.



Contained in DSPACE(f(n)^2^) [[ZooRefs#BCP83|[BCP83] ]].



Equals [[Class_PrHSPACE(f(n))|PrHSPACE(f(n))]] [[ZooRefs#Jun85|[Jun85] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_PromiseRP|PromiseRP]], but for [[Class_BPP|BPP]] instead of [[Class_RP|RP]].



Defined in [[ZooRefs#BF99|[BF99] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_PromiseBPP|PromiseBPP]], but for [[Class_BQP|BQP]] instead of [[Class_BPP|BPP]].



If [[Class_PromiseBQP|PromiseBQP]] = [[Class_PromiseP|PromiseP]] then [[Class_BQP/mpoly|BQP/mpoly]] = [[Class_P/poly|P/poly]].



Same as [[Class_PromiseBQP|PromiseBQP]], but for [[Class_BQP|BQP]] instead of [[Class_BPP|BPP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of promise problems solvable by a [[Class_P|P]] machine.
== Relations ==


== See Also ==

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

== Comments ==

The class of promise problems solvable by an [[Class_RP|RP]] machine. I.e., the machine must accept with probability at least 1/2 for "yes" inputs, and with probability 0 for "no" inputs, but could have acceptance probability between 0 and 1/2 for inputs that do not satisfy the promise.



Defined in [[ZooRefs#BF99|[BF99] ]], where it was also shown that [[Class_BPP|BPP]] is in RP^PromiseRP[1]^ (i.e. with a single oracle query to PromiseRP).



Contained in [[Class_PromiseBPP|PromiseBPP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of promise problems solvable by an [[Class_UP|UP]] machine. I.e., the nondeterministic machine must have a unique accepting path for "yes" inputs, and no accepting paths "no" inputs, but could have any number of accepting paths for inputs that do not satisfy the promise.



Although not originally stated with this notation, the main result of [[ZooRefs#VV86|[VV86] ]] is that [[Class_NP|NP]] is contained in RP^PromiseUP^.
== Relations ==


== See Also ==

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

== Comments ==

Equals [[Class_PNP[log]|PNP[log]]] ([[ZooRefs#BH91|[BH91] ]] and [[ZooRefs#Hem89|[Hem89] ]] independently).
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a nondeterministic multitape Turing machine in linear time. Defined in [[ZooRefs#BG69|[BG69] ]], where it was shown that [[Class_Q|Q]] equals the class of problems solvable by a nondeterministic multitape Turing machine in exactly n steps (as opposed to O(n) steps).



Contains [[Class_GCSL|GCSL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a family of constant-depth, polynomial-size quantum circuits.  Here each layer of the circuit is a tensor product of one-qubit gates and Toffoli gates, or is a tensor product of controlled-NOT gates.



A uniformity condition may also be imposed.



Defined in [[ZooRefs#Moo99|[Moo99] ]].



It is contained in [[Class_QACf0|QACf0]], but it is not known if it contains [[Class_AC0|AC0]]. Notice that the latter containment is not obvious, since the set of gates in [[Class_QAC0|QAC0]] do not allow to implement fanout in any way we may take for granted.



Contains [[Class_AC0|AC0]], and is contained in [[Class_QACf0|QACf0]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QAC0|QAC0]], except that now Mod-m gates are also allowed.  A Mod-m gate computes whether the sum of a given set of bits is congruent to 0 modulo m, and exclusive-OR's the answer into another bit.



Defined in [[ZooRefs#Moo99|[Moo99] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QAC0[m]|QAC0[m]]], except that Mod-m gates are allowed for any m.



Defined in [[ZooRefs#Moo99|[Moo99] ]].



[[ZooRefs#GHP00|[GHP00] ]] showed that [[Class_QACC0|QACC0]] equals QAC^0^[p] for any prime p.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QAC0|QAC0]], except that an additional "quantum fanout" gate is available, which CNOT's a qubit into arbitrarily many target qubits in a single step.



Defined in [[ZooRefs#Moo99|[Moo99] ]], where it was also shown that [[Class_QACf0|QACf0]] =

QAC^0^[2] = [[Class_QACC0|QACC0]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a "yes" answer can be verified by a public-coin quantum [[Class_AM|AM]] protocol, as follows.  Arthur generates a uniformly random (classical) string and sends it to Merlin.  Merlin responds with a polynomial-size quantum certificate, on which Arthur can perform any [[Class_BQP|BQP]] operation.  The completeness and soundness requirements are the same as for [[Class_AM|AM]].



Defined by Marriott and Watrous [[ZooRefs#MW05|[MW05] ]].



Contains [[Class_QMA|QMA]] and is contained in [[Class_QIP[2]|QIP[2]]] and BP•PP (and therefore PSPACE).
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems recognized by quantum context-free languages, which are defined in [[ZooRefs#MC00|[MC00] ]].  The authors also showed that [[Class_QCFL|QCFL]] does not equal [[Class_CFL|CFL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a "yes" answer can be verified by a quantum computer with access to a classical proof. Also known as the subclass of of [[Class_QMA|QMA]] with classical witnesses.



Called MQA by Watrous [[ZooRefs#Wat09|[Wat09] ]].



Contains [[Class_MA|MA]], and is contained in [[Class_QMA|QMA]].



Given a black-box group G and a subgroup H, the problem of testing non-membership in H has polynomial [[Class_QCMA|QCMA]] query complexity [[ZooRefs#AK06|[AK06] ]].



See [[ZooRefs#AK06|[AK06] ]] for a "quantum oracle separation" between [[Class_QCMA|QCMA]] and [[Class_QMA|QMA]].  No classical oracle separation between [[Class_QCMA|QCMA]] and [[Class_QMA|QMA]] is currently known.



The class of decision problems for which a "yes" answer can be verified by a quantum computer with access to a classical proof.
== Relations ==


== See Also ==

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

== Comments ==

QH,,k,, is defined to be [[Class_PNP[k]|PNP[k]]]; that is, [[Class_P|P]] with k queries to an [[Class_NP|NP]] oracle (where k is a constant).  Then [[Class_QH|QH]] is the union of QH,,k,, over all nonnegative k.



[[Class_QH|QH]] = [[Class_BH|BH]] [[ZooRefs#Wag88|[Wag88] ]]; thus, either both hierarchies are infinite or both collapse to some finite level.



QH,,i,, is defined to be [[Class_PNP[k]|PNP[k]]]; that is, [[Class_P|P]] with k queries to an [[Class_NP|NP]] oracle (where k is a constant).  Then [[Class_QH|QH]] is the union of QH,,i,, over all nonnegative i.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems such that a "yes" answer can be verified by a quantum interactive proof.  Here the verifier is a [[Class_BQP|BQP]] (i.e. quantum polynomial-time) algorithm, while the prover has unbounded computational resources (though cannot violate the linearity of quantum mechanics). The prover and verifier exchange a polynomial number of messages, which can be quantum states.  Thus, the verifier's and prover's states may become entangled during the course of the protocol.  Given the verifier's algorithm, we require that



If the answer is "yes," then the prover can behave in such a way that the verifier accepts with probability at least 2/3.

If the answer is "no," then however the prover behaves, the verifier rejects with probability at least 2/3.



Let QIP[k] be [[Class_QIP|QIP]] where the prover and verifier are restricted to exchanging k messages (with the prover going last).



Defined in [[ZooRefs#Wat99|[Wat99] ]], where it was also shown that [[Class_PSPACE|PSPACE]] is in QIP[3].



Subsequently [[ZooRefs#KW00|[KW00] ]] showed that for all k>3, QIP[k] = QIP[3] = [[Class_QIP|QIP]].



[[Class_QIP|QIP]] is contained in [[Class_EXP|EXP]] [[ZooRefs#KW00|[KW00] ]].



[[Class_QIP|QIP]] = [[Class_IP|IP]] = [[Class_PSPACE|PSPACE]] [[ZooRefs#JJUW09|[JJUW09] ]]; thus quantum computing adds no power to interactive proofs.



QIP(1) is more commonly known as [[Class_QMA|QMA]].



See also: [[Class_QIP[2]|QIP[2]]], [[Class_QSZK|QSZK]].
== Relations ==


== See Also ==

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

== Comments ==

See [[Class_QIP|QIP]] for definition.



Contains [[Class_QSZK|QSZK]] [[ZooRefs#Wat02|[Wat02] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems that can be decided in quasi-linear time by a multitape deterministic Turing machine.  Quasi-linear time here means n(log n)^k^ + k, for some k.



Defined in [[ZooRefs#Sch78|[Sch78] ]].



See also: [[Class_Q|Q]], [[Class_NQL|NQL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems such that a "yes" answer can be verified by a 1-message quantum interactive proof.  That is, a [[Class_BQP|BQP]] (i.e. quantum polynomial-time) verifier is given a quantum state (the "proof").  We require that



If the answer is "yes," then there exists a state such that verifier accepts with probability at least 2/3.

If the answer is "no," then for all states the verifier rejects with probability at least 2/3.



[[Class_QMA|QMA]] = QIP(1).



Defined in [[ZooRefs#Wat00|[Wat00] ]], where it is also shown that group non-membership is in [[Class_QMA|QMA]].



Based on this, [[ZooRefs#Wat00|[Wat00] ]] gives an oracle relative to which [[Class_MA|MA]] is strictly contained in [[Class_QMA|QMA]].



Kitaev and Watrous (unpublished) showed [[Class_QMA|QMA]] is contained in [[Class_PP|PP]] (see [[ZooRefs#MW05|[MW05] ]] for a proof).  Combining that result with [[ZooRefs#Ver92|[Ver92] ]], one can obtain an oracle relative to which [[Class_AM|AM]] is not in [[Class_QMA|QMA]].



Kitaev ([[ZooRefs#KSV02|[KSV02] ]], see also [[ZooRefs#AN02|[AN02] ]]) showed that the 5-Local Hamiltonians Problem is QMA-complete. Subsequently, Kempe and Regev [[ZooRefs#KR03|[KR03] ]] showed that even 3-Local Hamiltonians is QMA-complete.  A subsequent paper by Kempe, Kitaev, and Regev [[ZooRefs#KKR04|[KKR04] ]], has hit rock bottom (assuming [[Class_P|P]] does not equal QMA), by showing 2-local Hamiltonians QMA-complete.



Compare to [[Class_NQP|NQP]].



If [[Class_QMA|QMA]] = [[Class_PP|PP]] then [[Class_PP|PP]] contains [[Class_PH|PH]] [[ZooRefs#Vya03|[Vya03] ]].  This result uses the fact that [[Class_QMA|QMA]] is contained in [[Class_A0PP|A0PP]].



Approximating the ground state energy of a system composed of a line of quantum particles is QMA-complete [[ZooRefs#AGK07|[AGK07] ]].



See also: [[Class_QCMA|QCMA]], [[Class_QMA/qpoly|QMA/qpoly]], [[Class_QSZK|QSZK]], [[Class_QMA(2)|QMA(2)]], [[Class_QMA-plus|QMA-plus]].



Defined in [[ZooRefs#Wat00|[Wat00] ]], where it is also shown that group non-membership is in [[Class_QMA|QMA]].  That is: let G be a group, whose elements are represented by polynomial-size strings.  We're given a "black box" that correctly multiplies and inverts elements of G.  Then given elements g and h,,1,,,...,h,,k,,, we can verify in [[Class_QMA|QMA]] that g is not in the subgroup generated by h,,1,,,...,h,,k,,.



Kitaev and Watrous (unpublished) showed [[Class_QMA|QMA]] is contained in [[Class_PP|PP]].  Combining that result with [[ZooRefs#Ver92|[Ver92] ]], one can obtain an oracle relative to which [[Class_AM|AM]] is not in [[Class_QMA|QMA]].



[[ZooRefs#KSV02|[KSV02] ]]



[[ZooRefs#AN02|[AN02] ]]



5-Local Hamiltonians.  Given an n-qubit Hilbert space, as well as a collection H,,1,,,...,H,,k,, of Hamiltonians (i.e. Hermitian positive semidefinite matrices), each of which acts on at most 5 qubits of the space.  Also given reals a,b such that b-a = Θ(1/poly(n)).  Decide whether the smallest eigenvalue of H=H,,1,,+...+H,,k,, is less than a or greater than b, promised that one of these is the case.



Subsequently Kempe and Regev [[ZooRefs#KR03|[KR03] ]] showed that even 3-Local Hamiltonians is QMA-complete.  A subsequent paper by Kempe, Kitaev, and Regev [[ZooRefs#KKR04|[KKR04] ]], has hit rock bottom (assuming [[Class_P|P]] does not equal QMA), by showing 2-local Hamiltonians QMA-complete.



[[Class_NQP|NQP]]
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QMA|QMA]], except that now the verifier is given two polynomial-size quantum certificates, which are guaranteed to be unentangled.



Defined in [[ZooRefs#KMY01|[KMY01] ]].



It was shown in [[ZooRefs#ABD+08|[ABD+08] ]] that a conjecture they call the Strong Amplification Conjecture implies that [[Class_QMA(2)|QMA(2)]] is contained in [[Class_PSPACE|PSPACE]]. The authors also show that there exists no perfectly disentangler that can be used to simulate [[Class_QMA(2)|QMA(2)]] in [[Class_QMA|QMA]], though other approaches to showing [[Class_QMA|QMA]] = [[Class_QMA(2)|QMA(2)]] may still exist.



It was shown in [[ZooRefs#HM13|[HM13] ]] that QMA(k) = [[Class_QMA(2)|QMA(2)]] for k >= 2. However we still do not know if [[Class_QMA(2)|QMA(2)]] = [[Class_QMA|QMA]] and we also do not know any upper bound for [[Class_QMA(2)|QMA(2)]] better than [[Class_NEXP|NEXP]].



Defined in [[ZooRefs#KMY01|[KMY01] ]].  It is unknown whether QMA(k) = [[Class_QMA(2)|QMA(2)]] for all k>2, and also whether [[Class_QMA(2)|QMA(2)]] = [[Class_QMA|QMA]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QMA|QMA]], except now the verifier can directly obtain the probability that a given observable of the certificate state, if measured, would equal 1.  (In the usual model, by contrast, one can only sample an observable.)



Defined in [[ZooRefs#AR03|[AR03] ]], where it was also shown that [[Class_QMA-plus|QMA-plus]] = [[Class_QMA|QMA]].
== Relations ==


== See Also ==

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

== Comments ==

Is contained in [[Class_PSPACE/poly|PSPACE/poly]] [Aar06b].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QMA|QMA]] except that for a "yes" instance, there exists a state that is accepted with probability 1.



Defined in [[ZooRefs#Bra06|[Bra06] ]]. It was shown there that Quantum k-SAT is QMA,,1,,-complete for any . It was also shown there that Quantum 2-SAT is in [[Class_P|P]].



This result was later improved in [[ZooRefs#GN13|[GN13] ]] where it was shown that Quantum 3-SAT is QMA,,1,,-complete.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a "yes" answer can be verified by a public-coin quantum MAM protocol, as follows.  Merlin sends a polynomial-size quantum state to Arthur.  Arthur then flips some classical coins (in fact, he only has to flip one without loss of generality) and sends the outcome to Merlin.  At this stage Arthur is not yet allowed to perform any quantum operations.  Merlin then sends Arthur another quantum state.  Finally, Arthur performs a [[Class_BQP|BQP]] operation on both of the states simultaneously, and either accepts or rejects.  The completeness and soundness requirements are the same as for [[Class_AM|AM]].  Also, Merlin's messages might be entangled.



Defined by Marriott and Watrous [[ZooRefs#MW05|[MW05] ]], who also showed that [[Class_QMAM|QMAM]] = QIP(3) = [[Class_QIP|QIP]].



Hence [[Class_QMAM|QMAM]] contains [[Class_PSPACE|PSPACE]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QMA|QMA]] except that the quantum proof has O(log n) qubits instead of a polynomial number.



Equals [[Class_BQP|BQP]] [[ZooRefs#MW05|[MW05] ]].
== Relations ==


== See Also ==

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

== Comments ==

The quantum generalization of [[Class_MIP|MIP]], and the multi-prover generalization of [[Class_QIP|QIP]].



A quantum multi-prover interactive proof system is the same as a classical one, except that all messages and verifier computations are quantum.  As in [[Class_MIP|MIP]], there is no communication among the provers; however, the provers share unlimited prior entanglement.  The number of provers and number of rounds can both be polynomial in n.



Defined in [[ZooRefs#KM02|[KM02] ]].



Shown to be equal to [[Class_MIP*|MIP*]] in [[ZooRefs#RUV12|[RUV12] ]].



[[Class_QMIP|QMIP]] contains [[Class_NEXP|NEXP]] simply because [[Class_MIP*|MIP*]] contains [[Class_NEXP|NEXP]] [[ZooRefs#IV12|[IV12] ]]. Since we know that [[Class_NEXP|NEXP]] = [[Class_QMIPne|QMIPne]], this tells us that giving the provers unlimited prior entanglement does not make the class less powerful.



Fascinatingly, no relationship between [[Class_QMIP|QMIP]] and [[Class_NEXP|NEXP]] is known.  We don't know whether allowing the provers unlimited prior entanglement makes the class more powerful, less powerful, or both!
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QMIP|QMIP]], except that now the provers share only a polynomial number of EPR pairs, instead of an unlimited number.



Defined in [[ZooRefs#KM02|[KM02] ]], where it was also shown that [[Class_QMIPle|QMIPle]] is contained in [[Class_NEXP|NEXP]] = [[Class_QMIPne|QMIPne]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QMIP|QMIP]], except that now the provers have no prior entanglement.



Defined in [[ZooRefs#KM02|[KM02] ]], where it was also shown that [[Class_QMIPne|QMIPne]] = [[Class_NEXP|NEXP]].  Thus, [[Class_QMIPne|QMIPne]] contains [[Class_QMIPle|QMIPle]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by polylogarithmic-depth quantum circuits with bounded probability of error.  (A uniformity condition may also be imposed.)



Has the same relation to [[Class_NC|NC]] as [[Class_BQP|BQP]] does to [[Class_P|P]].



[[ZooRefs#CW00|[CW00] ]] showed that factoring is in [[Class_ZPP|ZPP]] with a [[Class_QNC|QNC]] oracle.



Is incomparable with [[Class_BPP|BPP]] as far as anyone knows.



See also: [[Class_RNC|RNC]].
== Relations ==


== See Also ==

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

== Comments ==

Constant-depth quantum circuits without fanout gates.



Defined in [[ZooRefs#Spa02|[Spa02] ]].



Contained in [[Class_QNCf0|QNCf0]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QNC1|QNC1]], but for the exact rather than bounded-error case.



In contrast to [[Class_NC1|NC1]], it is not clear how to simulate [[Class_QNC1|QNC1]] on a quantum computer in which one qubit is initialized to a pure state, and the remaining qubits are in the maximally mixed state [[ZooRefs#ASV00|[ASV00] ]].



See also [[ZooRefs#MN02|[MN02] ]].
== Relations ==


== See Also ==

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

== Comments ==

Constant-depth quantum circuits with unbounded-fanout gates.



Defined in [[ZooRefs#Spa02|[Spa02] ]].



Contains [[Class_QNC0|QNC0]], and is contained in [[Class_QACC0|QACC0]].
== Relations ==


== See Also ==

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

== Comments ==

Equals DTIME(2^polylog(n)^).
== Relations ==


== See Also ==

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

== Comments ==

Equals DTIME(n^O(log n)^).



Has the same relationship to [[Class_QP|QP]] that [[Class_E|E]] does to [[Class_EXP|EXP]].
== Relations ==


== See Also ==

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

== Comments ==

Equals DSPACE(2^polylog(n)^).



According to [[ZooRefs#BG94|[BG94] ]], Beigel and Feigenbaum and (independently) Krawczyk showed that [[Class_QPSPACE|QPSPACE]] is not contained in [[Class_Check|Check]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_RG|RG]], except that now the verifier is a [[Class_BQP|BQP]] machine, and can exchange polynomially many quantum messages with the competing provers.



The two provers are computationally unbounded, but must obey the laws of quantum mechanics.  Also, we can assume without loss of generality that the provers share no entanglement, because adversaries gain no advantage by sharing information.



Defined in [[ZooRefs#Gut05|[Gut05] ]], where it was also shown that [[Class_QRG|QRG]] is contained in [[Class_NEXP|NEXP]] ∩ [[Class_coNEXP|coNEXP]].



[[Class_QRG|QRG]] trivially contains [[Class_RG|RG]] (and hence EXP), as well as [[Class_SQG|SQG]].



[[Class_QRG|QRG]] is contained in [[Class_EXP|EXP]] [[ZooRefs#GW07|[GW07] ]].  Hence [[Class_QRG|QRG]] = [[Class_RG|RG]] = [[Class_EXP|EXP]] and finding optimal strategies for zero-sum quantum games is no harder than finding optimal strategies for zero-sum classical games.
== Relations ==


== See Also ==

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

== Comments ==

The class of problems for which there exists a [[Class_BQP|BQP]] machine M such that:



If the answer is "yes," then there exists a quantum state ρ such that for all quantum states σ, M(ρ,σ) accepts with probability at least 2/3.

If the answer is "no," then there exists a σ such that for all ρ, M(ρ,σ) rejects with probability at least 2/3.



In other words, it's the same as [[Class_QRG(k)|QRG(k)]] for , the class of problems that admit quantum interactive proofs with competing provers in which there's no communication from the verifier back to the provers.  [[Class_QRG(1)|QRG(1)]] is the quantum version of [[Class_RG(1)|RG(1)]].



Defined in [[ZooRefs#JW09|[JW09] ]], where it was shown that [[Class_QRG(1)|QRG(1)]] is contained in [[Class_PSPACE|PSPACE]] .



[[Class_QRG(1)|QRG(1)]] trivially contains [[Class_QMA|QMA]] (and indeed P^QMA^).



[[Class_QRG(1)|QRG(1)]] is trivially contained in [[Class_QRG(2)|QRG(2)]] (and hence PSPACE).
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QRG|QRG]], except that now the verifier can exchange only two messages with each prover.  Messages are exchanged in parallel, so the verifier cannot process the answer from one prover before preparing the question for the other.  [[Class_QRG(2)|QRG(2)]] is the quantum version of [[Class_RG(2)|RG(2)]].  See also [[Class_QRG(k)|QRG(k)]].



[[Class_QRG(2)|QRG(2)]] trivially contains [[Class_RG(2)|RG(2)]] (and hence PSPACE).



[[Class_QRG(2)|QRG(2)]] is trivially contained in [[Class_SQG|SQG]] (and hence PSPACE).  Hence [[Class_QRG(2)|QRG(2)]] = [[Class_RG(2)|RG(2)]] = [[Class_PSPACE|PSPACE]] and finding optimal strategies for two-turn zero-sum quantum games is no harder than finding optimal strategies for two-turn zero-sum classical games.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QRG|QRG]], except that now the verifier exchanges exactly k messages with each prover where k is a polynomial-bounded function of the input length.  Messages are exchanged in parallel.  [[Class_QRG(k)|QRG(k)]] is the quantum version of [[Class_RG(k)|RG(k)]].  By definition, QRG(poly) = [[Class_QRG|QRG]].  See also [[Class_QRG(1)|QRG(1)]] and [[Class_QRG(2)|QRG(2)]].



[[Class_QRG(k)|QRG(k)]] trivially contains [[Class_RG(k)|RG(k)]] for each k (and hence [[Class_PSPACE|PSPACE]] when ).  QRG(4) trivially contains [[Class_SQG|SQG]].



[[Class_QRG(k)|QRG(k)]] is trivially contained in [[Class_QRG|QRG]] for each k (and hence EXP).



Other than these trivial bounds, very little is known of [[Class_QRG(k)|QRG(k)]] for intermediate values of k.  For example, does [[Class_QRG(k)|QRG(k)]] = [[Class_RG(k)|RG(k)]] for each k?
== Relations ==


== See Also ==

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

== Comments ==

The class of problems for which there exists a [[Class_BQP|BQP]] machine M such that:



If the answer is "yes," then there exists a quantum state ρ such that for all quantum states σ, M(ρ,Ï) accepts with probability at least 2/3.

If the answer is "no," then there exists a σ such that for all ρ, M(ρ,σ) rejects with probability at least 2/3.



In other words, it's the same as [[Class_SQG|SQG]], but without communication from the verifier back to the provers.



Contains [[Class_QMA|QMA]] (and indeed P^QMA^), and is contained in [[Class_SQG|SQG]] and hence [[Class_EXP|EXP]].
== Relations ==


== See Also ==

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

== Comments ==

A quantum analog of [[Class_SZK|SZK]] (or more precisely HVSZK).



Arthur is a [[Class_BQP|BQP]] (i.e. quantum) verifier who can exchange quantum messages with Merlin.  So Arthur and Merlin's states may become entangled during the course of the protocol.



Arthur's "view" of his interaction with Merlin is taken to be the sequence of mixed states he has, over all steps of the protocol.  The zero-knowledge requirement is that each of these states must have trace distance at most (say) 1/10 from a state that Arthur could prepare himself (in BQP), without help from Merlin.  Arthur is assumed to be an honest verifier.



Defined in [[ZooRefs#Wat02|[Wat02] ]], where the following was also shown:



[[Class_QSZK|QSZK]] is contained in [[Class_PSPACE|PSPACE]].

[[Class_QSZK|QSZK]] is closed under complement.

Any protocol can be parallelized to consist of two messages, so that [[Class_QSZK|QSZK]] is in [[Class_QIP[2]|QIP[2]]].

One can assume without loss of generality that protocols are public-coin, as for [[Class_SZK|SZK]].

[[Class_QSZK|QSZK]] has a natural complete promise problem, called Quantum State Distinguishability (QSD).  We are given quantum circuits Q,,0,, and Q,,1,,.  Let ρ,,0,, and ρ,,1,, be the mixed states they produce respectively, when run on the all-0 state (and when non-output qubits are traced out).  We are promised that the trace distance between ρ,,0,, and ρ,,1,, is either at most α or at least β, where α and β are constants in [0,1] satisfying α < β^2^.  The problem is to decide which of these is the case.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a Turing machine.  Often identified with the class of 'effectively computable' functions (the Church-Turing thesis).



Defined in [[ZooRefs#Tur36|[Tur36] ]], [[ZooRefs#Chu41|[Chu41] ]], and other seminal early papers.



Equals [[Class_RE|RE]] ∩ [[Class_coRE|coRE]].



Strictly contains [[Class_PR|PR]], the primitive recursive functions (see [[ZooRefs#Kle71|[Kle71] ]]).
== Relations ==


== See Also ==

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

== Comments ==

The class of problems in [[Class_NP|NP]] whose witnesses are in [[Class_FBQP|FBQP]].  For example, the set of square-free numbers is in coRBQP using only the fact that factoring is in [[Class_FBQP|FBQP]].  (Even without a proof that the factors are prime, the factorization proves that there is a square divisor.)



Contains [[Class_RP|RP]] and [[Class_ZBQP|ZBQP]], and is contained in [[Class_BQP|BQP]] and [[Class_RQP|RQP]].  Defined here to clarify [[Class_EQP|EQP]]; see also [[Class_ZBQP|ZBQP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a 'yes' answer can be verified by a Turing machine in a finite amount of time.  (If the answer is 'no,' on the other hand, the machine might never halt.)



Equivalently, the class of decision problems for which a Turing machine can list all the 'yes' instances, one by one (this is what 'enumerable' means).



A problem C is complete for [[Class_RE|RE]] if (1) C is in [[Class_RE|RE]] and (2) any problem in [[Class_RE|RE]] can be reduced to C by a Turing machine.



Actually there are two types of reduction: M-reductions (for many-one), in which a single instance of the original problem is mapped to an instance of C, and T-reductions (for Turing), in which an algorithm for the original problem can make arbitrarily many calls to an oracle for C.



RE-complete sets are also called creative sets for some reason.



The canonical RE-complete problem is the halting problem: i.e., given a Turing machine, does it halt when started on a blank tape?



The famous unsolvability of the halting problem [[ZooRefs#Tur36|[Tur36] ]] implies that [[Class_R|R]] does not equal [[Class_RE|RE]].



Also, [[Class_RE|RE]] does not equal [[Class_coRE|coRE]].



[[Class_RE|RE]] and [[Class_coRE|coRE]] can be generalized to the arithmetic hierarchy [[Class_AH|AH]].



There are problems in [[Class_RE|RE]] that are neither RE-complete under T-reductions, nor in [[Class_R|R]] [[ZooRefs#Fri57|[Fri57] ]] [[ZooRefs#Muc56|[Muc56] ]].  This is the resolution of Post's problem [[ZooRefs#Pos44|[Pos44] ]].



Indeed, [[Class_RE|RE]] contains infinitely many nonequivalent 'T-degrees.'  (A T-degree is a class of problems, all of which can be T-reduced to one another.)  The structure of the T-degrees has been studied in more detail than you can possibly imagine [[ZooRefs#Sho99|[Sho99] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by deterministic finite automata (DFAs).



Equals the class solvable by nondeterministic finite automata (NDFAs).



Equals DSPACE(O(1)) [[ZooRefs#She59|[She59] ]], which equals DSPACE(o(log log n)) [[ZooRefs#HLS65|[HLS65] ]].



Includes, i.e., "Is the parity of the input odd?," but not "Are the majority of bits in the input 1's?"  This is sometimes expressed as "finite automata can't count."



Contained in [[Class_NC1|NC1]].



See e.g. [[ZooRefs#Koz97|[Koz97] ]], [[ZooRefs#Gur89|[Gur89] ]] for basic results on regular languages.



The class of decision problems solvable by deterministic finite automata (DFA's).



Equals the class solvable by nondeterministic finite automata (NDFA's).
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a probabilistic polynomial-time verifier who can exchange a polynomial number of messages with two competing, computationally-unbounded provers -- one trying to convince the verifier that the answer is "yes," the other that the answer is "no."  Note that the verifier can hide information from the provers.  Public-coin [[Class_RG|RG]] amounts to [[Class_SAPTIME|SAPTIME]], which equals [[Class_PSPACE|PSPACE]] [[ZooRefs#Pap83|[Pap83] ]].



[[Class_RG|RG]] is in [[Class_EXP|EXP]] relative to any oracle [[ZooRefs#KM92|[KM92] ]]; they are equal, unrelativized [FK97b].



See also PCD, GPCD.



Contains [[Class_RG[1]|RG[1]]], and is contained in [[Class_QRG|QRG]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems for which there exists a [[Class_BPP|BPP]] machine M such that, on input x:



If the answer is 'yes,' then there exists a distribution Y such that for all distributions Z, M(x,Y,Z) accepts with probability at least 2/3.

If the answer is 'no,' then there exists a distribution Z such that for all distributions Y, M(x,Y,Z) rejects with probability at least 2/3.



In other words, it's the same as [[Class_RG(k)|RG(k)]] for , the class of problems that admit interactive proofs with competing provers in which there's no communication from the verifier back to the provers.



[[Class_RG(1)|RG(1)]] trivially contains [[Class_S2P|S2P]].  Indeed, [[Class_RG(1)|RG(1)]] can be viewed as a randomized version of [[Class_S2P|S2P]].



[[Class_RG(1)|RG(1)]] is trivially contained in [[Class_RG(2)|RG(2)]] (and hence PSPACE).
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_RG|RG]], except that now the verifier can exchange only two messages with each prover. Messages are exchanged in parallel, so the verifier cannot process the answer from one prover before preparing the question for the other.  See also [[Class_RG(k)|RG(k)]].



[[Class_RG(2)|RG(2)]] is contained in [[Class_PSPACE|PSPACE]], and they are equal, unrelativized [FK97b].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_RG|RG]], except that now the verifier exchanges exactly k messages with each prover where k is a polynomial-bounded function of the input length. Messages are exchanged in parallel.  By definition, RG(poly) = [[Class_RG|RG]]. See also [[Class_RG(1)|RG(1)]] and [[Class_RG(2)|RG(2)]].



Other than trivial bounds, very little is known of [[Class_RG(k)|RG(k)]] for intermediate values of k. For example, does [[Class_RG(k)|RG(k)]] = [[Class_PSPACE|PSPACE]] for each constant ?
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_RG|RG]], except that now the verifier can exchange only a single round of messages with the two provers.  A round consists of private messages from the verifier to the provers, followed by private responses from the provers to the verifier.  Since the queries are private, they may as well be parallel; likewise the responses.  This makes [[Class_RG[1]|RG[1]]] a symmetric class, indeed a randomized analogue of [[Class_S2P|S2P]].



[[Class_RG[1]|RG[1]]] is contained in [[Class_PSPACE|PSPACE]], and they are equal, unrelativized [FK97b].



Contains [[Class_S2P|S2P]] and is contained in [[Class_SQG|SQG]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_RP|RP]] does to [[Class_P|P]].  The randomized machine must halt for every input and every setting of the random tape.



Contains undirected reachability (is there a path from vertex u to vertex v in an undirected graph?) [[ZooRefs#AKL+79|[AKL+79] ]].



Contained in [[Class_RL|RL]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_BPHSPACE(f(n))|BPHSPACE(f(n))]] as [[Class_RP|RP]] does to [[Class_BPP|BPP]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_RP|RP]] does to [[Class_P|P]].  The randomized machine must halt with probability 1 on any input.  It must also run in polynomial time (since otherwise we would just get

NL).



Contains [[Class_RHL|RHL]].



Contained in [[Class_SC|SC]] [[ZooRefs#Nis92|[Nis92] ]].



[[ZooRefs#RTV05|[RTV05] ]] give strong evidence that [[Class_RL|RL]] = [[Class_L|L]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_NC|NC]] as [[Class_RP|RP]] does to [[Class_P|P]].



Contains the maximum matching problem for bipartite graphs [[ZooRefs#MVV87|[MVV87] ]].



Contained in [[Class_QNC|QNC]].



See also: [[Class_coRNC|coRNC]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is 'yes,' at least 1/2 of computation paths accept.

If the answer is 'no,' all computation paths reject.



Defined in [[ZooRefs#Gil77|[Gil77] ]] (implicitly: the class VPP that is defined is equivalent to [[Class_RP|RP]] by running the recognizer as many times as necessary to reach probability 1/2).



Contains the problem of testing whether an integer is prime [[ZooRefs#AH87|[AH87] ]], although this problem was subsequently shown to be in [[Class_P|P]] [[ZooRefs#AKS02|[AKS02] ]].



For other problems in [[Class_RP|RP]], see the standard text on randomized algorithms, [[ZooRefs#MR95|[MR95] ]].



Has the same p-measure as [[Class_ZPP|ZPP]]. Moreover, this measure is either zero or one. If the measure is non-zero, then [[Class_ZPP|ZPP]] = [[Class_BPP|BPP]] = [[Class_EXP|EXP]] [[ZooRefs#IM03|[IM03] ]].



See also: [[Class_coRP|coRP]], [[Class_ZPP|ZPP]], [[Class_BPP|BPP]].



Defined in [[ZooRefs#Gil77|[Gil77] ]].



Contains the problem of testing whether an integer is prime [[ZooRefs#AH87|[AH87] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems (x,m) (where x is an input of length |x|=n and m is an integer parameter), that are solvable by a nondeterministic (i.e. NP) machine in poly(n+m) time and O(m+log n) space simultaneously.



Defined in [[ZooRefs#Mon80|[Mon80] ]].



See also [[Class_FPT|FPT]].
== Relations ==


== See Also ==

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

pagename = u"Class_RPcc"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RP,,,,^cc^ - Randomized Pcc =

== Comments ==

The class of functions  which can be computed by  players with access to shared random bits in the number-on-forehead (defined as in P,,,,^cc^) model, subject to two constraints:



The communication cost (the sum of the number of random bits used and bits written to the shared blackboard) is .

 If , then the players decide correctly with probably at least 2/3, whereas if , the players always decide correctly.



[[Class_NPcc|NPcc]] is not equal to [[Class_RPcc|RPcc]] for  players, for any constant  [[ZooRefs#DP08|[DP08] ]].
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save RPcc because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_RQP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= RQP - One-sided Error Extension of EQP =

== Comments ==

The class of questions that can be answered by a QTM that accepts with probability 0 when the true answer is no, and accepts with probability at least 1/2 when the true answer is yes.  Since one of the probabilities has to vanish, [[Class_RQP|RQP]] has the same technical caveats as [[Class_EQP|EQP]].



Contains [[Class_ZQP|ZQP]] and [[Class_RBQP|RBQP]], and is contained in [[Class_BQP|BQP]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_RL|RL]], but for O(f(n))-space instead of logarithmic-space.  (Just as an [[Class_RL|RL]] machine must run in polynomial time, so an [[Class_RSPACE(f(n))|RSPACE(f(n))]] machine must run in 2^O(f(n))^ time.)



Contained in [[Class_NSPACE(f(n))|NSPACE(f(n))]] and [[Class_BPSPACE(f(n))|BPSPACE(f(n))]].



Same as [[Class_RL|RL]], but for O(f(n))-space instead of logarithmic-space.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable in space O(f(n)) by a reversible Turing machine (a deterministic Turing machine for which every configuration has at most one immediate predecessor).



Was shown to equal [[Class_DSPACE(f(n))|DSPACE(f(n))]] [[ZooRefs#LMT97|[LMT97] ]].
== Relations ==


== See Also ==

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

== Comments ==

One of the caged classes of the Complexity Zoo.



Has been implicated in a collapse scandal involving [[Class_AM[polylog]|AM[polylog]]], [[Class_coNP|coNP]], and [[Class_EH|EH]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which there is a polynomial-time predicate [[Class_P|P]] such that, on input x,



If the answer is 'yes,' then there exists a y such that for all z, P(x,y,z) is true.

If the answer is 'no,' then there exists a z such that for all y, P(x,y,z) is false.



Note that this differs from [[Class_Σ2P|Σ2P]] in that the quantifiers in the second condition are reversed.



Less formally, [[Class_S2P|S2P]] is the class of one-round games in which a prover and a disprover submit simultaneous moves to a deterministic, polynomial-time referee.  In [[Class_Σ2P|Σ2P]], the disprover moves first.



Defined in [[ZooRefs#RS98|[RS98] ]], where it was also shown that [[Class_S2P|S2P]] contains [[Class_MA|MA]] and [[Class_Δ2P|Δ2P]].  Defined independently in [[ZooRefs#Can96|[Can96] ]].



Contained in ZPP^NP^ [[ZooRefs#Cai01|[Cai01] ]].



[[Class_S2-EXP•PNP|S2-EXP•PNP]]: Don't Ask 

One of the caged classes of the Complexity Zoo.

Has been implicated in a collapse scandal involving [[Class_AM[polylog]|AM[polylog]]], [[Class_coNP|coNP]], and [[Class_EH|EH]].
== Relations ==


== See Also ==

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

== Comments ==

SAC^k^ is the class of decision problems solvable by a family of depth-O(log^k^n) circuits with unbounded-fanin OR & bounded-fanin AND gates.  Negations are only allowed at the input level.



A uniformity condition may also be imposed.



Defined by [[ZooRefs#BCD+89|[BCD+89] ]], who also showed that SAC,,k,, is closed under complement for every k>0.
== Relations ==


== See Also ==

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

== Comments ==

See [[Class_SAC|SAC]] for definition.



Not closed under complement [[ZooRefs#BCD+89|[BCD+89] ]].
== Relations ==


== See Also ==

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

== Comments ==

See [[Class_SAC|SAC]] for definition.



Equals LOGCFL/poly [[ZooRefs#Ven91|[Ven91] ]].



Contained in [[Class_⊕SAC1|⊕SAC1]] [[ZooRefs#GW96|[GW96] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a polynomial-time Turing machine with three kinds of quantifiers: existential, universal, and randomized.



Defined in [[ZooRefs#Pap83|[Pap83] ]], where it was also observed that [[Class_SAPTIME|SAPTIME]] = [[Class_PSPACE|PSPACE]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which the following holds.  There exists a [[Class_#P|#P]] function f and an [[Class_FP|FP]] function g such that, for all inputs x,



If the answer is "yes" then f(x) > g(x).

If the answer is "no" then f(x) < g(x)/2.



Defined in [[ZooRefs#BGM02|[BGM02] ]], where the following was also shown:



[[Class_SBP|SBP]] contains [[Class_MA|MA]], [[Class_WAPP|WAPP]], and [[Class_∃BPP|∃BPP]].

[[Class_SBP|SBP]] is contained in [[Class_AM|AM]] and [[Class_BPPpath|BPPpath]].

There exists an oracle relative to which [[Class_SBP|SBP]] is not contained in [[Class_Σ2P|Σ2P]].

[[Class_SBP|SBP]] is closed under union.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which there exists a polynomial-time quantum algorithm that accepts with probability at least 2^−p(n)^ if the answer is "yes", and with probability at most 2^−p(n)−1^ if the answer is "no", for some polynomial p.



Defined by Kuperberg in [[ZooRefs#Kup09|[Kup09] ]], where he showed that [[Class_SBQP|SBQP]] = [[Class_A0PP|A0PP]].
== Relations ==


== See Also ==

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

== Comments ==

(Named in honor of Stephen Cook.)



The class of decision problems solvable by a Turing machine that simultaneously uses polynomial time and polylogarithmic space.



Note that [[Class_SC|SC]] might be smaller than [[Class_P|P]] ∩ [[Class_polyL|polyL]], since for the latter, it suffices to have two separate algorithms: one polynomial-time and the other polylogarithmic-space.



Deterministic context-free languages (DCFLs) can be recognized in [[Class_SC|SC]] [[ZooRefs#Coo79|[Coo79] ]].



[[Class_SC|SC]] contains [[Class_RL|RL]] and [[Class_BPL|BPL]] [[ZooRefs#Nis92|[Nis92] ]].



[[Class_SC|SC]] equals DTISP(poly,polylog) by definition.



Deterministic context-free languages (DCFL's) can be recognized in [[Class_SC|SC]] [[ZooRefs#Coo79|[Coo79] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of [[Class_FNP|FNP]] search problems solvable in O(2^εn^) time for every ε>0.



Defined in [[ZooRefs#IPZ01|[IPZ01] ]], who also gave reductions showing that if any of k-SAT, k-colorability, k-set cover, clique, or vertex cover is in [[Class_SE|SE]], then all of them are.
== Relations ==


== See Also ==

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

== Comments ==

The union of [[Class_NE|NE]], NP^NE^, NP^NP^NE^, and so on.



Is called "strong" to contrast it with the ordinary Exponential Hierarchy [[Class_EH|EH]].



Note that we would get the same class if we replaced [[Class_NE|NE]] by [[Class_NEXP|NEXP]].



[[Class_SEH|SEH]] collapses to P^NE^ [[ZooRefs#Hem89|[Hem89] ]]



There exists an oracle relative to which [[Class_SEH|SEH]] is not contained in [[Class_EH|EH]] [[ZooRefs#Hem89|[Hem89] ]].

[[Class_EH|EH]] and [[Class_SEH|SEH]] are incomparable for all anyone knows.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a k-bottleneck Turing machine. This is a machine that, after a polynomial amount of time, erases everything on the tape except for a single k-valued "safe-storage".  There's also a counter recording the number of erasings, which is in effect a non-deterministic witness.  For example, SF,,2,, contains both [[Class_⊕P|⊕P]] and [[Class_NP|NP]] by using the counter as a witness.



Defined in [[ZooRefs#CF91|[CF91] ]], where it was also shown that SF,,5,, = [[Class_PSPACE|PSPACE]].



The complexity of SF,,2,,, SF,,3,,, and SF,,4,, was studied in [[ZooRefs#Ogi94|[Ogi94] ]] and [[ZooRefs#Her97|[Her97] ]].  The following result of those authors is among the caged beasts of the Complexity Zoo:



SF,,4,, is contained in BP ⊕P^Mod_3P ^ [[Class_⊕P|⊕P]] ^ Mod_3P ^ [[Class_⊕P|⊕P]]



(Here the BP operator means that one makes the class into a bounded-error probabilistic class, the same way one makes [[Class_P|P]] into [[Class_BPP|BPP]] and [[Class_NP|NP]] into AM.)
== Relations ==


== See Also ==

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

== Comments ==

A hierarchy of generalizations of [[Class_SZK|SZK]], in which Arthur is allowed to gain some information from his interaction with Merlin.



Defined in [[ZooRefs#GP91|[GP91] ]].



There are several variants (which we only describe roughly), including:



SKC,,hint,,(k(n)): Hint sense.  The simulator can reproduce Arthur's view of the protocol if given a hint string of size k(n).

SKC,,hint,,(k(n)): Strict oracle sense.  The simulator can reproduce Arthur's view if allowed k(n) queries to an oracle O.

SKC,,avg,,(k(n)): Average oracle sense.  For each input, the expected number of queries the simulator makes to oracle O is at most k(n).

SKC,,ent,,(k(n)): Entropy sense.  Defined in [[ZooRefs#ABV95|[ABV95] ]]. For each input, the expectation (over Arthur's random coins) of -log(P) is at most k(n), where [[Class_P|P]] is the probability that the view output by the simulator equals the view resulting from the actual protocol.



See also: [[Class_PKC|PKC]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a nondeterministic Turing machine in logarithmic space, such that



If the answer is 'yes,' one or more computation paths accept.

If the answer is 'no,' all paths reject.

If the machine can make a nondeterministic transition from configuration A to configuration B, then it can also transition from B to A.  (This is what 'symmetric' means.)



Defined in [[ZooRefs#LP82|[LP82] ]].



The undirected s-t connectivity problem (USTCON: is there a path from vertex s to vertex t in a given undirected graph?) is complete for [[Class_SL|SL]], under L-reductions.



[[Class_SL|SL]] contains [[Class_L|L]], and is contained in [[Class_NL|NL]].



It follows from [[ZooRefs#AKL+79|[AKL+79] ]] that [[Class_SL|SL]] is contained in [[Class_L/poly|L/poly]].



[[ZooRefs#KW93|[KW93] ]] showed that [[Class_SL|SL]] is contained in [[Class_⊕L|⊕L]], as well as [[Class_ModkL|ModkL]] for every prime k.



[[Class_SL|SL]] is also contained in DSPACE(log^3/2^n) [[ZooRefs#NSW92|[NSW92] ]], and indeed in DSPACE(log^4/3^n) [[ZooRefs#ATW+00|[ATW+00] ]].



[[ZooRefs#NT95|[NT95] ]] showed that [[Class_SL|SL]] equals [[Class_coSL|coSL]], and furthermore that SL^SL^ = [[Class_SL|SL]] (that is, the symmetric logspace hierarchy collapses).



Reingold ultimately showed that [[Class_SL|SL]] = [[Class_L|L]] [[ZooRefs#Rei04|[Rei04] ]], even relative to an oracle. This subsumes many of the earlier results.



The reachability problem (is there a path from vertex s to vertex t?) for undirected graphs is complete for [[Class_SL|SL]], under L-reduction.



The story ends with the remarkable result that [[Class_SL|SL]] = [[Class_L|L]] (even relative to an oracle)

[[ZooRefs#Rei04|[Rei04] ]].
== Relations ==


== See Also ==

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

== Comments ==

The parameterized version of [[Class_PSPACE|PSPACE]].



Same as [[Class_FPT|FPT]], except that now on input (x,k) (k a parameter), the space used must be f(k)p(|x|), where p is a polynomial.



If [[Class_P|P]] = [[Class_PSPACE|PSPACE]], then [[Class_FPT|FPT]] = SLICEWISE [[Class_PSPACE|PSPACE]].



Defined in [[ZooRefs#DF99|[DF99] ]].
== Relations ==


== See Also ==

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

== Comments ==

[[ZooRefs#Fag74|[Fag74] ]] showed that [[Class_NP|NP]] is precisely the class of decision problems reducible to a graph-theoretic property expressible in second-order existential logic.



Then [[Class_SNP|SNP]] is the class of decision problems reducible to a graph-theoretic predicate with only universal quantifiers over vertices, no existential quantifiers.  As an example, k-SAT (CNF satisfiability with at most k literals per clause, for k a constant) is in [[Class_SNP|SNP]].  But general SAT is not in [[Class_SNP|SNP]], basically because we're not allowed to say, "There exists a literal in this clause that satisfies the clause."



Contains [[Class_MMSNP|MMSNP]].



See also: [[Class_MaxSNP|MaxSNP]].



[[ZooRefs#Fag74|[Fag74] ]]



[[Class_NP|NP]]



[[ZooRefs#Pap94|[Pap94] ]]



There exists a relation P(u,v) on vertices of G, such that P(u,u) is false, and for all distinct u,v either P(u,v) or P(v,u), and P(u,v) and P(v,w) implies P(u,w), and if P(u,w) and there does not exist a v for which P(u,v) and P(v,w), then there is an edge from u to w.



total order
== Relations ==


== See Also ==

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

== Comments ==

We define second-order variable  has got an arity k and represent any proposition of arity . They are usually written in upper-case.



Second order logic is the set of [[Class_FO|FO]] formulae where we add quantification over second-order variables.



Every formuale is equivalent to a formulae in prenex normal form, where we first write quantification on variable on second order and then a FO-formulae in prenex normal form.



In Descriptive complexity we can see that [[Class_SO|SO]] is equal to [[Class_PH|PH]], more precisely we have that formulae in prenex normal form where existantial and universal of second order alternate k times are the kth level of the polynomial hierarchy.



This means that [[Class_SO|SO]] with only existantial second-order quantification is equal to  which is [[Class_NP|NP]], and with only universal quantification is equal to  which is Co-NP.
== Relations ==


== See Also ==

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

== Comments ==

SO(horn) is the set of boolean queries definable with second-order formulae in normal form such that the quantifier-free part of the formula is in conjunctive normal form with at most one positive instance of a quantified relation per clause.  (Atomic queries to the database don't count.)



It was shown in [Grä92] that this class is equal to [[Class_P|P]].



Those formulae can be made in prenex form where the second order is existential and the first order universal without loss of generality.
== Relations ==


== See Also ==

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

== Comments ==

SO(krom) is the set of boolean queries definable with second-order formulae in normal form such that the quantifier-free part of the formula is in Krom form, wich means that in every clause there is at most two literals and the first-order portion contains no existential quantifiers.



It was shown in [Grä92] that this class is equal to [[Class_NL|NL]].



Those formulaes can be made in prenex form where the second order is existential and the first order universal without loss of generalities.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a "yes" answer is expressible by a proposition with second-order existential quantifiers followed by a first-order formula.  See [[ZooRefs#Imm98|[Imm98] ]] for a full definition.



[[Class_SO-E|SO-E]] = [[Class_NP|NP]] [[ZooRefs#Fag74|[Fag74] ]].



Contains FO(poly(n)).
== Relations ==


== See Also ==

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

== Comments ==

[[Class_SO[LFP]|SO[LFP]]] is to [[Class_SO|SO]] what FO[LFP] is to [[Class_FO|FO]]. The LFP operator can now also take second-order variable as argument.



In Descriptive complexity we can see that 

[[Class_SO[LFP]|SO[LFP]]] is  equal to EXPTIME.
== Relations ==


== See Also ==

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

== Comments ==

[[Class_SO[TC]|SO[TC]]] is to [[Class_SO|SO]] what FO[TC] is to [[Class_FO|FO]]. The TC operator can now also take second-order variable as argument.



In Descriptive complexity we can see that :

[[Class_SO[TC]|SO[TC]]] is  equal to [[Class_PSPACE|PSPACE]].
== Relations ==


== See Also ==

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

pagename = u"Class_SO[]"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SO[] - Iterated Second-Order logic =

== Comments ==

[[Class_SO[]|SO[]]] is to [[Class_SO|SO]] what [[Class_FO[]|FO[]]] is to [[Class_FO|FO]]. But we now also have second-order quantifier in the quantifier block.



In Descriptive complexity we can see that :



[[Class_SO[]|SO[]]] is  equal to [[Class_PSPACE|PSPACE]] it is also another way to write SO(TC)

[[Class_SO[]|SO[]]] is equal to EXPTIME it is also another way to write SO(LFP)
== Relations ==


== See Also ==

'''
_, rev, _ = editor.get_rev()
p = None
try:
    editor.saveText(text, rev)
    p = Page(request, pagename)
    print p.page_name
except Exception as e:
    print ("Couldn't save SO[] because")
    print (e)

if p:
    assert p.exists()

pagename = u"Class_SP"
request = ScriptContext('localhost:8080', pagename)
editor = PageEditor(request, pagename)
text = u'''
<<TableOfContents()>>


= SP - Semi-Efficient Parallel =

== Comments ==

The class of problems in [[Class_P|P]] for which the best parallel algorithm (using a polynomial number of processors) is faster than the best serial algorithm by a factor of Ω(n^ε^) for some ε>0.



Defined in [[ZooRefs#KRS90|[KRS90] ]].



[[Class_SP|SP]] is also an alternate name for [[Class_XPuniform|XPuniform]]
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which the number of 'yes' instances of size n is upper-bounded by a polynomial in n.  If [[Class_SPARSE|SPARSE]] intersects [[Class_NPC|NPC]] then [[Class_P|P]] = [[Class_NP|NP]] [[ZooRefs#Mah82|[Mah82] ]].



Contains [[Class_TALLY|TALLY]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_PL|PL]] as [[Class_SPP|SPP]] does to [[Class_PP|PP]].



Contains the maximum matching and perfect matching problems under a pseudorandom assumption [[ZooRefs#ARZ99|[ARZ99] ]].



Contains [[Class_UL|UL]].



Contained in [[Class_C=L|C=L]] and [[Class_ModkL|ModkL]].



Equals the set of problems low for [[Class_GapL|GapL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is "no," then the number of accepting computation paths exactly equals the number of rejecting paths.

If the answer is "yes," then these numbers differ by 2.



(A technicality: If the total number of paths is even then the numbers can't differ by 1.)



Defined in [[ZooRefs#FFK94|[FFK94] ]], where it was also shown that [[Class_SPP|SPP]] is low for [[Class_PP|PP]], [[Class_C=P|C=P]], [[Class_ModkP|ModkP]], and [[Class_SPP|SPP]] itself.  (I.e. adding [[Class_SPP|SPP]] as an oracle does not increase the power of these classes.)



Independently defined in [[ZooRefs#OH93|[OH93] ]], who called the class [[Class_XP|XP]].



Contained in [[Class_LWPP|LWPP]], [[Class_C=P|C=P]], and [[Class_WPP|WPP]] among other classes.



Contains [[Class_FewP|FewP]]; indeed, [[Class_FewP|FewP]] is low for [[Class_SPP|SPP]], so that SPP^FewP^ = [[Class_SPP|SPP]] [[ZooRefs#FFK94|[FFK94] ]].



Contains the problem of deciding whether a graph has any nontrivial automorphisms [[ZooRefs#KST92|[KST92] ]].



Indeed, contains graph isomorphism [[ZooRefs#AK02|[AK02] ]].



Contains a whole gaggle of problems for solvable black-box groups: solvability testing, membership testing, subgroup testing, normality testing, order verification, nilpotetence testing, group isomorphism, and group intersection [[ZooRefs#Vin04|[Vin04] ]]



[[ZooRefs#AK02|[AK02] ]] also showed that the Hidden Subgroup Problem for permutation groups, of interest in quantum computing, is in FP^SPP^.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_QRG(2)|QRG(2)]], except that now the verifier can process the yes-prover's answer before preparing the no-prover's question.



Defined in [[ZooRefs#GW05|[GW05] ]], where it was also shown that [[Class_SQG|SQG]] contains [[Class_QIP|QIP]].



[[Class_SQG|SQG]] is contained in [[Class_EXP|EXP]] [[ZooRefs#Gut05|[Gut05] ]].



[[Class_SQG|SQG]] is trivially contained in QRG(4) (and hence EXP).



[[Class_SQG|SQG]] trivially contains [[Class_QRG(2)|QRG(2)]] (and hence PSPACE).



[[Class_SQG|SQG]] is contained in [[Class_PSPACE|PSPACE]] [[ZooRefs#GW10|[GW10] ]].  Hence [[Class_SQG|SQG]] = [[Class_QRG(2)|QRG(2)]] = [[Class_RG(2)|RG(2)]] = [[Class_PSPACE|PSPACE]] and the addition of quantum information, combined with the ability of the verifier to process the one prover's answer before preparing the other prover's question, has no effect on the complexity of two-turn (one-round) zero-sum games.



Same as [[Class_QRG|QRG]], except that now the verifier can exchange only a single round of quantum messages with the two provers.  The verifier may process the yes-prover's response before sending a message to the no-prover (compare with [[Class_RG[1]|RG[1]]], wherein the verifier's messages must be sent to the provers in parallel).



[[Class_SQG|SQG]] is contained in [[Class_EXP|EXP]] [[ZooRefs#Gut05|[Gut05] ]], as well as in [[Class_QRG|QRG]].



[[Class_SQG|SQG]] trivially contains [[Class_QS2P|QS2P]].
== Relations ==


== See Also ==

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

== Comments ==

The intersection of DTIME(2^n^ε^) over all ε>0.  (Note that the algorithm used may vary with ε.)
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a "yes" answer can be verified by a statistical zero-knowledge proof protocol.  In such an interactive proof

(see IP), we have a probabilistic polynomial-time verifier, and a prover who has unbounded computational resources.  By exchanging messages with the prover, the verifier must become convinced (with high probability) that the answer is "yes," without learning anything else about the problem (statistically).



What does that mean?  For each choice of random coins, the verifier has a "view" of his entire interaction with prover, consisting of his random coins as well as all messages sent back and forth.  Then the distribution over views resulting from interaction with the prover has to be statistically close to a distribution that the verifier could generate himself (in polynomial-time), without interacting with anyone.  (Here "statistically close" means that, say, the trace distance is at most 1/10.)



The most famous example of such a protocol is for graph nonisomorphism. Given two graphs G and H, the verifier picks at random one of the graphs (each with probability 1/2), permutes its vertices randomly, sends the resulting graph to the prover, and asks, "Which graph did I start with, G or H?"  If G and H are non-isomorphic, the prover can always answer correctly (since he can use exponential time), but if they're isomorphic, he can answer correctly with probability at most 1/2. Thus, if the prover always gives the correct answer, then the verifier becomes convinced the graphs are not isomorphic.  On the other hand, the verifier already knew which graph (G or H) he started with, so he could simulate his entire view of the interaction himself, without the prover's help.



If that sounds like a complicated definition, well, it is.  But it turns out that [[Class_SZK|SZK]] has extremely nice properties. [[ZooRefs#Oka96|[Oka96] ]] showed that:



[[Class_SZK|SZK]] is closed under complement.  E.g., a verifier can verify in zero-knowledge that two graphs are isomorphic, not only that they aren't. 

We can assume without loss of generality that the whole interaction consists of a constant number of messages.

Amazingly, we can also assume without loss of generality that the protocol is public-coin. That is, the verifier (often called Arthur) doesn't need to hide any of his random bits, as he did in the graph nonisomorphism protocol above, but can just send them all to the prover (called Merlin)!

Finally, we can assume without loss of generality that the verifier (Arthur) is honest. A dishonest verifier would be one that tries to learn something about the problem (violating the zero-knowledge requirement) by deviating from the protocol.



Subsequently, [[ZooRefs#SV97|[SV97] ]] showed that [[Class_SZK|SZK]] has a natural complete promise problem, called Statistical Difference (SD).  Given two polynomial-size circuits, C,,0,, and C,,1,,, let D,,0,, and D,,1,, be the distributions over their respective outputs when they're given as input a uniformly random n-bit string.  We're promised that D,,0,, and D,,1,, have trace distance either at most 1/3 or at least 2/3; the problem is to decide which is the case.



Note: The constants 1/3 and 2/3 can be amplified to 2^-poly(n)^ and 1-2^-poly(n)^ respectively.  But it is crucial that (2/3)^2^ > 1/3.



Another complete promise problem for [[Class_SZK|SZK]] is Entropy Difference (ED) [[ZooRefs#GV99|[GV99] ]].  Here we're promised that either H(D,,0,,)>H(D,,1,,)+1 or H(D,,1,,)>H(D,,0,,)+1, where the distributions D,,0,, and D,,1,, are as above, and H denotes Shannon entropy.  The problem is to determine which is the case.



If any hard-on-average language is in [[Class_SZK|SZK]], then one-way functions exist [[ZooRefs#Ost91|[Ost91] ]].



See general zero-knowledge (ZK).



Contains [[Class_PZK|PZK]] and [[Class_NISZK|NISZK]], and is contained in [[Class_AM|AM]] ∩ [[Class_coAM|coAM]], as well as [[Class_CZK|CZK]] and [[Class_QSZK|QSZK]].



There exists an oracle relative to which [[Class_SZK|SZK]] is not in [[Class_BQP|BQP]] [[ZooRefs#Aar02|[Aar02] ]].



Contained in [[Class_DQP|DQP]] [Aar02b].



The class of decision problems for which a "yes" answer can be verified by a statistical zero-knowledge proof protocol.  In such a protocol, we have a [[Class_BPP|BPP]] (i.e. probabilistic polynomial-time) verifier, Arthur, and a prover, Merlin, who has unbounded computational resources.  By sending messages back and forth with Merlin, Arthur must become convinced (with high probability) that the answer is "yes," without learning anything else about the problem (statistically).



What does that mean?  For each choice of random coins, Arthur has a "view" of his entire interaction with Merlin, consisting of his random coins as well as all messages sent back and forth.  Then the distribution over views resulting from interaction with Merlin has to be statistically close to a distribution that Arthur could generate himself (in polynomial-time), without interacting with Merlin.  (Here "statistically close" means that, say, the trace distance is at most 1/10.)



The most famous example of such a protocol is for graph nonisomorphism. Given two graphs G and H, Arthur can pick one of the graphs (each with probability 1/2), permute its vertices randomly, send the resulting graph to Merlin, and ask, "Which graph did I start with, G or H?"  If G and H are non-isomorphic, Merlin can always answer correctly (since he can use exponential time), but if they're isomorphic, he can answer correctly with probability at most 1/2. Thus, if Merlin always gives the correct answer, Arthur becomes convinced the graphs are not isomorphic.  On the other hand, Arthur already knew which graph (G or H) he started with, so he could simulate his entire view of the interaction himself, without Merlin's help.



[[Class_SZK|SZK]] is closed under complement.  I.e. Arthur can verify in zero-knowledge that two graphs are isomorphic, not only that they aren't. We can assume without loss of generality that the whole interaction consists of a constant number of messages.

Amazingly, we can also assume without loss of generality that the protocol is public-coin. I.e. Arthur doesn't need to hide any of his random bits, as he did in the graph nonisomorphism protocol above, but can just send them all to Merlin!

Finally, we can assume without loss of generality that the verifier (Arthur) is honest. A dishonest verifier would be one that tries to learn something about the problem (violating the zero-knowledge requirement) by deviating from the protocol.



Zero-knowledge proofs were first studied in [[ZooRefs#GMW91|[GMW91] ]], [[ZooRefs#GMR89|[GMR89] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a "yes" answer can be verified by a statistical zero-knowledge proof protocol, and the prover and verifier both have access to a string computed by a trusted probabilistic polynomial-time third party with access to the input.



Defined in [[ZooRefs#BG03|[BG03] ]], where it was also shown that [[Class_SZKh|SZKh]] = [[Class_SZK|SZK]].



Contains [[Class_NISZKh|NISZKh]].
== Relations ==


== See Also ==

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

== Comments ==

The class of languages [[Class_L|L]] in [[Class_NP|NP]] such that the union, over all x in [[Class_L|L]], of the set of valid witnesses for x equals [[Class_L|L]] itself.



Defined in [[ZooRefs#HT03|[HT03] ]], where it was shown that the closure of [[Class_SelfNP|SelfNP]] under polynomial-time many-one reductions is [[Class_NP|NP]].



They also show that if [[Class_SelfNP|SelfNP]] = [[Class_NP|NP]], then [[Class_E|E]] = [[Class_NE|NE]]; and that SAT is contained in [[Class_SelfNP|SelfNP]].



See also: [[Class_PermUP|PermUP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which every 'yes' instance has the form 0^n^ (i.e. inputs are encoded in unary).  If [[Class_TALLY|TALLY]] intersects [[Class_NPC|NPC]] then [[Class_P|P]] = [[Class_NP|NP]] [[ZooRefs#Mah82|[Mah82] ]].



Contained in [[Class_SPARSE|SPARSE]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by polynomial-size, constant-depth circuits with unbounded fanin, which can use AND, OR, and NOT gates (as in AC^0^) as well as threshold gates.  A threshold gate returns 1 if at least half of its inputs are 1, and 0 otherwise.



A uniformity requirement is sometimes also placed.



[[Class_TC0|TC0]] contains [[Class_ACC0|ACC0]], and is contained in [[Class_NC1|NC1]].



[[Class_TC0|TC0]] circuits of depth 3 are strictly more powerful than [[Class_TC0|TC0]] circuits of depth 2 [[ZooRefs#HMP+93|[HMP+93] ]].



[[Class_TC0|TC0]] circuits of depth 3 and quasipolynomial size can simulate all of [[Class_ACC0|ACC0]] [[ZooRefs#Yao90|[Yao90] ]].



There is a function in [[Class_AC0|AC0]] (explicitly given in [[ZooRefs#She08|[She08] ]]), whose computation with [[Class_TC0|TC0]]  circuits of depth 2 requires an exponential number of gates.



[[ZooRefs#NR97|[NR97] ]] give a candidate pseudorandom function family computable in [[Class_TC0|TC0]], that is secure assuming a subexponential lower bound on the hardness of factoring.  (See also [[ZooRefs#NRR01|[NRR01] ]] for an improvement of this construction, as well as [[ZooRefs#Kha93|[Kha93] ]].)



One implication is that, assuming such a bound, there is no natural proof in the sense of [[ZooRefs#RR97|[RR97] ]] separating [[Class_TC0|TC0]] from [[Class_P/poly|P/poly]].  (It is important for this that a function family, and not just a candidate pseudorandom generator, is computable in TC^0^.)  Another implication is that functions in [[Class_TC0|TC0]] are likely to be difficult to learn.



The permanent of a 0-1 matrix cannot be computed in uniform [[Class_TC0|TC0]] [[ZooRefs#All99|[All99] ]].



In a breakthrough result [[ZooRefs#Hes01|[Hes01] ]] (building on [[ZooRefs#BCH86|[BCH86] ]] and [[ZooRefs#CDL01|[CDL01] ]]), integer division was shown to be in U,,D,,-uniform [[Class_TC0|TC0]].  Indeed division is complete for this class under [[Class_AC0|AC0]] reductions.



In a breakthrough result [[ZooRefs#Hes01|[Hes01] ]] (building on [[ZooRefs#BCH86|[BCH86] ]] and [[ZooRefs#CDL01|[CDL01] ]]), integer division was shown to be in L-uniform [[Class_TC0|TC0]].  Indeed division is complete for this class under [[Class_AC0|AC0]] reductions.
== Relations ==


== See Also ==

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

== Comments ==

The class of function problems of the following form:



Given an input x and a polynomial-time predicate F(x,y), output any y satisfying F(x,y).  (Such a y is promised to exist.)



Can be considered as the functional analogue of [[Class_NP|NP]] ∩ [[Class_coNP|coNP]]. Defined in [[ZooRefs#MP91|[MP91] ]].



Contained in [[Class_FNP|FNP]].



Subclasses include [[Class_PPA|PPA]], [[Class_PPP|PPP]], and [[Class_PLS|PLS]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_REG|REG]], except that now the inputs are trees (say, binary trees) instead of strings.  Each vertex is labeled with a symbol from a fixed alphabet.  Evaluation begins at the leaves and proceeds to the root.  The state of the finite automaton at each vertex v is a function of (1) the states at v's children (if any), and (2) the symbol at v.  The tree is in the language if and only if the automaton is in an 'accept' state at the root.



See [[ZooRefs#Koz92|[Koz92] ]] for example.
== Relations ==


== See Also ==

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

== Comments ==

The class of languages accepted by a [[Class_BQP|BQP]] machine subject to the constraint that at every time step t, the machine's state is exponentially close to a tree state -- that is, a state expressible by a polynomial-size tree of additions and tensor products (together with complex constants and |0> and |1> leaf nodes).



More formally, a uniform classical polynomial-time algorithm generates a sequence of gates g^(1)^, ... ,g^(p(n))^.  Each g^(t)^ can be either be selected from some finite universal basis of unitary gates (the choice turns out not to matter), or can be a 1-qubit measurement.  When we perform a measurement, the state evolves to one of two possible pure states, with the usual probabilities, rather than to a mixed state.  We require that the final gate g^(p(n))^ is a measurement of the first qubit.  If at least one intermediate state was more than distance 2^-Ω(n)^ away from the nearest state of tree size at most p(n), then the outcome of the final measurement is chosen adversarially; otherwise it is given by the usual Born probabilities.  The measurement must return 1 with probability at least 2/3 if the input is in the language, and with probability at most 1/3 otherwise.



Contains [[Class_BPP|BPP]], and is contained in [[Class_BQP|BQP]].



Defined in [Aar03b], where it was also shown that [[Class_TreeBQP|TreeBQP]] is

contained in the third level of [[Class_PH|PH]], which might provide weak evidence that

[[Class_TreeBQP|TreeBQP]] does not equal [[Class_BQP|BQP]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_AP|AP]], except we are promised that each existential quantifier has at most one 'yes' path, and each universal quantifier has at most one 'no' path.



Contains [[Class_UP|UP]].



Defined in [[ZooRefs#NR98|[NR98] ]], where it was also shown that, even though [[Class_AP|AP]] = [[Class_PSPACE|PSPACE]], it is unlikely that the same is true for [[Class_UAP|UAP]], since [[Class_UAP|UAP]] is contained in [[Class_SPP|SPP]].



[[ZooRefs#CGR+04|[CGR+04] ]] have also shown that UAP^UAP^ = [[Class_UAP|UAP]], and that [[Class_UAP|UAP]] contains Graph Isomorphism problem.



[[ZooRefs#CGR+04|[CGR+04] ]] have also shown that UAP^UAP^ = [[Class_UAP|UAP]], and that [[Class_UAP|UAP]] contains the Graph Isomorphism problem.
== Relations ==


== See Also ==

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

== Comments ==

The class of problems reducible in [[Class_L|L]] to the problem of whether an undirected graph has a unique connected component.



See [[ZooRefs#AG00|[AG00] ]] for more information.



Contained in [[Class_SL|SL]].



See also [[Class_coUCC|coUCC]].
== Relations ==


== See Also ==

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

== Comments ==

The class of context-free languages which can be represented by grammars where each word in the language has exactly one leftmost derivation.



Strictly contains Deterministic [[Class_CFL|CFL]].  Strictly contained in [[Class_CFL|CFL]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_E|E]] as [[Class_UP|UP]] does to [[Class_P|P]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_UP|UP]] does to [[Class_P|P]].



If [[Class_UL|UL]] = [[Class_NL|NL]], then [[Class_FNL|FNL]] is contained in [[Class_#L|#L]] [[ZooRefs#AJ93|[AJ93] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_UL|UL]] as [[Class_P/poly|P/poly]] does to [[Class_P|P]].



Equals [[Class_NL/poly|NL/poly]] [[ZooRefs#RA00|[RA00] ]]. (A corollary is that [[Class_UL/poly|UL/poly]] is closed under complement).



Note that in [[Class_UL/poly|UL/poly]], the witness must be unique even for bad advice. UL/mpoly (as in BQP/mpoly) is a more natural definition, but this is a moot distinction here because [[ZooRefs#RA00|[RA00] ]] show that they both equal [[Class_NL/poly|NL/poly]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is 'yes,' exactly one computation path accepts.

If the answer is 'no,' all computation paths reject.



Defined by [[ZooRefs#Val76|[Val76] ]].



"Worst-case" one-way functions exist if and only if [[Class_P|P]] does not equal [[Class_UP|UP]] ([[ZooRefs#GS88|[GS88] ]] and independently [[ZooRefs#Ko85|[Ko85] ]]).  "Worst-case" one-way permutations exist if and only if [[Class_P|P]] does not equal [[Class_UP|UP]] ∩ [[Class_coUP|coUP]] [[ZooRefs#HT03|[HT03] ]].  Note that these are weaker than the one-way functions and permutations that are needed for cryptographic applications.



There exists an oracle relative to which [[Class_P|P]] is strictly contained in [[Class_UP|UP]] is strictly contained in [[Class_NP|NP]] [[ZooRefs#Rac82|[Rac82] ]]; indeed, these classes are distinct with probability 1 relative to a random oracle [[ZooRefs#Bei89|[Bei89] ]].



[[Class_NP|NP]] is contained in RP^PromiseUP^ [[ZooRefs#VV86|[VV86] ]].  On the other hand, [[ZooRefs#BBF98|[BBF98] ]] give an oracle relative to which [[Class_P|P]] = [[Class_UP|UP]] but still [[Class_P|P]] does not equal [[Class_NP|NP]].



[[Class_UP|UP]] is not known or believed to contain complete problems.  [[ZooRefs#Sip82|[Sip82] ]], [[ZooRefs#HH86|[HH86] ]] give oracles relative to which [[Class_UP|UP]] has no complete problems.



[[Class_NP|NP]] is contained in RP^Promise-UP^ [[ZooRefs#VV86|[VV86] ]].  On the other hand, [[ZooRefs#BBF98|[BBF98] ]] give an oracle relative to which [[Class_P|P]] = [[Class_UP|UP]] but still [[Class_P|P]] does not equal [[Class_NP|NP]].
== Relations ==


== See Also ==

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

== Comments ==

Defined by [[ZooRefs#BFS86|[BFS86] ]], [[Class_UPPcc|UPPcc]] is one of two communication complexity analogues of [[Class_PP|PP]].

[[Class_UPPcc|UPPcc]] is the class of all languages defined by functions  which are computable by polylogarithmic protocols that accept with probability strictly greater than 1/2 when  and accept with probably strictly less than 1/2 otherwise. No accounting is made for how many random bits are consulted during the protocol.



See also: [[Class_PPcc|PPcc]].
== Relations ==


== See Also ==

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

== Comments ==

The all-American counting class.



The class of decision problems solvable by an [[Class_NP|NP]] machine such that the answer is 'yes' if and only if exactly one computation path accepts.



In contrast to [[Class_UP|UP]], a machine can legally have more than one accepting path - that just means that the corresponding input is not in the language.



Defined in [[ZooRefs#BG82|[BG82] ]].



Contains [[Class_coNP|coNP]].
== Relations ==


== See Also ==

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

== Comments ==

For k = 0, VC,,0,, is the class of compressible languages.

 For k = 1, VC,,1,, is the class of languages that have local verification: they can be verified by testing only a small part of the instance. (Small means polynomial in the witness length and the log of the instance length.)

 For k ≥ 2, [[Class_VCk|VCk]] is the class of languages that can be verified by a circuit of depth k, with size polynomial in the witness length and instance length.



VC,,0,, ⊆ VC,,OR,, ⊆ VC,,1,, ⊆ VC,,2,, ⊆ VC,,3,, ...



Introduced in [[ZooRefs#HN06|[HN06] ]]; see there for formal definitions.
== Relations ==


== See Also ==

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

== Comments ==

The class of languages that have verification presentable as the OR of m instances of SAT, each of size n. (m is the witness length of an instance and n is the instance length.)



Introduced in [[ZooRefs#HN06|[HN06] ]].



See also [[Class_VCk|VCk]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_VPk|VPk]] as [[Class_NC|NC]] does to [[Class_P|P]].



More formally, the class of [[Class_VPk|VPk]] problems computable by a straight-line program of depth polylogarithmic in n.



Surprisingly, [[Class_VNCk|VNCk]] = [[Class_VPk|VPk]] for any k [[ZooRefs#VSB+83|[VSB+83] ]].
== Relations ==


== See Also ==

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

== Comments ==

A superclass of [[Class_VPk|VPk]] in Valiant's algebraic complexity theory, but not quite the analogue of [[Class_NP|NP]].



A problem is in [[Class_VNPk|VNPk]] if there exists a polynomial p with the following properties:



p is computable in [[Class_VPk|VPk]]; that is, by a polynomial-size straight-line program.

The inputs to p are constants c,,1,,,...,c,,m,,,e,,1,,,...,e,,h,, and indeterminates X,,1,,,...,X,,n,, over the base field k.

When p is summed over all 2^h^ possible assignments of {0,1} to each of e,,1,,,...,e,,h,,, the result is some specified polynomial q.



Originated in [Val79b].



If the field k has characteristic greater than 2, then the permanent of an n-by-n matrix of indeterminates is VNP,,k,,-complete under a type of reduction called p-projections ([Val79b]; see also [[ZooRefs#Bur00|[Bur00] ]]).



A central conjecture is that for all k, [[Class_VPk|VPk]] is not equal to [[Class_VNPk|VNPk]].  Bürgisser [[ZooRefs#Bur00|[Bur00] ]] shows that if this were false then:



If k is finite, NC^2^/poly = [[Class_P/poly|P/poly]] = [[Class_NP/poly|NP/poly]] = PH/poly.

If k has characteristic 0, then assuming the Generalized Riemann Hypothesis (GRH), NC^3^/poly = [[Class_P/poly|P/poly]] = [[Class_NP/poly|NP/poly]] = PH/poly, and #P/poly = FP/poly.



In both cases, [[Class_PH|PH]] collapses to [[Class_Σ2P|Σ2P]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems that can be decided by a visibly pushdown automaton. In a visibly pushdown automaton, all push and pop transitions have to be triggered by special alphabet symbols, and thus are visible in the input word. Nondeterminism does not add to the expressive power of this automaton model, and the complexity class is closed under all Boolean operations.



Originated in [[ZooRefs#AM04|[AM04] ]]. See also [[ZooRefs#AM09|[AM09] ]].



Properly contains [[Class_REG|REG]]. Properly contained in [[Class_DCFL|DCFL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of efficiently-solvable problems in Valiant's algebraic complexity theory.



More formally, the input consists of constants c,,1,,,...,c,,m,, and indeterminates X,,1,,,...,X,,n,, over a base field k (for instance, the complex numbers or Z,,2,,).  The desired output is a collection of polynomials over the X,,i,,'s.  The complexity is the minimum number of pairwise additions, subtractions, and multiplications needed by a straight-line program to produce these polynomials.  [[Class_VPk|VPk]] is the class of problems whose complexity is polynomial in n.  (Hence, [[Class_VPk|VPk]] is a nonuniform class, in contrast to [[Class_PC|PC]] and P,,R,,.)



Originated in [Val79b]; see [[ZooRefs#Bur00|[Bur00] ]] for more information.



Contained in [[Class_VNPk|VNPk]] and [[Class_VQPk|VQPk]], and contains [[Class_VNCk|VNCk]].



More formally, the input consists of constants c,,1,,,...,c,,m,, and indeterminates X^1^,...,X,,n,, over a base field k (for instance, the complex numbers or Z,,2,,).  The desired output is a collection of polynomials over the X,,i,,'s.  The complexity is the minimum number of pairwise additions, subtractions, and multiplications needed by a straight-line program to produce these polynomials.  [[Class_VPk|VPk]] is the class of problems whose complexity is polynomial in n.  (Hence, [[Class_VPk|VPk]] is a nonuniform class, in contrast to [[Class_PC|PC]] and P,,R,,.)
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_VPk|VPk]] as [[Class_QP|QP]] does to [[Class_P|P]].



Originated in [Val79b].



The determinant of an n-by-n matrix of indeterminates is VQP,,k,,-complete under a type of reduction called qp-projections (see [[ZooRefs#Bur00|[Bur00] ]] for example).  It is an open problem whether the determinant is VP,,k,,-complete.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_W[t]|W[t]]], except that now the circuit depth can depend on the parameter k rather than being constant.  (The number of unbounded-fanin gates along any path to the root is still at most t.)



W^*^[1] = [[Class_W[1]|W[1]]] [[ZooRefs#DFT96|[DFT96] ]], and W^*^[2] = W[2] [[ZooRefs#DF97|[DF97] ]], but the problem is open for larger t.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which there exists a [[Class_#P|#P]] function f, a polynomial p, and an ε > 0, such that for all inputs x,



If the answer is "yes" then 2^p(|x|)^ ≥ f(x) > (1+ε) 2^p(|x|)-1^.

If the answer is "no" then 0 ≤ f(x) < (1-ε) 2^p(|x|)-1^.



Defined in [[ZooRefs#BGM02|[BGM02] ]], where it is also shown that [[Class_WAPP|WAPP]] is contained in [[Class_AWPP|AWPP]] and [[Class_SBP|SBP]].
== Relations ==


== See Also ==

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

== Comments ==

While is a theorical programing language defined in [[ZooRefs#jon98|[jon98] ]],  is a way to define syntacticaly [[Class_P|P]] and a syntactic resctriction of [[Class_WHILE|WHILE]] is exactly [[Class_L|L]]. The important point is that those two languages are powerful enough to simulate all of [[Class_P|P]] (and L) and when we write a program in this language we never need to prove his time (space) complexity, since the language garantee it !



In While, input are composed only of lists (in a lisp-way where a list is either an empty list or a pair of his first element and his tail) and the elements of the list and variables are only pointers to list.



A program contains global variables and procedures.



Every procedure are composed of a name, a list of argument and local variables and a list of command. The procedure doesn't return any value, they only affect global variables.

The command are: variable affectation, while loop, if/then/else and procedure call.

The empty list is considered as false and everything else as true, this is the only way to do while/if test.



There are three primitives function, tail, head, and cons(h,t), who give the first value of a list, the tail of the list and who return a list whose first element is h and the rest of the list is t and we can call defined procedure.



We can then define WHILE^/cons-rec^ which is [[Class_WHILE|WHILE]] without "cons" primitive and procedure call[#]. It is equivalent to [[Class_L|L]]. The trick to do the computation in logspace is that without recursion we only need to save a fixed number of variables who are only pointers to part of the input, so they only take logspace. Since any logspace TM can avoid having a work tape by having a fixed number of reading head on his input, we can simulate logspace TM by using a variable for every reading head. (The binary string is coded as a list of () for 0 and (()) for 1, so equality can be checked trivially)



[#] in fact we only need to forbid recursive call, hence the name, but when we lose recursion we can assume there is no procedure call w.l.o.g, in fact in [[ZooRefs#jon98|[jon98] ]] [[Class_WHILE|WHILE]] is first defined without procedure call and procedure are defined later, but this presentation may be more easy to understand and at least more general.



We can then also define WHILE^rec/cons^ which is [[Class_WHILE|WHILE]] without "cons" primitive but with procedure calls, and hence recursion. It is equivalent to [[Class_P|P]]. 

The trick to do a computation of a WHILE^rec/cons^ in [[Class_P|P]] is to memoize the couple (global variables, input) when a procedure is called and the value of the globals variable when the procedure end, since we don't have cons, only a polynomial number of call will really be executed and we can detect loop.

Simulating [[Class_P|P]] in WHILE^rec/cons^ is quite more subtle, [[Class_P|P]] TM are equivalent to some counter machine wich can easily be simulated by [[Class_WHILE|WHILE]] programs with cons, and then we can simulate the cons thanks to the call stack.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is "no," then the number of accepting computation paths exactly equals the number of rejecting paths.

If the answer is "yes," then their difference exactly equals a function f(x) computable in polynomial time (i.e. FP).



Defined in [[ZooRefs#FFK94|[FFK94] ]].



Contained in [[Class_C=P|C=P]] ∩ [[Class_coC=P|coC=P]], as well as [[Class_AWPP|AWPP]].



Contains [[Class_SPP|SPP]] and [[Class_LWPP|LWPP]].
== Relations ==


== See Also ==

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

== Comments ==

The union of [[Class_W[t]|W[t]]] over all t.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems of the form (x,k) (k a parameter), that are fixed-parameter reducible to the following:



Weighted 3SAT: Given a 3SAT formula, does it have a satisfying assignment of Hamming weight k?



A fixed-parameter reduction is a Turing reduction that takes time at most f(k)p(|x|), where f is an arbitrary function and p is a polynomial.  Also, if the input is (x,k), then all Weighted 3SAT instances the algorithm queries about must have the form <x',k'> where k' is at most k.



Contains [[Class_FPT|FPT]].



Defined in [[ZooRefs#DF99|[DF99] ]], where the following is also shown:



If [[Class_FPT|FPT]] = [[Class_W[1]|W[1]]] then [[Class_NP|NP]] is contained in DTIME(2^o(n)^).



[[Class_W[1]|W[1]]] can be generalized to [[Class_W[t]|W[t]]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems of the form (x,k) (k a parameter), that are fixed-parameter reducible to the following problem, for some constant h:



Weighted Circuit-SAT: Given a Boolean circuit C (with no restriction on depth), does C have a satisfying assignment of Hamming weight k?



See [[Class_W[1]|W[1]]] for the definition of fixed-parameter reducibility.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contains [[Class_W[SAT]|W[SAT]]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems of the form (x,k) (k a parameter), that are fixed-parameter reducible to the following problem, for some constant h:



Weighted SAT: Given a Boolean formula F (with no restriction on depth), does F have a satisfying assignment of Hamming weight k?



See [[Class_W[1]|W[1]]] for the definition of fixed-parameter reducibility.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contains [[Class_W[t]|W[t]]] for every t, and is contained in [[Class_W[P]|W[P]]].
== Relations ==


== See Also ==

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

== Comments ==

A generalization of [[Class_W[1]|W[1]]].



The class of decision problems of the form (x,k) (k a parameter), that are fixed-parameter reducible to the following problem, for some constant h:



Weighted Weft-t Depth-h Circuit-SAT: Given a Boolean circuit C, with a mixture of fanin-2 and unbounded-fanin gates.  The number unbounded-fanin gates along any path to the root is at most t, and the total depth (fanin-2 and unbounded-fanin) is at most h.  Does C have a satisfying assignment of Hamming weight k?



See [[Class_W[1]|W[1]]] for the definition of fixed-parameter reducibility.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contained in [[Class_W[SAT]|W[SAT]]] and in [[Class_W*[t]|W*[t]]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_MIP*[2,1]|MIP*[2,1]]], but with the further restriction that both provers send only a single bit to the verifier, and the verifier's output is a function of the exclusive-OR of those bits.  There should exist 0<a<b<1 such that if the answer is "yes", then for some responses of the provers the verifier accepts with probability at least b, while if the answer is "no", then for all responses of the provers the verifier accepts with probability at most a.



Defined by [[ZooRefs#CHT+04|[CHT+04] ]], whose motivation was a connection to the Bell and CHSH inequalities of quantum physics.



[[Class_XOR-MIP*[2,1]|XOR-MIP*[2,1]]] is contained in [[Class_NEXP|NEXP]] [[ZooRefs#CHT+04|[CHT+04] ]].



[[Class_XOR-MIP*[2,1]|XOR-MIP*[2,1]]] is contained in [[Class_QIP[2]|QIP[2]]] [[ZooRefs#Weh06|[Weh06] ]]
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems of the form (x,k) (k a parameter) that are solvable in time O(|x|^f(k)^) for some function f.  The algorithm used may depend on k.



Defined in [[ZooRefs#DF99|[DF99] ]].



Contains [[Class_XPuniform|XPuniform]].



Strictly contains [[Class_FPT|FPT]] (by diagonalization).
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_XP|XP]] except that the algorithm used must be the same for each k (though it can take k as input).



Defined in [[ZooRefs#DF99|[DF99] ]].
== Relations ==


== See Also ==

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

== Comments ==

A term of derision, used against a complexity class.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which there exists a polynomial-time machine M such that:



For all input sizes n, there exists a polynomial-size advice string s,,n,, such that M(x,s,,n,,) outputs the correct answer for all inputs x of size n.

For all inputs x and advice strings s, M(x,s) outputs either the correct answer or "I don't know."



Defined in a recent post of the blog Shtetl-Optimized.  See there for an explanation of the class's name.



Contains [[Class_ZPP|ZPP]] by the same argument that places [[Class_BPP|BPP]] in [[Class_P/poly|P/poly]].



Also contains [[Class_P|P]] with [[Class_TALLY|TALLY]] ∩ [[Class_NP|NP]] ∩ [[Class_coNP|coNP]] oracle.



Is contained in [[Class_NP|NP]] ∩ [[Class_coNP|coNP]] and [[Class_YPP|YPP]].
== Relations ==


== See Also ==

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

== Comments ==

The probabilistic analogue of [[Class_YP|YP]]; it is to [[Class_YP|YP]] what [[Class_MA|MA]] is to [[Class_NP|NP]].  Formally, the class of decision problems for which there exists a syntactic [[Class_BPP|BPP]] machine M such that:



For all input sizes n, there exists a polynomial-size advice string a,,n,, such that for all inputs x of size n, M(x,a,,n,,) outputs the correct answer with probability at least 2/3.

For all inputs x and advice strings a, the probability that M(x,a) outputs the incorrect answer is at most 1/3.  In other words, the sum of the probabilities of the correct answer and "I don't know" is at least 2/3.



To amplify a [[Class_YPP|YPP]] machine, one can run it multiple times, then accept if a majority of runs accept, reject if a majority reject, and otherwise output "I don't know."



Contains [[Class_BPP|BPP]] and [[Class_YP|YP]], and is contained in [[Class_MA|MA]] and [[Class_P/poly|P/poly]].
== Relations ==


== See Also ==

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

== Comments ==

Is to [[Class_YPP|YPP]] as [[Class_BQP|BQP]] is to [[Class_BPP|BPP]], and [[Class_QMA|QMA]] is to [[Class_MA|MA]].  The machine is now a quantum computer and the advice is a quantum state |ψ_n>.



Contains [[Class_BQP|BQP]] and [[Class_YPP|YPP]], and is contained in [[Class_QMA|QMA]] and [[Class_BQP/qpoly|BQP/qpoly]].
== Relations ==


== See Also ==

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

== Comments ==

Defined as [[Class_RBQP|RBQP]] ∩ coRBQP.  Equivalently, the class of problems in [[Class_NP|NP]] ∩ [[Class_coNP|coNP]] such that both positive and negative witnesses are in [[Class_FBQP|FBQP]].



For example, the language of square-free numbers is in [[Class_ZBQP|ZBQP]], because factoring is in [[Class_FBQP|FBQP]] and a factorization can be certified in [[Class_ZPP|ZPP]] (indeed in [[Class_P|P]], by [[ZooRefs#AKS02|[AKS02] ]]).



Unlike [[Class_EQP|EQP]] or [[Class_ZQP|ZQP]], [[Class_ZBQP|ZBQP]] would generalize [[Class_ZPP|ZPP]] in practice if quantum computers existed, in the sense that it provides proven answers.



Contains [[Class_ZPP|ZPP]] and is contained in [[Class_RBQP|RBQP]] and [[Class_ZQP|ZQP]].  Also, ZBQP^ZBQP^ = [[Class_ZBQP|ZBQP]].  Defined here to clarify [[Class_EQP|EQP]] and [[Class_ZQP|ZQP]].
== Relations ==


== See Also ==

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

== Comments ==

Often used as a shorthand for (computational zero-knowledge) [[Class_CZK|CZK]], but may also be used as a general paradigm encomposing various classes ranging from perfect and statistical zero-knowledge (SZK) to computational ones (CZK), and also various forms of non-interactive zero-knowledge proof systems.



Zero-knowledge proofs were introduced in [[ZooRefs#GMR89|[GMR89] ]], and further studied in [[ZooRefs#GMW91|[GMW91] ]], which demonstrated the wide applicability of the concept.
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_ZPP|ZPP]], but with 2^O(n)^-time instead of polynomial-time.



[[Class_ZPE|ZPE]] = [[Class_EE|EE]] if and only if [[Class_ZPP|ZPP]] = [[Class_EXP|EXP]] [[ZooRefs#IKW01|[IKW01] ]].
== Relations ==


== See Also ==

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

== Comments ==

Defined as [[Class_RP|RP]] ∩ [[Class_coRP|coRP]].



Defined as the class of problems solvable by randomized algorithms that always return the correct answer, and whose expected running time (on any input) is polynomial, in [[ZooRefs#Gil77|[Gil77] ]].  (Proposition 5.5(iii) in this paper shows that the two definitions above are equivalent.)



Contains the problem of testing whether an integer is prime [[ZooRefs#SS77|[SS77] ]] [[ZooRefs#AH87|[AH87] ]].



In contrast to [[Class_BPP|BPP]] and [[Class_RP|RP]], it is not known whether showing [[Class_ZPP|ZPP]] = [[Class_P|P]] requires proving superpolynomial circuit lower bounds [[ZooRefs#KI02|[KI02] ]].



There exists an oracle relative to which [[Class_ZPP|ZPP]] = [[Class_EXP|EXP]] [Hel84a], [Hel84b], [[ZooRefs#Kur85|[Kur85] ]], [[ZooRefs#Hel86|[Hel86] ]].



Has the same p-measure as [[Class_RP|RP]]. Moreover, this measure is either zero or one. If the measure is non-zero, then [[Class_ZPP|ZPP]] = [[Class_BPP|BPP]] = [[Class_EXP|EXP]] [[ZooRefs#IM03|[IM03] ]].



The class of problems solvable by randomized algorithms that always return the correct answer, and whose expected running time (on any input) is polynomial.



Defined in [[ZooRefs#Gil77|[Gil77] ]].



There exists an oracle relative to which [[Class_ZPP|ZPP]] = [[Class_EXP|EXP]] [[ZooRefs#Hel84|[Hel84] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_ZPP|ZPP]], but with O(f(n))-time instead of polynomial-time.



For any constructible superpolynomial f, [[Class_ZPTIME(f(n))|ZPTIME(f(n))]] with [[Class_NP|NP]] oracle is not contained in [[Class_P/poly|P/poly]] [[ZooRefs#KW98|[KW98] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of questions that can be answered by a QTM that answers yes, no, or "maybe".  If the correct answer is yes, then P[no] = 0, and vice-versa; and the probability of maybe is at most 1/2.  Since some of the probabilities have to vanish, [[Class_ZQP|ZQP]] has the same technical caveats as [[Class_EQP|EQP]].



Defined independently in [[ZooRefs#BW03|[BW03] ]] and in [[ZooRefs#Nis02|[Nis02] ]].



Contains [[Class_EQP|EQP]] and [[Class_ZBQP|ZBQP]] and is contained in [[Class_BQP|BQP]].  Equals [[Class_RQP|RQP]] ∩ coRQP.  There is an oracle such that ZQP^ZQP^ is larger than [[Class_ZQP|ZQP]] [[ZooRefs#BW03|[BW03] ]]; c.f. with [[Class_ZBQP|ZBQP]].
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

Equals [[Class_NQP|NQP]] [[ZooRefs#FGH+98|[FGH+98] ]].
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

Contained in [[Class_NEXP/poly|NEXP/poly]] (folklore result reported in [Fortnow's weblog]).



Contained in [[Class_NEXP/poly|NEXP/poly]] (folklore result reported in [weblog]).
== Relations ==


== See Also ==

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

== Comments ==

Equals [[Class_NL|NL]] [[ZooRefs#Imm88|[Imm88] ]] [[ZooRefs#Sze87|[Sze87] ]].
== Relations ==


== See Also ==

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

== Comments ==

If [[Class_NP|NP]] = [[Class_coNP|coNP]], then any inconsistent Boolean formula of size n has a proof of inconsistency of size polynomial in n.



If [[Class_NP|NP]] does not equal [[Class_coNP|coNP]], then [[Class_P|P]] does not equal [[Class_NP|NP]].  But the other direction is not known.



See also: [[Class_NP|NP]] ∩ [[Class_coNP|coNP]].



Every problem in [[Class_coNP|coNP]] has an [[Class_IP|IP]] (interactive proof) system, where moreover the prover can be restricted to BPP^#P^. If every problem in [[Class_coNP|coNP]] has an interactive protocol whose rounds are bounded by a polylogarithmic function, then [[Class_EH|EH]] collapses to the third level [[ZooRefs#SS04|[SS04] ]].



Co-NP is equal to SO-A, the second-order queries where the second-order quantifiers are only universals.



Every problem in [[Class_coNP|coNP]] has an [[Class_IP|IP]] (interactive proof) system, where moreover the prover can be restricted to BPP^#P^.
== Relations ==


== See Also ==

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

== Comments ==

If [[Class_NP|NP]] is contained in [[Class_coNP/poly|coNP/poly]] then [[Class_PH|PH]] collapses to S,,2,,P^NP^ [[ZooRefs#CCH+01|[CCH+01] ]].



NP^NP^NP^(coNP/poly ∩ NP)^ = NP^NP^NP^ [[ZooRefs#HNO+96|[HNO+96] ]]



Note: At the suggestion of Luis Antuñes, the above specimen of the Complexity Zoo has been locked in a cage.
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

Equals [[Class_C=P|C=P]] [[ZooRefs#FGH+98|[FGH+98] ]].
== Relations ==


== See Also ==

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

== Comments ==

Does not equal [[Class_RE|RE]].



The problem "given a computable predicate [[Class_P|P]], is [[Class_P|P]] true of all positive integers?" is coRE-complete.
== Relations ==


== See Also ==

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

== Comments ==

Contains the problem of whether a bipartite graph has a perfect matching [[ZooRefs#Kar86|[Kar86] ]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#Gil77|[Gil77] ]].  (This paper does not actually discuss [[Class_coRP|coRP]], other than implicitly mentioning that [[Class_ZPP|ZPP]] = [[Class_RP|RP]] ∩ co-RP.  Is there a better reference?)



Contains the problem of testing whether an integer is prime [[ZooRefs#SS77|[SS77] ]].



Defined in [[ZooRefs#Gil77|[Gil77] ]].
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

[[ZooRefs#Tor00|[Tor00] ]] showed the following problem complete for [[Class_coUCC|coUCC]] under [[Class_L|L]] reductions:



Given a colored graph G with at most two vertices having any given color, does G have any nontrivial automorphisms?
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_compNP|compNP]] but for interactive (IP) proofs instead of [[Class_NP|NP]] proofs.



More formally, [[Class_compIP|compIP]] is the class of decision problems [[Class_L|L]] in [[Class_IP|IP]] = [[Class_PSPACE|PSPACE]] such that, if the answer is "yes," then that can be proven by an interactive protocol between a [[Class_BPP|BPP]] verifier and a prover, a [[Class_BPP|BPP]] machine with access only to an oracle for [[Class_L|L]].



Assuming [[Class_NEE|NEE]] is not contained in [[Class_BPEE|BPEE]], [[Class_NP|NP]] (and indeed [[Class_NP|NP]] ∩ Coh) is not contained in [[Class_compIP|compIP]] [[ZooRefs#BG94|[BG94] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems [[Class_L|L]] in [[Class_NP|NP]] such that, if the answer is "yes," then a proof can be constructed in polynomial time given access only to an oracle for [[Class_L|L]].



Contains [[Class_NPC|NPC]].



[[ZooRefs#BG94|[BG94] ]] show that [[Class_compNP|compNP]] is contained in [[Class_frIP|frIP]], and that assuming [[Class_NEE|NEE]] is not contained in [[Class_BPEE|BPEE]], [[Class_compNP|compNP]] does not equal [[Class_NP|NP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems [[Class_L|L]] that have a decider in the following sense.  There exists a [[Class_BPP|BPP]] machine D such that for all inputs x,



If the answer is "yes" then D^L^(x) (D with oracle for L) accepts with probability at least 2/3.

If the answer is "no" then D^A^(x) accepts with probability at most 1/3 for all oracles A.



Contains [[Class_compIP|compIP]] [[ZooRefs#BG94|[BG94] ]] and [[Class_Check|Check]] [[ZooRefs#BK89|[BK89] ]].



Contained in [[Class_MIP|MIP]] = [[Class_NEXP|NEXP]] [[ZooRefs#FRS88|[FRS88] ]].



Assuming [[Class_NEE|NEE]] is not contained in [[Class_BPEE|BPEE]], [[Class_NP|NP]] (and indeed [[Class_NP|NP]] ∩ Coh) is not contained in [[Class_frIP|frIP]] [[ZooRefs#BG94|[BG94] ]].
== Relations ==


== See Also ==

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

== Comments ==

Alternate name for [[Class_k-PBP|k-PBP]].
== Relations ==


== See Also ==

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

== Comments ==

See [[Class_k-PBP|k-PBP]] for the definition of a classical branching program.



A quantum branching program is the natural quantum generalization: we have a quantum state in a Hilbert space of dimension k.  Each step t consists of applying a unitary matrix U^(t)^(x,,i,,): that is, U^(t)^ depends on a single bit x,,i,, of the input.  (So these are the quantum analogues of so-called oblivious branching programs.)  In the end we measure to decide whether to accept; there must be zero probability of error.



Defined in [[ZooRefs#AMP02|[AMP02] ]], where it was also shown that [[Class_NC1|NC1]] is contained in 2-EQBP.



k-BQBP can be defined similarly.
== Relations ==


== See Also ==

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

== Comments ==

A branching program is a directed acyclic graph with a designated start vertex.  Each (non-sink) vertex is labeled by the name of an input bit, and has two outgoing edges, one of which is followed if that input bit is 0, the other if the bit is 1.  A sink vertex can be either an 'accept' or a 'reject' vertex.



The size of the branching program is the number of vertices.  The branching program has width k if the vertices can be sorted into levels, each with at most k vertices, such that each edge goes from a level to the one immediately after it.



Then [[Class_k-PBP|k-PBP]] is the class of decision problems solvable by a family of polynomial-size, width-k branching programs.  (A uniformity condition may also be imposed.)



[[Class_k-PBP|k-PBP]] equals (nonuniform) [[Class_NC1|NC1]] for constant k at least 5 [[ZooRefs#Bar89|[Bar89] ]].  On the other hand, 4-PBP is in [[Class_ACC0|ACC0]] [[ZooRefs#BT88|[BT88] ]].



Contained in [[Class_k-EQBP|k-EQBP]], as well as [[Class_PBP|PBP]].



See also [[Class_BPd(P)|BPd(P)]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#GS90|[GS90] ]].  Equals [[Class_mP|mP]] by definition.
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a family of monotone log-width polynomial-size leveled circuits.  (A leveled circuit is one where gates on each level can depend only on the level immediately below it.)



Defined in [[ZooRefs#GS90|[GS90] ]], who raise as an open problem to define a uniform version of [[Class_mL|mL]].



Strictly contains [[Class_mNC1|mNC1]] [[ZooRefs#GS91|[GS91] ]].



Contained in (nonuniform versions of) [[Class_mNL|mNL]] and [[Class_mcoNL|mcoNL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a family of monotone [[Class_NC1|NC1]] circuits (i.e. AND and OR gates only).



A uniformity condition could also be imposed.



Defined in [[ZooRefs#GS90|[GS90] ]].



Strictly contained in [[Class_mNL|mNL]] [[ZooRefs#KW88|[KW88] ]], and indeed in [[Class_mL|mL]] [[ZooRefs#GS91|[GS91] ]].



Strictly contains [[Class_mTC0|mTC0]] [[ZooRefs#Yao89|[Yao89] ]].
== Relations ==


== See Also ==

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

== Comments ==

See [[Class_mP|mP]] for the definition of a monotone nondeterministic Turing machine, due to [[ZooRefs#GS90|[GS90] ]].



[[Class_mNL|mNL]] is the class of decision problems solvable by a monotone nondeterministic log-space Turing machine.



[[Class_mNL|mNL]] does not equal [[Class_mcoNL|mcoNL]] [[ZooRefs#GS90|[GS90] ]], in contrast to the case for [[Class_NL|NL]] and [[Class_coNL|coNL]].



Also, [[Class_mNL|mNL]] strictly contains [[Class_mNC1|mNC1]] [[ZooRefs#KW88|[KW88] ]].



See also: [[Class_mL|mL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems for which a 'yes' answer can be verified in [[Class_mP|mP]] (that is, monotone polynomial-time).  The monotonicity requirement applies only to the input bits, not to the bits that are guessed nondeterministically. So, in the corresponding circuit, one can have NOT gates so long as they depend only on the nondeterministic guess bits.



Defined in [[ZooRefs#GS90|[GS90] ]], where it was also shown that [[Class_mNP|mNP]] is 'trivial': that is, it contains exactly the monotone problems in [[Class_NP|NP]].



Strictly contains [[Class_mP|mP]] [[ZooRefs#Raz85|[Raz85] ]].
== Relations ==


== See Also ==

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

== Comments ==

The definition of this class, due to [[ZooRefs#GS90|[GS90] ]], is not obvious.  First, a monotone nondeterministic Turing machine is one such that, whenever it can make a transition with a 0 on its input tape, it can also make that same transition with a 1 on its input tape. (This restriction does not apply to the work tape.)  A monotone alternating Turing machine is subject to the restriction that it can only reference an input bit x by, "there exists a z at most x," or "for all z at least x."



Then applying the result of [[ZooRefs#CKS81|[CKS81] ]] that [[Class_P|P]] = [[Class_AL|AL]], [[Class_mP|mP]] is defined to be [[Class_mAL|mAL]]: the class of decision problems solvable by a monotone alternating log-space Turing machine.



Actually there's a caveat: A monotone Turing machine or circuit can first negate the entire input, then perform a monotone computation.  That way it becomes meaningful to talk about whether a monotone complexity class is closed under complement.



Strictly contained in [[Class_mNP|mNP]] [[ZooRefs#Raz85|[Raz85] ]].



Deciding whether a bipartite graph has a perfect matching, despite being both a monotone problem and in [[Class_P|P]], requires monotone circuits of superpolynomial size [Raz85b].  Letting MONO be the class of monotone problems, it follows that [[Class_mP|mP]] is strictly contained in MONO ∩ [[Class_P|P]].



See also: [[Class_mNC1|mNC1]], [[Class_mL|mL]], [[Class_mNL|mNL]], [[Class_mcoNL|mcoNL]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a nonuniform family of polynomial-size Boolean circuits with only AND and OR gates, no NOT gates.  (Or rather, following the definitions of [[ZooRefs#GS90|[GS90] ]], the entire input can be negated as long as there are no other negations.)



More straightforward to define than [[Class_mP|mP]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by a family of monotone [[Class_TC0|TC0]] circuits (i.e. constant-depth, polynomial-size, AND, OR, and threshold gates, but no NOT gates).



A uniformity condition could also be imposed.



Defined in [[ZooRefs#GS90|[GS90] ]].



Strictly contained in [[Class_mNC1|mNC1]] [[ZooRefs#Yao89|[Yao89] ]].
== Relations ==


== See Also ==

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

== Comments ==

Defined in [[ZooRefs#GS90|[GS90] ]], where it was also shown that [[Class_mcoNL|mcoNL]] does not equal [[Class_mNL|mNL]].



See also: [[Class_mL|mL]].
== Relations ==


== See Also ==

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

== Comments ==

Equals DSPACE((log n)^c^).



In contrast to [[Class_L|L]], which is contained in [[Class_P|P]], it is not known if [[Class_polyL|polyL]] is contained in [[Class_P|P]] or vice versa.  On the other hand, we do know that [[Class_polyL|polyL]] does not equal [[Class_P|P]], since (for example) [[Class_polyL|polyL]] does not have complete problems under many-to-one logspace reductions.
== Relations ==


== See Also ==

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

== Comments ==

The class of functions computable as |S|, where S is the set of output values returned by the accepting paths of an [[Class_NP|NP]] machine.



Defined in [[ZooRefs#KST+89|[KST+89] ]], where it is also shown that [[Class_span-P|span-P]] contains [[Class_#P|#P]] and [[Class_OptP|OptP]]; and that [[Class_span-P|span-P]] = [[Class_#P|#P]] if and only if [[Class_UP|UP]] = [[Class_NP|NP]].
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

A level of [[Class_PH|PH]], the polynomial hierarchy.



Contains [[Class_BH|BH]].



There exists an oracle relative to which [[Class_Δ2P|Δ2P]] is not contained in [[Class_PP|PP]] [[ZooRefs#Bei94|[Bei94] ]].



There exists another oracle relative to which [[Class_Δ2P|Δ2P]] is contained in [[Class_P/poly|P/poly]] [[ZooRefs#BGS75|[BGS75] ]], and indeed has linear-size circuits [[ZooRefs#Wil85|[Wil85] ]].



There exists an oracle B for which BPP^B^ is exponentially more powerful than Δ,,2,,P^B^ [[ZooRefs#KV96|[KV96] ]].



If [[Class_P|P]] = [[Class_NP|NP]], then any polynomial-size circuit C can be learned in [[Class_Δ2P|Δ2P]] with C oracle [[ZooRefs#Aar06|[Aar06] ]].
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

Complement of [[Class_Σ2P|Σ2P]].



Along with [[Class_Σ2P|Σ2P]], comprises the second level of [[Class_PH|PH]], the polynomial hierarchy. For any fixed k, there is a problem in [[Class_Π2P|Π2P]] ∩ [[Class_Σ2P|Σ2P]] that cannot be solved by circuits of size n^k^ [[ZooRefs#Kan82|[Kan82] ]].
== Relations ==


== See Also ==

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

== Comments ==

Complement of [[Class_Π2P|Π2P]].



Along with [[Class_Π2P|Π2P]], comprises the second level of [[Class_PH|PH]], the polynomial hierarchy.



[[ZooRefs#Uma98|[Uma98] ]] has shown that the following problems are complete for [[Class_Σ2P|Σ2P]]:



Minimum equivalent DNF.  Given a DNF formula F and integer k, is there a DNF formula equivalent to F with k or fewer occurences of literals?

Shortest implicant.  Given a formula F and integer k, is there a conjunction of k or fewer literals that implies F?  (Note that this problem cannot be Σ,,2,,P-complete for DNF formulas unless [[Class_Σ2P|Σ2P]] equals βP^NP^.)



For any fixed k, there is a problem in [[Class_Σ2P|Σ2P]] ∩ [[Class_Π2P|Π2P]] that cannot be solved by circuits of size n^k^ [[ZooRefs#Kan82|[Kan82] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems for which there exists a polynomial-time predicate P(x,y,z) such that for all x, if the answer on input x is "yes," then



For all y, there exists a z for which P(x,y,z).

For all z, there exists a y for which P(x,y,z).



Contained in [[Class_Σ2P|Σ2P]] and [[Class_Π2P|Π2P]].



Defined in [[ZooRefs#Can96|[Can96] ]], where it was also observed that [[Class_Φ2P|Φ2P]] = [[Class_S2P|S2P]].
== Relations ==


== See Also ==

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

== Comments ==

β,,k,,P is the class of decision problems solvable by a polynomial-time Turing machine that makes O(log^k^n) nondeterministic transitions, with the same acceptance mechanism as [[Class_NP|NP]].  Equivalently, the machine receives a purported proof of size O(log^k^n) that the answer is 'yes.'



Then [[Class_βP|βP]] is the union of β,,k,,P over all constant k.



Defined in [[ZooRefs#KF84|[KF84] ]].  See also the survey [[ZooRefs#GLM96|[GLM96] ]].



There exist oracles relative to which basically any consistent inclusion structure among the β,,k,,P's can be realized [[ZooRefs#BG98|[BG98] ]].



β,,2,,P contains [[Class_LOGNP|LOGNP]] and [[Class_LOGSNP|LOGSNP]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_BPP|BPP]], except that the random bit source is biased as follows.  Each bit could depend on all the previous bits in arbitrarily complicated ways; the only promise is that the bit is 1 with probability in the range [δ,1-δ], conditioned on all previous bits.



So clearly 0-BPP = [[Class_P|P]] and 1/2-BPP = [[Class_BPP|BPP]].



It turns out that, for any δ>0, [[Class_δ-BPP|δ-BPP]] = [[Class_BPP|BPP]] [[ZooRefs#VV85|[VV85] ]], [[ZooRefs#Zuc91|[Zuc91] ]].
== Relations ==


== See Also ==

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

== Comments ==

Same as [[Class_δ-BPP|δ-BPP]], but for [[Class_RP|RP]] instead of [[Class_BPP|BPP]].



For any δ>0, [[Class_δ-RP|δ-RP]] = [[Class_RP|RP]] [[ZooRefs#VV85|[VV85] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of problems for which there exists a [[Class_BPP|BPP]] machine M such that, for all inputs x,



If the answer is "yes" then there exists a y such that M(x,y) accepts.

If the answer is "no" then for all y, M(x,y) rejects.



Alternatively defined as NP^BPP^.



Contains [[Class_NP|NP]] and [[Class_BPP|BPP]], and is contained in [[Class_MA|MA]] and [[Class_SBP|SBP]].



[[Class_∃BPP|∃BPP]] seems obviously equal to [[Class_MA|MA]], yet [[ZooRefs#FFK+93|[FFK+93] ]] constructed an oracle relative to which they're unequal!  Here is the difference: if the answer is "yes," [[Class_MA|MA]] requires only that there exist a y such that for at least 2/3 of random strings r, M(x,y,r) accepts (where M is a [[Class_P|P]] predicate).  For all other y's, the proportion of r's such that M(x,y,r) accepts can be arbitrary (say, 1/2).  For [[Class_∃BPP|∃BPP]], by contrast, the probability that M(x,y) accepts must always be either at most 1/3 or at least 2/3, for all y's.
== Relations ==


== See Also ==

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

== Comments ==

Contains [[Class_NP|NP]] and [[Class_NISZK|NISZK]], and is contained in the third level of [[Class_PH|PH]].
== Relations ==


== See Also ==

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

== Comments ==

The exponential-time analogue of [[Class_⊕P|⊕P]].



There exists an oracle relative to which [[Class_⊕EXP|⊕EXP]] = [[Class_ZPP|ZPP]] [[ZooRefs#BBF98|[BBF98] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_L|L]] as [[Class_⊕P|⊕P]] does to [[Class_P|P]].



Contains [[Class_SL|SL]] [[ZooRefs#KW93|[KW93] ]].



Solving a linear system over Z,,2,, is complete for [[Class_⊕L|⊕L]] [[ZooRefs#Dam90|[Dam90] ]].



⊕L^⊕L^ = [[Class_⊕L|⊕L]] [[ZooRefs#HRV00|[HRV00] ]].
== Relations ==


== See Also ==

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

== Comments ==

Has the same relation to [[Class_⊕L|⊕L]] as [[Class_P/poly|P/poly]] does to [[Class_P|P]].



Contains [[Class_NL/poly|NL/poly]] [[ZooRefs#GW96|[GW96] ]].
== Relations ==


== See Also ==

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

== Comments ==

The class of decision problems solvable by an [[Class_NP|NP]] machine such that



If the answer is 'yes,' then the number of accepting paths is odd.

If the answer is 'no,' then the number of accepting paths is even.



Defined in [[ZooRefs#PZ83|[PZ83] ]].



Contains graph isomorphism; indeed, graph isomorphism is low for [[Class_⊕P|⊕P]] [[ZooRefs#AK02|[AK02] ]].



Contains [[Class_FewP|FewP]] [[ZooRefs#CH89|[CH89] ]].



There exists an oracle relative to which [[Class_P|P]] = [[Class_⊕P|⊕P]] but [[Class_P|P]] is not equal to [[Class_NP|NP]] (and indeed [[Class_NP|NP]] = EXP) [[ZooRefs#BBF98|[BBF98] ]].



Equals Mod,,2^m,,P for every positive integer m.
== Relations ==


== See Also ==

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

== Comments ==


== Relations ==


== See Also ==

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

== Comments ==

The class of problems solvable by a nonuniform family of polynomial-size, polylog-depth circuits with unbounded-fanin XOR and bounded-fanin AND gates.



Defined in [[ZooRefs#GW96|[GW96] ]], where it was also shown that [[Class_⊕SAC1|⊕SAC1]] contains [[Class_SAC1|SAC1]].
== Relations ==


== See Also ==

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

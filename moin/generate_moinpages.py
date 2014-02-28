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

Contained in GapAC^0^.
== Relations ==

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

Counterpart of GI.
== Relations ==

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

Has the same relation to L as #P does to P.

#L is contained in DET [AJ93].
== Relations ==

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

Has the same relation to #L as P/poly does to P.
== Relations ==

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

The class of function problems of the form "compute f(x)," where f is the number of accepting paths of an NP machine.

The canonical #P-complete problem is #SAT: given a Boolean formula, compute how many satisfying assignments it has.

Defined in [Val79], where it was also shown that the problem of counting the number of perfect matchings in a bipartite graph (or equivalently, computing the permanent of a 0-1 matrix) is #P-complete.

What makes that interesting is that the associated decision problem (whether a bipartite graph has a perfect matching) is in P.

PH is in P^#P^ [Tod89].

Any function in #P can be approximated to within a polynomial factor in BPP with NP oracle [Sto85].
== Relations ==

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

Roughly, the analogue of #P for parameterized complexity.  I.e. the class of parameterized counting problems that are fixed-parameter parsimonious reducible to the following problem:

#WSAT: Given a Boolean formula, count the number of satisfying assignments of Hamming weight k (where k is the parameter).

Defined in [FG02], which should be consulted for the full definition.  [FG02] also showed that there exist #W[1]-complete problems whose corresponding decision problems are fixed-parameter tractable (i.e. in FPT).
== Relations ==

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

Then (M,,k,,)P is the class of decision problems solvable by an NP machine with the following acceptance mechanism.  The i^th^ computation path (under some lexicographic ordering) outputs an element m,,i,, of M,,k,,.  Then the machine accepts if and only if m,,1,,m,,2,,...m,,s,, is the identity (where s is the number of paths).

Defined by Hertrampf [Her97], who also showed the following (in the special case M is a group):

If G is any nonsolvable group (for example S,,5,,, the symmetric group on 5 elements), then (G)P = PSPACE.
(Z,,k,,)P = coMod,,k,,P, where Z,,k,, is the cyclic group on k elements.
If |G|=k, then (G)P contains coMod,,k,,P.
== Relations ==

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

Together with NP/poly ∩ coNP/poly, has the same relation to NP ∩ coNP as P/poly has to P.  A language in (NP ∩ coNP)/poly is defined by a single language in NP ∩ coNP which is then modified by advice.  A language in NP/poly ∩ coNP/poly comes from two possibly different languages in NP and coNP which become the same with good advice.

There is an oracle relative to which NP/poly ∩ coNP/poly, indeed NP/1 ∩ coNP/1, is not contained in (NP ∩ coNP)/poly [FFK+93].  Recently they improved this to NP/1 ∩ coNP [FF..].

If NP is contained in (NP ∩ coNP)/poly, then PH collapses to S,,2,,P^NP ∩ coNP^ [CCH+01].
== Relations ==

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

See AvgP for basic notions of average-case complexity.

(NP,P-samplable) is the same as DistNP, except that the distribution μ only needs to be samplable in polynomial time.  μ's cumulative density function does not need to be computable in polynomial time.

Any problem complete for DistNP is also complete for (NP,P-samplable) [IL90].
== Relations ==

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

The intersection of NP,,C,, with {0,1}^*^ (i.e. the set of binary strings).

Contains NP.

Is contained in PSPACE, and in AM assuming the Extended Riemann Hypothesis [Koi96].
== Relations ==

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

Defined in [Bra77], where it was also shown that 1NAuxPDA^p^ strictly contains CFL and is strictly contained in LOGCFL. The class corresponds to the closure of CFL under one-way log-space reductions.
== Relations ==

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

Same as SBP, except that f is a nonnegative-valued GapP function rather than a #P function.

Defined in [Vya03], where the following was also shown:

A,,0,,PP contains QMA, AWPP, and coC,,=,,P.
A,,0,,PP is contained in PP.
If A,,0,,PP = PP then PH is contained in PP.

Kuperberg ([Kup09]) showed that A,,0,,PP = SBQP.

Same as SBP, except that f is a GapP rather than #P function.
== Relations ==

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

Then AC is the union of AC^i^ over all nonnegative i.

AC^i^ is contained in NC^i+1^; thus, AC = NC.

Contains NL.

For a random oracle A, (AC^i^)^A^ is strictly contained in (AC^i+1^)^A^, and (uniform) AC^A^ is strictly contained in P^A^, with probability 1 [Mil92].

fo-uniform AC with depth  is equal to FO[]
== Relations ==

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

An especially important subclass of AC, corresponding to constant-depth, unbounded-fanin, polynomial-size circuits with AND, OR, and NOT gates.

Computing the Parity or Majority of n bits is not in AC^0^ [FSS84].

There are functions in AC^0^ that are pseudorandom for all statistical tests in AC^0^ [NW94].  But there are no functions in AC^0^ that are pseudorandom for all statistical tests in QP (quasipolynomial time) [LMN93].

[LMN93] showed furthermore that functions with AC^0^ circuits of depth d are learnable in QP, given their outputs on O(2^log(n)^O(d)^) randomly chosen inputs.  On the other hand, this learning algorithm is essentially optimal, unless there is a 2^n^o(1)^ algorithm for factoring [Kha93].

Although there are no good pseudorandom functions in AC^0^, [IN96] showed that there are pseudorandom generators that stretch n bits to n+Θ(log n), assuming the hardness of a problem based on subset sum.

AC^0^ contains NC^0^, and is contained in QAC,,f,,^0^ and MAC^0^.

In descriptive complexity, uniform AC^0^ can be characterized as the class of problems expressible by first-order predicates with addition and multiplication operators - or indeed, with ordering and multiplication, or ordering and division (see [Lee02]). So it's equivalent to the class FO and to AL the alternating logtime hierarchy.

[BLM+98] showed the following problem is complete for depth-k AC^0^ circuits (with a uniformity condition):

Given a grid graph of polynomial length and width k, decide whether there is a path between vertices s and t (which can be given as part of the input).

Computing the parity or majority of n bits is not in AC^0^ [FSS84].

Although there are no good pseudorandom functions in AC^0^, [IN96] showed that there are pseudorandom generators in AC^0^ that stretch n bits to n+Θ(log n), assuming the hardness of a problem based on subset sum. Work of [AIK04] shows pseudorandom generators in NC^0^ under more relaxed assumptions.

AC^0^ contains NC^0^, and is contained in QAC^0^ and MAC^0^.

In descriptive complexity, uniform AC^0^ can be characterized as the class of problems expressible by first-order predicates with addition and multiplication operators - or indeed, with ordering and multiplication, or ordering and division (see [Lee02]).
== Relations ==

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

Same as AC^0^, but now "MOD m" gates (for a specific m) are allowed in addition to AND, OR, and NOT gates.  (A MOD m gate outputs 0 if the sum of its inputs is congruent to 0 modulo m, and 1 otherwise.)

If m is a power of a prime p, then for any prime q not equal to p, deciding whether the sum of n bits is congruent to 0 modulo q is not in AC^0^[m] [Raz87] [Smo87].  It follows that, for any such m, AC^0^[m] is strictly contained in NC^1^.

However, if m is a product of distinct primes (e.g. 6), then it is not even known whether AC^0^[m] = NP!

See also: QAC^0^[m].

However, if m is a product of distinct primes (i.e. 6), then it is not even known whether AC^0^[m] = NP!
== Relations ==

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

See AC.
== Relations ==

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

Same as AC^0^[m], but now the constant-depth circuit can contain MOD m gates for any m.

Contained in TC^0^.

Indeed, can be simulated by depth-3 threshold circuits of quasipolynomial size [Yao90].

According to [All96], there is no good evidence for the existence of cryptographically secure functions in ACC^0^.

There is no non-uniform ACC^0^ circuits of polynomial size for NTIMES[2^n^] and no ACC^0^ circuit of size 2^n^O(1)^^ for E^NP^ (The class E with an NP oracle). These are the only two known nontrivial lower bounds against ACC^0^ and were recently discovered by [Wil11].

Contains 4-PBP [BT88].

See also: QACC^0^.

In 1996, [All96] suggested the existence of cryptographically secure functions in ACC^0^ as an important open question. In 2004, work of [AIK04] showed pseudorandom generators in NC^0^ based on widely-believed assumptions.
== Relations ==

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

The analog of PH in computability theory.

Let Δ,,0,, = Σ,,0,, = Π,,0,, = R.  Then for i>0, let

Δ,,i,, = R with Σ,,i-1,, oracle.
Σ,,i,, = RE with Σ,,i-1,, oracle.
Π,,i,, = coRE with Σ,,i-1,, oracle.

Then AH is the union of these classes for all nonnegative constant i.

Each level of AH strictly contains the levels below it.

An equivalent definition is:  is the set of numbers decided by formula with one free variable and bounded quantifier, where the primitives are + and . A bounded quantifier is of the form  or  where   is considered to be free in . Then  is the sets of number validating a formula of the form  with .  is the set of formula who are negation of  formula.
== Relations ==

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

Same as AP, but for logarithmic-space instead of polynomial-time.

AL = P [CKS81].
== Relations ==

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

Literally, the class of ALL languages.

ALL is a gargantuan beast that's been wreaking havoc in the Zoo of late.

First [Aar04b] observed that PP/rpoly (PP with polynomial-size randomized advice) equals ALL, as does PostBQP/qpoly (PostBQP with polynomial-size quantum advice).

Then [Raz05] showed that QIP/qpoly, and even IP(2)/rpoly, equal ALL.

Nor is it hard to show that MA,,EXP,,/rpoly = ALL.

On the other hand, even though PSPACE contains PP, and EXPSPACE contains MA,,EXP,,, it's easy to see that PSPACE/rpoly = PSPACE/poly and EXPSPACE/rpoly = EXPSPACE/poly are not ALL.

So does ALL have no respect for complexity class inclusions at ALL?  (Sorry.)

It is not as contradictory as it first seems.  The deterministic base class in all of these examples is modified by computational non-determinism after it is modified by advice.  For example, MA,,EXP,,/rpoly means M(A,,EXP,,/rpoly), while (MA,,EXP,,)/rpoly equals MA,,EXP,,/poly by a standard argument.  In other words, it's only the verifier, not the prover or post-selector, who receives the randomized or quantum advice. The prover knows a description of the advice state, but not its measured values.  Modification by /rpoly does preserve class inclusions when it is applied after other changes.
== Relations ==

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

ALOGTIME is the class of languages decidable in logarithmic time by a random access alternating Turing machine.

Known to be equal to U,,E^*^,,-uniform NC^1^.
== Relations ==

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

Arthur, a BPP (i.e. probabilistic polynomial-time) verifier, generates a "challenge" based on the input, and sends it together with his random coins to Merlin.  Merlin sends back a response, and then Arthur decides whether to accept.  Given an algorithm for Arthur, we require that

If the answer is "yes," then Merlin can act in such a way that Arthur accepts with probability at least 2/3 (over the choice of Arthur's random bits).
If the answer is "no," then however Merlin acts, Arthur will reject with probability at least 2/3.

Surprisingly, it turns out that such a system is just as powerful as a private-coin one, in which Arthur does not need to send his random coins to Merlin [GS86].  So, Arthur never needs to hide information from Merlin.

Furthermore, define AM[k] similarly to AM, except that Arthur and Merlin have k rounds of interaction.  Then for all constant k>2, AM[k] = AM[2] = AM [BM88].  Also, the result of [GS86] can then be stated as follows: IP[k] is contained in AM[k+2] for every k (constant or non-constant).

AM contains graph nonisomorphism.

Contains NP, BPP, and SZK, and is contained in Π,,2,,P and NP/poly.

If AM contains coNP then PH collapses to Σ,,2,,P ∩ Π,,2,,P [BHZ87].

There exists an oracle relative to which AM is not contained in PP [Ver92].

AM = NP under a strong derandomization assumption: namely that some language in NE ∩ coNE requires nondeterministic circuits of size 2^Ω(n)^ ([MV99], improving [KM99]).  (A nondeterministic circuit C has two inputs, x and y, and accepts on x if there exists a y such that C(x,y)=1.)
== Relations ==

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

The class of decision problems for which both "yes" and "no" answers can be verified by an AM protocol.

If EXP requires exponential time even for AM protocols, then AM ∩ coAM = NP ∩ coNP [GST03].

There exists an oracle relative to which AM ∩ coAM is not contained in PP [Ver95].
== Relations ==

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

Same as AM, except that Arthur is exponential-time and can exchange exponentially long messages with Merlin.

Contains MA,,EXP,,, and is contained in EH and indeed S,,2,,-EXP•P^NP^.

If coNP is contained in AM[polylog] then EH collapses to AM,,EXP,, [PV04].
== Relations ==

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

Same as AM, except that we allow polylog(n) rounds of interaction between Arthur and Merlin instead of a constant number.

Not much is known about AM[polylog] -- for example, whether it sits in PH.  However, [SS04] show that if AM[polylog] contains coNP, then EH collapses to S,,2,,-EXP•P^NP^.  ([PV04] improved the collapse to AM,,EXP,,.)
== Relations ==

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

Then AP is the class of decision problems solvable in polynomial time by an alternating Turing machine.

AP = PSPACE [CKS81].

The abbreviation AP is also used for Approximable in Polynomial Time, see AxP.
== Relations ==

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

Roughly, the class of decision problems for which the following holds.  For all polynomials p(n), there exist GapP functions f and g such that for all inputs x with n=|x|,

If the answer is "yes" then 1 > f(x)/g(1^n^) > 1-2^-p(n)^.
If the answer is "no" then 0 < f(x)/g(1^n^) < 2^-p(n)^.

Defined in [Li93], where the following was also shown:

APP is contained in PP, and indeed is low for PP.
APP is closed under intersection, union, and complement.

APP contains AWPP [Fen02].

The abbreviation APP is also used for Approximable in Probabilistic Polynomial Time, see AxPP.
== Relations ==

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

The subclass of NPO problems that admit constant-factor approximation algorithms.  (I.e., there is a polynomial-time algorithm that is guaranteed to find a solution within a constant factor of the optimum cost.)

Contains PTAS.

Equals the closure of MaxSNP and of MaxNP under PTAS reduction [KMS+99], [CT94].

Defined in [ACG+99].
== Relations ==

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

In particular, AP = ATIME(poly(n)).
== Relations ==

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

Contains GAN-SPACE(f(n)).

AUC-SPACE(poly(n)) = SAPTIME = PSPACE [Pap83].

[Con92] shows that AUC-SPACE(log n) has a natural complete problem, and is contained in NP ∩ coNP.
== Relations ==

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

Defined in [OW93] to be the class of decision problems that have a good average-case BPP algorithm, whenever the input is chosen from an efficiently samplable distribution.

Note that this is not the same as the BPP version of AvgP.
== Relations ==

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

The class of decision problems solvable by an NP machine such that for some polynomial-time computable (i.e. FP) function f,

If the answer is "no," then the difference between the number of accepting and rejecting paths is non-negative and at most 2^-poly(n)^f(x).
If the answer is "yes," then the difference is between (1-2^-poly(n)^)f(x) and f(x).

Defined in [FFK94].

Contains BQP [FR98], WAPP [BGM02], LWPP, and WPP.

Contained in APP [Fen02].
== Relations ==

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

The union of AW[t] over all t.
== Relations ==

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

Same as AW[SAT] but with 'circuit' instead of 'formula.'

Has the same relation to AW[SAT] as W[P] has to W[SAT].

Defined in [DF99].
== Relations ==

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

Basically has the same relation to W[SAT] as PSPACE does to NP.

The class of decision problems of the form (x,r,k,,1,,,...,k,,r,,) (r,k,,1,,,...,k,,r,, parameters), that are fixed-parameter reducible to the following problem, for some constant h:

Parameterized QBFSAT: Given a Boolean formula F (with no restriction on depth), over disjoint variable sets S,,1,,,...,S,,r,,.  Does there exist an assignment to S,,1,, of Hamming weight k,,1,,, such that for all assignments to S,,2,, of Hamming weight k,,2,,, etc. (alternating 'there exists' and 'for all'), F is satisfied?

See W[1] for the definition of fixed-parameter reducibility.

Defined in [DF99].

Contains AW[*], and is contained in AW[P].
== Relations ==

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

Has the same relation to W[t] as PSPACE does to NP.

Same as AW[SAT], except that the formula F can have depth at most t.

Defined in [DF99].

Contained in AW[*].
== Relations ==

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

Named in [Imp02], though it has been considered since the 1970's.

If P = BPP (or even BPP is contained in NE), then either NEXP is not in P/poly, or else the permanent polynomial of a matrix is not in AlgP/poly [KI02].
== Relations ==

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

Equals AM [NW94].
== Relations ==

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

Equals BPP [BG81].
== Relations ==

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

Almost-PSPACE is not known to equal PSPACE -- rather surprisingly, given the fact that PSPACE equals BPPSPACE and even PPSPACE.

What's known is that Almost-PSPACE = BP^exp^•PSPACE, where BP^exp^• is like the BP• operator but with exponentially-long strings [BVW98].  It follows that Almost-PSPACE is contained in NEXP^NP^ ∩ coNEXP^NP^.

Whereas both BP^exp^•PSPACE and BPPSPACE machines are allowed exponentially many random bits, the former has a reusable record of all of these bits on a witness tape, while the latter can only preserve a fraction of them on the work tape.
== Relations ==

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

The class of decision problems such that for some #P function f(x,0^m^),

The answer on input x is 'yes' if and only if the middle bit of f(x) is 1.
The m bits of f(x) to the left and right of the middle bit are all 0.

Defined in [GKR+95].

Contains PH and Contained in MP.
== Relations ==

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

Similar to TreeBQP except that the quantum computer's state at each time step is restricted to being exponentially close to a state in AmpP (that is, a state for which the amplitudes are computable by a classical polynomial-size circuit).

Defined in [Aar03b], where it was also observed that AmpP-BQP is contained in the third level of PH, just as TreeBQP is.
== Relations ==

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

Equivalent to NAuxPDA^p^ without the running-time restriction.

Equals P [Coo71b].
== Relations ==

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

Has the same relation to E as AvgP does to P.
== Relations ==

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

Then (A,μ) is in AvgP if there is an algorithm for A whose running time is polynomial on μ-average.

This convoluted definition is due to Levin [Lev86], who realized that simpler definitions lead to classes that fail to satisfy basic closure properties.  Also see [Gol97] for more information.

If AvgP = DistNP then EXP = NEXP [BCG+92].

Strictly contained in HeurP [NS05].

See also: (NP,P-samplable).
== Relations ==

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

Usually called AP in the literature.  I've renamed it AxP to distinguish it from the "other" AP.

The class of real-valued functions from {0,1}^n^ to [0,1] that can be approximated within any ε>0 by a deterministic Turing machine in time polynomial in n and 1/ε.

Defined by [KRC00], who also showed that the set of AxP machines is in RE.
== Relations ==

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

Usually called APP.  I've renamed it AxPP to distinguish it from the "other" APP.

The class of real-valued functions from {0,1}^n^ to [0,1] that can be approximated within any ε>0 by a probabilistic Turing machine in time polynomial in n and 1/ε.

Defined by [KRC00], who also show the following:

Approximating the acceptance probability of a Boolean circuit is AxPP-complete.  The authors argue that this makes AxPP a more natural class than BPP, since the latter is not believed to have complete problems.
If AxPP = AxP, then BPP = P.
On the other hand, there exists an oracle relative to which BPP = P but AxPP does not equal AxP.

AxPP is recursively enumerable [Jeř07].

Interestingly, it is unclear whether the set of AxPP machines is in RE.
== Relations ==

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

The smallest class that contains NP and is closed under union, intersection, and complement.

The levels are defined as follows:

BH,,1,, = NP.
BH,,2i,, is the class of languages that are the intersection of a BH,,2i-1,, language with a coNP language.
BH,,2i+1,, is the class of languages that are the union of a BH,,2i,, language with an NP language.

Then BH is the union over all i of BH,,i,,.

Defined in [WW85].

For more detail see [CGH+88].

Contained in Δ,,2,,P and indeed in P^NP[log]^.

If BH collapses at any level, then PH collapses to Σ,,3,,P [Kad88].

See also: DP, QH.

See also: QH.
== Relations ==

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

Has the same relation to E as BPP does to P.

EE = BPE if and only if EXP = BPP [IKW01].
== Relations ==

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

Has the same relation to EE as BPP does to P.
== Relations ==

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

Contains R,,H,,SPACE(f(n)).

Is contained in DSPACE(f(n)^3/2^) [SZ95].
== Relations ==

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

Has the same relation to L as BPP does to P.  The Turing machine has to halt with probability 1 on every input.

Contained in SC [Nis92] and in PL.
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is 'yes' then at least 2/3 of the computation paths accept.
If the answer is 'no' then at most 1/3 of the computation paths accept.

(Here all computation paths have the same length.)

Often identified as the class of feasible problems for a computer with access to a genuine random-number source.

Defined in [Gil77].

Contained in Σ,,2,,P ∩ Π,,2,,P [Lau83], and indeed in ZPP^NP^ [GZ97].

If BPP contains NP, then RP = NP [Ko82,Gil77] and PH is contained in BPP [Zac88].

If any problem in E requires circuits of size 2^Ω(n)^, then BPP = P [IW97] (in other words, BPP can be derandomized).

Indeed, any proof that BPP = P requires showing either that NEXP is not in P/poly, or else that #P requires superpolynomial-size arithmetic circuits [KI02].

BPP is not known to contain complete problems.  [Sip82], [HH86] give oracles relative to which BPP has no complete problems.

There exist oracles relative to which P = RP but still P is not equal to BPP [BF99].

In contrast to the case of P, it is unknown whether BPP collapses to BPTIME(n^c^) for some fixed constant c.  However, [Bar02] and [FS04] have shown hierarchy theorems for BPP with a small amount of advice.

A zero-one law exists stating that BPP has p-measure zero unless BPP = EXP [Mel00].

Equals Almost-P.

See also: BPP,,path,,.

If BPP contains NP, then RP = NP [Ko82] and PH is contained in BPP [Zac88].
== Relations ==

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

Same as P-OBDD, except that probabilistic transitions are allowed and the OBDD need only accept with probability at least 2/3.

Does not contain the integer multiplication problem [AK96].

Strictly contained in BQP-OBDD [NHK00].
== Relations ==

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

The class of problems solvable by a BPP machine that is given O(log n) advice bits, which can depend on both the machine's random coin flips and the input length n, but not on the input itself.

Defined in [TV02], where it was also shown that if EXP is in BPP//log then
EXP = BPP, and if PSPACE is in BPP//log then PSPACE = BPP.
== Relations ==

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

The class of problems solvable by a semantic BPP machine with O(log n) advice bits that depend only on the input length n.  If the advice is good, the output must be correct with probability at least 2/3.  If it is bad, the machine must provide some answer with probability at least 2/3.  See the discussion for BQP/poly.

Contained in BPP/mlog.
== Relations ==

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

The class of problems solvable by a syntactic BPP machine with O(log n) advice bits that depend only on the input length n.  If the advice is good, the output must be correct with probability at least 2/3.  If it is bad, it need not be.

Contained in BPP/rlog.
== Relations ==

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

The class of problems solvable by a syntactic BPP machine with O(log n) random advice bits whose probability distribution depends only on the input length n.  For each n, there exists good advice such that the output is correct with probability at least 2/3.

Contains BPP/mlog.  The inclusion is strict, because BPP/rlog contains any finitely sparse language by fingerprinting; see the discussion for ALL.

Contained in BPP//log.
== Relations ==

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

BPP with an oracle that, given a string x, returns the minimum over all programs P that output x,,i,, on input i, of the length of P plus the maximum time taken by P on any input.

A similar class was defined in [ABK+02], where it was also shown that in BPP^KT^ one can factor, compute discrete logarithms, and more generally invert any one-way function on a non-negligible fraction of inputs.

See also: P^K^.
== Relations ==

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

The analogue of P^cc^ for bounded-error probabilistic communication complexity.

Does not equal P^cc^, and is not contained in NP^cc^, because of the EQUALITY problem.

Defined in [BFS86].

Has the same relation to BPP^cc^ and BPP as P,,,,^cc^ does to P^cc^ and P.

NP,,,,^cc^ is not contained in BPP,,,,^cc^ for  players, for any constant  [DP08].
== Relations ==

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

Same as BPP, except that now the computation paths need not all have the same length.

Defined in [HHT97], where the following was also shown:

BPP,,path,, contains MA and P^NP[log]^, and is contained in PP and BPP^NP^.
BPP,,path,, is closed under complementation, intersection, and union.
If BPP,,path,, = BPP,,path,,^BPP,,path,,^, then PH collapses to BPP,,path,,.
If BPP,,path,, contains Σ,,2,,P, then PH collapses to BPP^NP^.

There exists an oracle relative to which BPP,,path,, is not contained in Σ,,2,,P [BGM02].

An alternate characterization of BPP,,path,, uses the idea of post-selection. That is, BPP,,path,, is the class of languages  for which there exists a pair of polynomial-time Turing machines  and  such that the following conditions hold for all :

If , .
 If , .
 .

We say that  is the post-selector. Intuitively, this characterization allows a BPP machine to require that its random bits have some special but easily verifiable property. This characterization makes the inclusion NP ⊆ BPP,,path,, nearly trivial.

See Also: PostBQP (quantum analogue).

BPP,,path,, contains MA and P^NP[log]^, and is contained in PP and BPP^NP^.
BPP,,path,, is closed under complementation, intersection, and union.
If BPP,,path,, = BPP,,path,,^BPPpath^, then PH collapses to BPP,,path,,.
If BPP,,path,, contains Σ,,2,,P, then PH collapses to BPP^NP^.
== Relations ==

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

Defined in [CNS99], where the following was also shown:

If either (1) #P does not have a subexponential-time bounded-error algorithm, or (2) EXP does not have subexponential-size circuits, then the BPQP hierarchy is strict -- that is, for all a < b at least 1, BPTIME(2^(log n)^a^) is strictly contained in BPTIME(2^(log n)^b^).
== Relations ==

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

Contains RSPACE(f(n)) and BP,,H,,SPACE(f(n)).
== Relations ==

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

Same as BPP, but with f(n)-time (for some constructible function f) rather than polynomial-time machines.

Defined in [Gil77].

BPTIME(n^log n^) does not equal BPTIME(2^n^ε^) for any ε>0 [KV88].  Proving a stronger time hierarchy theorem for BPTIME is a longstanding open problem; see [BH97] for details.

[Bar02] has shown the following:

If we allow a small number of advice bits (say log n), then there is a strict hierarchy: for every d at least 1, BPTIME(n^d^)/(log n) does not equal BPTIME(n^d+1^)/(log n).
In the uniform setting, if BPP has complete problems then BPTIME(n^d^) does not equal BPTIME(n^d+1^).
BPTIME(n) does not equal NP.

Subsequently, [FS04] managed to reduce the number of advice bits to only 1: BPTIME(n^d^)/1 does not equal BPTIME(n^d+1^)/1.  They also proved a hierarchy theorem for HeurBPTIME.

For another bounded-error hierarchy result, see BPQP.
== Relations ==

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

Defined in [Weg88].

The class of decision problems solvable by a family of polynomial size branching programs, with the additional condition that each bit of the input is tested at most d times.

BP,,d,,(P) strictly contains BP,,d-1,,(P), for every d > 1 [Tha98].

Contained in PBP.

See also: P-OBDD, k-PBP.
== Relations ==

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

Equals AM.
== Relations ==

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

One can equivalently define BQP as the class of decision problems solvable by a uniform family of polynomial-size quantum circuits, with at most 1/3 probability of error [Yao93].  Any universal gate set can be used as a basis; however, a technicality is that the transition amplitudes must be efficiently computable, since otherwise one could use them to encode the solutions to hard problems (see [ADH97]).

BQP is often identified as the class of feasible problems for quantum computers.

Contains the factoring and discrete logarithm problems [Sho97], the hidden Legendre symbol problem [DHI02], the Pell's equation and principal ideal problems [Hal02], and some other problems not thought to be in BPP.

Defined in [BV97], where it is also shown that BQP contains BPP and is contained in P with a #P oracle.

BQP^BQP^ = BQP [BV97].

[ADH97] showed that BQP is contained in PP, and [FR98] showed that BQP is contained in AWPP.

There exist oracles relative to which:

BQP does not equal to BPP [BV97] (and by similar arguments, is not in P/poly).
BQP is not contained in MA [Wat00].
BQP is not contained in Mod,,p,,P for prime p [GV02].
NP, and indeed NP ∩ coNP, are not contained in BQP  with probability 1 relative to a random oracle and a random permutation oracle, respectively [BBB+97].
SZK is not contained in BQP [Aar02].
BQP is not contained in SZK (follows easily using the quantum walk problem in [CCD+03]).
PPAD is not contained in BQP [Li11].

BQP does not equal BPP [BV97] (and by similar arguments, is not in P/poly).
BQP is not contained in MA [Wat00].
BQP is not contained in Mod,,p,,P for prime p [GV02].
NP, and indeed NP ∩ coNP, are not contained in BQP (in fact, this holds with probability 1 relative to a random oracle and a random permutation oracle, respectively) [BBB+97].
SZK is not contained in BQP [Aar02].
BQP is not contained in SZK (follows easily using the quantum walk problem in [CCD+03]).
== Relations ==

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

Same as P-OBDD, except that unitary (quantum) transitions are allowed and the OBDD need only accept with probability at least 2/3.

Strictly contains BPP-OBDD [NHK00].
== Relations ==

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

Same as BQP/poly except that the advice is O(log n) bits instead of a polynomial number.

Contained in BQP/mlog.
== Relations ==

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

Same as BQP/mpoly except that the advice is O(log n) bits instead of a polynomial number.

Strictly contained in BQP/qlog [NY03].
== Relations ==

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

The class of languages recognized by a syntactic BQP machine with deterministic polynomial advice that depends only on the input length, such that the output is correct with probability 2/3 when the advice is good.

Can also be defined as the class of problems solvable by a nonuniform family of polynomial-size quantum circuits, just as P/poly is the class solvable by a nonuniform family of polynomial-size classical circuits.

Referred to with a variety of other ad hoc names, including BQP/poly on occassion.

Contains BQP/qlog, and is contained in BQP/qpoly.

Does not contain ESPACE [NY03].
== Relations ==

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

Is to BQP/mpoly as ∃BPP is to MA.  Namely, the BQP machine is required to give some answer with probability at least 2/3 even if the advice is bad.  Even though BQP/mpoly is a more natural class, BQP/poly follows the standard definition of advice as a class operator [KL82].

Contained in BQP/mpoly and contains BQP/log.
== Relations ==

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

Same as BQP/mlog except that the advice is quantum instead of classical.

Strictly contains BQP/mlog [NY03].

Contained in BQP/mpoly.
== Relations ==

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

The class of problems solvable by a BQP machine that receives a quantum state ψ,,n,, as advice, which depends only on the input length n.

As with BQP/mpoly, the acceptance probability does not need to be bounded away from 1/2 if the machine is given bad advice. (Thus, we are discussing the class that [NY03] call BQP/*Qpoly.) Indeed, such a condition would make quantum advice unusable, by a continuity argument.

Does not contain EESPACE [NY03].

[Aar04b] shows the following:

There exists an oracle relative to which BQP/qpoly does not contain NP.
BQP/qpoly is contained in PP/poly.

A classical oracle separation between BQP/qpoly and BQP/mpoly is presently unknown, but there is a quantum oracle separation [AK06].  An unrelativized separation is too much to hope for, since it would imply that PP is not contained in P/poly.

Contains BQP/mpoly.
== Relations ==

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

Same as BQP with access to two sets of qubits: causality-respecting qubits and CTC qubits.

Defined in [Aar05c], where it was shown that PSPACE is contained in BQP,,CTC,,, which in turn is contained in SQG.

See also P,,CTC,,.
== Relations ==

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

Equals PSPACE and PPSPACE.
== Relations ==

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

Same as BQP/mpoly, except that the machine only gets to make nonadaptive queries to whatever oracle it might have.

Defined in [NY03b], where it was also shown that P is not contained in BQP,,tt,,/poly relative to an oracle.
== Relations ==

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

Same as BQP, but with f(n)-time (for some constructible function f) rather than polynomial-time machines.

Defined in [BV97].
== Relations ==

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

The class of problems for which there exists a DiffAC^0^ function f such that the answer is "yes" on input x if and only if f(x)=0.

Equals TC^0^ and PAC^0^ under logspace uniformity [ABL98].
== Relations ==

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

Has the same relation to L as C,,=,,P does to P.

C,,=,,L^C=L^ = L^C=L^ [ABO99].
== Relations ==

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

The class of decision problems solvable by an NP machine such that the number of accepting paths exactly equals the number of rejecting paths, if and only if the answer is 'yes.'

Equals coNQP [FGH+98].
== Relations ==

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

CC is defined as the class of problems log-space many-one reducible to CCVP [MS89]. At present it is only known that NLCCP [MS89]. CC is an example of a complexity class neither known to be in NC nor P-complete.

Natural complete problems for the CC class include Stable Marriage Problem, Stable Roommate Problem, Lex-first Maximal Matching [Sub94].
== Relations ==

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

Does not equal QCFL [MC00].

Contained in LOGCFL.

Strictly contains DCFL [Bra77] and indeed UCFL.

Strictly contains DCFL [Bra77].
== Relations ==

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

Contained in PSPACE.

Strictly contains DLOGTIME-uniform NC^1^ [CMTV98].

It is an open problem whether there exists an oracle relative to which CH is infinite, or even unequal to PSPACE.  This is closely related to the problem of whether TC^0^ = NC^1^, since a padding argument shows that TC^0^ = NC^1^ implies CH = PSPACE.

It is an open problem whether there exists an oracle relative to which CH is infinite, or even unequal to PSPACE.  This is closely related to the problem of whether TC^0^ = NC^1^.
== Relations ==

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

The class of #P function problems such that some underlying NP machine  witnessing membership in #P has
"clustered" accepting paths. That is:

There exists a polynomial  such that each computation path of  on each input  is exactly  bits long.
There is a length-respecting total order  having polynomial-time computable adjacency checks on the computation paths of .
The accepting paths of  on any input  are contiguous with respect to .

Defined in [HHK+05].
== Relations ==

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

Roughly, the class of continuous problems solvable by an ordinary differential equation (ODE) with convergence time logarithmic in the size of the input.  The vector field of the ODE is specified by an NC^1^ formula, with n parameters that represent the input.  The point to which the ODE converges (assuming it does) is the output.

Defined in [BSF02], which should be consulted for more details.

[BSF02] show that finding the maximum of n integers is in CLOG.  Thus, CLOG is best thought of as the continuous-time analog of NC^1^, not of DTIME(log n).

Contained in CP.
== Relations ==

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

A nondeterministic analog of CP.  Defined in [SF98], which should be consulted for the definition (it has something to do with strange attractors, I think).

The authors raise the question of whether CP equals CNP.
== Relations ==

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

Same as CLOG, except that the convergence time can be polynomial rather than logarithmic in the input size.

Defined in [BSF02] and [SF98].

Finding a maximum flow, which is P-complete, can be done in CP [BSF02].  Based on this the authors argue that "P is contained in CP," but this seems hard to formalize, since CP is not a complexity class in the usual sense.  They also conjecture that "CP is contained in P" (i.e. the class of ODE's they consider can be integrated efficiently on a standard Turing machine), but this is open.

Contained in CNP.
== Relations ==

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

So for example, CSIZE(poly(n)) (the union of CSIZE(n^k^) over all k) equals P/poly.

Defined in [SM02] among other places.
== Relations ==

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

Equals NSPACE(n) [Kur64].
== Relations ==

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

Defined in [FV93] as the class of languages corresponding to fixed templates (where a template is a set of allowed constraints on values and variables) in the general Constraint Satisfaction Problem. Under this construction, 3SAT may be expressed as the fixed template (over the alphabet ) containing :

For example, a 3SAT clause  is represented in the CSP construction as . By similar constructions, any k-SAT problem can be seen to be in CSP. The class also includes Graph k-Coloring (for ), Graph H-Coloring (for some graph ) and Linear Programming mod .

In [FV93], where the class is defined, the authors show that every problem in MMSNP is reducible under randomized polynomial-time reductions to a problem in CSP.
== Relations ==

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

Same as SZK, except that now the two distributions are merely required to be computationally indistinguishable by any BPP algorithm; they don't have to be statistically close.  (The "two distributions" are (1) the distribution over the verifier's view of their interaction with the prover, conditioned on the verifier's random coins, and (2) the distribution over views that the verifier can simulate without the prover's help.)

Unlike SZK, it is not known if CZK is closed under complement.  CZK is now known to share other properties with SZK: the verifier may as well be honest and may as well show their coins, and CZK is closed under unions [Vad06].  (Previously, these properties were only established in the presence of one-way functions [GMW91].)

Assuming the existence of one-way functions, CZK contains NP [GMW91], and actually equals IP=PSPACE [BGG+90].  However, none of these implications of one-way functions relativize (Impagliazzo, unpublished).

On the other hand, if one-way functions do not exist then CZK = AVBPP [OW93].

Contains PZK and SZK.

Same as SZK, except that now the two distributions are merely required to be computationally indistinguishable by any BPP algorithm; they don't have to be statistically close.  (The "two distributions" are (1) the distribution over Arthur's view of his interaction with Merlin, conditioned on Arthur's random coins, and (2) the distribution over views that Arthur can simulate without Merlin's help.)

Unlike SZK, it is not known if CZK is closed under complement.  CZK is now known to share other properties with SZK: the verifier may as well be honest and may as well show his coins, and CZK is closed under unions [Vad06].  (Previously, these properties were only established in the presence of one-way functions.)

Assuming the existence of one-way functions, CZK contains NP [GMW91], and indeed equals IP=PSPACE [BGG+90].  However, none of these implications of one-way functions relativize (Impagliazzo, unpublished).
== Relations ==

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

The class of problems such that a polynomial-time program P that allegedly solves them can be checked efficiently.  That is, f is in Check if there exists a BPP algorithm C such that for all programs P and inputs x,

If P(y)=f(y) for all inputs y, then C^P^(x) (C with oracle access to P) accepts with probability at least 2/3.
If P(x) is not equal to f(x) then C^P^(x) accepts with probability at most 1/3.

Introduced in [BK89], where it was also shown that Check equals frIP ∩ cofrIP.

Check is contained in NEXP ∩ coNEXP [FRS88].

[BG94] show that if NEE is not contained in BPEE then NP is not contained in Check.
== Relations ==

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

C,,0,,P = P
C,,1,,P = PP
C,,2,,P = PP^PP^
In general, C,,k+1,,P is PP with C,,k,,P oracle

The union of the C,,k,,P's is called the counting hierarchy, CH.

Defined in [Wag86].

See [Tor91] or [AW90] for more information.
== Relations ==

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

The class of problems L that are efficiently autoreducible, in the sense that given an input x and access to an oracle for L, a BPP machine can compute L(x) by querying L only on points that differ from x.

Defined in [Yao90b].

[BG94] show that, assuming NEE is not contained in BPEE, Coh ∩ NP is not contained in any of compNP, Check, or frIP.
== Relations ==

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

Defined in [GG66], where it was also shown that DCFL is strictly contained in CFL, contained in UCFL, and strictly contains REG.  The inclusion in UCFL is also strict.

Defined in [GG66], where it was also shown that DCFL is strictly contained in CFL and strictly contains REG.
== Relations ==

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

The class of decision problems reducible in L to the problem of computing the determinant of an n-by-n matrix of n-bit integers.

Defined in [Coo85].

Contained in NC^2^, and contains NL and PL [BCP83].

Graph isomorphism is hard for DET under L-reductions [Tor00].
== Relations ==

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

DP = BH,,2,,, the second level of the Boolean hierarchy.

Defined in [PY84].
== Relations ==

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

The class of decision problems solvable by a BQP machine with oracle access to a dynamical simulator. When given a polynomial-size quantum circuit, the simulator returns a sample from the distribution over "classical histories" induced by the circuit. The simulator can adversarially choose any history distribution that satisfies the axioms of "symmetry" and "locality" -- so that the DQP algorithm has to work for any distribution satisfying these axioms.

See [Aar05] for a full definition.

There it is also shown that SZK is contained in DQP.

Contains BQP, and is contained in EXP [Aar05].

There exists an oracle relative to which DQP does not contain NP [Aar05].
== Relations ==

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
n, DSPACE(f(n)) is strictly contained in DSPACE(f(n) log(f(n))) [HLS65].

For space constructible f(n), strictly contains DTIME(f(n)) [HPV77].

DSPACE(n) does not equal NP (though we have no idea if one contains the other)!

See also: NSPACE(f(n)).
== Relations ==

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

Of great relevance to DTIME is the Time Hierarchy Theorem: For any constructible function  greater than , DTIME() is strictly contained in DTIME() [HS65]. As a corollary, P ⊂ EXP.

For any space constructible , DTIME() is strictly contained in DSPACE() [HPV77].

Also, DTIME() is strictly contained in NTIME() [PPS+83] (this result does not work for arbitrary ).

For any constructible superpolynomial , DTIME() with PP oracle is not in P/poly (see [All96]).

The class of decision problems solvable by a Turing machine in time O(f(n)).

The Time Hierarchy Theorem: For constructible f(n) greater than n, DTIME(f(n)) is strictly contained in DTIME(f(n) log(f(n)) loglog(f(n))) [HS65].

For any space constructible f(n), DTIME(f(n)) is strictly contained in DSPACE(f(n)) [HPV77].

Also, DTIME(n) is strictly contained in NTIME(n) [PPS+83] (this result does not work for arbitrary f(n)).

For any constructible superpolynomial f(n), DTIME(f(n)) with PP oracle is not in P/poly (see [All96]).
== Relations ==

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

Thus SC = DTISP(poly,polylog) for example.

Defined in [Nis92], where it was also shown that for all space-constructible s(n)=Ω(log n), BPSPACE(s(n)) is contained in DTISP(2^O(s(n))^,s^2^(n)).
== Relations ==

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

The class of functions from {0,1}^n^ to integers expressible as the difference of two #AC^0^ functions.

Equals GapAC^0^ under logspace uniformity [ABL98].
== Relations ==

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

The class of pairs (A,B), where A and B are NP problems whose sets of "yes" instances are nonempty and disjoint.

If there exists an optimal propositional proof system, then DisNP has a complete pair [Raz94].  On the other hand, there exists an oracle relative to which DisNP does not have a complete pair [GSS+03].

If P does not equal UP, then DisNP contains pairs not separated by any set in P [GS88].  On the other hand, there exists an oracle relative to which P does not equal NP but still DisNP does not contain any P-inseparable pairs [HS92].
== Relations ==

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

(A,μ) is in DistNP if A is in NP, and μ is P-computable (meaning that its cumulative density function can be evaluated in polynomial time).

DistNP has complete problems [Lev86] (see also [Gur87]), although unlike for NP this is not immediate.

Any DistNP-complete problem is also complete for (NP,P-samplable) [IL90].

DistNP has complete problems [Gur87], although unlike for NP this is not immediate.
== Relations ==

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

Basically what this means is that an algorithm maintains some polynomial-size data structure (say a graph), and receives a sequence of updates (add this edge, delete that one, etc.).  For each update, it computes a new value for the data structure in FO -- that is, for each bit of the data structure, there is an FO function representing the new value of that bit, which takes as input both the update and the previous value of the data structure.  At the end the algorithm needs to answer some question (i.e. is the graph connected?).

See [HI02] for more information, and a complete problem for Dyn-FO.

See also Dyn-ThC^0^.
== Relations ==

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

Same as Dyn-FO, except that now updates are computed via constant-depth predicates that have "COUNT" available, in addition to AND, OR, and NOT -- so it's a uniform version of TC^0^ rather than of AC^0^.

See [HI02] for more information.
== Relations ==

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

Does not equal NP [Boo72] or PSPACE [Boo74] relative to any oracle.  However, there is an oracle relative to which E is contained in NP (see ZPP), and an oracle relative to PSPACE is contained in E (by equating the former with P).

There exists a problem that is complete for E under polynomial-time Turing reductions but not polynomial-time truth-table reductions [Wat87].

Problems hard for BPP under Turing reductions have measure 1 in E [AS94].

It follows that, if the problems complete for E under Turing reductions do not have measure 1 in E, then BPP does not equal EXP.

[IT89] gave an oracle relative to which E = NE but still there is an exponential-time binary predicate whose corresponding search problem is not in E.

[BF03] gave a proof that if E = NE, then no sparse set is collapsing, where they defined a set  to be collapsing if  and if for all  such that  and  are Turing reducible to each other,  and  are many-to-one reducible to each other.

Contrast with EXP.
== Relations ==

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

EE = BPE if and only if EXP = BPP [IKW01].

Contained in EEXP and NEE.

Equals DTIME(2^2^O(n)^) (though some authors alternatively define it as being equal to DTIME(2^O(2^n)^)).
== Relations ==

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

In contrast to the case of EE, it is not known whether EEE = BPEE implies EE = BPE [IKW01].

Equals DTIME(2^2^2^O(n)^).
== Relations ==

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

Is not contained in BQP/qpoly [NY03].

Equals DSPACE(2^2^O(n)^).
== Relations ==

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

Contains EE, and is contained in NEEXP.

Equals DTIME(2^2^p(n)^) for p a polynomial.
== Relations ==

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

Has roughly the same relationship to E as PH does to P.

More formally, EH is defined as the union of E, NE, NE^NP^, NE with Σ,,2,,P oracle, and so on.

See [Har87] for more information.

If coNP is contained in AM[polylog], then EH collapses to S,,2,,-EXP•P^NP^ [SS04] and indeed AM,,EXP,, [PV04].

On the other hand, coNE is contained in NE/poly, so perhaps it wouldn't be so surprising if NE collapses.

There exists an oracle relative to which EH does not contain SEH [Hem89]. EH and SEH are incomparable for all anyone knows.
== Relations ==

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

Contained in PR.

Equals the union of DTIME(2^n^), DTIME(2^2^n^), DTIME(2^2^2^n^), and so on.
== Relations ==

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

An extension of L,,k,,P.

The class of problems A such that Σ,,k,,P^A^ is contained in Σ,,k-1,,P^A,NP^.

Defined in [BBS86].
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is 'no,' then all computation paths reject.
If the answer is 'yes,' then the number of accepting paths is a power of two.

Contained in C,,=,,P, and in Mod,,k,,P for any odd k.  Contains UP.

Defined in [BHR00].
== Relations ==

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

Contains FPTAS and is contained in PTAS.

Defined in [CT97], where the following was also shown:

If FPT = XP,,uniform,, then EPTAS = PTAS.
If EPTAS = PTAS then FPT = W[P].
If FPT is strictly contained in W[1], then there is a natural problem that is in PTAS but not in EPTAS.  (See [CT97] for the statement of the problem, since it's not that natural.)
== Relations ==

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

The same as BQP, except that the quantum algorithm must return the correct answer with probability 1, and run in polynomial time with probability 1.  Unlike bounded-error quantum computing, there is no theory of universal QTMs for exact quantum computing models.  In the original definition in [BV97], each language in EQP is computed by a single QTM, equivalently to a uniform family of quantum circuits with a finite gate set K whose amplitudes can be computed in polynomial time. See EQP,,K,,.  However, some results require an infinite gate set.  The official definition here is that the gate set should be finite.

Without loss of generality, the amplitudes in the gate set K are algebraic numbers [ADH97].

There is an oracle that separates EQP from NP [BV97], indeed from Δ,,2,,P [GP01].  There is also an oracle relative to which EQP is not in Mod,,p,,P where p is prime [GV02].  On the other hand, EQP is in LWPP [FR98].

P^||NP[2k]^ is contained in EQP^||NP[k]^, where "||NP[k]" denotes k nonadaptive oracle queries to NP (queries that cannot depend on the results of previous queries) [BD99].

See also ZBQP.
== Relations ==

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

The set of problems that can be answered by a uniform family of polynomial-sized quantum circuits whose gates are drawn from a set K, and that return the correct answer with probability 1, and run in polynomial time with probability 1, and the allowed gates are drawn from a set K.  K may be either finite or countable and enumerated.  If S is a ring, the union of EQP,,K,, over all finite gate sets K whose amplitudes are in the ring R can be written EQP,,S,,.

Defined in [ADH97] in the special case of a finite set of 1-qubit gates controlled by a second qubit.  It was shown there that transcendental gates may be replaced by algebraic gates without decreasing the size of EQP,,K,,.

[FR98] show that EQP,,Q,, is in LWPP.  The proof can be generalized to any finite, algebraic gate set K.

The hidden shift problem for a vector space over Z/2 is in EQP,,Q,, by Simon's algorithm.  The discrete logarithm problem over Z/p is in EQP,,Q-bar,, using infinitely many gates [MZ03].
== Relations ==

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

Same as EQP, but with f(n)-time (for some constructible function f) rather than polynomial-time machines.

Defined in [BV97].
== Relations ==

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

If E = ESPACE then P = BPP [HY84].

Indeed if E has nonzero measure in ESPACE then P = BPP [Lut91].

ESPACE is not contained in P/poly [Kan82].

Is not contained in BQP/mpoly [NY03].

See also: EXPSPACE.
== Relations ==

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

Also equals P with E oracle.

If L = P then PSPACE = EXP.

If EXP is in P/poly then EXP = MA [BFL91].

Problems complete for EXP under many-one reductions have measure 0 in EXP [May94], [JL95].

There exist oracles relative to which

EXP = NP = ZPP [Hel84a], [Hel84b], [Kur85], [Hel86],
EXP = NEXP but still P does not equal NP [Dek76],
EXP does not equal PSPACE [Dek76].

[BT04] show the following rather striking result: let A be many-one complete for EXP, and let S be any set in P of subexponential density.  Then A-S is Turing-complete for EXP.

[SM03] show that if EXP has circuits of polynomial size, then P can be simulated in MA,,POLYLOG,, such that no deterministic polynomial-time adversary can generate a list of inputs for a P problem that includes one which fails to be simulated. As a result, EXP ⊆ MA if EXP has circuits of polynomial size.

[SU05] show that EXP  NP/poly implies EXP  P^||NP^/poly.

In descriptive complexity EXPTIME can be defined as SO() which is also SO(LFP)

EXP = NP = ZPP [Hel84],
EXP = NEXP but still P does not equal NP [Dek76],
EXP does not equal PSPACE [Dek76].
== Relations ==

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

The class of decision problems solvable in EXP with the help of a polynomial-length advice string that depends only on the input length.

Contains BQP/qpoly [Aar04b].
== Relations ==

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

See also: ESPACE.

Given a first-order statement about real numbers, involving only addition and comparison (no multiplication), we can decide in EXPSPACE whether it's true or not [Ber80].
== Relations ==

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

Defined in [Har78].

See also F-TIME(f(n)).  The results about F-TAPE mirror those about F-TIME, but in some cases are sharper.
== Relations ==

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

Defined in [Har78], where the following was also shown:

If F-TIME(f(n)) = DTIME(f(n)), then DTIME(f(n)) is strictly contained in DTIME(f(n)g(n)) for any nondecreasing, unbounded, recursive g(n).
There exist recursive, monotonically increasing f(n) such that F-TIME(f(n)) is strictly contained in DTIME(f(n)).

See also F-TAPE(f(n)).
== Relations ==

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

Has the same relation to BQP as FNP does to NP.

There exists an oracle relative to which PLS is not contained in FBQP [Aar03].
== Relations ==

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

FH,,0,, = P
FH,,1,, = BPP
FH,,2,, contains factoring because of Kitaev's phase estimation algorithm

It is an open problem to show that the Fourier hierarchy is infinite relative to an oracle (that is, FH,,k,, is strictly contained in FH,,k+1,,).

Defined in [Shi03].

FH,,0,, = P
FH,,1,, = BPP
FH,,2,, contains factoring, because of Kitaev's phase estimation algorithm
== Relations ==

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

Properties of FIXP problems:

the function F,,I,, is represented by an algebraic circuit over {+, -, *, /, max, min} with rational constants
 there is a polynomial time algorithm that computes the circuit from I.

Every FIXP problem has Partial Computation, Decision, (Strong) Approximation, and Existence counterparts; these can all be solved in PSPACE.

The Nash equilibrium problem for 3 or more players is FIXP-complete.

Linear-FIXP = PPAD.

Defined in [EY07].
== Relations ==

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

Has the same relation to NL as FNP does to NP.

Defined by [AJ93], who also showed that if NL = UL, then FNL is contained in #L.
== Relations ==

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

Has the same relation to FNL as P/poly does to P.

Contained in #L/poly [RA00].
== Relations ==

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

FNP generalizes NP, which is defined in terms of decision problems only.

Actually the word "function" is misleading, since there could be many valid outputs y.  That's unavoidable, since given a predicate F there's no "syntactic" criterion ensuring that y is unique.

FP = FNP if and only if P = NP.

Contains TFNP.

A basic question about FNP problems is whether they're self-reducible; that is, whether they reduce to the corresponding NP decision problems.  Although this is true for all NPC problems, [BG94] shows that if EE does not equal NEE, then there is a problem in NP such that no corresponding FNP problem can be reduced to it.  [BG94] cites Impagliazzo and Sudan as giving the same conclusion under the assumption that NE does not equal coNE.
== Relations ==

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

First order logic is the smallest logical class of logic language. It is the base of Descriptive complexity and equal to the class AC^0^ and to AH, the alternating logtime hierarchy.

When we use logic formalism, the input is a structure, usually it is either strings (of bits or over an alphabet) whose elements are position of the strings, or graphs whose elements are vertices. The mesure of the input will there be the size of the structure.
Whatever the structure is, we can suppose that there are relation that you can test, by example  is true iff there is an edge from  to  if the structure is a graph, and  is true iff the nth letter of the string is 1. We also have constant, who are special elements of the structure, by example if we want to check reachability in a graph, we will have to choose two constant s and t.

In descriptive complexity we almost always suppose that there is a total order over the elements and that we can check equality between elements. This let us consider elements as number,  is the number  iff there is  elements  such that . Thanks to this we also want the primitive "bit", where  is true if only the th bith of  is 1. (We can replace  by plus and time, ternary relation such that  is true iff  and  is true iff ).

Since in a computer elements are only pointers or string of bit, thoses assumptions make sens, and those primitive function can be calculated in most of the small complexity classes. We can also imagine FO without those primitives, which gives us smaller complexity classes.

The language FO is then defined as the closure by conjunction ( ), negation () and universal quantification () over element of the structures. We also often use existantial quantification () and disjunction () but those can be defined thanks to the 3 first symbols.

The semantics of the formulae in FO is straightforward,  is true iff  is false,  is true iff  is true and  is true, and () is true iff whatever element we decide that  is we can choose,  is true.

A querie in FO will then be to check if a FO formulae is true over a given structure, this structure is the input of the problem. One should not confuse this kind of problem with checking if a quantified boolean formula is true, which is the definition of QBF, which is Pspace-complete. The difference between those two problem is that in QBF the size of the problem is the size of the formula and elements are just boolean value, whereas in FO the size of the problem is the size of the structure and the formula is fixed.

Every formulae is equivalent to a formulae in prenexe normal form where we put recursively every quantifier and then a quantifier-free formulae.
== Relations ==

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

FO(DTC) is defined as FO(tc) where the transitive closure operator is deterministic, which means that when we apply DTC(), we know that for all , there exist at most one  such that phi(u,v).

We can suppose that DTC() is syntactic sugar for TC() where .

It was shown in [Imm99] page 144 that this class is equal to L.
== Relations ==

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

FO(LFP) is the set of boolean queries definable with first-order fixed-point formulae where the partial fixed point is limited to be monotone, which means that if the second order variable is , then  always implies .

We can obtain the monotony by restricting the formula  to have only positive occurrences of  (i.e. there is an even number of negations before every occurrence of ). We can also describe LFP() as syntactic sugar of PFP() where .

Thanks to monotonicity we only add and never remove vectors to the truth table of , and since there is only  possible vectors we always find a fixed point before  iterations. Hence it was shown in [Imm82] that FO(LFP)=P. This definition is equivalent to FO().
== Relations ==

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

Let  be an integer,   vectors of  variables,  a second-order variable of arity , and  a FO(PFP) function using  and  as variables, then we can define iteratively  such that  and  which means that the property  is true on the input  if  is true on input , and when the variable  is replaced by . Then, either there is a fixed point, or the list of  is looping.

PFP( is defined as the value of the fixed point of  on y if there is a fixed point, else as false.

Since s are property of arity , there is at most  values for the s, so with a poly-space counter we can check if there is a loop or not.

It was proved in [Imm98] that FO(pfp) is equal to PSPACE.
== Relations ==

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

FO(TC) is the set of boolean queries definable with first-order formulae with a transitive closure (TC) operator.

TC is defined this way: let  be a positiver integer and  be vectors of  variables, then TC( is true if there exist  variables  such that  and for all  . Here,  is a formula over  written in FO(TC) and  means that the variables  and  are replaced by  and .

Every formula of TC can be written in a normal form FO( where  is a FO formula and we suppose that there is an order on the model where variables are quantified, so we can choose the minimum and maximum element.

It was shown in [Imm98] page 150 that this class is equal to NL.
== Relations ==

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

The class of decision problems for which a "yes" answer can be expressed by a first-order logic predicate, with a block of restricted quantifiers repeated t(n) times.  See [Imm98] for a full definition.

FO(poly(n)) = P (see [Var82] for example).

FO(poly(n)) is contained in SO-E.
== Relations ==

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

Defined in [BKL+00], where it was also shown that many problems on finite groups are in FOLL.

Contains uniform AC^0^, and is contained in uniform AC^1^.

Is not known to be comparable to L or NL.

The class of decision problems solvable by a nonuniform family of polynomial-size, unbounded-fanin, depth O(loglog n) circuits with AND, OR, and NOT gates.

Contains AC^0^, and is contained in AC^1^.

Is not known to be comparable to L/poly or NL/poly.
== Relations ==

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

FO[] consists of the FO-formulae with quantifier blocks that are iterated  times.

In Descriptive complexity we can see that :

FO[] is equal to fo-uniform AC^i^, and in fact FO[] is fo-uniform AC of depth 
FO[] is equal to NC
FO[] is equal to P and FO(LFP)
FO[] is equal to PSPACE and FO(PFP)
== Relations ==

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

Sometimes defined as the class of functions computable in polynomial time by a Turing machine.  (Generalizes P, which is defined in terms of decision problems only.)

However, if we want to compare FP to FNP, we should instead define it as the class of FNP problems (that is, polynomial-time predicates P(x,y)) for which there exists a polynomial-time algorithm that, given x, outputs any y such that P(x,y).  That is, there could be more than one valid output, even though any given algorithm only returns one of them.

FP = FNP if and only if P = NP.

If FP^NP^ = FP^NP[log]^ (that is, allowed only a logarithmic number of queries), then P = NP [Kre88].  The corresponding result for P^NP^ versus P^NP[log]^ is not known, and indeed fails relative to some oracles (see [Har87b]).
== Relations ==

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

Given a graph, the problem of outputting the size of its maximum clique is complete for FP^NP[log]^.
== Relations ==

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

Has the same relation to FPT as RP does to P.

Defined in [AR01], where it was shown that, if the Resolution proof system is automatizable (that is, if a refutation can always be found in time polynomial in the length of the shortest refutation), then W[P] is contained in FPR.

Has the same relation to FPT as R does to P.
== Relations ==

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

The subclass of #P counting problems whose answer, y, is approximable in the following sense.  There exists a randomized algorithm that, with probability at least 1-δ, approximates y to within an ε multiplicative factor in time polynomial in n (the input size), 1/ε, and log(1/δ).

The permanent of a nonnegative matrix is in FPRAS [JSV01].
== Relations ==

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

The basic class of the theory of fixed-parameter tractability, as described by Downey and Fellows [DF99].

To separate FPT and W[2], one could show there is no proof system for CNF formulae that admits proofs of size f(k)n^O(1)^, where f is a computable function and n is the size of the formula.

Contained in FPT,,nu,,, W[1], and FPR.

Contains FPTAS [CC97], as well as FPT,,su,,.

Contains EPTAS unless FPT = W[1] [Baz95].
== Relations ==

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

The subclass of NPO problems that admit an approximation scheme in the following sense.  For any ε>0, there is an algorithm that is guaranteed to find a solution whose cost is within a 1+ε factor of the optimum cost.  Furthermore, the running time of the algorithm is polynomial in n (the size of the problem) and in 1/ε.

Contained in PTAS.

Defined in [ACG+99].

Contained in FPT [CC97].
== Relations ==

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

Same as FPT except that the algorithm can vary with the parameter k (though its running time must always be O(p(|x|)), for a fixed polynomial p).

An alternate view is that a single algorithm can take a polynomial-length advice string, depending on k.

Defined in [DF99] (though they did not use our notation).
== Relations ==

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

Same as FPT except that f has to be recursive.

Defined in [DF99] (though they did not use our notation).
== Relations ==

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

The class of problems for which the task is to output a quantum certificate for a QMA problem, when such a certificate exists.  Thus, the desired output is a quantum state.

Defined in [JWB03], where it is also shown that state preparation for 3-local Hamiltonians is FQMA-complete.  The authors also observe that, in contrast to the case of FNP versus NP, there is no obvious reduction of FQMA problems to QMA problems.
== Relations ==

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

The class of decision problems solvable by an NP machine such that

The number of accepting paths a is bounded by a polynomial in the size of the input x.
For some polynomial-time predicate Q, Q(x,a) is true if and only if the answer is 'yes.'

Also called FewPaths.

Defined in [CH89].

Contains FewP, and is contained in P^FewP^ [Kob89] and in SPP [FFK94].

See also the survey [Tor90].
== Relations ==

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

The class of decision problems solvable by an NEXP machine such that, given a "yes" instance, no more than an exponential number of computation paths accept.

Contained in MIP[NP^FewEXP^] (MIP where provers are not unbounded in computational power, but are limited to NP^FewEXP^) [AKS+94].

Alternatively, FewEXP can refer to the sparsity of accepting paths in a given instance. In [AKR+03], the authors show that the conjectures "FewEXP search instances are EXP-solvable" and "FewEXP decision instances are EXP/poly-solvable" are equivalent. That is, for all NEXP machines , the following conditions are equivalent:

There exists an EXP machine  such that if given a string ,  accepts and has exponentially bounded accepting paths, then  produces one such path.
 There exists an EXP/poly machine  which accepts a string  if and only  accepts.
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is 'no,' then all computation paths reject.
If the answer is 'yes,' then at least one path accepts; furthermore, the number of accepting paths is upper-bounded by a polynomial in n, the size of the input.

Defined in [AR88].

Is contained in ⊕P [CH89].

There exists an oracle relative to which P, UP, FewP, and NP are all distinct [Rub88].

Also, there exists an oracle relative to which FewP does not have a Turing-complete set [HJV93].

Contained in Few.

See also the survey [Tor90].
== Relations ==

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

Contains P and is contained in GI.

See [KST93] for much more information about GA.

Can be defined as the class of problems polynomial-time Turing reducible to the problem of deciding whether a given graph has any nontrivial automorphisms.
== Relations ==

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

Contains NSPACE(f(n)) and BPSPACE(f(n)), and is contained in AUC-SPACE(f(n)).

By linear programming, GAN-SPACE(log n) is contained in P.
== Relations ==

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

For example, GC(p(n),P) = NP where p is a polynomial.

Defined in [CC93].

Umans [Uma98] has shown that given a DNF expression Φ, the Shortest Implicant problem is GC(log^2^n, coNP)-complete.

Umans [Uma98] has shown that given a DNF expression Φ, the Shortest Implicant problem (is there a conjunction of at most k negated or non-negated literals that implies Φ?) is GC(log^2^n, coNP)-complete.
== Relations ==

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

Defined in [DW86] and shown to be contained in LOGCFL (and therefore in P among others).

Shown to be equivalent to Acyclic CSL in [Nie02].

The class of languages generated by context-sensitive grammars in which the right-hand side of each transformation is strictly longer than the left-hand side.

Defined in [DW86].
== Relations ==

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

Contains GA and is contained in Δ,,2,,P.

The Graph Isomorphism problem itself (as opposed to the set of problems Turing reducible to Graph Isomorphism) is contained in NP as well as coAM (and indeed SZK).  So in particular, if Graph Isomorphism is NP-complete, then PH collapses.

See [KST93] for much more information about GI.

Can be defined as the class of problems polynomial-time Turing reducible to the problem of deciding whether two graphs are isomorphic.

The GI problem itself (as opposed to the set of problems Turing reducible to GI) is contained in NP as well as coAM (and indeed SZK).  So in particular, if graph isomorphism is NP-complete, then PH collapses.
== Relations ==

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

The class of NPO problems which have the property that for all locally optimal solutions, the ratio between the values of the local and global optima is upper-bounded by a constant.

Defined in [AP95], where it was also shown that GLO is strictly contained in APX.

[KMS+99] showed that MaxSNP is not contained in GLO.
== Relations ==

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

Same as PCD(r(n),q(n)), except that now the verifier is allowed nonadaptively to query O(q(n)) rounds of the debate, with no restriction on the number of bits it looks at within each round.

Defined in [CFL+93], who also showed that PCD(log n, q(n)) = GPCD(log n, q(n)) for every q(n).
== Relations ==

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

Defined in [DF99], which should be consulted for the full definition.

Uniform G[P] (i.e. with no restriction on depth) is equal to FPT.
== Relations ==

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

The class of functions from {0,1}^n^ to integers computable by constant-depth, polynomial-size arithmetic circuits with addition and multiplication gates and the constants 0, 1, and -1.  (The only difference from #AC^0^ is the ability to subtract, using the constant -1.)

Equals DiffAC^0^ under logspace uniformity [ABL98].
== Relations ==

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

Has the same relation to L as GapP does to P.
== Relations ==

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

The class of functions f(x) such that for some NP machine, f(x) is the number of accepting paths minus the number of rejecting paths.

Equivalently, the closure of the #P functions under subtraction.

Defined in [FFK94] and independently [Gup95].
== Relations ==

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

We define a relation of order  and arity  to be a subset of -tuple of relation of order  and arity . When  it is by extension a first order variable. The quantification of formula in HO is over a given order (which is a straightforward extension of SO where we add quantification over constant (first-order variable) and relation (second-order variables). The atomic predicates now can be general application of relation of order  and arity  to  relations of order  and arity  and  test of equality between two relations of the same order and arity.

is the set of formulae with quantification up to order O. (resp. ) is defined as the set of formula in  beginning by an existantial (resp universal) quantifier followed by at most  alternation of quantifiers.

This class was define in [HT06], and it was proved that  where  is the th level of the polynomial hierarchy.
== Relations ==

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

The class of decision problems that have SZK protocols assuming an honest verifier (i.e. one who doesn't try to learn more about the problem by deviating from the protocol).

Equals SZK [Oka96].
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is 'yes,' exactly 1/2 of computation paths accept.
If the answer is 'no,' all computation paths reject.

Significantly, the number of candidate witnesses is restricted to be a power of 2.  (This is implicit if they are binary strings.)

Contained in RP, EP, and Mod,,k,,P for every odd k.  Contained in EQP by the Deutsch-Jozsa algorithm.

Defined in [BB92], where it was called C,,==,,P[half].  The name used here is from [BS00].  There it was shown that HalfP is contained in every similar class in which 1/2 is replaced by some other dyadic fraction.
== Relations ==

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

The class of problems for which a 1-1/poly(n) fraction of instances are solvable by a BPP machine.

[FS04] showed a strict hierarchy theorem for HeurBPP; thus, HeurBPP does not equal HeurBPTIME(n^c^) for any fixed c.
== Relations ==

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

The class of problems for which a 1-1/poly(n) fraction of instances are solvable by a BPTIME(f(n)) machine. Thus, HeurBPTIME(f(n)) has the same relationship with BPTIME as HeurDTIME.

Thus HeurBPP is the union of HeurBPTIME(n^c^) over all c.

The class of problems for which a 1-1/poly(n) fraction of instances are solvable by a BPTIME(f(n)) machine.
== Relations ==

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

For functions  and , we say that tuple , where  is a language and  is a distribution of problem instances, if there exists a heuristic deterministic algorithm  such that for all  in the support of ,  runs in time bounded by  and with failure probability bounded by  [BT06].
== Relations ==

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

NP is not contained in HeurNTIME,,,,() for any constants  [Per07].
== Relations ==

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

The class of distributional problems solvable by a P machine. Defined in [Imp95], though he calls the class HP.

Alternately, [BT06] define HeurP as being the set of tuples , where  is a language and  is a distribution of problem instances, such that there exists an algorithm  satisfying two properties:

For every , for every  in the support of , and for every ,  runs in time bounded by .
 For every ,  is a heuristic algorithm for  whose error probability is bounded by .
== Relations ==

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

The class of distributional problems solvable by a PP machine. Defined in [Ill95], though he calls the class HPP.
== Relations ==

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

The class of problems A in NP such that Σ,,k,,P^A^ = Σ,,k+1,,P; that is, adding A as an oracle increases the power of the k^th^ level of the polynomial hierarchy by a maximum amount.

For all k, H,,k,, is contained in H,,k+1,,.

H,,0,, consists exactly of the problems complete for NP under Cook reductions.

H,,1,, consists exactly of the problems complete for NP under strong non-deterministic Turing reductions [Sch83].

Defined in [Sch83].

See also L,,k,,P.
== Relations ==

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

Defined in [OKS+94]; see also [LV97].

If NP is contained in IC[log,poly], then P = NP [OKS+94].  Indeed, any self-reducible problem in IC[log,poly] is also in P.

Strictly contains P/log, and is strictly contained in P/poly.
== Relations ==

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

Defined in [GMR89], with the motivation of providing a framework for the introduction of zero-knowledge proofs (see the class ZK). Interestingly, the power of general interactive proof systems is not decreased if the verifier is only allowed random queries (i.e., it merely tosses coins and sends any outcome to the prover). The latter model, known as the Arthur-Merlin (or public-coin) model was introduced independently (but later) in [Bab85], and a strong equivalent (which preserves the number of rounds) is proved in [GS86]. 
Often, it is required that the prover can convince the verifier to accept correct assertions with probability 1; this is called perfect completeness.
However, the definitions with one-sided and two-sided error can be shown to be equivalent (see [FGM+89]).

First demonstration to the power of interactive proofs was given by showing that for graph nonisomorphism (a problem not known in NP) has such proofs [GMW91]. Five years later is was shown that
IP contains PH [LFK+90], and indeed (this was discovered only a few weeks later) equals PSPACE [Sha90].  On the other hand, coNP is not contained in IP relative to a random oracle [CCG+94].

See also: MIP, QIP, MA, AM.

The class of decision problems for which a "yes" answer can be verified by an interactive proof.  Here a BPP (i.e. probabilistic polynomial-time) verifier sends messages back and forth with an all-powerful prover.  They can have polynomially many rounds of interaction. Given the verifier's algorithm, at the end:

IP contains PH [LFK+90], and indeed (this was discovered only a few days later) equals PSPACE [Sha90].  On the other hand, coNP is not contained in IP relative to a random oracle [CCG+94].

See also: MIP, QIP, MA, AM.
== Relations ==

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

Same as IP, except that if the answer is "yes," there need only be a prover strategy that causes the verifier to accept with probability greater than 1/2, while if the answer is "no," then for all prover strategies the verifier accepts with probability less than 1/2.

Defined in [CCG+94], where it was also shown that IPP = PSPACE relative to all oracles.  Since IP is strictly contained in PSPACE relative to a random oracle, the authors interpreted this as evidence against the Random Oracle Hypothesis (a slight change in definition can cause the behavior of a class relative to a random oracle to change drastically).

See also: PPSPACE.
== Relations ==

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

Alternate name for AM[polylog].
== Relations ==

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

A class of number-theoretic functions, defined as the closure of basic integer arithmetic operations (, as well as constants 0, 1, and projections) under composition and polynomially long sums and products. Defined by [Con73], who mistakenly claimed it coincides with FP.

Equals U,,D,,-uniform FTC^0^ by [Hes01].
== Relations ==

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

L is contained in P.  L contains NC^1^ [Bor77], and is contained in generalizations including NL, L/poly, SL, RL, ⊕L, and Mod,,k,,L.

Reingold [Rei04] showed that, remarkably, L = SL.  In other words, undirected graph connectivity is solvable in deterministic logarithmic space.

Immerman [Imm83] showed that L is the class FO(dtc) of first-order expressible queries with a deterministic transitive closure.

L queries are exactly the one that can be written in a syntactic restriction of  While languages.

L contains NC^1^ [Bor77], and is contained in generalizations including NL, L/poly, SL, RL, ⊕L, and Mod,,k,,L.
== Relations ==

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

Has the same relation to L as P/poly does to P.

Equals PBP [Cob66].

Contains SL [AKL+79].
== Relations ==

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

It is equivalent to AC^0^ with bounded fanout and it is properly contained in AC^0^ [CR96].
== Relations ==

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

The th level of the Logarithmic Time Hierarchy is the set of languages recognised by alternating Turing machine in logtime with random access and  alternation, begining with existantial state. LH is the union of all levels and is equal to tothe class AC^0^ and to FO Descriptive complexity.
== Relations ==

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

Strictly Contained in NLIN. [PPS+83].

Contained in NLIN.
== Relations ==

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

The class of decision problems reducible in L to the problem of deciding membership in a context-free language.

Equivalently, LOGCFL is the class of decision problems solvable by a uniform family of AC^1^ circuits, in which no AND gate has fan-in exceeding 2 (see e.g. [Joh90], p. 137).

LOGCFL is closed under complement [BCD+89].

Contains NL [Sud78].
== Relations ==

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

There are several possible definitions of this class; the most common is the class of languages which can be computed in space O(log log n) by a deterministic Turing machine with two-way access to the input. A typical nonregular language in this class has a form such as 00..00a00..01b00..10b00..11a..., with the successive numbers having logarithmic length. It is the smallest of a collection of sublogarithmically bounded space classes, since any smaller space class contains only the regular languages. These and related classes are studied extensively in [Szep94] and [LiRe93]. The alternation hierarchy for this class is infinite ([BGR93]), and the  and  levels are incomparable unless ; however, the nondeterministic version of the class is closed under complement ([Geff91]).

Sublogarithmically-bounded Turing reductions are equivalent to "regular" (constant-bounded) reductions, however ([Agr01]).

Note that while there are no decision problems that can be tested in one-way loglog space, there are promise problems which can be so tested, such as Balanced Monotone Boolean Sentence Value [Buss91]. Also, the alternation hierarchy over 1-way loglog space still does not collapse.

Obviously contained in L.
== Relations ==

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

The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists y such that for all j in S, the predicate φ(I,s,,j,,,x,y,j) holds.  Here x and y are logarithmic-length strings, or equivalently polynomially bounded numbers, and φ is computable in P.

LOGNP,,0,, is the subclass in which φ is a first-order predicate without quantifiers and x and y are bounded lists of indices of input bits.  LOGNP is also the closure of LOGNP,,0,, under many-one reduction.

The motivation is that the analogue of LOGNP,,0,, without the logarithmic bound on |S| is SO-E, which by Fagin's theorem equals NP [Fag74].

Defined in [PY96], where it was also shown that the following problem is complete for LOGNP under many-one reductions:

Vapnik-Chervonenkis (V-C) Dimension.  Given a family F of subsets of a set U, find a subset of S of U of maximum cardinality, such that every subset of S can be written as the intersection of S with some set in F.

Contains LOGSNP, and is contained in βP (indeed β,,2,,P).

The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists y such that for all j, the predicate φ(I,s,,j,,,x,y,j) holds.  Here x and y are logarithmic-length strings, or equivalently polynomially bounded numbers, and φ is computable in P.
== Relations ==

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

The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists j in S such that the predicate φ(I,s,,j,,,x,j) holds.  Here x is a logarithmic-length string, or equivalently a polynomially bounded number, and φ is computable in P.

LOGSNP,,0,, is the subclass in which φ is a first-order predicate without quantifiers and x is a bounded lists of indices of input bits.  LOGSNP is also the closure of LOGSNP,,0,, under many-one reduction.  See LOGNP and SNP for the motivation.

Defined in [PY96].

Contained in LOGNP, and therefore QPLIN.

If P = LOGSNP, then for every constructible f(n) > n, NTIME(f(n)) is contained in DTIME(g(n)^sqrt(g(n))^), where g(n) = O(f(n) logf(n)) [FK97].

The set of I for which there exists a subset S={s,,1,,,...,s,,log n,,} of {1,...,n} of size log n, such that for all x there exists j such that the predicate φ(I,s,,j,,,x,j) holds.  Here x and y are logarithmic-length strings, or equivalently polynomially bounded numbers, and φ is computable in P.
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is "no," then the number of accepting computation paths exactly equals the number of rejecting paths.
If the answer is "yes," then the difference of these numbers equals a function f(|x|) computable in polynomial time (i.e. FP).  Here |x| is the length of the input x, and ``polynomial time means polynomial in |x|, the length of x, rather than the length of |x|.

Defined in [FFK94], where it was also shown that LWPP is low for PP and C,,=,,P.  (I.e. adding LWPP as an oracle does not increase the power of these classes.)

Contained in WPP and AWPP.

Contains SPP.

Also, contains the graph isomorphism problem [KST92].

Contains a whole litter of problems for solvable black-box groups: group intersection, group factorization, coset intersection, and double-coset membership [Vin04].

Contains a whole litter of problems for solvable black-box groups: group intersection, group factorization, coset intersection, and double-coset membership [Vin04]
== Relations ==

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

L,,1,,P = NP ∩ coNP.

For all k, L,,k,, is contained in L,,k+1,, and in NP.

Defined in [Sch83].

See also H,,k,,P.
== Relations ==

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

The class of decision problems solvable by an NL machine such that

The number of accepting paths on input x is f(x), and
The answer is 'yes' if and only if R(x,f(x))=1, where R is some predicate computable in L.

Defined in [BDH+92], where it was also shown that LogFew is contained in Mod,,k,,L for all k>1.
== Relations ==

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

Same as FewP but for logspace-bounded (i.e. NL) machines.

Defined in [BDH+92], where it was also shown that LogFewNL is contained in ModZ,,k,,L for all k>1.
== Relations ==

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

The class of decision problems solvable by a Merlin-Arthur protocol, which goes as follows.  Merlin, who has unbounded computational resources, sends Arthur a polynomial-size purported proof that the answer to the problem is "yes."  Arthur must verify the proof in BPP (i.e. probabilistic polynomial-time), so that

If the answer is "yes," then there exists a proof such that Arthur accepts with probability at least 2/3.
If the answer is "no," then for all proofs Arthur accepts with probability at most 1/3.

An alternative definition requires that if the answer is "yes," then there exists a proof such that Arthur accepts with certainty.  However, the definitions with one-sided and two-sided error can be shown to be equivalent (see [FGM+89]).

Contains NP and BPP 
(in fact also ∃BPP), and is contained in AM and in QMA.

Also contained in Σ,,2,,P ∩ Π,,2,,P.

There exists an oracle relative to which BQP is not in MA [Wat00].

Equals NP under a derandomization assumption: if E requires exponentially-sized circuits, then PromiseBPP = PromiseP, implying that MA = NP [IW97].

Shown in [San07] that MA/1 does not have circuits of size  for any . In the same paper, the result was used to show that MA/1 cannot be solved on more than a  fraction of inputs having length  by any circuit of size . Finally, it was shown that MA does not have arithmetic circuits of size .

See also: MA,,E,,, MA,,EXP,,.

An alternative definition requires that if the answer is "yes," then there exists a proof such that Arthur accepts with certainty.  However, the definitions with one-sided and two-sided error can be shown to be equivalent (exercise for the Zoo visitor).

Contains NP and ∃BPP, and is contained in AM and in QMA.

Equals NP under a derandomization assumption.
== Relations ==

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

The subclass of MA such that for each input size n, there is a sparse set S,,n,, that Merlin's proof string always belongs to (no matter what the input is).

Defined in [KST93], where it is also observed that if graph isomorphism is in P/poly, then the complement of graph isomorphism is in MA'.
== Relations ==

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

Same as AC^0^, except now we're allowed a single unbounded-fanin majority gate at the root.

Defined in [JKS02].

MAC^0^ is strictly contained in TC^0^ [ABF+94].
== Relations ==

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

Same as MA, except now Arthur is E instead of polynomial-time.

If MA,,E,, = NEE then MA = NEXP ∩ coNEXP [IKW01].
== Relations ==

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

Same as MA, except now Arthur is EXP instead of polynomial-time, and the message from Merlin can be exponentially long.

There is a problem in MA,,EXP,, that does not have polynomial-size circuits [BFT98].  On the other hand, there is an oracle relative to which every problem in MA,,EXP,, does have polynomial-size circuits.

[MVW99] considered the best circuit lower bound obtainable for a problem in MA,,EXP,,, using current techniques.  They found that this bound is half-exponential: i.e. a function f such that f(f(n))=2^n^.  Such functions exist, but are not expressible using standard asymptotic notation.
== Relations ==

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

Identical to MA except for that Arthur (the verifier) has random access to the proof string given by Merlin, and is limited to running times of order .

This class was used by [SM03] to show that if EXP has circuits of polynomial size, then EXP = MA.
== Relations ==

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

Same as IP, except that now the verifier can exchange messages with many provers, not just one.  The provers cannot communicate with each other during the execution of the protocol, so the verifier can "cross-check" their assertions (as with suspects in separate interrogation rooms).

Defined in [BGK+88].

Let MIP[k] be the class of decision problems for which a "yes" answer can be verified with k provers.  Then for all k>2, MIP[k] = MIP[2] = MIP [BGK+88].

MIP equals NEXP [BFL91]; this is a famous non-relativizing result.
== Relations ==

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

Same as MIP, except that the provers can share arbitrarily many entangled qubits.  The verifier is classical, as are all messages between the provers and verifier.

Defined in [CHT+04], where evidence was given suggesting that MIP* does not "obviously" equal NEXP.

MIP* contains NEXP [IV12]. By contrast, MIP, the corresponding class without entanglement, equals NEXP (and even MIP[2,1] with two provers and one round equals NEXP).

Even MIP*[4,poly] and MIP[5,1] contain NEXP [IV12].

MIP*[2,1] contains XOR-MIP*[2,1].

In 2012 it was shown that QMIP = MIP* [RUV12]
== Relations ==

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

Defined in [CHT+04], where evidence was given suggesting that MIP* does not "obviously" equal NEXP.  By contrast, MIP[2,1], the corresponding class without entanglement, equals NEXP.

Indeed, the relationship between MIP* and MIP = NEXP is completely unknown -- either could contain the other, or they could be incomparable.

It is also unknown whether increasing the number of provers or rounds changes MIP*[2,1].

Contains XOR-MIP*[2,1].
== Relations ==

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

The exponential-time analogue of MIP.

In the unrelativized world, equals NEEXP.

There exists an oracle relative to which MIP,,EXP,, equals the intersection of P/poly, P^NP^, and ⊕P [BFT98].
== Relations ==

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

Currently, the best known algorithm for multiplying two  matrices is the Coppersmith–Winograd_algorithm, which has a time complexity of  [CW90]. Note that for the general problem, a lower bound of  is trivial from the number of elements being considered.
== Relations ==

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

Defined in [FV93] as a subclass of SNP.  There are three syntactic restrictions defining the subclass MMSNP, based on the form of the SNP formula defining the language:

The second order existentially quantified variables, known as the proof relations, are restricted to be monadic.  (Monadic relations can be treated as sets.)
 Any relations in the formula other than the proof relations must occur only negated (the formula is monotone).
 No inequality relations can occur in the formula.

MMSNP seems to obey dichotomy, by excluding languages that are NP-intermediate.  This is still open but widely believed.  Dropping any of the restrictions monotone/monadic/without inequalities allows NP-intermediate languages unless P = NP, since any problem in NP is polynomial time equivalent to a problem in each of these broader classes.  MMSNP therefore seems to be a maximal fragment of NP where NP-intermediate languages are excluded.

Every constraint satisfaction problem with a fixed target structure is expressible in MMSNP, and there is a polynomial time Turing reduction from every MMSNP query to finitely many constraint satisfaction problems.  MMSNP therefore seems to capture the class of constraint satisfaction problems with fixed templates, CSP.

Defined in [FV93] as a subclass of SNP, where the second order existentially quantified variables are sets (monadic) and any relations in the first-order part occur negated (monotone).  Further, no inequalities can occur in the first-order part.

MMSNP seems to obey dichotomy, by excluding Ladner languages.  This is still open but widely believed.  Dropping any of the restrictions monotone/monadic/without inequalities          allows Ladner languages unless P = NP, since any problem in NP is polynomial time equivalent to a problem in each of these broader classes.  MMSNP therefore seems to be a maximal fragment of NP where Ladner languages are excluded.

Every constraint satisfaction problem is expressible in MMSNP, and there is a polynomial time Turing reduction from every MMSNP query to finitely many constraint satisfaction problems.  MMSNP therefore seems to capture the class of constraint satisfaction problems.
== Relations ==

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

The class of decision problems such that for some #P function f, the answer on input x is 'yes' if and only if the middle bit of f(x) is 1.

Defined in [GKR+95].

Contains AmpMP and PH.

MP with ModP oracle equals MP with #P oracle [KT96].
== Relations ==

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

Defined in [DC89].

[BLM+99] showed that we can assume without loss of generality that the circuit has width n and depth n^3^.
== Relations ==

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

Has the same relation to NP as MaxSNP does to SNP.

Contains MaxPB.

The closure of MaxNP under PTAS reduction is APX [KMS+99], [CT94].
== Relations ==

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

The subclass of MaxNP problems for which the cost function is guaranteed always to be bounded by a polynomial.

MinPB can be defined similarly.

Defined in [KT94].

The closure of MaxPB under PTAS reductions equals NPOPB [CKS+99].
== Relations ==

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

The class of optimization problems reducible by an "L-reduction" to a problem in MaxSNP,,0,,.  (Note: 'L' stands for linear -- this is not the same as an L reduction!  For more details see [PY88].)

Defined in [PY88], where the following was also shown:

Max3SAT is MaxSNP-complete.  (Max3SAT is the problem of finding an assignment that maximizes the number of satisfied clauses in a CNF formula with at most 3 literals per clause.)
Any problem in MaxSNP can be approximated to within a fixed ratio.

The closure of MaxSNP under PTAS reduction is APX [KMS+99], [CT94].
== Relations ==

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

The class of function problems expressible as "find a relation such that the set of k-tuples for which a given SNP predicate holds has maximum cardinality."

For example (see [Pap94]), the Max-Cut problem can be expressed as follows:

Given a graph G, find a subset S of vertices that maximizes the number of pairs (u,v) of vertices such that u is in S, and v is not in S, and G has an edge from u to v.

Defined in [PY88].
== Relations ==

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

Same as MaxPB but for minimization instead of maximization problems.
== Relations ==

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

Thus, for any prime  and natural number , . Moreover, FL^ModL^ = FL^GapL^ [AV04].

Defined in [AV04].
== Relations ==

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

The class of decision problems solvable by a Mod,,k,,P machine where k can vary depending on the input.  The only requirement is that 0^k^ be computable in polynomial time.

Defined in [KT96], where it was also shown that ModP is contained in AmpMP.
== Relations ==

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

Defined in [BDH+92], where it was also shown that ModZ,,k,,L contains LogFewNL for all k>1.

Contained in Mod,,k,,L and in NL.
== Relations ==

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

Has the same relation to L as Mod,,k,,P does to P.

For any prime k, Mod,,k,,L contains SL [KW93].

For any prime k, Mod,,k,,L^ModkL^ = Mod,,k,,L [HRV00].

For any k>1, contains LogFew [BDH+92].
== Relations ==

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

For any k>1: The class of decision problems solvable by an NP machine such that the number of accepting paths is divisible by k, if and only if the answer is "no."

Mod,,2,,P is more commonly known as ⊕P "parity-P."

For every k, Mod,,k,,P contains graph isomorphism [AK02].

Defined in [CH89], [Her90].

[Her90] and [BG92] showed that Mod,,k,,P is the set of unions of languages in Mod,,p,,P for each prime p that divides k.  In particular, if p is prime, then Mod,,p,,P = Mod,,p^m,,P for all positive integers m.  A further fact is that Mod,,p,,P is closed under union, intersection, and complement for p prime.

On the other hand, if k is not a prime power, then there exists an oracle relative to which Mod,,k,,P is not closed under intersection or complement [BBR94].

For prime p, there exists an oracle relative to which Mod,,p,,P does not contain EQP [GV02].
== Relations ==

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

Equals LOGCFL [Sud78].
== Relations ==

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

Then NC is the union of NC^i^ over all nonnegative i.

Also, NC equals the union of PT/WK(log^k^n, n^k^)/poly over all constants k.

NC^i^ is contained in AC^i^; thus, NC = AC.

Contains NL.

Generalizations include RNC and QNC.

[IN96] construct a candidate pseudorandom generator in NC based on the subset sum problem.

For a random oracle A, (NC^i^)^A^ is strictly contained in (NC^i+1^)^A^, and uniform NC^A^ is strictly contained in P^A^, with probability 1 [Mil92].

In descriptive complexity, NC can be defined by FO[]

NC^i^ is the class of decision problems solvable by a nonuniform family of Boolean circuits, with polynomial size, depth O(log^i^(n)), and fan-in 2.
== Relations ==

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

By definition, a decision problem in NC^0^ can depend on only a constant number of bits of the input.  Thus, NC^0^ usually refers to functions computable by constant-depth, bounded-fanin circuits.

There is a family of permutations computable by a uniform family of NC^0^ circuits that is P-hard to invert [Has88].

Recently [AIK04] solved a longstanding open problem by showing that there exist pseudorandom generators and one-way functions in NC^0^, based on (for example) the hardness of factoring.  Specifically, in these generators every bit of the output depends on only 4 input bits.  Whether the dependence can be reduced to 3 bits under the same cryptographic assumptions is open, but [AIK04] have some partial results in this direction.  It is known that the dependence cannot be reduced to 2 bits.
== Relations ==

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

See NC for definition.

[KV94] give a family of functions that is computable in NC^1^, but not efficiently learnable unless there exists an efficient algorithm for factoring Blum integers.

Was shown to equal 5-PBP [Bar89].  On the other hand, width 5 is necessary unless NC^1^ = ACC^0^ [BT88].

As an application of this result, NC^1^ can be simulated on a quantum computer with three qubits, one initialized to a pure state and the remaining two in the maximally mixed state [ASV00].  Surprisingly, [AMP02] showed that only a single qubit is needed to simulate NC^1^ - i.e. that NC^1^ is contained in 2-EQBP.  (Complex amplitudes are needed for this result.)

Is contained in L [Bor77].

Contains TC^0^.

NC^1^ contains the integer division problem [BCH86], even if an L-uniformity condition is imposed [CDL01].

U,,E^*^,,-uniform NC^1^ is equal to ALOGTIME [RUZ81].
== Relations ==

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

See NC for definition.

Contains NL.
== Relations ==

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

P^NE^ = NP^NE^ [Hem89].

Contained in NEXP.
== Relations ==

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

Contains coNE, just as NEXP/poly contains coNEXP.
== Relations ==

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

If MA,,E,, = NEE then MA = NEXP ∩ coNEXP [IKW01].

Contained in NEEXP.

Nondeterministic double-exponential time with linear exponent (i.e. NTIME(2^2^O(n)^)).
== Relations ==

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

Equals MIP,,EXP,, (unrelativized).

Nondeterministic double-exponential time (i.e. NTIME(2^2^p(n)^) for p a polynomial).
== Relations ==

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

Equals MIP [BFL91] (but not relative to all oracles).

NEXP is in MIP* [IV12].

NEXP is in P/poly if and only if NEXP = MA [IKW01].

[KI02] show the following:

If P = RP, then NEXP is not computable by polynomial-size arithmetic circuits.
If P = BPP and if checking whether a Boolean circuit computes a function that is close to a low-degree polynomial over a finite field is in P, then NEXP is not in P/poly.
If NEXP is in P/poly, then matrix permanent is NEXP-complete.

Does not equal NP [SFM78].

Does not equal EXP if and only if there is a sparse set in NP that is not in P.

There exists an oracle relative to which EXP = NEXP but still P does not equal NP [Dek76].

The theory of reals with addition (see EXPSPACE) is hard for NEXP [FR74].
== Relations ==

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

Contains coNEXP (folklore result reported in [weblog]).
== Relations ==

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

Defined in [M08] based on [DDPY98],[BFM88].

Contained in PZK.

[M08] showed a complete promise-problem for NIPZK, called Unifrom (UN). Instances 
in UN are circuits with n+1 output bits. The first n bits represent the uniform distribution, and the last bit is 1 with probability at least 2/3. For instances not in UN, when the last bit is 1, at most 1/3 of the strings of length n can appear as the output of the circuit. The problem is to decide which is the case.
== Relations ==

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

Has the same relation to QSZK as NISZK does to SZK.

Defined in [Kob02], where it was also shown that the following promise problem is complete for NIQSZK.  Given a quantum circuit, we are promised that the state it prepares (when run on the all-0 state, and tracing out non-output qubits) has trace distance either at most 1/3 or at least 2/3 from the maximally mixed state. The problem is to output "no" in the former case and "yes" in the latter.

NIQPZK can be defined similarly.
== Relations ==

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

Defined in [DDP+98].

Contained in SZK.

[GSV99] showed the following:

If SZK does not equal BPP then NISZK does not equal BPP.
NISZK equals SZK if and only if NISZK is closed under complement.
NISZK has natural complete promise problems:
  
    Statistical Distance from Uniform (SDU): Given a circuit, consider the distribution over outputs when the circuit is given a uniformly random n-bit string.  We're promised that the trace distance between this distribution and the uniform distribution is either at most 1/3 or at least 2/3.  The problem is to output "yes" in the former case and "no" in the latter.
    Entropy Approximation (EA): Now we're promised that the entropy of the circuit's output distribution is either at least k+1 or at most k-1.  The problem is to output "yes" in the former case and "no" in the latter.

NIPZK can be defined similarly.
== Relations ==

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

The non-interactive analogue of SZK,,h,,.

Defined in [BG03], where the following was also shown:

NISZK,,h,, contains NISZK and is contained in SZK.
Graph Isomorphism is in NISZK,,h,,.
The following problem is complete for NISZK,,h,,: Given two functions from {0,1}^n^ to {0,1}^n^ (specified by circuits), decide whether their ranges are almost equal or almost disjoint, given that one of these is the case.

The quantum lower bound for the set comparison problem in [Aar02] implies an oracle relative to which NISZK,,h,, is not in BQP.
== Relations ==

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

Has the same relation to L as NP does to P.

In a breakthrough result, was shown to equal coNL [Imm88] [Sze87].  (Though contrast to mNL.)

Is contained in LOGCFL [Sud78], as well as NC^2^.

Is contained in UL/poly [RA00].

Deciding whether a bipartite graph has a perfect matching is hard for NL [KUW86].

NL can be defined in a logical formalism as SO(krom) and also as FO(tc), reachability in directed graph is NL-Complete under FO-reduction.
== Relations ==

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

Has the same relation to NL as P/poly does to P.

Is contained in ⊕L/poly [GW96], as well as SAC^1^.

Equals UL/poly [RA00].
== Relations ==

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

Has the same relation to LIN as NP does to P.
== Relations ==

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

Same as NL -- but if there's an oracle, then NLOG can make queries nondeterministically on a polynomial-size, one-way oracle tape.  (NL, by contrast, can use nondeterministic transitions only on the worktape; oracle queries have to be deterministic.)

See [LL76] or [HCK+88] for more information.

Although NLOG is contained in P, there exists an oracle relative to which that is not the case.  This illustrates that care is needed when defining oracle access mechanisms.
== Relations ==

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

Defined in [GS89].

See also QL.
== Relations ==

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

Same as NC, but with O(f(n)) nondeterministic gates. A nondeterministic gate has no inputs and a single output bit.

Defined in [Wol94], where the author proves various inclusions, including but not limited to NNC(poly(n))=NP, NNC(log(n))=NC, and NNC(polylog)⊆DSPACE(polylog).
== Relations ==

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

Class of functions computable in nearly linear time n(log n)^O(1)^ on nondeterministic random access machines.  Equals NQL [GS89].

Defined in [GS89].
== Relations ==

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

Is the opposite of ALL, but does not equal the complement coALL = ALL.

Is closed under polynomial-time Turing reductions :-).

Equals SPARSE ∩ coSPARSE and TALLY ∩ coTALLY.
== Relations ==

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

Then NP is the class of decision problems solvable by an NP machine such that

If the answer is "yes," at least one computation path accepts.
If the answer is "no," all computation paths reject.

Equivalently, NP is the class of decision problems such that, if the answer is "yes," then there is a proof of this fact, of length polynomial in the size of the input, that can be verified in P (i.e. by a deterministic polynomial-time algorithm).  On the other hand, if the answer is "no," then the algorithm must declare invalid any purported proof that the answer is "yes."

For example, the SAT problem is to decide whether a given Boolean formula has any satisfying truth assignments. SAT is in NP, since a "yes" answer can be proved by just exhibiting a satisfying assignment.

A decision problem is NP-complete if (1) it is in NP, and (2) any problem in NP can be reduced to it (under some notion of reduction).  The class of NP-complete problems is sometimes called NPC.

That NP-complete problems exist is immediate from the definition.  The seminal result of Cook [Coo71], Karp [Kar72], and Levin [Lev73] is that many natural problems (that have nothing to do with Turing machines) are NP-complete.

The first such problem to be shown NP-complete was SAT [Coo71].  Other classic NP-complete problems include:

3-Colorability: Given a graph, can each vertex be colored red, green, or blue so that no two neighboring vertices have the same color?
Hamiltonian Cycle: Given a graph, is there a cycle that visits each vertex exactly once?
Traveling Salesperson: Given a set of n cities, and the distance
between each pair of cities, is there a route that visits each city exactly
once before returning to the starting city, and has length at most T?
Maximum Clique: Given a graph, are there k vertices all of which are neighbors of each other?
Subset Sum: Given a collection of integers, is there a subset of the integers that sums to exactly x?

For many, many more NP-complete problems, see [GJ79].

NP contains P.  I've discovered a marvelous proof that NP and P are unequal, but this web page is too small to contain it.  Too bad, since otherwise I'd be eligible for $1,000,000 [CMI00].

There exists an oracle relative to which P and NP are unequal [BGS75].  Indeed, P and NP are unequal relative to a random oracle with probability 1 [BG81] (see [AFM01] for a novel take on this result).  Though random oracle results are not always indicative about the unrelativized case [CCG+94].

There even exists an oracle relative to which the P versus NP problem is outside the usual axioms of set theory [HH76].

If we restrict to monotone classes, mP is strictly contained in mNP [Raz85].

Perhaps the most important insight anyone has had into P versus NP is to be found in [RR97].  There the authors show that no 'natural proof' can separate P from NP (or more precisely, place NP outside of P/poly), unless secure pseudorandom generators do not exist.  A proof is 'natural' if it satisfies two conditions called constructivity and largeness; essentially all lower bound techniques known to date satisfy these conditions.  To obtain unnatural proof techniques, some people suspect we need to relate P versus NP to heavy-duty 'traditional' mathematics, for instance algebraic geometry.  See [MS02] (and the survey article [Reg02]) for a development of this point of view.

For more on P versus NP (circa 1992) see [Sip92].  For an opinion poll, see [Gas02].

If P equals NP, then NP equals its complement coNP.  Whether NP equals coNP is also open.  NP and coNP can be extended to the polynomial hierarchy PH.

The set of decision problems in NP, but not in P or NPC, is sometimes called NPI.  If P does not equal NP then NPI is nonempty [Lad75].

Probabilistic generalizations of NP include MA and AM.  If NP is in coAM (or BPP) then PH collapses to Σ,,2,,P [BHZ87].

PH also collapses to Σ,,2,,P if NP is in P/poly [KL82].

There exist oracles relative to which NP is not in BQP [BBB+97].

An alternate characterization is NP = PCP(log n, O(1)) [ALM+98].

Also, [Fag74] showed that NP is precisely the class of decision problems reducible to a graph-theoretic property expressible in second-order existential logic. This leads to the subclass SNP.

It is known that if any NP-complete language is sparse (contains no more than a polynomial number of strings of length ), then P = NP. [BH08] improved this result, showing that if any language in NP has an NP-hard set of subexponential density, then coNP is contained in NP/poly and thus, by [Yap82], PH collapses to the third level.

NP is equal to SO-E, the second-order queries where the second-order quantifiers are only existantials.

For example, the SAT problem is to decide whether a given Boolean formula has any satisfying truth assignments.  SAT is in NP, since a "yes" answer can be proved by just exhibiting a satisfying assignment.

Also, [Fag74] gave a logical characterization of NP, which leads to the subclass SNP.
== Relations ==

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

The class of problems in both NP and coNP.

Contains factoring [Pra75].

Contains graph isomorphism under the assumption that some language in NE ∩ coNE requires nondeterministic circuits of size 2^Ω(n)^ ([MV99], improving [KM99]).  (A nondeterministic circuit C has two inputs, x and y, and accepts on x if there exists a y such that C(x,y)=1.)

Equals P^NP ∩ coNP^ [Bra79].  In particular, if a problem in NP ∩ coNP is NP-hard with Turing reduction, then NP = coNP.

Is not believed to contain complete problems.
== Relations ==

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

Same as NP/poly, except that now the advice string is logarithmic-size.

Shown in [FK05] that EXP ⊆ NP/log if and only if EXP = P^||NP^.
== Relations ==

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

Has the same relation to NP as P/poly does to P.

Contains AM.  On the other hand, if NP/poly contains coNP then PH collapses to the third level.

NP/poly-natural proofs cannot show that circuit families are outside P/poly, under a pseudorandomness assumption [Rud97].
== Relations ==

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

The class of decision problems such that (1) they're in NP and (2) every problem in NP is reducible to them (under some notion of reduction).  In other words, the hardest problems in NP.

Two notions of reduction from problem A to problem B are usually considered:

Karp or many-one reductions.  Here a polynomial-time algorithm is given as input an instance of problem A, and must produce as output an instance of problem B.
Turing reductions, in this context also called Cook reductions.  Here the algorithm for problem B can make arbitrarily many calls to an oracle for problem A.

Some examples of NP-complete problems are discussed under the entry for NP.

The classic reference on NPC is [GJ79].

Unless P = NP, NPC does not contain any sparse problems: that is, problems such that the number of 'yes' instances of size n is upper-bounded by a polynomial in n [Mah82].

A famous conjecture [BH77] asserts that all NP-complete problems are polynomial-time isomorphic -- i.e. between any two problems, there is a one-to-one and onto Karp reduction. If that's true, the NP-complete problems could be interpreted as mere "relabelings" of one another.

NP-complete problems are p-superterse unless P = NP [BKS95].  This means that, given k Boolean formulas F,,1,,,...,F,,k,,, if you can rule out even one of the 2^k^ possibilities in polynomial time (e.g., "if F,,1,,,...,F,,k-1,, are all unsatisfiable then F,,k,, is satisfiable"), then P = NP.

An analog of NP for Turing machines over a complex number field.

Defined in [BCS+97].

It is unknown whether P,,C,, = NP,,C,,, nor are implications known among this question, P,,R,, versus NP,,R,,, and P versus NP.

However, [CKK+95] show that if P/poly does not equal NP/poly then P,,C,, does not equal NP,,C,,.

[BCS+97] show the following striking result.  For a positive integer n, let t(n) denote the minimum number of additions, subtractions, and multiplications needed to construct n, starting from 1.  If for every sequence {n,,k,,} of positive integers, t(n,,k,, k!) grows faster than polylogarithmically in k, then P,,C,, does not equal NP,,C,,.

See also VNP,,k,,.
== Relations ==

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

Sometimes used to denote the set of decision problems in NP that are neither NP-complete (that is, in NPC) nor in P.

Is thought to contain (for example) decision versions of factoring and graph isomorphism.

Is nonempty if P does not equal NP [Lad75].  Indeed, under this assumption, it contains an infinite number of distinct polynomial-time equivalence classes.
== Relations ==

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

The class of all (possibly partial, possibly multivalued) functions computed by an NP machine as follows: ignore the rejecting paths, and consider any output of an accepting path to be "one of the outputs."

Contains NPSV and NPMV,,t,,.

Defined in [BLS84].

Contrast with FNP.
== Relations ==

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

Has the same relation to NPMV as P-Sel does to P.

Defined in [HHN+95].
== Relations ==

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

The class of all (possibly multivalued) NPMV functions that are total (that is, defined for every input).
== Relations ==

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

Has the same relation to NPMV,,t,, as P-Sel does to P.

Defined in [HHN+95].
== Relations ==

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

The class of function problems of the form, "Find any n-bit string x that maximizes a cost function C(x), where C is computable in FP (i.e. polynomial-time)."

Defined in [ACG+99].

Contains APX and NPOPB.
== Relations ==

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

The subclass of NPO problems for which the cost function is guaranteed always to be bounded by a polynomial in n (the input size).

See [ACG+99].

NPOPB equals the closure of MaxPB under PTAS reductions [CKS+99].
== Relations ==

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

An analog of NP for Turing machines over a real number field.

Defined in [BCS+97].

It is unknown whether P,,R,, = NP,,R,,, nor are implications known among this question, P,,C,, versus NP,,C,,, and P versus NP.

Also, in contrast to the case of NP,,C,,, it is an open problem to show that P/poly distinct from NP/poly implies P,,R,, distinct from NP,,R,,.  The difference is that in the real case, a comparison (or greater-than) operator is available, and it is not known how much power this yields in comparison to the complex case.

See also VNP,,k,,.
== Relations ==

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

Equals PSPACE [Sav70].

On the other hand, this result does not relativize if we allow strings of unbounded length to be written to the oracle tape.  In particular, there exists an oracle relative to which NPSPACE is not contained in EXP [GTW+91].
== Relations ==

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

The class of NPMV functions that are single-valued (i.e., such that every accepting path outputs the same value).

Defined in [BLS84].

Contains NPSV,,t,,.

P = NP if and only if FP = NPSV.
== Relations ==

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

Has the same relation to NPSV as P-Sel does to P.

Defined in [HHN+95].

Has the same relation to href="#npsv">NPSV as P-Sel does to P.
== Relations ==

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

The class of all NPSV functions that are total (that is, defined on every input).

Contained in NPMV,,t,,.
== Relations ==

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

Has the same relation to NPSV,,t,, as P-Sel does to P.

Also known as NP-sel.

Defined in [HHN+95].
== Relations ==

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

The analogue of P^cc^ for nondeterministic communication complexity.  Both communication bits and nondeterministic guess bits count toward the complexity.

Does not equal P^cc^ or coNP^cc^ because of the EQUALITY problem.  Also, does not contain BPP^cc^ because of that problem.

Defined in [BFS86].

Contained in PH^cc^.

Has the same relation to NP^cc^ and NP as P,,,,^cc^ does to P^cc^ and P.

NP,,,,^cc^ is not contained in BPP,,,,^cc^ for  players, for any constant . As a result, NP,,,,^cc^ is not equal to RP,,,,^cc^ under the same conditions [DP08].
== Relations ==

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

Equals NNLT.

SAT is NQL-complete under quasi-linear-time reductions (which can be computed in deterministic quasi-linear time) [Sch78].

Defined in [Sch78].

See also: NLT, Q, QL.
== Relations ==

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

The class of decision problems solvable by a QTM in polynomial time such that a particular '|Accept>' state has nonzero amplitude at the end of the computation, if and only if the answer is 'yes.'  Since it has an exact amplitude condition, NQP has the same technical caveats as EQP.  Or it would, except that it turns out to equal coC,,=,,P [FGH+98].

Defined in [ADH97].

Contrast with QMA.
== Relations ==

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

Same as NPSPACE, but with f(n)-space (for some constructible function f) rather than polynomial-space machines.

Contained in DSPACE(f(n)^2^) [Sav70], and indeed RevSPACE(f(n)^2^) 95|[CP95].

NSPACE(n^k^) is strictly contained in NSPACE(n^k+ε^) for ε>0 [Iba72] (actually the hierarchy theorem is stronger than this, but pretty technical to state).

Contained in DSPACE(f(n)^2^) [Sav70], and indeed RevSPACE(f(n)^2^) [CP95].
== Relations ==

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

Is contained in E, NT*, and ⊕P.  Defined in [GHJ+91] to study ⊕P-complete problems.  They show  that P, NT, NT*, and ⊕P are either all equal or strictly nested.  In particular, they differ with probability 1 relative to a random oracle.
== Relations ==

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

Defined like NT, but with a more general ordering on inputs.  A problem L is in NT* if, first, there is a partially defined predecessor function pred(x) in FP that organizes the space of inputs into a forest.  The size of the lineage of each x must also be bounded by 2^poly(|x|)^.  Second, if L(x) is the Boolean answer to L on input x, then L(x)+L(pred(x)) is computable in polynomial time; or if pred(x) does not exist, L(x) is computable in polynomial time.

Defined in [GHJ+91].

Contains NT and is contained in ⊕P.  The inclusions are either both strict or both equalities (whence ⊕P = P as well).
== Relations ==

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

Same as NP, but with f(n)-time (for some constructible function f) rather than polynomial-time machines.

The Nondeterministic Time Hierarchy Theorem: If f and g are time-constructible and f(n+1)=o(g), then NTIME(f(n)) does not equal NTIME(g(n)) [SFM78] (this is actually stronger than the hierarchy theorem for DTIME).

NTIME(n) strictly contains DTIME(n) [PPS+83] (this result does not work for arbitrary f(n)).

For any constructible superpolynomial f, NTIME(f(n)) with NP oracle is not in P/poly [Kan82].
== Relations ==

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

The set of languages L such that for every k, there is a language L_k in P that differs from L on at most 2^n^/n^k^ inputs of length n.  Discussed in [NS05] and implicitly defined in [Yam99].

The set of languages L such that for every k, there is a language L_k in P that differs from L on at most 2^n/n^k inputs of length n.  Discussed in [NS05] and implicitly defined in [Yam99].
== Relations ==

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

The class of problems solvable by a BQP machine in which a single qubit is initialized to the '0' state, and the remaining qubits are initialized to the maximally mixed state.  (This definition is not known to be robust, so one also needs to specify a gate set.)

We also need to stipulate that there are no "strong measurements" -- intermediate measurements on which later operations are conditioned -- since otherwise we can do all of BQP by first initializing the computer to the all-0 state.  Parker and Plenio [PP00] failed to appreciate this point.

Defined by [ASV00] (though they didn't use the name OCQ), who also showed that if OCQ = BQP, something other than gate-by-gate simulation will be needed to show this.
== Relations ==

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

The class of functions computable by taking the maximum of the output values over all accepting paths of an NP machine.

Defined in [Kre88].

Contrast with FNP.
== Relations ==

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

The class of decision problems solvable in polynomial time by a Turing machine.  (See also FP, for function problems.)

Defined in [Edm65], [Cob64], [Rab60], and other seminal early papers.

Contains some highly nontrivial problems, including linear programming [Kha79] and finding a maximum matching in a general graph [Edm65].

Contains the problem of testing whether an integer is prime [AKS02], an important result that improved on a proof requiring an assumption of the generalized Riemann hypothesis [Mil76].

A decision problem is P-complete if it is in P, and if every problem in P can be reduced to it in L (logarithmic space).  The canonical P-complete problem is circuit evaluation: given a Boolean circuit and an input, decide what the circuit outputs when given the input.

Important subclasses of P include L, NL, NC, and SC.

P is contained in NP, but whether they're equal seemed to be an open problem when I last checked.

Efforts to generalize P resulted in BPP and BQP.

The nonuniform version is P/poly, the monotone version is mP, and versions over the real and complex number fields are P,,R,, and P,,C,, respectively.

In descriptive complexity, P can be defined by three different kind of formulae, FO(lfp) which is also FO()], and also as SO(Horn)

P queries are exactly the one that can be written in the While^/cons^ languages.
== Relations ==

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

I decided this class is so important that it deserves an entry of its own, apart from #P.

Contains PH [Tod89], and is contained in PSPACE.

Equals P^PP^ (exercise for the visitor).
== Relations ==

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

Contains PH [Tod89].
== Relations ==

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

Defined in [Yes83].

Contains Almost-P and is contained in P/poly [Sch86].
== Relations ==

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

Then P-OBDD is the class of decision problems solvable by polynomial-size OBDD's.

Contained in PBP, as well as BPP-OBDD.
== Relations ==

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

Defined in [Sel79], where it was also shown that if NP is contained in P-Sel then P = NP.

There exist P-selective sets that are not recursive (i.e. not in R).
== Relations ==

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

Same as P/poly, except that the advice string for input size n can have length at most logarithmic in n, rather than polynomial.

Strictly contained in IC[log,poly].

If NP is contained in P/log then P = NP.
== Relations ==

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

Equivalently, P/poly is the class of decision problems solvable by a polynomial-time Turing machine that receives an 'advice string,' that depends only on the size n of the input, and that itself has size upper-bounded by a polynomial in n.

Contains BPP by the progenitor of derandomization arguments [Adl78] [KL82].  By extension, BPP/poly, BPP/mpoly, and BPP/rpoly all equal P/poly. (By contrast, there is an oracle relative to which BPP/log does not equal BPP/mlog, while BPP/mlog and BPP/rlog are not equal relative to any oracle.)

[KL82] showed that, if P/poly contains NP, then PH collapses to the second level, Σ,,2,,P.

They also showed:

If PSPACE is in P/poly then PSPACE equals Σ,,2,,P ∩ Π,,2,,P.
If EXP is in P/poly then EXP = Σ,,2,,P.

It was later shown that, if NP is contained in P/poly, then PH collapses to ZPP^NP^ [KW98] and indeed S,,2,,P [Cai01]. This seems close to optimal, since there exists an oracle relative to which the collapse cannot be improved to Δ,,2,,P [Wil85].

If NP is not contained in P/poly, then P does not equal NP.  Much of the effort toward separating P from NP is based on this observation.  However, a 'natural proof' as defined by [RR97] cannot be used to show NP is outside P/poly, if there is any pseudorandom generator in P/poly that has hardness 2^Ω(n^ε)^ for some ε>0.

If NP is contained in P/poly, then MA = AM [AKS+95]

The monotone version of P/poly is mP/poly.

P/poly has measure 0 in E with Σ,,2,,P oracle [May94b].

Strictly contains IC[log,poly] and P/log.
== Relations ==

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

The class of problems for which there exists a DiffAC^0^ function f such that the answer is "yes" on input x if and only if f(x)>0.

Equals TC^0^ and C,,=,,AC^0^ under logspace uniformity [ABL98].
== Relations ==

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

Same as k-PBP but with no width restriction.

Equals L/poly [Cob66].

Contains P-OBDD, BP,,d,,(P).
== Relations ==

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

An analog of P for Turing machines over a complex number field.

Defined in [BCS+97].

See also P,,R,,, NP,,C,,, NP,,R,,, VP,,k,,.
== Relations ==

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

Defined in [CFL+93], who also showed that PCD(log n, 1) = PSPACE.  This result was used to show that certain problems are PSPACE-hard even to approximate.

Contained in GPCD(r(n),q(n)).
== Relations ==

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

Defined in [AS98].

By definition NP = PCP(0,poly(n)).

MIP = PCP(poly(n),poly(n)).

PCP(r(n),q(n)) is contained in NTIME(2^O(r(n))^q(n) + poly(n)).

NP = PCP(log n, log n) [AS98].

In fact, NP = PCP(log n, 1) [ALM+98]!

On the other hand, if NP is contained in PCP(o(log n), o(log n)), then P = NP [FGL+91].

Also, even though there exists an oracle relative to which NP = EXP [Hel84], if we could show there exists an oracle relative to which PCP(log n, 1) = EXP, then we'd have proved P not equal to NP [For94].

Another weird oracle fact: since NP does not equal NEXP [SFM78], PCP(0,log n) does not equal PCP(0,poly(n)).  However, there exist oracles relative to which the latter inequality is false [HCC+92].
== Relations ==

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

Same as P with access to bits along a closed time curve.

Implicitly defined in [Aar05c], where it was shown that PSPACE = P,,CTC,,.

See also BQP,,CTC,,.
== Relations ==

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

Has the same relation to EXP as PP does to P.

Is not contained in P/poly [BFT98].
== Relations ==

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

Credited in [For94] to S. Arora, R. Impagliazzo, and U. Vazirani.

An interesting question is whether NP = PFCHK(log n) relative to all possible oracles.  Fortnow [For94] observes that the answer depends on what oracle access mechanism is used.
== Relations ==

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

Let Δ,,0,,P = Σ,,0,,P = Π,,0,,P = P.  Then for i>0, let

Δ,,i,,P = P with Σ,,i-1,,P oracle.
Σ,,i,,P = NP with Σ,,i-1,,P oracle.
Π,,i,,P = coNP with Σ,,i-1,,P oracle.

Then PH is the union of these classes for all nonnegative constant i.

PH can also be defined using alternating quantifiers: it's the class of problems of the form, "given an input x, does there exist a y such that for all z, there exists a w ... such that φ(x,y,z,w,...)," where y,z,w,... are polynomial-size strings and φ is a polynomial-time computable predicate.  It's not totally obvious that this is equivalent to the first definition, since the first one involves adaptive NP oracle queries and the second one doesn't, but it is.

Defined in [Sto76].

Contained in P with a PP oracle [Tod89].

Contains BPP [Lau83].

Relative to a random oracle, PH is strictly contained in PSPACE with probability 1 [Cai86].

Furthermore, there exist oracles separating any Σ,,i,,P from Σ,,i+1,,P.  On the other hand, it is unknown whether Σ,,i,,P is strictly contained in Σ,,i+1,,P relative to a random oracle with probability 1 (see [Has87]).  Book [Boo94] shows that if PH collapses relative to a random oracle with probability 1, then it collapses unrelativized.

It was shown in [CPO7] that if the NP Machine Hypothesis holds, then
.

For a compendium of problems complete for different classes of the Polynomial Hierarchy see [Sch02a] and [Sch02b].

PH is equal to the set of boolean queries recognizable by a concurent random acess machine using exponentially many processors and constant time[Imm89].

Since NP is the class of query expressible in second-order existantial logic, PH can also be defined as the query expressible in second-order logic.
== Relations ==

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

The obvious generalization of NP^cc^ and coNP^cc^ to a nondeterministic hierarchy.

It is unknown whether Σ,,2,,^cc^ equals Π,,2,,^cc^.

Defined in [BFS86], where it was also shown (among other things) that BPP^cc^ is contained in Σ,,2,,^cc^ ∩ Π,,2,,^cc^.
== Relations ==

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

(Actually, I've since been informed that PINC means "Incremental Polynomial-Time.")

The class of function problems, f:{0,1}^n^->{0,1}^m^, such that the k^th^ output bit is computable in time polynomial in n and k.

Defined in [JY88].

Contained in PIO.  This containment is strict, since if m=2^n^ (say), then computing the first bit of f(x) might be EXP-complete.
== Relations ==

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

Defined in [Yan81].

Strictly contains PINC.
== Relations ==

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

P equipped with an oracle that, given a string x, returns the length of the shortest program that outputs x.

A similar class was defined in [ABK+02], where it was also shown that P^K^ contains PSPACE.  It is not known whether P^K^ contains all of R, or even any recursive problem not in PSPACE.

See also: BPP^KT^.
== Relations ==

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

Has the same relation to PZK as SKC does to SZK.

Defined in [GP91].
== Relations ==

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

Has the same relation to L that PP has to P.

Contains BPL.

PL^PL^ = PL (see [HO02]).
== Relations ==

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

Defined in [BS90], where it was also shown that PL,,1,, is contained in PT,,1,, (and this inclusion is strict).
== Relations ==

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

Defined in [Pap90].

I believe it's the same as PPA.
== Relations ==

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

The class of TFNP function problems that are guaranteed to have a solution because of the Lovász Local Lemma.  Defined in [Pap94b].
== Relations ==

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

The subclass of TFNP function problems that are guaranteed to have a solution because of the lemma that "every finite directed acyclic graph has a sink."

More precisely, for each input, there's a finite set of solutions (i.e. strings), and a polynomial-time algorithm that computes a cost for each solution, and a neighboring solution of lower cost provided that one exists.  Then the problem is to return any solution that has cost less than or equal to all of its neighbors.  (In other words, a local optimum.)

(Note: In the Zookeeper's humble opinion, PLS should have been defined as follows: there exist polynomial-time algorithms that compute the cost of a solution, and the set of all neighbors of a given solution, not just a single solution of lower cost. Of course we'd require that every solution has only polynomially many neighbors.  The two definitions are not obviously equivalent, and it's conceivable that knowing all the neighbors would be helpful -- for example, in simulated annealing one sometimes makes uphill moves.)

(Note to Note: The equivalance of these classes was shown (though not stated explicitly) in Theorem 1 of [JPY88].)

Defined in [JPY88], [PY88].

There exists an oracle relative to which PLS is not contained in FBQP [Aar03].

Also, there exist oracles relative to which PLS is not contained in PPA [BM04], and PPA and PPP are not contained in PLS [Mor01].

Whether PLS is not in PPP relative to some oracle remains open.

[CT07] conjecture that if PPAD is in P, then PLS is in P.
== Relations ==

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

Defined in [BS90], where it was also shown that PL,,∞,, contains PT,,1,, (and this inclusion is strict).
== Relations ==

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

See Δ,,2,,P.
== Relations ==

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

Equals P with 2^k^-1 parallel queries to NP (i.e. queries that do not depend on the outcomes of previous queries) ([BH91] and [Hem89] independently).

If P^NP[1]^ = P^NP[2]^, then P^NP[1]^ = P^NP[log]^ and indeed PH collapses to Δ,,3,,P (attributed in [Har87b] to J. Kadin).
== Relations ==

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

The class of decision problems solvable by a P machine, that can make O(log n) queries to an NP oracle (where n is the length of the input).

Equals P^||NP^, the class of decision problems solvable by a P machine that can make polynomially many nonadaptive queries to an NP oracle (i.e. queries that do not depend on the outcomes of previous queries) ([BH91] and [Hem89] independently).

P^NP[log]^ is contained in PP [BHW89].

Determining the winner in an election system proposed in 1876 by Charles Dodgson (a.k.a. Lewis Carroll) has been shown to be complete for P^NP[log]^ [HHR97].

Contains P^NP[k]^ for all constants k.
== Relations ==

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

Same as P^NP[log]^, except that now log^2^ queries can be made.

The model-checking problem for a certain temporal logic is P^NP[log^2]^-complete [Sch03].

For all k, P with log^k^ adaptive queries to NP coincides with P with log^k+1^ nonadaptive queries [CS92].
== Relations ==

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

The subclass of TFNP function problems that are guaranteed to have a solution because of the lemma that "every finite graph has an even number of odd-degree nodes."

Equals PPA [Pap90].
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is 'yes' then at least 1/2 of computation paths accept.
If the answer is 'no' then less than 1/2 of computation paths accept.

Defined in [Gil77].

PP is closed under union and intersection [BRS91] (this was an open problem for 14 years).

Contains P^NP[log]^ [BHW89].

Equals PP^BPP^ [KST+89b] as well as PostBQP [Aar05b].

However, there exists an oracle relative to which PP does not contain Δ,,2,,P [Bei94].

PH is in P^PP^ [Tod89].

BQP is low for PP; i.e. PP^BQP^ = PP [FR98].

For a random oracle A, PP^A^ is strictly contained in PSPACE^A^ with probability 1 [ABF+94].

For any fixed k, there exists a language in PP that does not have circuits of size n^k^ [Vin04b].  Indeed, there exists a language in PP that does not even have quantum circuits of size n^k^ with quantum advice [Aar06].

By contrast, there exists an oracle relative to which PP has linear-size circuits [Aar06].

PP can be generalized to the counting hierarchy CH.
== Relations ==

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

Contains BQP/qpoly [Aar04b].

If PP/poly = P/poly then PP is contained in P/poly.  Indeed this is true with any syntactically defined class in place of PP.  An implication is that any unrelativized separation of BQP/qpoly from BQP/mpoly would imply that PP does not have polynomial-size circuits.
== Relations ==

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

Defined in [Pap94b]; see also [BCE+95].

The subclass of TFNP function problems that are guaranteed to have a solution because of the lemma that "all graphs of maximum degree 2
have an even number of leaves."

More precisely, there's a polynomial-time algorithm that, given any string, computes its 'neighbor' strings (of which there are at most two). Then given a leaf string (i.e. one with only one neighbor), the problem is to output another leaf string.

As an example, suppose you're given a cubic graph (one where every vertex has degree 3), and a Hamiltonian cycle H on that graph.  Then by making a sequence of modifications to H (albeit possibly exponentially many), it is always possible to find a second Hamilton cycle (see [Pap94]).  So this problem is in PPA.

Another problem in PPA is finding an Arrow-Debreu equilibrium, given the goods and utility functions of traders in a marketplace.

Contained in TFNP.

Contains PPAD.

There exist oracles relative to which PPA does not contain PLS [BM04] and PPP [BCE+95].  There also exists an oracle relative to which PPA is not contained in PPP [BCE+95].
== Relations ==

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

Defined in [Pap94b]; see also [BCE+95].

Same as PPA, except now the graph is directed, and we're asked to find either a source or a sink.

Contained in PPA and PPADS.

NASH, the problem of finding a Nash equilibrium in a normal form game of two or more players with specified utilities, is in PPAD [Pap94b], and proved to be complete for PPAD with four players in [DGP05], and shortly after extended to the case of three players [DP05] and independently [CD05].

There exists an oracle relative to which PPP is not contained in PPAD [BCE+95].
There exists an oracle relative to which PPAD is not contained in BQP [Li11].

There exists an oracle relative to which PPP is not contained in PPAD [BCE+95].
== Relations ==

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

Defined in [Pap94b]; see also [BCE+95].

Same as PPA, except now the graph is directed, and we're asked to find a sink.

Contained in PPP.

Contains PPAD.
== Relations ==

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

Defined in [Pap94b]; see also [BCE+95].

The subclass of TFNP function problems that are guaranteed to have a solution because of the Pigeonhole Principle.

More precisely, we're given a Boolean circuit, that maps n-bit strings to n-bit strings.  The problem is to return either an input that maps to 0^n^, or two inputs that map to the same output.

Contained in TFNP.

Contains PPADS.

[BCE+95] give oracles relative to which PPP is not contained in PPA and PPAD, and PPA is not contained in PPP.

[Mor01] gives an oracle relative to which PPP is not contained in PLS.

Whether PLS is not contained in PPP relative to some oracle remains open.

A level of the counting hierarchy CH.

It is not known whether there exists an oracle relative to which P^PP^ does not equal PSPACE.

Contains PP^PH^ [Tod89].

Equals P^#P^ (exercise for the visitor).

Since the permanent of a matrix is #P-complete [Val79], Toda's theorem implies that any problem in the polynomial hierarchy can be solved by computing a sequence of permanents.
== Relations ==

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

Same as IPP, except that IPP uses private coins while PPSPACE uses public coins.

Can also be defined as a probabilistic version of PSPACE.

Equals PSPACE.

Defined in [Pap83].
== Relations ==

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

Defined in [BFS86], PP^cc^ is one of two ways to define a communication complexity analogue of PP. In PP^cc^, we note that in an algorithm that uses an amount of random bits bounded by , the bias between the accept and reject probabilities can be no smaller than . Thus, in PP^cc^, the communication complexity is defined as the sum of the traditional communication complexity (the number of exchanged bits) and the log of the reciprocal of the worst-case (smallest) bias.

The difference between this class and UPP^cc^ is discussed further in [BVW07], where it is shown that PP^cc^ ⊂ UPP^cc^.

See Also: UPP^cc^.
== Relations ==

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

Thus, PQUERY = PSPACE, but PQUERY^A^ does not equal PSPACE^A^ for some oracles A.

Defined in [Kur83], where it was actually put forward as a serious argument (!!) against believing relativization results.
== Relations ==

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

Basically, the class of functions definable by recursively building up arithmetic functions: addition, multiplication, exponentiation, tetration, etc.  What's not allowed is to "diagonalize" a whole series of such functions to produce an even faster-growing one.  Thus, the Ackermann function was proposed in 1928 as an example of a recursive function that's not primitive recursive, showing that PR is strictly contained in R.

Alternatively, the PR functions are exactly those functions that can be computed via programs in any reasonable, idealized ALGOL-like programming language where only definite loops are allowed, that is, loops where the number of iterations is specified before the loop starts (so FOR-loops are okay but not WHILE- or REPEAT-loops), and recursive calls are not allowed.

An interesting difference is that PR functions can be explicitly enumerated, whereas functions in R cannot be (since otherwise the halting problem would be decidable).  That is, PR is a "syntactic" class whereas R is "semantic."

On the other hand, we can "enumerate" any RE set by a PR function in the following sense: given an input (M,k), where M is a Turing machine and k is an integer, if M halts within k steps then output M; otherwise output nothing.  Then the union of the outputs, over all possible inputs (M,k), is exactly the set of M that halt.

PR strictly contains ELEMENTARY.

An analog of P for Turing machines over a real number field.

Defined in [BCS+97].

See also P,,C,,, NP,,C,,, NP,,R,,, VP,,k,,.
== Relations ==

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

Yeah, I'm told that's what the S and K stand for.  Go figure.

The class of total function problems definable as follows: given a directed graph of indegree and outdegree at most 1, and given a source, find a sink.

Defined in [Pap90].

Equals PPADS.
== Relations ==

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

Equals NPSPACE [Sav70], AP [CKS81], IP [Sha90], and, assuming the existence of one-way functions, CZK [BGG+90].

Contains P with #P oracle.

A canonical PSPACE-complete problem is QBF.

Relative to a random oracle, PSPACE strictly contains PH with probability 1 [Cai86].

PSPACE has a complete problem that is both downward self-reducible and random self-reducible [TV02].  It is the largest class with such a complete problem.

Contained in EXP.  There exists an oracle relative to which this containment is proper [Dek76].

In descriptive complexity, PSPACE can be defined with 4 differents kind of formulae, FO() which is also FO(PFP) and SO() which is also SO(TC).

A canonical PSPACE-complete problem is Quantified Boolean Formula (QBF): Given a Boolean formula with universal and existential quantifiers, decide whether it's true or false.
== Relations ==

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

Contains QMA/qpoly [Aar06b].
== Relations ==

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

The union of PT/WK(log^k^n, n^k^) over all constants k equals NC.
== Relations ==

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

Defined in [BS90], where it was also shown that PT,,1,, contains PL,,1,, (and this inclusion is strict), and that PT,,1,, is contained in PL,,∞,, (and this inclusion is strict).
== Relations ==

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

The subclass of NPO problems that admit an approximation scheme in the following sense.  For any ε>0, there is a polynomial-time algorithm that is guaranteed to find a solution whose cost is within a 1+ε factor of the optimum cost.  (However, the exponent of the polynomial might depend strongly on ε.)

Contains FPTAS, and is contained in APX.

As an example, the Traveling Salesman Problem in the Euclidean plane is in PTAS [Aro96].

Defined in [ACG+99].
== Relations ==

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

Same as SZK, but now the two distributions must be identical, not merely statistically close.  (The "two distributions" are (1) the distribution over the verifier's view of his interaction with the prover, conditioned on the verifier's random coins, and (2) the distribution over views that the verifier can simulate without the prover's help.)

Contained in SZK.

See also: CZK.

Same as SZK, but now the two distributions must be identical, not merely statistically close.  (The "two distributions" are (1) the distribution over Arthur's view of his interaction with Merlin, conditioned on Arthur's random coins, and (2) the distribution over views that Arthur can simulate without Merlin's help.)
== Relations ==

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

In a two-party communication complexity problem, Alice and Bob have n-bit strings x and y respectively, and they wish to evaluate some Boolean function f(x,y) using as few bits of communication as possible.  P^cc^ is the class of (infinite families of) f's, such that the amount of communication needed is only O(polylog(n)), even if Alice and Bob are restricted to a deterministic protocol.

Note that all functions of the form above are solvable given  bits of communication, since no bounds are placed on the computational abilities of Alice and Bob. Thus, when discussing this class, "polynomially" is sometimes used in place of "polylogarithmically."

Is strictly contained in NP^cc^ and in BPP^cc^ because of the EQUALITY problem.

Equals NP^cc^ ∩ coNP^cc^.

Defined in [BFS86].

Like P^cc^, but with  players, where each player can see all of the other player's bits, but not their own. Intuitively, each player has their bits written on their forehead.

More formally, P,,,,^cc^ is the class of functions  where for all , , such that  is solvable in a deterministic sense by  players, each of which is aware of all inputs  other than his own, and such that  bits of communication are used.

P,,,,^cc^ is trivially contained in BPP,,,,^cc^, RP,,,,^cc^ and NP,,,,^cc^.
== Relations ==

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

The class of languages L in UP such that the mapping from an input x to the unique witness for x is a permutation of L.

Contains P.

Defined in [HT03], where it was also shown that the closure of PermUP under polynomial-time one-to-one reductions is UP.

On the other hand, they show that if PermUP = UP then E = UE.

See also: SelfNP.
== Relations ==

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

Defined by Valiant [Val03] to be "the class of physically constructible polynomial resource computers" (characterizing what "can be computed in the physical world in practice").  There he says that PhP contains P and BPP, but that it is open whether PhP contains BQP, since no scalable quantum computing proposal has been demonstrated beyond reasonable doubt.

For what it's worth, the present zookeeper has more qualms about admitting DTIME(n^1000^) into PhP than BQTIME(n^2^).  It is very possible that the total number of bits or bit tranisitions that can be witnessed by any one observer in the universe is finite.  (Recent observations of the cosmological constant combined with plausible fundamental physics yields a bound of 10^k^ with k in the low hundreds.)  In practice, less than 10^50^ bits and less than 10^80^ bit transitions are available for human use.  (This is combining the number of atoms in the Earth with the number of signals that they can exchange in a millenium.)

The present veterinarian concurs that PhP is an unhealthy animal, although it is valid to ask whether BQP is a realistic class.
== Relations ==

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

Formally, the class of decision problems solvable by a BQP machine such that

If the answer is 'yes' then the second qubit has at least 2/3 probability of being measured 1, conditioned on the first qubit having been measured 1.
If the answer is 'no' then the second qubit has at most 1/3 probability of being measured 1, conditioned on the first qubit having been measured 1.
On any input, the first qubit has a nonzero probability of being measured 1.

Defined in [Aar05b], where it is also shown that PostBQP equals PP.

[Aar05b] also gives the following alternate characterizations of PostBQP (and therefore of PP):

The quantum analogue of BPP,,path,,.
The class of problems solvable in quantum polynomial time if we allow arbitrary linear operations (not just unitary ones). Before measuring, we divide all amplitudes by a normalizing factor to make the probabilities sum to 1.
The class of problems solvable in quantum polynomial time if we take the probability of measuring a basis state with amplitude α to be not |α|^2^ but |α|^p^, where p is an even integer greater than 2.  (Again we need to divide all amplitudes by a normalizing factor to make the probabilities sum to 1.)
== Relations ==

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

Has the same relation to DSPACE(f(n)) as PP does to P.  The Turing machine has to halt on every input and every setting of the random tape.

Equals PrSPACE(f(n)) [Jun85].
== Relations ==

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

Has the same relation to DSPACE(f(n)) as PP does to P.  The Turing machine has to halt with probability 1 on every input.

Contained in DSPACE(f(n)^2^) [BCP83].

Equals Pr,,H,,SPACE(f(n)) [Jun85].
== Relations ==

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

Same as PromiseRP, but for BPP instead of RP.

Defined in [BF99].
== Relations ==

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

Same as PromiseBPP, but for BQP instead of BPP.

If PromiseBQP = PromiseP then BQP/mpoly = P/poly.

Same as PromiseBQP, but for BQP instead of BPP.
== Relations ==

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

The class of promise problems solvable by a P machine.
== Relations ==

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

The class of promise problems solvable by an RP machine. I.e., the machine must accept with probability at least 1/2 for "yes" inputs, and with probability 0 for "no" inputs, but could have acceptance probability between 0 and 1/2 for inputs that do not satisfy the promise.

Defined in [BF99], where it was also shown that BPP is in RP^PromiseRP[1]^ (i.e. with a single oracle query to PromiseRP).

Contained in PromiseBPP.
== Relations ==

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

The class of promise problems solvable by an UP machine. I.e., the nondeterministic machine must have a unique accepting path for "yes" inputs, and no accepting paths "no" inputs, but could have any number of accepting paths for inputs that do not satisfy the promise.

Although not originally stated with this notation, the main result of [VV86] is that NP is contained in RP^PromiseUP^.
== Relations ==

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

Equals P^NP[log]^ ([BH91] and [Hem89] independently).
== Relations ==

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

The class of problems solvable by a nondeterministic multitape Turing machine in linear time. Defined in [BG69], where it was shown that Q equals the class of problems solvable by a nondeterministic multitape Turing machine in exactly n steps (as opposed to O(n) steps).

Contains GCSL.
== Relations ==

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

Defined in [Moo99].

It is contained in QAC,,f,,^0^, but it is not known if it contains AC^0^. Notice that the latter containment is not obvious, since the set of gates in QAC^0^ do not allow to implement fanout in any way we may take for granted.

Contains AC^0^, and is contained in QAC,,f,,^0^.
== Relations ==

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

Same as QAC^0^, except that now Mod-m gates are also allowed.  A Mod-m gate computes whether the sum of a given set of bits is congruent to 0 modulo m, and exclusive-OR's the answer into another bit.

Defined in [Moo99].
== Relations ==

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

Same as QAC^0^[m], except that Mod-m gates are allowed for any m.

Defined in [Moo99].

[GHP00] showed that QACC^0^ equals QAC^0^[p] for any prime p.
== Relations ==

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

Same as QAC^0^, except that an additional "quantum fanout" gate is available, which CNOT's a qubit into arbitrarily many target qubits in a single step.

Defined in [Moo99], where it was also shown that QAC,,f,,^0^ =
QAC^0^[2] = QACC^0^.
== Relations ==

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

The class of decision problems for which a "yes" answer can be verified by a public-coin quantum AM protocol, as follows.  Arthur generates a uniformly random (classical) string and sends it to Merlin.  Merlin responds with a polynomial-size quantum certificate, on which Arthur can perform any BQP operation.  The completeness and soundness requirements are the same as for AM.

Defined by Marriott and Watrous [MW05].

Contains QMA and is contained in QIP[2] and BP•PP (and therefore PSPACE).
== Relations ==

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

The class of decision problems recognized by quantum context-free languages, which are defined in [MC00].  The authors also showed that QCFL does not equal CFL.
== Relations ==

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

The class of decision problems for which a "yes" answer can be verified by a quantum computer with access to a classical proof. Also known as the subclass of of QMA with classical witnesses.

Called MQA by Watrous [Wat09].

Contains MA, and is contained in QMA.

Given a black-box group G and a subgroup H, the problem of testing non-membership in H has polynomial QCMA query complexity [AK06].

See [AK06] for a "quantum oracle separation" between QCMA and QMA.  No classical oracle separation between QCMA and QMA is currently known.

The class of decision problems for which a "yes" answer can be verified by a quantum computer with access to a classical proof.
== Relations ==

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

QH,,k,, is defined to be P^NP[k]^; that is, P with k queries to an NP oracle (where k is a constant).  Then QH is the union of QH,,k,, over all nonnegative k.

QH = BH [Wag88]; thus, either both hierarchies are infinite or both collapse to some finite level.

QH,,i,, is defined to be P^NP[k]^; that is, P with k queries to an NP oracle (where k is a constant).  Then QH is the union of QH,,i,, over all nonnegative i.
== Relations ==

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

The class of decision problems such that a "yes" answer can be verified by a quantum interactive proof.  Here the verifier is a BQP (i.e. quantum polynomial-time) algorithm, while the prover has unbounded computational resources (though cannot violate the linearity of quantum mechanics). The prover and verifier exchange a polynomial number of messages, which can be quantum states.  Thus, the verifier's and prover's states may become entangled during the course of the protocol.  Given the verifier's algorithm, we require that

If the answer is "yes," then the prover can behave in such a way that the verifier accepts with probability at least 2/3.
If the answer is "no," then however the prover behaves, the verifier rejects with probability at least 2/3.

Let QIP[k] be QIP where the prover and verifier are restricted to exchanging k messages (with the prover going last).

Defined in [Wat99], where it was also shown that PSPACE is in QIP[3].

Subsequently [KW00] showed that for all k>3, QIP[k] = QIP[3] = QIP.

QIP is contained in EXP [KW00].

QIP = IP = PSPACE [JJUW09]; thus quantum computing adds no power to interactive proofs.

QIP(1) is more commonly known as QMA.

See also: QIP[2], QSZK.
== Relations ==

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

See QIP for definition.

Contains QSZK [Wat02].
== Relations ==

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

Defined in [Sch78].

See also: Q, NQL.
== Relations ==

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

The class of decision problems such that a "yes" answer can be verified by a 1-message quantum interactive proof.  That is, a BQP (i.e. quantum polynomial-time) verifier is given a quantum state (the "proof").  We require that

If the answer is "yes," then there exists a state such that verifier accepts with probability at least 2/3.
If the answer is "no," then for all states the verifier rejects with probability at least 2/3.

QMA = QIP(1).

Defined in [Wat00], where it is also shown that group non-membership is in QMA.

Based on this, [Wat00] gives an oracle relative to which MA is strictly contained in QMA.

Kitaev and Watrous (unpublished) showed QMA is contained in PP (see [MW05] for a proof).  Combining that result with [Ver92], one can obtain an oracle relative to which AM is not in QMA.

Kitaev ([KSV02], see also [AN02]) showed that the 5-Local Hamiltonians Problem is QMA-complete. Subsequently, Kempe and Regev [KR03] showed that even 3-Local Hamiltonians is QMA-complete.  A subsequent paper by Kempe, Kitaev, and Regev [KKR04], has hit rock bottom (assuming P does not equal QMA), by showing 2-local Hamiltonians QMA-complete.

Compare to NQP.

If QMA = PP then PP contains PH [Vya03].  This result uses the fact that QMA is contained in A,,0,,PP.

Approximating the ground state energy of a system composed of a line of quantum particles is QMA-complete [AGK07].

See also: QCMA, QMA/qpoly, QSZK, QMA(2), QMA-plus.

Defined in [Wat00], where it is also shown that group non-membership is in QMA.  That is: let G be a group, whose elements are represented by polynomial-size strings.  We're given a "black box" that correctly multiplies and inverts elements of G.  Then given elements g and h,,1,,,...,h,,k,,, we can verify in QMA that g is not in the subgroup generated by h,,1,,,...,h,,k,,.

Kitaev and Watrous (unpublished) showed QMA is contained in PP.  Combining that result with [Ver92], one can obtain an oracle relative to which AM is not in QMA.

[KSV02]

[AN02]

5-Local Hamiltonians.  Given an n-qubit Hilbert space, as well as a collection H,,1,,,...,H,,k,, of Hamiltonians (i.e. Hermitian positive semidefinite matrices), each of which acts on at most 5 qubits of the space.  Also given reals a,b such that b-a = Θ(1/poly(n)).  Decide whether the smallest eigenvalue of H=H,,1,,+...+H,,k,, is less than a or greater than b, promised that one of these is the case.

Subsequently Kempe and Regev [KR03] showed that even 3-Local Hamiltonians is QMA-complete.  A subsequent paper by Kempe, Kitaev, and Regev [KKR04], has hit rock bottom (assuming P does not equal QMA), by showing 2-local Hamiltonians QMA-complete.

NQP
== Relations ==

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

Same as QMA, except that now the verifier is given two polynomial-size quantum certificates, which are guaranteed to be unentangled.

Defined in [KMY01].

It was shown in [ABD+08] that a conjecture they call the Strong Amplification Conjecture implies that QMA(2) is contained in PSPACE. The authors also show that there exists no perfectly disentangler that can be used to simulate QMA(2) in QMA, though other approaches to showing QMA = QMA(2) may still exist.

It was shown in [HM13] that QMA(k) = QMA(2) for k >= 2. However we still do not know if QMA(2) = QMA and we also do not know any upper bound for QMA(2) better than NEXP.

Defined in [KMY01].  It is unknown whether QMA(k) = QMA(2) for all k>2, and also whether QMA(2) = QMA.
== Relations ==

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

Same as QMA, except now the verifier can directly obtain the probability that a given observable of the certificate state, if measured, would equal 1.  (In the usual model, by contrast, one can only sample an observable.)

Defined in [AR03], where it was also shown that QMA-plus = QMA.
== Relations ==

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

Is contained in PSPACE/poly [Aar06b].
== Relations ==

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

Same as QMA except that for a "yes" instance, there exists a state that is accepted with probability 1.

Defined in [Bra06]. It was shown there that Quantum k-SAT is QMA,,1,,-complete for any . It was also shown there that Quantum 2-SAT is in P.

This result was later improved in [GN13] where it was shown that Quantum 3-SAT is QMA,,1,,-complete.
== Relations ==

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

The class of decision problems for which a "yes" answer can be verified by a public-coin quantum MAM protocol, as follows.  Merlin sends a polynomial-size quantum state to Arthur.  Arthur then flips some classical coins (in fact, he only has to flip one without loss of generality) and sends the outcome to Merlin.  At this stage Arthur is not yet allowed to perform any quantum operations.  Merlin then sends Arthur another quantum state.  Finally, Arthur performs a BQP operation on both of the states simultaneously, and either accepts or rejects.  The completeness and soundness requirements are the same as for AM.  Also, Merlin's messages might be entangled.

Defined by Marriott and Watrous [MW05], who also showed that QMAM = QIP(3) = QIP.

Hence QMAM contains PSPACE.
== Relations ==

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

Same as QMA except that the quantum proof has O(log n) qubits instead of a polynomial number.

Equals BQP [MW05].
== Relations ==

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

The quantum generalization of MIP, and the multi-prover generalization of QIP.

A quantum multi-prover interactive proof system is the same as a classical one, except that all messages and verifier computations are quantum.  As in MIP, there is no communication among the provers; however, the provers share unlimited prior entanglement.  The number of provers and number of rounds can both be polynomial in n.

Defined in [KM02].

Shown to be equal to MIP* in [RUV12].

QMIP contains NEXP simply because MIP* contains NEXP [IV12]. Since we know that NEXP = QMIP,,ne,,, this tells us that giving the provers unlimited prior entanglement does not make the class less powerful.

Fascinatingly, no relationship between QMIP and NEXP is known.  We don't know whether allowing the provers unlimited prior entanglement makes the class more powerful, less powerful, or both!
== Relations ==

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

Same as QMIP, except that now the provers share only a polynomial number of EPR pairs, instead of an unlimited number.

Defined in [KM02], where it was also shown that QMIP,,le,, is contained in NEXP = QMIP,,ne,,.
== Relations ==

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

Same as QMIP, except that now the provers have no prior entanglement.

Defined in [KM02], where it was also shown that QMIP,,ne,, = NEXP.  Thus, QMIP,,ne,, contains QMIP,,le,,.
== Relations ==

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

Has the same relation to NC as BQP does to P.

[CW00] showed that factoring is in ZPP with a QNC oracle.

Is incomparable with BPP as far as anyone knows.

See also: RNC.
== Relations ==

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

Defined in [Spa02].

Contained in QNC,,f,,^0^.
== Relations ==

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

Same as QNC^1^, but for the exact rather than bounded-error case.

In contrast to NC^1^, it is not clear how to simulate QNC^1^ on a quantum computer in which one qubit is initialized to a pure state, and the remaining qubits are in the maximally mixed state [ASV00].

See also [MN02].
== Relations ==

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

Defined in [Spa02].

Contains QNC^0^, and is contained in QACC^0^.
== Relations ==

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

Has the same relationship to QP that E does to EXP.
== Relations ==

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

According to [BG94], Beigel and Feigenbaum and (independently) Krawczyk showed that QPSPACE is not contained in Check.
== Relations ==

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

Same as RG, except that now the verifier is a BQP machine, and can exchange polynomially many quantum messages with the competing provers.

The two provers are computationally unbounded, but must obey the laws of quantum mechanics.  Also, we can assume without loss of generality that the provers share no entanglement, because adversaries gain no advantage by sharing information.

Defined in [Gut05], where it was also shown that QRG is contained in NEXP ∩ coNEXP.

QRG trivially contains RG (and hence EXP), as well as SQG.

QRG is contained in EXP [GW07].  Hence QRG = RG = EXP and finding optimal strategies for zero-sum quantum games is no harder than finding optimal strategies for zero-sum classical games.
== Relations ==

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

The class of problems for which there exists a BQP machine M such that:

If the answer is "yes," then there exists a quantum state ρ such that for all quantum states σ, M(ρ,σ) accepts with probability at least 2/3.
If the answer is "no," then there exists a σ such that for all ρ, M(ρ,σ) rejects with probability at least 2/3.

In other words, it's the same as QRG(k) for , the class of problems that admit quantum interactive proofs with competing provers in which there's no communication from the verifier back to the provers.  QRG(1) is the quantum version of RG(1).

Defined in [JW09], where it was shown that QRG(1) is contained in PSPACE .

QRG(1) trivially contains QMA (and indeed P^QMA^).

QRG(1) is trivially contained in QRG(2) (and hence PSPACE).
== Relations ==

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

Same as QRG, except that now the verifier can exchange only two messages with each prover.  Messages are exchanged in parallel, so the verifier cannot process the answer from one prover before preparing the question for the other.  QRG(2) is the quantum version of RG(2).  See also QRG(k).

QRG(2) trivially contains RG(2) (and hence PSPACE).

QRG(2) is trivially contained in SQG (and hence PSPACE).  Hence QRG(2) = RG(2) = PSPACE and finding optimal strategies for two-turn zero-sum quantum games is no harder than finding optimal strategies for two-turn zero-sum classical games.
== Relations ==

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

Same as QRG, except that now the verifier exchanges exactly k messages with each prover where k is a polynomial-bounded function of the input length.  Messages are exchanged in parallel.  QRG(k) is the quantum version of RG(k).  By definition, QRG(poly) = QRG.  See also QRG(1) and QRG(2).

QRG(k) trivially contains RG(k) for each k (and hence PSPACE when ).  QRG(4) trivially contains SQG.

QRG(k) is trivially contained in QRG for each k (and hence EXP).

Other than these trivial bounds, very little is known of QRG(k) for intermediate values of k.  For example, does QRG(k) = RG(k) for each k?
== Relations ==

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

The class of problems for which there exists a BQP machine M such that:

If the answer is "yes," then there exists a quantum state ρ such that for all quantum states σ, M(ρ,Ï) accepts with probability at least 2/3.
If the answer is "no," then there exists a σ such that for all ρ, M(ρ,σ) rejects with probability at least 2/3.

In other words, it's the same as SQG, but without communication from the verifier back to the provers.

Contains QMA (and indeed P^QMA^), and is contained in SQG and hence EXP.
== Relations ==

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

A quantum analog of SZK (or more precisely HVSZK).

Arthur is a BQP (i.e. quantum) verifier who can exchange quantum messages with Merlin.  So Arthur and Merlin's states may become entangled during the course of the protocol.

Arthur's "view" of his interaction with Merlin is taken to be the sequence of mixed states he has, over all steps of the protocol.  The zero-knowledge requirement is that each of these states must have trace distance at most (say) 1/10 from a state that Arthur could prepare himself (in BQP), without help from Merlin.  Arthur is assumed to be an honest verifier.

Defined in [Wat02], where the following was also shown:

QSZK is contained in PSPACE.
QSZK is closed under complement.
Any protocol can be parallelized to consist of two messages, so that QSZK is in QIP[2].
One can assume without loss of generality that protocols are public-coin, as for SZK.
QSZK has a natural complete promise problem, called Quantum State Distinguishability (QSD).  We are given quantum circuits Q,,0,, and Q,,1,,.  Let ρ,,0,, and ρ,,1,, be the mixed states they produce respectively, when run on the all-0 state (and when non-output qubits are traced out).  We are promised that the trace distance between ρ,,0,, and ρ,,1,, is either at most α or at least β, where α and β are constants in [0,1] satisfying α < β^2^.  The problem is to decide which of these is the case.
== Relations ==

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

Defined in [Tur36], [Chu41], and other seminal early papers.

Equals RE ∩ coRE.

Strictly contains PR, the primitive recursive functions (see [Kle71]).
== Relations ==

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

The class of problems in NP whose witnesses are in FBQP.  For example, the set of square-free numbers is in coRBQP using only the fact that factoring is in FBQP.  (Even without a proof that the factors are prime, the factorization proves that there is a square divisor.)

Contains RP and ZBQP, and is contained in BQP and RQP.  Defined here to clarify EQP; see also ZBQP.
== Relations ==

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

A problem C is complete for RE if (1) C is in RE and (2) any problem in RE can be reduced to C by a Turing machine.

Actually there are two types of reduction: M-reductions (for many-one), in which a single instance of the original problem is mapped to an instance of C, and T-reductions (for Turing), in which an algorithm for the original problem can make arbitrarily many calls to an oracle for C.

RE-complete sets are also called creative sets for some reason.

The canonical RE-complete problem is the halting problem: i.e., given a Turing machine, does it halt when started on a blank tape?

The famous unsolvability of the halting problem [Tur36] implies that R does not equal RE.

Also, RE does not equal coRE.

RE and coRE can be generalized to the arithmetic hierarchy AH.

There are problems in RE that are neither RE-complete under T-reductions, nor in R [Fri57] [Muc56].  This is the resolution of Post's problem [Pos44].

Indeed, RE contains infinitely many nonequivalent 'T-degrees.'  (A T-degree is a class of problems, all of which can be T-reduced to one another.)  The structure of the T-degrees has been studied in more detail than you can possibly imagine [Sho99].
== Relations ==

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

Equals DSPACE(O(1)) [She59], which equals DSPACE(o(log log n)) [HLS65].

Includes, i.e., "Is the parity of the input odd?," but not "Are the majority of bits in the input 1's?"  This is sometimes expressed as "finite automata can't count."

Contained in NC^1^.

See e.g. [Koz97], [Gur89] for basic results on regular languages.

The class of decision problems solvable by deterministic finite automata (DFA's).

Equals the class solvable by nondeterministic finite automata (NDFA's).
== Relations ==

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

The class of problems solvable by a probabilistic polynomial-time verifier who can exchange a polynomial number of messages with two competing, computationally-unbounded provers -- one trying to convince the verifier that the answer is "yes," the other that the answer is "no."  Note that the verifier can hide information from the provers.  Public-coin RG amounts to SAPTIME, which equals PSPACE [Pap83].

RG is in EXP relative to any oracle [KM92]; they are equal, unrelativized [FK97b].

See also PCD, GPCD.

Contains RG[1], and is contained in QRG.
== Relations ==

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

The class of problems for which there exists a BPP machine M such that, on input x:

If the answer is 'yes,' then there exists a distribution Y such that for all distributions Z, M(x,Y,Z) accepts with probability at least 2/3.
If the answer is 'no,' then there exists a distribution Z such that for all distributions Y, M(x,Y,Z) rejects with probability at least 2/3.

In other words, it's the same as RG(k) for , the class of problems that admit interactive proofs with competing provers in which there's no communication from the verifier back to the provers.

RG(1) trivially contains S,,2,,P.  Indeed, RG(1) can be viewed as a randomized version of S,,2,,P.

RG(1) is trivially contained in RG(2) (and hence PSPACE).
== Relations ==

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

Same as RG, except that now the verifier can exchange only two messages with each prover. Messages are exchanged in parallel, so the verifier cannot process the answer from one prover before preparing the question for the other.  See also RG(k).

RG(2) is contained in PSPACE, and they are equal, unrelativized [FK97b].
== Relations ==

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

Same as RG, except that now the verifier exchanges exactly k messages with each prover where k is a polynomial-bounded function of the input length. Messages are exchanged in parallel.  By definition, RG(poly) = RG. See also RG(1) and RG(2).

Other than trivial bounds, very little is known of RG(k) for intermediate values of k. For example, does RG(k) = PSPACE for each constant ?
== Relations ==

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

Same as RG, except that now the verifier can exchange only a single round of messages with the two provers.  A round consists of private messages from the verifier to the provers, followed by private responses from the provers to the verifier.  Since the queries are private, they may as well be parallel; likewise the responses.  This makes RG[1] a symmetric class, indeed a randomized analogue of S,,2,,P.

RG[1] is contained in PSPACE, and they are equal, unrelativized [FK97b].

Contains S,,2,,P and is contained in SQG.
== Relations ==

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

Has the same relation to L as RP does to P.  The randomized machine must halt for every input and every setting of the random tape.

Contains undirected reachability (is there a path from vertex u to vertex v in an undirected graph?) [AKL+79].

Contained in RL.
== Relations ==

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

Has the same relation to BP,,H,,SPACE(f(n)) as RP does to BPP.
== Relations ==

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

Has the same relation to L as RP does to P.  The randomized machine must halt with probability 1 on any input.  It must also run in polynomial time (since otherwise we would just get
NL).

Contains R,,H,,L.

Contained in SC [Nis92].

[RTV05] give strong evidence that RL = L.
== Relations ==

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

Has the same relation to NC as RP does to P.

Contains the maximum matching problem for bipartite graphs [MVV87].

Contained in QNC.

See also: coRNC.
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is 'yes,' at least 1/2 of computation paths accept.
If the answer is 'no,' all computation paths reject.

Defined in [Gil77] (implicitly: the class VPP that is defined is equivalent to RP by running the recognizer as many times as necessary to reach probability 1/2).

Contains the problem of testing whether an integer is prime [AH87], although this problem was subsequently shown to be in P [AKS02].

For other problems in RP, see the standard text on randomized algorithms, [MR95].

Has the same p-measure as ZPP. Moreover, this measure is either zero or one. If the measure is non-zero, then ZPP = BPP = EXP [IM03].

See also: coRP, ZPP, BPP.

Defined in [Gil77].

Contains the problem of testing whether an integer is prime [AH87].
== Relations ==

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

Defined in [Mon80].

See also FPT.
== Relations ==

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

NP,,,,^cc^ is not equal to RP,,,,^cc^ for  players, for any constant  [DP08].
== Relations ==

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

The class of questions that can be answered by a QTM that accepts with probability 0 when the true answer is no, and accepts with probability at least 1/2 when the true answer is yes.  Since one of the probabilities has to vanish, RQP has the same technical caveats as EQP.

Contains ZQP and RBQP, and is contained in BQP.
== Relations ==

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

Same as RL, but for O(f(n))-space instead of logarithmic-space.  (Just as an RL machine must run in polynomial time, so an RSPACE(f(n)) machine must run in 2^O(f(n))^ time.)

Contained in NSPACE(f(n)) and BPSPACE(f(n)).

Same as RL, but for O(f(n))-space instead of logarithmic-space.
== Relations ==

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

Was shown to equal DSPACE(f(n)) [LMT97].
== Relations ==

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

Has been implicated in a collapse scandal involving AM[polylog], coNP, and EH.
== Relations ==

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

The class of decision problems for which there is a polynomial-time predicate P such that, on input x,

If the answer is 'yes,' then there exists a y such that for all z, P(x,y,z) is true.
If the answer is 'no,' then there exists a z such that for all y, P(x,y,z) is false.

Note that this differs from Σ,,2,,P in that the quantifiers in the second condition are reversed.

Less formally, S,,2,,P is the class of one-round games in which a prover and a disprover submit simultaneous moves to a deterministic, polynomial-time referee.  In Σ,,2,,P, the disprover moves first.

Defined in [RS98], where it was also shown that S,,2,,P contains MA and Δ,,2,,P.  Defined independently in [Can96].

Contained in ZPP^NP^ [Cai01].

S,,2,,-EXP•P^NP^: Don't Ask 
One of the caged classes of the Complexity Zoo.
Has been implicated in a collapse scandal involving AM[polylog], coNP, and EH.
== Relations ==

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

Defined by [BCD+89], who also showed that SAC,,k,, is closed under complement for every k>0.
== Relations ==

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

See SAC for definition.

Not closed under complement [BCD+89].
== Relations ==

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

See SAC for definition.

Equals LOGCFL/poly [Ven91].

Contained in ⊕SAC^1^ [GW96].
== Relations ==

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

Defined in [Pap83], where it was also observed that SAPTIME = PSPACE.
== Relations ==

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

The class of decision problems for which the following holds.  There exists a #P function f and an FP function g such that, for all inputs x,

If the answer is "yes" then f(x) > g(x).
If the answer is "no" then f(x) < g(x)/2.

Defined in [BGM02], where the following was also shown:

SBP contains MA, WAPP, and ∃BPP.
SBP is contained in AM and BPP,,path,,.
There exists an oracle relative to which SBP is not contained in Σ,,2,,P.
SBP is closed under union.
== Relations ==

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

Defined by Kuperberg in [Kup09], where he showed that SBQP = A,,0,,PP.
== Relations ==

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

Note that SC might be smaller than P ∩ polyL, since for the latter, it suffices to have two separate algorithms: one polynomial-time and the other polylogarithmic-space.

Deterministic context-free languages (DCFLs) can be recognized in SC [Coo79].

SC contains RL and BPL [Nis92].

SC equals DTISP(poly,polylog) by definition.

Deterministic context-free languages (DCFL's) can be recognized in SC [Coo79].
== Relations ==

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

The class of FNP search problems solvable in O(2^εn^) time for every ε>0.

Defined in [IPZ01], who also gave reductions showing that if any of k-SAT, k-colorability, k-set cover, clique, or vertex cover is in SE, then all of them are.
== Relations ==

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

The union of NE, NP^NE^, NP^NP^NE^, and so on.

Is called "strong" to contrast it with the ordinary Exponential Hierarchy EH.

Note that we would get the same class if we replaced NE by NEXP.

SEH collapses to P^NE^ [Hem89]

There exists an oracle relative to which SEH is not contained in EH [Hem89].
EH and SEH are incomparable for all anyone knows.
== Relations ==

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

The class of decision problems solvable by a k-bottleneck Turing machine. This is a machine that, after a polynomial amount of time, erases everything on the tape except for a single k-valued "safe-storage".  There's also a counter recording the number of erasings, which is in effect a non-deterministic witness.  For example, SF,,2,, contains both ⊕P and NP by using the counter as a witness.

Defined in [CF91], where it was also shown that SF,,5,, = PSPACE.

The complexity of SF,,2,,, SF,,3,,, and SF,,4,, was studied in [Ogi94] and [Her97].  The following result of those authors is among the caged beasts of the Complexity Zoo:

SF,,4,, is contained in BP ⊕P^Mod_3P ^ ⊕P ^ Mod_3P ^ ⊕P^

(Here the BP operator means that one makes the class into a bounded-error probabilistic class, the same way one makes P into BPP and NP into AM.)
== Relations ==

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

A hierarchy of generalizations of SZK, in which Arthur is allowed to gain some information from his interaction with Merlin.

Defined in [GP91].

There are several variants (which we only describe roughly), including:

SKC,,hint,,(k(n)): Hint sense.  The simulator can reproduce Arthur's view of the protocol if given a hint string of size k(n).
SKC,,hint,,(k(n)): Strict oracle sense.  The simulator can reproduce Arthur's view if allowed k(n) queries to an oracle O.
SKC,,avg,,(k(n)): Average oracle sense.  For each input, the expected number of queries the simulator makes to oracle O is at most k(n).
SKC,,ent,,(k(n)): Entropy sense.  Defined in [ABV95]. For each input, the expectation (over Arthur's random coins) of -log(P) is at most k(n), where P is the probability that the view output by the simulator equals the view resulting from the actual protocol.

See also: PKC.
== Relations ==

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

Defined in [LP82].

The undirected s-t connectivity problem (USTCON: is there a path from vertex s to vertex t in a given undirected graph?) is complete for SL, under L-reductions.

SL contains L, and is contained in NL.

It follows from [AKL+79] that SL is contained in L/poly.

[KW93] showed that SL is contained in ⊕L, as well as Mod,,k,,L for every prime k.

SL is also contained in DSPACE(log^3/2^n) [NSW92], and indeed in DSPACE(log^4/3^n) [ATW+00].

[NT95] showed that SL equals coSL, and furthermore that SL^SL^ = SL (that is, the symmetric logspace hierarchy collapses).

Reingold ultimately showed that SL = L [Rei04], even relative to an oracle. This subsumes many of the earlier results.

The reachability problem (is there a path from vertex s to vertex t?) for undirected graphs is complete for SL, under L-reduction.

The story ends with the remarkable result that SL = L (even relative to an oracle)
[Rei04].
== Relations ==

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

The parameterized version of PSPACE.

Same as FPT, except that now on input (x,k) (k a parameter), the space used must be f(k)p(|x|), where p is a polynomial.

If P = PSPACE, then FPT = SLICEWISE PSPACE.

Defined in [DF99].
== Relations ==

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

[Fag74] showed that NP is precisely the class of decision problems reducible to a graph-theoretic property expressible in second-order existential logic.

Then SNP is the class of decision problems reducible to a graph-theoretic predicate with only universal quantifiers over vertices, no existential quantifiers.  As an example, k-SAT (CNF satisfiability with at most k literals per clause, for k a constant) is in SNP.  But general SAT is not in SNP, basically because we're not allowed to say, "There exists a literal in this clause that satisfies the clause."

Contains MMSNP.

See also: MaxSNP.

[Fag74]

NP

[Pap94]

There exists a relation P(u,v) on vertices of G, such that P(u,u) is false, and for all distinct u,v either P(u,v) or P(v,u), and P(u,v) and P(v,w) implies P(u,w), and if P(u,w) and there does not exist a v for which P(u,v) and P(v,w), then there is an edge from u to w.

total order
== Relations ==

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

Second order logic is the set of FO formulae where we add quantification over second-order variables.

Every formuale is equivalent to a formulae in prenex normal form, where we first write quantification on variable on second order and then a FO-formulae in prenex normal form.

In Descriptive complexity we can see that SO is equal to PH, more precisely we have that formulae in prenex normal form where existantial and universal of second order alternate k times are the kth level of the polynomial hierarchy.

This means that SO with only existantial second-order quantification is equal to  which is NP, and with only universal quantification is equal to  which is Co-NP.
== Relations ==

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

It was shown in [Grä92] that this class is equal to P.

Those formulae can be made in prenex form where the second order is existential and the first order universal without loss of generality.
== Relations ==

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

It was shown in [Grä92] that this class is equal to NL.

Those formulaes can be made in prenex form where the second order is existential and the first order universal without loss of generalities.
== Relations ==

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

The class of decision problems for which a "yes" answer is expressible by a proposition with second-order existential quantifiers followed by a first-order formula.  See [Imm98] for a full definition.

SO-E = NP [Fag74].

Contains FO(poly(n)).
== Relations ==

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

SO[LFP] is to SO what FO[LFP] is to FO. The LFP operator can now also take second-order variable as argument.

In Descriptive complexity we can see that 
SO[LFP] is  equal to EXPTIME.
== Relations ==

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

SO[TC] is to SO what FO[TC] is to FO. The TC operator can now also take second-order variable as argument.

In Descriptive complexity we can see that :
SO[TC] is  equal to PSPACE.
== Relations ==

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

SO[] is to SO what FO[] is to FO. But we now also have second-order quantifier in the quantifier block.

In Descriptive complexity we can see that :

SO[] is  equal to PSPACE it is also another way to write SO(TC)
SO[] is equal to EXPTIME it is also another way to write SO(LFP)
== Relations ==

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

The class of problems in P for which the best parallel algorithm (using a polynomial number of processors) is faster than the best serial algorithm by a factor of Ω(n^ε^) for some ε>0.

Defined in [KRS90].

SP is also an alternate name for XP,,uniform,,
== Relations ==

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

The class of decision problems for which the number of 'yes' instances of size n is upper-bounded by a polynomial in n.  If SPARSE intersects NPC then P = NP [Mah82].

Contains TALLY.
== Relations ==

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

Has the same relation to PL as SPP does to PP.

Contains the maximum matching and perfect matching problems under a pseudorandom assumption [ARZ99].

Contains UL.

Contained in C,,=,,L and Mod,,k,,L.

Equals the set of problems low for GapL.
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is "no," then the number of accepting computation paths exactly equals the number of rejecting paths.
If the answer is "yes," then these numbers differ by 2.

(A technicality: If the total number of paths is even then the numbers can't differ by 1.)

Defined in [FFK94], where it was also shown that SPP is low for PP, C,,=,,P, Mod,,k,,P, and SPP itself.  (I.e. adding SPP as an oracle does not increase the power of these classes.)

Independently defined in [OH93], who called the class XP.

Contained in LWPP, C,,=,,P, and WPP among other classes.

Contains FewP; indeed, FewP is low for SPP, so that SPP^FewP^ = SPP [FFK94].

Contains the problem of deciding whether a graph has any nontrivial automorphisms [KST92].

Indeed, contains graph isomorphism [AK02].

Contains a whole gaggle of problems for solvable black-box groups: solvability testing, membership testing, subgroup testing, normality testing, order verification, nilpotetence testing, group isomorphism, and group intersection [Vin04]

[AK02] also showed that the Hidden Subgroup Problem for permutation groups, of interest in quantum computing, is in FP^SPP^.
== Relations ==

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

Same as QRG(2), except that now the verifier can process the yes-prover's answer before preparing the no-prover's question.

Defined in [GW05], where it was also shown that SQG contains QIP.

SQG is contained in EXP [Gut05].

SQG is trivially contained in QRG(4) (and hence EXP).

SQG trivially contains QRG(2) (and hence PSPACE).

SQG is contained in PSPACE [GW10].  Hence SQG = QRG(2) = RG(2) = PSPACE and the addition of quantum information, combined with the ability of the verifier to process the one prover's answer before preparing the other prover's question, has no effect on the complexity of two-turn (one-round) zero-sum games.

Same as QRG, except that now the verifier can exchange only a single round of quantum messages with the two provers.  The verifier may process the yes-prover's response before sending a message to the no-prover (compare with RG[1], wherein the verifier's messages must be sent to the provers in parallel).

SQG is contained in EXP [Gut05], as well as in QRG.

SQG trivially contains QS,,2,,P.
== Relations ==

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

If that sounds like a complicated definition, well, it is.  But it turns out that SZK has extremely nice properties. [Oka96] showed that:

SZK is closed under complement.  E.g., a verifier can verify in zero-knowledge that two graphs are isomorphic, not only that they aren't. 
We can assume without loss of generality that the whole interaction consists of a constant number of messages.
Amazingly, we can also assume without loss of generality that the protocol is public-coin. That is, the verifier (often called Arthur) doesn't need to hide any of his random bits, as he did in the graph nonisomorphism protocol above, but can just send them all to the prover (called Merlin)!
Finally, we can assume without loss of generality that the verifier (Arthur) is honest. A dishonest verifier would be one that tries to learn something about the problem (violating the zero-knowledge requirement) by deviating from the protocol.

Subsequently, [SV97] showed that SZK has a natural complete promise problem, called Statistical Difference (SD).  Given two polynomial-size circuits, C,,0,, and C,,1,,, let D,,0,, and D,,1,, be the distributions over their respective outputs when they're given as input a uniformly random n-bit string.  We're promised that D,,0,, and D,,1,, have trace distance either at most 1/3 or at least 2/3; the problem is to decide which is the case.

Note: The constants 1/3 and 2/3 can be amplified to 2^-poly(n)^ and 1-2^-poly(n)^ respectively.  But it is crucial that (2/3)^2^ > 1/3.

Another complete promise problem for SZK is Entropy Difference (ED) [GV99].  Here we're promised that either H(D,,0,,)>H(D,,1,,)+1 or H(D,,1,,)>H(D,,0,,)+1, where the distributions D,,0,, and D,,1,, are as above, and H denotes Shannon entropy.  The problem is to determine which is the case.

If any hard-on-average language is in SZK, then one-way functions exist [Ost91].

See general zero-knowledge (ZK).

Contains PZK and NISZK, and is contained in AM ∩ coAM, as well as CZK and QSZK.

There exists an oracle relative to which SZK is not in BQP [Aar02].

Contained in DQP [Aar02b].

The class of decision problems for which a "yes" answer can be verified by a statistical zero-knowledge proof protocol.  In such a protocol, we have a BPP (i.e. probabilistic polynomial-time) verifier, Arthur, and a prover, Merlin, who has unbounded computational resources.  By sending messages back and forth with Merlin, Arthur must become convinced (with high probability) that the answer is "yes," without learning anything else about the problem (statistically).

What does that mean?  For each choice of random coins, Arthur has a "view" of his entire interaction with Merlin, consisting of his random coins as well as all messages sent back and forth.  Then the distribution over views resulting from interaction with Merlin has to be statistically close to a distribution that Arthur could generate himself (in polynomial-time), without interacting with Merlin.  (Here "statistically close" means that, say, the trace distance is at most 1/10.)

The most famous example of such a protocol is for graph nonisomorphism. Given two graphs G and H, Arthur can pick one of the graphs (each with probability 1/2), permute its vertices randomly, send the resulting graph to Merlin, and ask, "Which graph did I start with, G or H?"  If G and H are non-isomorphic, Merlin can always answer correctly (since he can use exponential time), but if they're isomorphic, he can answer correctly with probability at most 1/2. Thus, if Merlin always gives the correct answer, Arthur becomes convinced the graphs are not isomorphic.  On the other hand, Arthur already knew which graph (G or H) he started with, so he could simulate his entire view of the interaction himself, without Merlin's help.

SZK is closed under complement.  I.e. Arthur can verify in zero-knowledge that two graphs are isomorphic, not only that they aren't. We can assume without loss of generality that the whole interaction consists of a constant number of messages.
Amazingly, we can also assume without loss of generality that the protocol is public-coin. I.e. Arthur doesn't need to hide any of his random bits, as he did in the graph nonisomorphism protocol above, but can just send them all to Merlin!
Finally, we can assume without loss of generality that the verifier (Arthur) is honest. A dishonest verifier would be one that tries to learn something about the problem (violating the zero-knowledge requirement) by deviating from the protocol.

Zero-knowledge proofs were first studied in [GMW91], [GMR89].
== Relations ==

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

Defined in [BG03], where it was also shown that SZK,,h,, = SZK.

Contains NISZK,,h,,.
== Relations ==

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

The class of languages L in NP such that the union, over all x in L, of the set of valid witnesses for x equals L itself.

Defined in [HT03], where it was shown that the closure of SelfNP under polynomial-time many-one reductions is NP.

They also show that if SelfNP = NP, then E = NE; and that SAT is contained in SelfNP.

See also: PermUP.
== Relations ==

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

The class of decision problems for which every 'yes' instance has the form 0^n^ (i.e. inputs are encoded in unary).  If TALLY intersects NPC then P = NP [Mah82].

Contained in SPARSE.
== Relations ==

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

TC^0^ contains ACC^0^, and is contained in NC^1^.

TC^0^ circuits of depth 3 are strictly more powerful than TC^0^ circuits of depth 2 [HMP+93].

TC^0^ circuits of depth 3 and quasipolynomial size can simulate all of ACC^0^ [Yao90].

There is a function in AC^0^ (explicitly given in [She08]), whose computation with TC^0^  circuits of depth 2 requires an exponential number of gates.

[NR97] give a candidate pseudorandom function family computable in TC^0^, that is secure assuming a subexponential lower bound on the hardness of factoring.  (See also [NRR01] for an improvement of this construction, as well as [Kha93].)

One implication is that, assuming such a bound, there is no natural proof in the sense of [RR97] separating TC^0^ from P/poly.  (It is important for this that a function family, and not just a candidate pseudorandom generator, is computable in TC^0^.)  Another implication is that functions in TC^0^ are likely to be difficult to learn.

The permanent of a 0-1 matrix cannot be computed in uniform TC^0^ [All99].

In a breakthrough result [Hes01] (building on [BCH86] and [CDL01]), integer division was shown to be in U,,D,,-uniform TC^0^.  Indeed division is complete for this class under AC^0^ reductions.

In a breakthrough result [Hes01] (building on [BCH86] and [CDL01]), integer division was shown to be in L-uniform TC^0^.  Indeed division is complete for this class under AC^0^ reductions.
== Relations ==

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

Can be considered as the functional analogue of NP ∩ coNP. Defined in [MP91].

Contained in FNP.

Subclasses include PPA, PPP, and PLS.
== Relations ==

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

Same as REG, except that now the inputs are trees (say, binary trees) instead of strings.  Each vertex is labeled with a symbol from a fixed alphabet.  Evaluation begins at the leaves and proceeds to the root.  The state of the finite automaton at each vertex v is a function of (1) the states at v's children (if any), and (2) the symbol at v.  The tree is in the language if and only if the automaton is in an 'accept' state at the root.

See [Koz92] for example.
== Relations ==

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

The class of languages accepted by a BQP machine subject to the constraint that at every time step t, the machine's state is exponentially close to a tree state -- that is, a state expressible by a polynomial-size tree of additions and tensor products (together with complex constants and |0> and |1> leaf nodes).

More formally, a uniform classical polynomial-time algorithm generates a sequence of gates g^(1)^, ... ,g^(p(n))^.  Each g^(t)^ can be either be selected from some finite universal basis of unitary gates (the choice turns out not to matter), or can be a 1-qubit measurement.  When we perform a measurement, the state evolves to one of two possible pure states, with the usual probabilities, rather than to a mixed state.  We require that the final gate g^(p(n))^ is a measurement of the first qubit.  If at least one intermediate state was more than distance 2^-Ω(n)^ away from the nearest state of tree size at most p(n), then the outcome of the final measurement is chosen adversarially; otherwise it is given by the usual Born probabilities.  The measurement must return 1 with probability at least 2/3 if the input is in the language, and with probability at most 1/3 otherwise.

Contains BPP, and is contained in BQP.

Defined in [Aar03b], where it was also shown that TreeBQP is
contained in the third level of PH, which might provide weak evidence that
TreeBQP does not equal BQP.
== Relations ==

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

Same as AP, except we are promised that each existential quantifier has at most one 'yes' path, and each universal quantifier has at most one 'no' path.

Contains UP.

Defined in [NR98], where it was also shown that, even though AP = PSPACE, it is unlikely that the same is true for UAP, since UAP is contained in SPP.

[CGR+04] have also shown that UAP^UAP^ = UAP, and that UAP contains Graph Isomorphism problem.

[CGR+04] have also shown that UAP^UAP^ = UAP, and that UAP contains the Graph Isomorphism problem.
== Relations ==

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

The class of problems reducible in L to the problem of whether an undirected graph has a unique connected component.

See [AG00] for more information.

Contained in SL.

See also coUCC.
== Relations ==

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

Strictly contains Deterministic CFL.  Strictly contained in CFL.
== Relations ==

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

Has the same relation to E as UP does to P.
== Relations ==

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

Has the same relation to L as UP does to P.

If UL = NL, then FNL is contained in #L [AJ93].
== Relations ==

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

Has the same relation to UL as P/poly does to P.

Equals NL/poly [RA00]. (A corollary is that UL/poly is closed under complement).

Note that in UL/poly, the witness must be unique even for bad advice. UL/mpoly (as in BQP/mpoly) is a more natural definition, but this is a moot distinction here because [RA00] show that they both equal NL/poly.
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is 'yes,' exactly one computation path accepts.
If the answer is 'no,' all computation paths reject.

Defined by [Val76].

"Worst-case" one-way functions exist if and only if P does not equal UP ([GS88] and independently [Ko85]).  "Worst-case" one-way permutations exist if and only if P does not equal UP ∩ coUP [HT03].  Note that these are weaker than the one-way functions and permutations that are needed for cryptographic applications.

There exists an oracle relative to which P is strictly contained in UP is strictly contained in NP [Rac82]; indeed, these classes are distinct with probability 1 relative to a random oracle [Bei89].

NP is contained in RP^PromiseUP^ [VV86].  On the other hand, [BBF98] give an oracle relative to which P = UP but still P does not equal NP.

UP is not known or believed to contain complete problems.  [Sip82], [HH86] give oracles relative to which UP has no complete problems.

NP is contained in RP^Promise-UP^ [VV86].  On the other hand, [BBF98] give an oracle relative to which P = UP but still P does not equal NP.
== Relations ==

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

Defined by [BFS86], UPP^cc^ is one of two communication complexity analogues of PP.
UPP^cc^ is the class of all languages defined by functions  which are computable by polylogarithmic protocols that accept with probability strictly greater than 1/2 when  and accept with probably strictly less than 1/2 otherwise. No accounting is made for how many random bits are consulted during the protocol.

See also: PP^cc^.
== Relations ==

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

The class of decision problems solvable by an NP machine such that the answer is 'yes' if and only if exactly one computation path accepts.

In contrast to UP, a machine can legally have more than one accepting path - that just means that the corresponding input is not in the language.

Defined in [BG82].

Contains coNP.
== Relations ==

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
 For k ≥ 2, VC,,k,, is the class of languages that can be verified by a circuit of depth k, with size polynomial in the witness length and instance length.

VC,,0,, ⊆ VC,,OR,, ⊆ VC,,1,, ⊆ VC,,2,, ⊆ VC,,3,, ...

Introduced in [HN06]; see there for formal definitions.
== Relations ==

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

Introduced in [HN06].

See also VC,,k,,.
== Relations ==

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

Has the same relation to VP,,k,, as NC does to P.

More formally, the class of VP,,k,, problems computable by a straight-line program of depth polylogarithmic in n.

Surprisingly, VNC,,k,, = VP,,k,, for any k [VSB+83].
== Relations ==

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

A superclass of VP,,k,, in Valiant's algebraic complexity theory, but not quite the analogue of NP.

A problem is in VNP,,k,, if there exists a polynomial p with the following properties:

p is computable in VP,,k,,; that is, by a polynomial-size straight-line program.
The inputs to p are constants c,,1,,,...,c,,m,,,e,,1,,,...,e,,h,, and indeterminates X,,1,,,...,X,,n,, over the base field k.
When p is summed over all 2^h^ possible assignments of {0,1} to each of e,,1,,,...,e,,h,,, the result is some specified polynomial q.

Originated in [Val79b].

If the field k has characteristic greater than 2, then the permanent of an n-by-n matrix of indeterminates is VNP,,k,,-complete under a type of reduction called p-projections ([Val79b]; see also [Bur00]).

A central conjecture is that for all k, VP,,k,, is not equal to VNP,,k,,.  Bürgisser [Bur00] shows that if this were false then:

If k is finite, NC^2^/poly = P/poly = NP/poly = PH/poly.
If k has characteristic 0, then assuming the Generalized Riemann Hypothesis (GRH), NC^3^/poly = P/poly = NP/poly = PH/poly, and #P/poly = FP/poly.

In both cases, PH collapses to Σ,,2,,P.
== Relations ==

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

Originated in [AM04]. See also [AM09].

Properly contains REG. Properly contained in DCFL.
== Relations ==

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

More formally, the input consists of constants c,,1,,,...,c,,m,, and indeterminates X,,1,,,...,X,,n,, over a base field k (for instance, the complex numbers or Z,,2,,).  The desired output is a collection of polynomials over the X,,i,,'s.  The complexity is the minimum number of pairwise additions, subtractions, and multiplications needed by a straight-line program to produce these polynomials.  VP,,k,, is the class of problems whose complexity is polynomial in n.  (Hence, VP,,k,, is a nonuniform class, in contrast to P,,C,, and P,,R,,.)

Originated in [Val79b]; see [Bur00] for more information.

Contained in VNP,,k,, and VQP,,k,,, and contains VNC,,k,,.

More formally, the input consists of constants c,,1,,,...,c,,m,, and indeterminates X^1^,...,X,,n,, over a base field k (for instance, the complex numbers or Z,,2,,).  The desired output is a collection of polynomials over the X,,i,,'s.  The complexity is the minimum number of pairwise additions, subtractions, and multiplications needed by a straight-line program to produce these polynomials.  VP,,k,, is the class of problems whose complexity is polynomial in n.  (Hence, VP,,k,, is a nonuniform class, in contrast to P,,C,, and P,,R,,.)
== Relations ==

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

Has the same relation to VP,,k,, as QP does to P.

Originated in [Val79b].

The determinant of an n-by-n matrix of indeterminates is VQP,,k,,-complete under a type of reduction called qp-projections (see [Bur00] for example).  It is an open problem whether the determinant is VP,,k,,-complete.
== Relations ==

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

Same as W[t], except that now the circuit depth can depend on the parameter k rather than being constant.  (The number of unbounded-fanin gates along any path to the root is still at most t.)

W^*^[1] = W[1] [DFT96], and W^*^[2] = W[2] [DF97], but the problem is open for larger t.
== Relations ==

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

The class of decision problems for which there exists a #P function f, a polynomial p, and an ε > 0, such that for all inputs x,

If the answer is "yes" then 2^p(|x|)^ ≥ f(x) > (1+ε) 2^p(|x|)-1^.
If the answer is "no" then 0 ≤ f(x) < (1-ε) 2^p(|x|)-1^.

Defined in [BGM02], where it is also shown that WAPP is contained in AWPP and SBP.
== Relations ==

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

While is a theorical programing language defined in [jon98],  is a way to define syntacticaly P and a syntactic resctriction of WHILE is exactly L. The important point is that those two languages are powerful enough to simulate all of P (and L) and when we write a program in this language we never need to prove his time (space) complexity, since the language garantee it !

In While, input are composed only of lists (in a lisp-way where a list is either an empty list or a pair of his first element and his tail) and the elements of the list and variables are only pointers to list.

A program contains global variables and procedures.

Every procedure are composed of a name, a list of argument and local variables and a list of command. The procedure doesn't return any value, they only affect global variables.
The command are: variable affectation, while loop, if/then/else and procedure call.
The empty list is considered as false and everything else as true, this is the only way to do while/if test.

There are three primitives function, tail, head, and cons(h,t), who give the first value of a list, the tail of the list and who return a list whose first element is h and the rest of the list is t and we can call defined procedure.

We can then define WHILE^/cons-rec^ which is WHILE without "cons" primitive and procedure call[#]. It is equivalent to L. The trick to do the computation in logspace is that without recursion we only need to save a fixed number of variables who are only pointers to part of the input, so they only take logspace. Since any logspace TM can avoid having a work tape by having a fixed number of reading head on his input, we can simulate logspace TM by using a variable for every reading head. (The binary string is coded as a list of () for 0 and (()) for 1, so equality can be checked trivially)

[#] in fact we only need to forbid recursive call, hence the name, but when we lose recursion we can assume there is no procedure call w.l.o.g, in fact in [jon98] WHILE is first defined without procedure call and procedure are defined later, but this presentation may be more easy to understand and at least more general.

We can then also define WHILE^rec/cons^ which is WHILE without "cons" primitive but with procedure calls, and hence recursion. It is equivalent to P. 
The trick to do a computation of a WHILE^rec/cons^ in P is to memoize the couple (global variables, input) when a procedure is called and the value of the globals variable when the procedure end, since we don't have cons, only a polynomial number of call will really be executed and we can detect loop.
Simulating P in WHILE^rec/cons^ is quite more subtle, P TM are equivalent to some counter machine wich can easily be simulated by WHILE programs with cons, and then we can simulate the cons thanks to the call stack.
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is "no," then the number of accepting computation paths exactly equals the number of rejecting paths.
If the answer is "yes," then their difference exactly equals a function f(x) computable in polynomial time (i.e. FP).

Defined in [FFK94].

Contained in C,,=,,P ∩ coC,,=,,P, as well as AWPP.

Contains SPP and LWPP.
== Relations ==

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

The union of W[t] over all t.
== Relations ==

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

Contains FPT.

Defined in [DF99], where the following is also shown:

If FPT = W[1] then NP is contained in DTIME(2^o(n)^).

W[1] can be generalized to W[t].
== Relations ==

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

See W[1] for the definition of fixed-parameter reducibility.

Defined in [DF99].

Contains W[SAT].
== Relations ==

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

See W[1] for the definition of fixed-parameter reducibility.

Defined in [DF99].

Contains W[t] for every t, and is contained in W[P].
== Relations ==

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

A generalization of W[1].

The class of decision problems of the form (x,k) (k a parameter), that are fixed-parameter reducible to the following problem, for some constant h:

Weighted Weft-t Depth-h Circuit-SAT: Given a Boolean circuit C, with a mixture of fanin-2 and unbounded-fanin gates.  The number unbounded-fanin gates along any path to the root is at most t, and the total depth (fanin-2 and unbounded-fanin) is at most h.  Does C have a satisfying assignment of Hamming weight k?

See W[1] for the definition of fixed-parameter reducibility.

Defined in [DF99].

Contained in W[SAT] and in W^*^[t].
== Relations ==

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

Same as MIP*[2,1], but with the further restriction that both provers send only a single bit to the verifier, and the verifier's output is a function of the exclusive-OR of those bits.  There should exist 0<a<b<1 such that if the answer is "yes", then for some responses of the provers the verifier accepts with probability at least b, while if the answer is "no", then for all responses of the provers the verifier accepts with probability at most a.

Defined by [CHT+04], whose motivation was a connection to the Bell and CHSH inequalities of quantum physics.

XOR-MIP*[2,1] is contained in NEXP [CHT+04].

XOR-MIP*[2,1] is contained in QIP[2] [Weh06]
== Relations ==

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

Defined in [DF99].

Contains XP,,uniform,,.

Strictly contains FPT (by diagonalization).
== Relations ==

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

Same as XP except that the algorithm used must be the same for each k (though it can take k as input).

Defined in [DF99].
== Relations ==

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

Contains ZPP by the same argument that places BPP in P/poly.

Also contains P with TALLY ∩ NP ∩ coNP oracle.

Is contained in NP ∩ coNP and YPP.
== Relations ==

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

The probabilistic analogue of YP; it is to YP what MA is to NP.  Formally, the class of decision problems for which there exists a syntactic BPP machine M such that:

For all input sizes n, there exists a polynomial-size advice string a,,n,, such that for all inputs x of size n, M(x,a,,n,,) outputs the correct answer with probability at least 2/3.
For all inputs x and advice strings a, the probability that M(x,a) outputs the incorrect answer is at most 1/3.  In other words, the sum of the probabilities of the correct answer and "I don't know" is at least 2/3.

To amplify a YPP machine, one can run it multiple times, then accept if a majority of runs accept, reject if a majority reject, and otherwise output "I don't know."

Contains BPP and YP, and is contained in MA and P/poly.
== Relations ==

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

Is to YPP as BQP is to BPP, and QMA is to MA.  The machine is now a quantum computer and the advice is a quantum state |ψ_n>.

Contains BQP and YPP, and is contained in QMA and BQP/qpoly.
== Relations ==

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

Defined as RBQP ∩ coRBQP.  Equivalently, the class of problems in NP ∩ coNP such that both positive and negative witnesses are in FBQP.

For example, the language of square-free numbers is in ZBQP, because factoring is in FBQP and a factorization can be certified in ZPP (indeed in P, by [AKS02]).

Unlike EQP or ZQP, ZBQP would generalize ZPP in practice if quantum computers existed, in the sense that it provides proven answers.

Contains ZPP and is contained in RBQP and ZQP.  Also, ZBQP^ZBQP^ = ZBQP.  Defined here to clarify EQP and ZQP.
== Relations ==

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

Often used as a shorthand for (computational zero-knowledge) CZK, but may also be used as a general paradigm encomposing various classes ranging from perfect and statistical zero-knowledge (SZK) to computational ones (CZK), and also various forms of non-interactive zero-knowledge proof systems.

Zero-knowledge proofs were introduced in [GMR89], and further studied in [GMW91], which demonstrated the wide applicability of the concept.
== Relations ==

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

Same as ZPP, but with 2^O(n)^-time instead of polynomial-time.

ZPE = EE if and only if ZPP = EXP [IKW01].
== Relations ==

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

Defined as RP ∩ coRP.

Defined as the class of problems solvable by randomized algorithms that always return the correct answer, and whose expected running time (on any input) is polynomial, in [Gil77].  (Proposition 5.5(iii) in this paper shows that the two definitions above are equivalent.)

Contains the problem of testing whether an integer is prime [SS77] [AH87].

In contrast to BPP and RP, it is not known whether showing ZPP = P requires proving superpolynomial circuit lower bounds [KI02].

There exists an oracle relative to which ZPP = EXP [Hel84a], [Hel84b], [Kur85], [Hel86].

Has the same p-measure as RP. Moreover, this measure is either zero or one. If the measure is non-zero, then ZPP = BPP = EXP [IM03].

The class of problems solvable by randomized algorithms that always return the correct answer, and whose expected running time (on any input) is polynomial.

Defined in [Gil77].

There exists an oracle relative to which ZPP = EXP [Hel84].
== Relations ==

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

Same as ZPP, but with O(f(n))-time instead of polynomial-time.

For any constructible superpolynomial f, ZPTIME(f(n)) with NP oracle is not contained in P/poly [KW98].
== Relations ==

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

The class of questions that can be answered by a QTM that answers yes, no, or "maybe".  If the correct answer is yes, then P[no] = 0, and vice-versa; and the probability of maybe is at most 1/2.  Since some of the probabilities have to vanish, ZQP has the same technical caveats as EQP.

Defined independently in [BW03] and in [Nis02].

Contains EQP and ZBQP and is contained in BQP.  Equals RQP ∩ coRQP.  There is an oracle such that ZQP^ZQP^ is larger than ZQP [BW03]; c.f. with ZBQP.
== Relations ==

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

Equals NQP [FGH+98].
== Relations ==

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

Contained in NEXP/poly (folklore result reported in [Fortnow's weblog]).

Contained in NEXP/poly (folklore result reported in [weblog]).
== Relations ==

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

Equals NL [Imm88] [Sze87].
== Relations ==

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

If NP = coNP, then any inconsistent Boolean formula of size n has a proof of inconsistency of size polynomial in n.

If NP does not equal coNP, then P does not equal NP.  But the other direction is not known.

See also: NP ∩ coNP.

Every problem in coNP has an IP (interactive proof) system, where moreover the prover can be restricted to BPP^#P^. If every problem in coNP has an interactive protocol whose rounds are bounded by a polylogarithmic function, then EH collapses to the third level [SS04].

Co-NP is equal to SO-A, the second-order queries where the second-order quantifiers are only universals.

Every problem in coNP has an IP (interactive proof) system, where moreover the prover can be restricted to BPP^#P^.
== Relations ==

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

If NP is contained in coNP/poly then PH collapses to S,,2,,P^NP^ [CCH+01].

NP^NP^NP^(coNP/poly ∩ NP)^ = NP^NP^NP^ [HNO+96]

Note: At the suggestion of Luis Antuñes, the above specimen of the Complexity Zoo has been locked in a cage.
== Relations ==

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

Equals C,,=,,P [FGH+98].
== Relations ==

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

Does not equal RE.

The problem "given a computable predicate P, is P true of all positive integers?" is coRE-complete.
== Relations ==

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

Contains the problem of whether a bipartite graph has a perfect matching [Kar86].
== Relations ==

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

Defined in [Gil77].  (This paper does not actually discuss coRP, other than implicitly mentioning that ZPP = RP ∩ co-RP.  Is there a better reference?)

Contains the problem of testing whether an integer is prime [SS77].

Defined in [Gil77].
== Relations ==

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

[Tor00] showed the following problem complete for coUCC under L reductions:

Given a colored graph G with at most two vertices having any given color, does G have any nontrivial automorphisms?
== Relations ==

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

Same as compNP but for interactive (IP) proofs instead of NP proofs.

More formally, compIP is the class of decision problems L in IP = PSPACE such that, if the answer is "yes," then that can be proven by an interactive protocol between a BPP verifier and a prover, a BPP machine with access only to an oracle for L.

Assuming NEE is not contained in BPEE, NP (and indeed NP ∩ Coh) is not contained in compIP [BG94].
== Relations ==

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

The class of decision problems L in NP such that, if the answer is "yes," then a proof can be constructed in polynomial time given access only to an oracle for L.

Contains NPC.

[BG94] show that compNP is contained in frIP, and that assuming NEE is not contained in BPEE, compNP does not equal NP.
== Relations ==

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

The class of problems L that have a decider in the following sense.  There exists a BPP machine D such that for all inputs x,

If the answer is "yes" then D^L^(x) (D with oracle for L) accepts with probability at least 2/3.
If the answer is "no" then D^A^(x) accepts with probability at most 1/3 for all oracles A.

Contains compIP [BG94] and Check [BK89].

Contained in MIP = NEXP [FRS88].

Assuming NEE is not contained in BPEE, NP (and indeed NP ∩ Coh) is not contained in frIP [BG94].
== Relations ==

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

Alternate name for k-PBP.
== Relations ==

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

See k-PBP for the definition of a classical branching program.

A quantum branching program is the natural quantum generalization: we have a quantum state in a Hilbert space of dimension k.  Each step t consists of applying a unitary matrix U^(t)^(x,,i,,): that is, U^(t)^ depends on a single bit x,,i,, of the input.  (So these are the quantum analogues of so-called oblivious branching programs.)  In the end we measure to decide whether to accept; there must be zero probability of error.

Defined in [AMP02], where it was also shown that NC^1^ is contained in 2-EQBP.

k-BQBP can be defined similarly.
== Relations ==

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

Then k-PBP is the class of decision problems solvable by a family of polynomial-size, width-k branching programs.  (A uniformity condition may also be imposed.)

k-PBP equals (nonuniform) NC^1^ for constant k at least 5 [Bar89].  On the other hand, 4-PBP is in ACC^0^ [BT88].

Contained in k-EQBP, as well as PBP.

See also BP,,d,,(P).
== Relations ==

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

Defined in [GS90].  Equals mP by definition.
== Relations ==

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

Defined in [GS90], who raise as an open problem to define a uniform version of mL.

Strictly contains mNC^1^ [GS91].

Contained in (nonuniform versions of) mNL and mcoNL.
== Relations ==

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

The class of decision problems solvable by a family of monotone NC^1^ circuits (i.e. AND and OR gates only).

A uniformity condition could also be imposed.

Defined in [GS90].

Strictly contained in mNL [KW88], and indeed in mL [GS91].

Strictly contains mTC^0^ [Yao89].
== Relations ==

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

See mP for the definition of a monotone nondeterministic Turing machine, due to [GS90].

mNL is the class of decision problems solvable by a monotone nondeterministic log-space Turing machine.

mNL does not equal mcoNL [GS90], in contrast to the case for NL and coNL.

Also, mNL strictly contains mNC^1^ [KW88].

See also: mL.
== Relations ==

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

The class of decision problems for which a 'yes' answer can be verified in mP (that is, monotone polynomial-time).  The monotonicity requirement applies only to the input bits, not to the bits that are guessed nondeterministically. So, in the corresponding circuit, one can have NOT gates so long as they depend only on the nondeterministic guess bits.

Defined in [GS90], where it was also shown that mNP is 'trivial': that is, it contains exactly the monotone problems in NP.

Strictly contains mP [Raz85].
== Relations ==

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

The definition of this class, due to [GS90], is not obvious.  First, a monotone nondeterministic Turing machine is one such that, whenever it can make a transition with a 0 on its input tape, it can also make that same transition with a 1 on its input tape. (This restriction does not apply to the work tape.)  A monotone alternating Turing machine is subject to the restriction that it can only reference an input bit x by, "there exists a z at most x," or "for all z at least x."

Then applying the result of [CKS81] that P = AL, mP is defined to be mAL: the class of decision problems solvable by a monotone alternating log-space Turing machine.

Actually there's a caveat: A monotone Turing machine or circuit can first negate the entire input, then perform a monotone computation.  That way it becomes meaningful to talk about whether a monotone complexity class is closed under complement.

Strictly contained in mNP [Raz85].

Deciding whether a bipartite graph has a perfect matching, despite being both a monotone problem and in P, requires monotone circuits of superpolynomial size [Raz85b].  Letting MONO be the class of monotone problems, it follows that mP is strictly contained in MONO ∩ P.

See also: mNC^1^, mL, mNL, mcoNL.
== Relations ==

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

The class of decision problems solvable by a nonuniform family of polynomial-size Boolean circuits with only AND and OR gates, no NOT gates.  (Or rather, following the definitions of [GS90], the entire input can be negated as long as there are no other negations.)

More straightforward to define than mP.
== Relations ==

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

The class of decision problems solvable by a family of monotone TC^0^ circuits (i.e. constant-depth, polynomial-size, AND, OR, and threshold gates, but no NOT gates).

A uniformity condition could also be imposed.

Defined in [GS90].

Strictly contained in mNC^1^ [Yao89].
== Relations ==

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

Defined in [GS90], where it was also shown that mcoNL does not equal mNL.

See also: mL.
== Relations ==

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

In contrast to L, which is contained in P, it is not known if polyL is contained in P or vice versa.  On the other hand, we do know that polyL does not equal P, since (for example) polyL does not have complete problems under many-to-one logspace reductions.
== Relations ==

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

The class of functions computable as |S|, where S is the set of output values returned by the accepting paths of an NP machine.

Defined in [KST+89], where it is also shown that span-P contains #P and OptP; and that span-P = #P if and only if UP = NP.
== Relations ==

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

A level of PH, the polynomial hierarchy.

Contains BH.

There exists an oracle relative to which Δ,,2,,P is not contained in PP [Bei94].

There exists another oracle relative to which Δ,,2,,P is contained in P/poly [BGS75], and indeed has linear-size circuits [Wil85].

There exists an oracle B for which BPP^B^ is exponentially more powerful than Δ,,2,,P^B^ [KV96].

If P = NP, then any polynomial-size circuit C can be learned in Δ,,2,,P with C oracle [Aar06].
== Relations ==

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

Complement of Σ,,2,,P.

Along with Σ,,2,,P, comprises the second level of PH, the polynomial hierarchy. For any fixed k, there is a problem in Π,,2,,P ∩ Σ,,2,,P that cannot be solved by circuits of size n^k^ [Kan82].
== Relations ==

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

Complement of Π,,2,,P.

Along with Π,,2,,P, comprises the second level of PH, the polynomial hierarchy.

[Uma98] has shown that the following problems are complete for Σ,,2,,P:

Minimum equivalent DNF.  Given a DNF formula F and integer k, is there a DNF formula equivalent to F with k or fewer occurences of literals?
Shortest implicant.  Given a formula F and integer k, is there a conjunction of k or fewer literals that implies F?  (Note that this problem cannot be Σ,,2,,P-complete for DNF formulas unless Σ,,2,,P equals βP^NP^.)

For any fixed k, there is a problem in Σ,,2,,P ∩ Π,,2,,P that cannot be solved by circuits of size n^k^ [Kan82].
== Relations ==

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

Contained in Σ,,2,,P and Π,,2,,P.

Defined in [Can96], where it was also observed that Φ,,2,,P = S,,2,,P.
== Relations ==

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

β,,k,,P is the class of decision problems solvable by a polynomial-time Turing machine that makes O(log^k^n) nondeterministic transitions, with the same acceptance mechanism as NP.  Equivalently, the machine receives a purported proof of size O(log^k^n) that the answer is 'yes.'

Then βP is the union of β,,k,,P over all constant k.

Defined in [KF84].  See also the survey [GLM96].

There exist oracles relative to which basically any consistent inclusion structure among the β,,k,,P's can be realized [BG98].

β,,2,,P contains LOGNP and LOGSNP.
== Relations ==

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

Same as BPP, except that the random bit source is biased as follows.  Each bit could depend on all the previous bits in arbitrarily complicated ways; the only promise is that the bit is 1 with probability in the range [δ,1-δ], conditioned on all previous bits.

So clearly 0-BPP = P and 1/2-BPP = BPP.

It turns out that, for any δ>0, δ-BPP = BPP [VV85], [Zuc91].
== Relations ==

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

Same as δ-BPP, but for RP instead of BPP.

For any δ>0, δ-RP = RP [VV85].
== Relations ==

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

The class of problems for which there exists a BPP machine M such that, for all inputs x,

If the answer is "yes" then there exists a y such that M(x,y) accepts.
If the answer is "no" then for all y, M(x,y) rejects.

Alternatively defined as NP^BPP^.

Contains NP and BPP, and is contained in MA and SBP.

∃BPP seems obviously equal to MA, yet [FFK+93] constructed an oracle relative to which they're unequal!  Here is the difference: if the answer is "yes," MA requires only that there exist a y such that for at least 2/3 of random strings r, M(x,y,r) accepts (where M is a P predicate).  For all other y's, the proportion of r's such that M(x,y,r) accepts can be arbitrary (say, 1/2).  For ∃BPP, by contrast, the probability that M(x,y) accepts must always be either at most 1/3 or at least 2/3, for all y's.
== Relations ==

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

Contains NP and NISZK, and is contained in the third level of PH.
== Relations ==

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

The exponential-time analogue of ⊕P.

There exists an oracle relative to which ⊕EXP = ZPP [BBF98].
== Relations ==

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

Has the same relation to L as ⊕P does to P.

Contains SL [KW93].

Solving a linear system over Z,,2,, is complete for ⊕L [Dam90].

⊕L^⊕L^ = ⊕L [HRV00].
== Relations ==

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

Has the same relation to ⊕L as P/poly does to P.

Contains NL/poly [GW96].
== Relations ==

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

The class of decision problems solvable by an NP machine such that

If the answer is 'yes,' then the number of accepting paths is odd.
If the answer is 'no,' then the number of accepting paths is even.

Defined in [PZ83].

Contains graph isomorphism; indeed, graph isomorphism is low for ⊕P [AK02].

Contains FewP [CH89].

There exists an oracle relative to which P = ⊕P but P is not equal to NP (and indeed NP = EXP) [BBF98].

Equals Mod,,2^m,,P for every positive integer m.
== Relations ==

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

Defined in [GW96], where it was also shown that ⊕SAC^1^ contains SAC^1^.
== Relations ==

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

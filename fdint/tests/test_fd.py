#
#   Copyright (c) 2015, Scott J. Maddox
#
#   This file is part of Fermi-Dirac Integrals (FDINT).
#
#   FDINT is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   FDINT is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with FDINT.  If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################
# Make sure we import the local package
import os
import sys
sys.path.insert(0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from fdint import fd, fdk, dfdk
import numpy
import unittest

RTOL = 1e-15
class TestFD(unittest.TestCase):
    
    def assertRTOL(self, a, b, RTOL):
        rerr = abs(a-b)/a
        if rerr > RTOL:
            self.fail('Outside of relative tolerance of {:g}: {:g}'
                      ''.format(RTOL, rerr))

    def test_fd_fdk2(self):
        v, e = fd.fdk2(1, 15.0)
        self.assertEqual(e, 0)
        self.assertRTOL(v,  3.894304660093270E+01, RTOL)

    def test_fd_vfdk2(self):
        v, e = fd.vfdk2(1, numpy.array([15.0]))
        self.assertEqual(e, 0)
        self.assertRTOL(v,  numpy.array([3.894304660093270E+01]), RTOL)

    def test_fd_dfdk2(self):
        v1, e1 = fd.dfdk2(1, 15.0, 1)
        self.assertEqual(e1, 0)
        v2, e2 = fd.fdk2(-1, 15.0)
        self.assertEqual(e2, 0)
        self.assertRTOL(v1, 0.5*v2, RTOL)
        
        v1, e1 = fd.dfdk2(1, 15.0, 2)
        self.assertEqual(e1, 0)
        v2, e2 = fd.fdk2(-3, 15.0)
        self.assertEqual(e2, 0)
        self.assertRTOL(v1, 0.5*-0.5*v2, RTOL)

    def test_fd_vdfdk2(self):
        v1, e1 = fd.vdfdk2(1, numpy.array([15.0]), 1)
        self.assertEqual(e1, 0)
        v2, e2 = fd.vfdk2(-1, numpy.array([15.0]))
        self.assertEqual(e2, 0)
        self.assertRTOL(v1, 0.5*v2, RTOL)
        
        v1, e1 = fd.vdfdk2(1, numpy.array([15.0]), 2)
        self.assertEqual(e1, 0)
        v2, e2 = fd.vfdk2(-3, numpy.array([15.0]))
        self.assertEqual(e2, 0)
        self.assertRTOL(v1, 0.5*-0.5*v2, RTOL)

    def test_fdk(self):
        self.assertRTOL(fdk(-4.5, -3.0),  7.240015921650838E-03, RTOL)
        self.assertRTOL(fdk(-4.5, -1.0), -2.442145618002432E-02, RTOL)
        self.assertRTOL(fdk(-4.5,  1.0),  1.647586588274429E-02, RTOL)
        self.assertRTOL(fdk(-4.5,  3.5),  1.029804636049462E-03, RTOL)
        self.assertRTOL(fdk(-4.5,  7.5), -4.060975578007697E-04, RTOL)
        self.assertRTOL(fdk(-4.5, 15.0), -2.508232176525567E-05, RTOL)
        self.assertRTOL(fdk(-4.5, 30.0), -1.990373968491516E-06, RTOL)
        self.assertRTOL(fdk(-4.5, 60.0), -1.720097159754510E-07, RTOL)
        self.assertRTOL(fdk(-3.5, -3.0), -3.545676388861523E-02, RTOL)
        self.assertRTOL(fdk(-3.5, -1.0), -2.657136470551858E-02, RTOL)
        self.assertRTOL(fdk(-3.5,  1.0),  9.517508954351293E-02, RTOL)
        self.assertRTOL(fdk(-3.5,  3.5), -1.294450181808404E-02, RTOL)
        self.assertRTOL(fdk(-3.5,  7.5), -3.613853399968076E-03, RTOL)
        self.assertRTOL(fdk(-3.5, 15.0), -4.935123501719669E-04, RTOL)
        self.assertRTOL(fdk(-3.5, 30.0), -8.248542579808003E-05, RTOL)
        self.assertRTOL(fdk(-3.5, 60.0), -1.440219364000877E-05, RTOL)
        self.assertRTOL(fdk(-2.5, -3.0),  1.024984312340880E-01, RTOL)
        self.assertRTOL(fdk(-2.5, -1.0),  3.492797177355019E-01, RTOL)
        self.assertRTOL(fdk(-2.5,  1.0),  2.502420253443888E-02, RTOL)
        self.assertRTOL(fdk(-2.5,  3.5), -1.233961959341110E-01, RTOL)
        self.assertRTOL(fdk(-2.5,  7.5), -3.760442897358426E-02, RTOL)
        self.assertRTOL(fdk(-2.5, 15.0), -1.182183957963569E-02, RTOL)
        self.assertRTOL(fdk(-2.5, 30.0), -4.085597149537218E-03, RTOL)
        self.assertRTOL(fdk(-2.5, 60.0), -1.436908659724343E-03, RTOL)
        self.assertRTOL(fdk(-1.5, -3.0), -1.647804107730068E-01, RTOL)
        self.assertRTOL(fdk(-1.5, -1.0), -8.394844152932343E-01, RTOL)
        self.assertRTOL(fdk(-1.5,  1.0), -1.580053773447138E+00, RTOL)
        self.assertRTOL(fdk(-1.5,  3.5), -1.176280028545422E+00, RTOL)
        self.assertRTOL(fdk(-1.5,  7.5), -7.505784586840675E-01, RTOL)
        self.assertRTOL(fdk(-1.5, 15.0), -5.193758746338315E-01, RTOL)
        self.assertRTOL(fdk(-1.5, 30.0), -3.656546825930124E-01, RTOL)
        self.assertRTOL(fdk(-1.5, 60.0), -2.582876225442183E-01, RTOL)
        self.assertRTOL(fdk(-0.5, -3.0),  8.525970123326887E-02, RTOL)
        self.assertRTOL(fdk(-0.5, -1.0),  5.211503831079912E-01, RTOL)
        self.assertRTOL(fdk(-0.5,  1.0),  1.820411357146962E+00, RTOL)
        self.assertRTOL(fdk(-0.5,  3.5),  3.591334824651103E+00, RTOL)
        self.assertRTOL(fdk(-0.5,  7.5),  5.432873628864860E+00, RTOL)
        self.assertRTOL(fdk(-0.5, 15.0),  7.731513057173728E+00, RTOL)
        self.assertRTOL(fdk(-0.5, 30.0),  1.094942130440661E+01, RTOL)
        self.assertRTOL(fdk(-0.5, 60.0),  1.549016158518217E+01, RTOL)
        self.assertRTOL(fdk( 0.0, -3.0),  4.858735157374205E-02, RTOL)
        self.assertRTOL(fdk( 0.0, -1.0),  3.132616875182229E-01, RTOL)
        self.assertRTOL(fdk( 0.0,  1.0),  1.313261687518223E+00, RTOL)
        self.assertRTOL(fdk( 0.0,  3.5),  3.529750418272620E+00, RTOL)
        self.assertRTOL(fdk( 0.0,  7.5),  7.500552931475361E+00, RTOL)
        self.assertRTOL(fdk( 0.0, 15.0),  1.500000030590227E+01, RTOL)
        self.assertRTOL(fdk( 0.0, 30.0),  3.000000000000009E+01, RTOL)
        self.assertRTOL(fdk( 0.0, 60.0),  6.000000000000000E+01, RTOL)
        self.assertRTOL(fdk( 0.5, -3.0),  4.336636755041557E-02, RTOL)
        self.assertRTOL(fdk( 0.5, -1.0),  2.905008961699176E-01, RTOL)
        self.assertRTOL(fdk( 0.5,  1.0),  1.396375280666564E+00, RTOL)
        self.assertRTOL(fdk( 0.5,  3.5),  4.837065897622567E+00, RTOL)
        self.assertRTOL(fdk( 0.5,  7.5),  1.399909743357599E+01, RTOL)
        self.assertRTOL(fdk( 0.5, 15.0),  3.894304660093270E+01, RTOL)
        self.assertRTOL(fdk( 0.5, 30.0),  1.096948183372665E+02, RTOL)
        self.assertRTOL(fdk( 0.5, 60.0),  3.099448732700438E+02, RTOL)
        self.assertRTOL(fdk( 1.0, -3.0),  4.918072033882423E-02, RTOL)
        self.assertRTOL(fdk( 1.0, -1.0),  3.386479964034522E-01, RTOL)
        self.assertRTOL(fdk( 1.0,  1.0),  1.806286070444774E+00, RTOL)
        self.assertRTOL(fdk( 1.0,  3.5),  7.739961645298564E+00, RTOL)
        self.assertRTOL(fdk( 1.0,  7.5),  2.976938105893487E+01, RTOL)
        self.assertRTOL(fdk( 1.0, 15.0),  1.141449337609459E+02, RTOL)
        self.assertRTOL(fdk( 1.0, 30.0),  4.516449340668481E+02, RTOL)
        self.assertRTOL(fdk( 1.0, 60.0),  1.801644934066848E+03, RTOL)
        self.assertRTOL(fdk( 1.5, -3.0),  6.561173880637544E-02, RTOL)
        self.assertRTOL(fdk( 1.5, -1.0),  4.608488062901017E-01, RTOL)
        self.assertRTOL(fdk( 1.5,  1.0),  2.661682624732004E+00, RTOL)
        self.assertRTOL(fdk( 1.5,  3.5),  1.365420168610915E+01, RTOL)
        self.assertRTOL(fdk( 1.5,  7.5),  6.833812856132876E+01, RTOL)
        self.assertRTOL(fdk( 1.5, 15.0),  3.581122477085265E+02, RTOL)
        self.assertRTOL(fdk( 1.5, 30.0),  1.985311377746038E+03, RTOL)
        self.assertRTOL(fdk( 1.5, 60.0),  1.117330291388515E+04, RTOL)
        self.assertRTOL(fdk( 2.0, -3.0),  9.896340290959225E-02, RTOL)
        self.assertRTOL(fdk( 2.0, -1.0),  7.051297585956156E-01, RTOL)
        self.assertRTOL(fdk( 2.0,  1.0),  4.328331225625401E+00, RTOL)
        self.assertRTOL(fdk( 2.0,  3.5),  2.586637394510408E+01, RTOL)
        self.assertRTOL(fdk( 2.0,  7.5),  1.653001170950006E+02, RTOL)
        self.assertRTOL(fdk( 2.0, 15.0),  1.174348022617251E+03, RTOL)
        self.assertRTOL(fdk( 2.0, 30.0),  9.098696044010894E+03, RTOL)
        self.assertRTOL(fdk( 2.0, 60.0),  7.219739208802179E+04, RTOL)
        self.assertRTOL(fdk( 2.5, -3.0),  1.647403937322051E-01, RTOL)
        self.assertRTOL(fdk( 2.5, -1.0),  1.185968175443467E+00, RTOL)
        self.assertRTOL(fdk( 2.5,  1.0),  7.626535355005596E+00, RTOL)
        self.assertRTOL(fdk( 2.5,  3.5),  5.186981146923186E+01, RTOL)
        self.assertRTOL(fdk( 2.5,  7.5),  4.158852838077063E+02, RTOL)
        self.assertRTOL(fdk( 2.5, 15.0),  3.974487881941656E+03, RTOL)
        self.assertRTOL(fdk( 2.5, 30.0),  4.292925758509993E+04, RTOL)
        self.assertRTOL(fdk( 2.5, 60.0),  4.799485008429281E+05, RTOL)
        self.assertRTOL(fdk( 3.0, -3.0),  2.978018784709205E-01, RTOL)
        self.assertRTOL(fdk( 3.0, -1.0),  2.159839661017986E+00, RTOL)
        self.assertRTOL(fdk( 3.0,  1.0),  1.438935649349364E+01, RTOL)
        self.assertRTOL(fdk( 3.0,  3.5),  1.091505015453568E+02, RTOL)
        self.assertRTOL(fdk( 3.0,  7.5),  1.079959324343085E+03, RTOL)
        self.assertRTOL(fdk( 3.0, 15.0),  1.377794488724111E+04, RTOL)
        self.assertRTOL(fdk( 3.0, 30.0),  2.069526863744442E+05, RTOL)
        self.assertRTOL(fdk( 3.0, 60.0),  3.257776652315915E+06, RTOL)
        self.assertRTOL(fdk( 3.5, -3.0),  5.778455375087482E-01, RTOL)
        self.assertRTOL(fdk( 3.5, -1.0),  4.213264071926359E+00, RTOL)
        self.assertRTOL(fdk( 3.5,  1.0),  2.883131841599375E+01, RTOL)
        self.assertRTOL(fdk( 3.5,  3.5),  2.396666058159899E+02, RTOL)
        self.assertRTOL(fdk( 3.5,  7.5),  2.880213529254126E+03, RTOL)
        self.assertRTOL(fdk( 3.5, 15.0),  4.868423690758540E+04, RTOL)
        self.assertRTOL(fdk( 3.5, 30.0),  1.014417201742514E+06, RTOL)
        self.assertRTOL(fdk( 3.5, 60.0),  2.246912083856067E+07, RTOL)
        self.assertRTOL(fdk( 4.0, -3.0),  1.193042623617263E+00, RTOL)
        self.assertRTOL(fdk( 4.0, -1.0),  8.732138288905944E+00, RTOL)
        self.assertRTOL(fdk( 4.0,  1.0),  6.096945037216665E+01, RTOL)
        self.assertRTOL(fdk( 4.0,  3.5),  5.469755138110205E+02, RTOL)
        self.assertRTOL(fdk( 4.0,  7.5),  7.862865080220864E+03, RTOL)
        self.assertRTOL(fdk( 4.0, 15.0),  1.747634735470307E+05, RTOL)
        self.assertRTOL(fdk( 4.0, 30.0),  5.039016606494085E+06, RTOL)
        self.assertRTOL(fdk( 4.0, 60.0),  1.569439504883058E+08, RTOL)
        self.assertRTOL(fdk( 4.5, -3.0),  2.603141667351258E+00, RTOL)
        self.assertRTOL(fdk( 4.5, -1.0),  1.910506806522883E+01, RTOL)
        self.assertRTOL(fdk( 4.5,  1.0),  1.354192084601931E+02, RTOL)
        self.assertRTOL(fdk( 4.5,  3.5),  1.293868145709697E+03, RTOL)
        self.assertRTOL(fdk( 4.5,  7.5),  2.192168139830375E+04, RTOL)
        self.assertRTOL(fdk( 4.5, 15.0),  6.358400491901155E+05, RTOL)
        self.assertRTOL(fdk( 4.5, 30.0),  2.530631914465860E+07, RTOL)
        self.assertRTOL(fdk( 4.5, 60.0),  1.107558362743446E+09, RTOL)
        self.assertRTOL(fdk( 5.0, -3.0),  5.969820680488160E+00, RTOL)
        self.assertRTOL(fdk( 5.0, -1.0),  4.389948426765305E+01, RTOL)
        self.assertRTOL(fdk( 5.0,  1.0),  3.146680541843087E+02, RTOL)
        self.assertRTOL(fdk( 5.0,  3.5),  3.165640736730491E+03, RTOL)
        self.assertRTOL(fdk( 5.0,  7.5),  6.231539440840174E+04, RTOL)
        self.assertRTOL(fdk( 5.0, 15.0),  2.340617854292586E+06, RTOL)
        self.assertRTOL(fdk( 5.0, 30.0),  1.282644990485829E+08, RTOL)
        self.assertRTOL(fdk( 5.0, 60.0),  7.883001082246370E+09, RTOL)
        self.assertRTOL(fdk( 5.5, -3.0),  1.432510773316834E+01, RTOL)
        self.assertRTOL(fdk( 5.5, -1.0),  1.054873701421355E+02, RTOL)
        self.assertRTOL(fdk( 5.5,  1.0),  7.624071301487685E+02, RTOL)
        self.assertRTOL(fdk( 5.5,  3.5),  7.997774066508814E+03, RTOL)
        self.assertRTOL(fdk( 5.5,  7.5),  1.804014784983563E+05, RTOL)
        self.assertRTOL(fdk( 5.5, 15.0),  8.706355279385276E+06, RTOL)
        self.assertRTOL(fdk( 5.5, 30.0),  6.552423229390368E+08, RTOL)
        self.assertRTOL(fdk( 5.5, 60.0),  5.651215902520975E+10, RTOL)
        self.assertRTOL(fdk( 6.0, -3.0),  3.583278660538172E+01, RTOL)
        self.assertRTOL(fdk( 6.0, -1.0),  2.641275790125708E+02, RTOL)
        self.assertRTOL(fdk( 6.0,  1.0),  1.920621491104163E+03, RTOL)
        self.assertRTOL(fdk( 6.0,  3.5),  2.083671641045758E+04, RTOL)
        self.assertRTOL(fdk( 6.0,  7.5),  5.314330295476191E+05, RTOL)
        self.assertRTOL(fdk( 6.0, 15.0),  3.269159748061942E+07, RTOL)
        self.assertRTOL(fdk( 6.0, 30.0),  3.370296449774471E+09, RTOL)
        self.assertRTOL(fdk( 6.0, 60.0),  4.076323551443539E+11, RTOL)
        self.assertRTOL(fdk( 6.5, -3.0),  9.313870302507033E+01, RTOL)
        self.assertRTOL(fdk( 6.5, -1.0),  6.870205993243595E+02, RTOL)
        self.assertRTOL(fdk( 6.5,  1.0),  5.017993045210247E+03, RTOL)
        self.assertRTOL(fdk( 6.5,  3.5),  5.591696834104130E+04, RTOL)
        self.assertRTOL(fdk( 6.5,  7.5),  1.592092071043047E+06, RTOL)
        self.assertRTOL(fdk( 6.5, 15.0),  1.238219532435030E+08, RTOL)
        self.assertRTOL(fdk( 6.5, 30.0),  1.744018597946511E+10, RTOL)
        self.assertRTOL(fdk( 6.5, 60.0),  2.956078846984141E+12, RTOL)
        self.assertRTOL(fdk( 7.0, -3.0),  2.508781184723398E+02, RTOL)
        self.assertRTOL(fdk( 7.0, -1.0),  1.851484886980967E+03, RTOL)
        self.assertRTOL(fdk( 7.0,  1.0),  1.356711459868958E+04, RTOL)
        self.assertRTOL(fdk( 7.0,  3.5),  1.544073285162487E+05, RTOL)
        self.assertRTOL(fdk( 7.0,  7.5),  4.848712724195143E+06, RTOL)
        self.assertRTOL(fdk( 7.0, 15.0),  4.727830603631850E+08, RTOL)
        self.assertRTOL(fdk( 7.0, 30.0),  9.073325961350024E+10, RTOL)
        self.assertRTOL(fdk( 7.0, 60.0),  2.153759508773864E+13, RTOL)
        self.assertRTOL(fdk( 7.5, -3.0),  6.986360585012507E+02, RTOL)
        self.assertRTOL(fdk( 7.5, -1.0),  5.157783274159222E+03, RTOL)
        self.assertRTOL(fdk( 7.5,  1.0),  3.788356128997377E+04, RTOL)
        self.assertRTOL(fdk( 7.5,  3.5),  4.383205315095304E+05, RTOL)
        self.assertRTOL(fdk( 7.5,  7.5),  1.500759095117367E+07, RTOL)
        self.assertRTOL(fdk( 7.5, 15.0),  1.818973214398967E+09, RTOL)
        self.assertRTOL(fdk( 7.5, 30.0),  4.743320667852189E+11, RTOL)
        self.assertRTOL(fdk( 7.5, 60.0),  1.575715160529580E+14, RTOL)
        self.assertRTOL(fdk( 8.0, -3.0),  2.007219646720646E+03, RTOL)
        self.assertRTOL(fdk( 8.0, -1.0),  1.482234071460382E+04, RTOL)
        self.assertRTOL(fdk( 8.0,  1.0),  1.090540532961069E+05, RTOL)
        self.assertRTOL(fdk( 8.0,  3.5),  1.277985060309017E+06, RTOL)
        self.assertRTOL(fdk( 8.0,  7.5),  4.720135119144394E+07, RTOL)
        self.assertRTOL(fdk( 8.0, 15.0),  7.049084121468240E+09, RTOL)
        self.assertRTOL(fdk( 8.0, 30.0),  2.490622378495212E+12, RTOL)
        self.assertRTOL(fdk( 8.0, 60.0),  1.157079836302754E+15, RTOL)
        self.assertRTOL(fdk( 8.5, -3.0),  5.938814014650166E+03, RTOL)
        self.assertRTOL(fdk( 8.5, -1.0),  4.386311784955336E+04, RTOL)
        self.assertRTOL(fdk( 8.5,  1.0),  3.231138561347001E+05, RTOL)
        self.assertRTOL(fdk( 8.5,  3.5),  3.823781896168859E+06, RTOL)
        self.assertRTOL(fdk( 8.5,  7.5),  1.508420732678749E+08, RTOL)
        self.assertRTOL(fdk( 8.5, 15.0),  2.750798130249417E+10, RTOL)
        self.assertRTOL(fdk( 8.5, 30.0),  1.313056860664467E+13, RTOL)
        self.assertRTOL(fdk( 8.5, 60.0),  8.524941900028644E+15, RTOL)
        self.assertRTOL(fdk( 9.0, -3.0),  1.806585371781600E+04, RTOL)
        self.assertRTOL(fdk( 9.0, -1.0),  1.334484320310655E+05, RTOL)
        self.assertRTOL(fdk( 9.0,  1.0),  9.839000912153142E+05, RTOL)
        self.assertRTOL(fdk( 9.0,  3.5),  1.173074963158710E+07, RTOL)
        self.assertRTOL(fdk( 9.0,  7.5),  4.897833845586907E+08, RTOL)
        self.assertRTOL(fdk( 9.0, 15.0),  1.080715538012005E+11, RTOL)
        self.assertRTOL(fdk( 9.0, 30.0),  6.948254776893934E+13, RTOL)
        self.assertRTOL(fdk( 9.0, 60.0),  6.299767361155796E+16, RTOL)
        self.assertRTOL(fdk( 9.5, -3.0),  5.642067020436533E+04, RTOL)
        self.assertRTOL(fdk( 9.5, -1.0),  4.168044535669152E+05, RTOL)
        self.assertRTOL(fdk( 9.5,  1.0),  3.074986313749142E+06, RTOL)
        self.assertRTOL(fdk( 9.5,  3.5),  3.686910477586340E+07, RTOL)
        self.assertRTOL(fdk( 9.5,  7.5),  1.615856749616024E+09, RTOL)
        self.assertRTOL(fdk( 9.5, 15.0),  4.273879330919564E+11, RTOL)
        self.assertRTOL(fdk( 9.5, 30.0),  3.689532972232714E+14, RTOL)
        self.assertRTOL(fdk( 9.5, 60.0),  4.668155109009914E+17, RTOL)
        self.assertRTOL(fdk(10.0, -3.0),  1.806629241770091E+05, RTOL)
        self.assertRTOL(fdk(10.0, -1.0),  1.334722123421517E+06, RTOL)
        self.assertRTOL(fdk(10.0,  1.0),  9.851381090333600E+06, RTOL)
        self.assertRTOL(fdk(10.0,  3.5),  1.186176377953597E+08, RTOL)
        self.assertRTOL(fdk(10.0,  7.5),  5.416646367586654E+09, RTOL)
        self.assertRTOL(fdk(10.0, 15.0),  1.701154132363905E+12, RTOL)
        self.assertRTOL(fdk(10.0, 30.0),  1.965505543248569E+15, RTOL)
        self.assertRTOL(fdk(10.0, 60.0),  3.467790683237043E+18, RTOL)
        self.assertRTOL(fdk(10.5, -3.0),  5.924272114982210E+05, RTOL)
        self.assertRTOL(fdk(10.5, -1.0),  4.376998997938984E+06, RTOL)
        self.assertRTOL(fdk(10.5,  1.0),  3.231634166275790E+07, RTOL)
        self.assertRTOL(fdk(10.5,  3.5),  3.903364896044762E+08, RTOL)
        self.assertRTOL(fdk(10.5,  7.5),  1.845016484905844E+10, RTOL)
        self.assertRTOL(fdk(10.5, 15.0),  6.814687278457835E+12, RTOL)
        self.assertRTOL(fdk(10.5, 30.0),  1.050272666569349E+16, RTOL)
        self.assertRTOL(fdk(10.5, 60.0),  2.582022264434903E+19, RTOL)


if __name__ == '__main__':
    unittest.main()
# Values from Fortran Tests:
#
#   k    x            result
# -4.5 -3.0    7.240015921650838E-03
# -4.5 -1.0   -2.442145618002432E-02
# -4.5  1.0    1.647586588274429E-02
# -4.5  3.5    1.029804636049462E-03
# -4.5  7.5   -4.060975578007697E-04
# -4.5 15.0   -2.508232176525567E-05
# -4.5 30.0   -1.990373968491516E-06
# -4.5 60.0   -1.720097159754510E-07
# -3.5 -3.0   -3.545676388861523E-02
# -3.5 -1.0   -2.657136470551858E-02
# -3.5  1.0    9.517508954351293E-02
# -3.5  3.5   -1.294450181808404E-02
# -3.5  7.5   -3.613853399968076E-03
# -3.5 15.0   -4.935123501719669E-04
# -3.5 30.0   -8.248542579808003E-05
# -3.5 60.0   -1.440219364000877E-05
# -2.5 -3.0    1.024984312340880E-01
# -2.5 -1.0    3.492797177355019E-01
# -2.5  1.0    2.502420253443888E-02
# -2.5  3.5   -1.233961959341110E-01
# -2.5  7.5   -3.760442897358426E-02
# -2.5 15.0   -1.182183957963569E-02
# -2.5 30.0   -4.085597149537218E-03
# -2.5 60.0   -1.436908659724343E-03
# -1.5 -3.0   -1.647804107730068E-01
# -1.5 -1.0   -8.394844152932343E-01
# -1.5  1.0   -1.580053773447138E+00
# -1.5  3.5   -1.176280028545422E+00
# -1.5  7.5   -7.505784586840675E-01
# -1.5 15.0   -5.193758746338315E-01
# -1.5 30.0   -3.656546825930124E-01
# -1.5 60.0   -2.582876225442183E-01
# -0.5 -3.0    8.525970123326887E-02
# -0.5 -1.0    5.211503831079912E-01
# -0.5  1.0    1.820411357146962E+00
# -0.5  3.5    3.591334824651103E+00
# -0.5  7.5    5.432873628864860E+00
# -0.5 15.0    7.731513057173728E+00
# -0.5 30.0    1.094942130440661E+01
# -0.5 60.0    1.549016158518217E+01
#  0.0 -3.0    4.858735157374205E-02
#  0.0 -1.0    3.132616875182229E-01
#  0.0  1.0    1.313261687518223E+00
#  0.0  3.5    3.529750418272620E+00
#  0.0  7.5    7.500552931475361E+00
#  0.0 15.0    1.500000030590227E+01
#  0.0 30.0    3.000000000000009E+01
#  0.0 60.0    6.000000000000000E+01
#  0.5 -3.0    4.336636755041557E-02
#  0.5 -1.0    2.905008961699176E-01
#  0.5  1.0    1.396375280666564E+00
#  0.5  3.5    4.837065897622567E+00
#  0.5  7.5    1.399909743357599E+01
#  0.5 15.0    3.894304660093270E+01
#  0.5 30.0    1.096948183372665E+02
#  0.5 60.0    3.099448732700438E+02
#  1.0 -3.0    4.918072033882423E-02
#  1.0 -1.0    3.386479964034522E-01
#  1.0  1.0    1.806286070444774E+00
#  1.0  3.5    7.739961645298564E+00
#  1.0  7.5    2.976938105893487E+01
#  1.0 15.0    1.141449337609459E+02
#  1.0 30.0    4.516449340668481E+02
#  1.0 60.0    1.801644934066848E+03
#  1.5 -3.0    6.561173880637544E-02
#  1.5 -1.0    4.608488062901017E-01
#  1.5  1.0    2.661682624732004E+00
#  1.5  3.5    1.365420168610915E+01
#  1.5  7.5    6.833812856132876E+01
#  1.5 15.0    3.581122477085265E+02
#  1.5 30.0    1.985311377746038E+03
#  1.5 60.0    1.117330291388515E+04
#  2.0 -3.0    9.896340290959225E-02
#  2.0 -1.0    7.051297585956156E-01
#  2.0  1.0    4.328331225625401E+00
#  2.0  3.5    2.586637394510408E+01
#  2.0  7.5    1.653001170950006E+02
#  2.0 15.0    1.174348022617251E+03
#  2.0 30.0    9.098696044010894E+03
#  2.0 60.0    7.219739208802179E+04
#  2.5 -3.0    1.647403937322051E-01
#  2.5 -1.0    1.185968175443467E+00
#  2.5  1.0    7.626535355005596E+00
#  2.5  3.5    5.186981146923186E+01
#  2.5  7.5    4.158852838077063E+02
#  2.5 15.0    3.974487881941656E+03
#  2.5 30.0    4.292925758509993E+04
#  2.5 60.0    4.799485008429281E+05
#  3.0 -3.0    2.978018784709205E-01
#  3.0 -1.0    2.159839661017986E+00
#  3.0  1.0    1.438935649349364E+01
#  3.0  3.5    1.091505015453568E+02
#  3.0  7.5    1.079959324343085E+03
#  3.0 15.0    1.377794488724111E+04
#  3.0 30.0    2.069526863744442E+05
#  3.0 60.0    3.257776652315915E+06
#  3.5 -3.0    5.778455375087482E-01
#  3.5 -1.0    4.213264071926359E+00
#  3.5  1.0    2.883131841599375E+01
#  3.5  3.5    2.396666058159899E+02
#  3.5  7.5    2.880213529254126E+03
#  3.5 15.0    4.868423690758540E+04
#  3.5 30.0    1.014417201742514E+06
#  3.5 60.0    2.246912083856067E+07
#  4.0 -3.0    1.193042623617263E+00
#  4.0 -1.0    8.732138288905944E+00
#  4.0  1.0    6.096945037216665E+01
#  4.0  3.5    5.469755138110205E+02
#  4.0  7.5    7.862865080220864E+03
#  4.0 15.0    1.747634735470307E+05
#  4.0 30.0    5.039016606494085E+06
#  4.0 60.0    1.569439504883058E+08
#  4.5 -3.0    2.603141667351258E+00
#  4.5 -1.0    1.910506806522883E+01
#  4.5  1.0    1.354192084601931E+02
#  4.5  3.5    1.293868145709697E+03
#  4.5  7.5    2.192168139830375E+04
#  4.5 15.0    6.358400491901155E+05
#  4.5 30.0    2.530631914465860E+07
#  4.5 60.0    1.107558362743446E+09
#  5.0 -3.0    5.969820680488160E+00
#  5.0 -1.0    4.389948426765305E+01
#  5.0  1.0    3.146680541843087E+02
#  5.0  3.5    3.165640736730491E+03
#  5.0  7.5    6.231539440840174E+04
#  5.0 15.0    2.340617854292586E+06
#  5.0 30.0    1.282644990485829E+08
#  5.0 60.0    7.883001082246370E+09
#  5.5 -3.0    1.432510773316834E+01
#  5.5 -1.0    1.054873701421355E+02
#  5.5  1.0    7.624071301487685E+02
#  5.5  3.5    7.997774066508814E+03
#  5.5  7.5    1.804014784983563E+05
#  5.5 15.0    8.706355279385276E+06
#  5.5 30.0    6.552423229390368E+08
#  5.5 60.0    5.651215902520975E+10
#  6.0 -3.0    3.583278660538172E+01
#  6.0 -1.0    2.641275790125708E+02
#  6.0  1.0    1.920621491104163E+03
#  6.0  3.5    2.083671641045758E+04
#  6.0  7.5    5.314330295476191E+05
#  6.0 15.0    3.269159748061942E+07
#  6.0 30.0    3.370296449774471E+09
#  6.0 60.0    4.076323551443539E+11
#  6.5 -3.0    9.313870302507033E+01
#  6.5 -1.0    6.870205993243595E+02
#  6.5  1.0    5.017993045210247E+03
#  6.5  3.5    5.591696834104130E+04
#  6.5  7.5    1.592092071043047E+06
#  6.5 15.0    1.238219532435030E+08
#  6.5 30.0    1.744018597946511E+10
#  6.5 60.0    2.956078846984141E+12
#  7.0 -3.0    2.508781184723398E+02
#  7.0 -1.0    1.851484886980967E+03
#  7.0  1.0    1.356711459868958E+04
#  7.0  3.5    1.544073285162487E+05
#  7.0  7.5    4.848712724195143E+06
#  7.0 15.0    4.727830603631850E+08
#  7.0 30.0    9.073325961350024E+10
#  7.0 60.0    2.153759508773864E+13
#  7.5 -3.0    6.986360585012507E+02
#  7.5 -1.0    5.157783274159222E+03
#  7.5  1.0    3.788356128997377E+04
#  7.5  3.5    4.383205315095304E+05
#  7.5  7.5    1.500759095117367E+07
#  7.5 15.0    1.818973214398967E+09
#  7.5 30.0    4.743320667852189E+11
#  7.5 60.0    1.575715160529580E+14
#  8.0 -3.0    2.007219646720646E+03
#  8.0 -1.0    1.482234071460382E+04
#  8.0  1.0    1.090540532961069E+05
#  8.0  3.5    1.277985060309017E+06
#  8.0  7.5    4.720135119144394E+07
#  8.0 15.0    7.049084121468240E+09
#  8.0 30.0    2.490622378495212E+12
#  8.0 60.0    1.157079836302754E+15
#  8.5 -3.0    5.938814014650166E+03
#  8.5 -1.0    4.386311784955336E+04
#  8.5  1.0    3.231138561347001E+05
#  8.5  3.5    3.823781896168859E+06
#  8.5  7.5    1.508420732678749E+08
#  8.5 15.0    2.750798130249417E+10
#  8.5 30.0    1.313056860664467E+13
#  8.5 60.0    8.524941900028644E+15
#  9.0 -3.0    1.806585371781600E+04
#  9.0 -1.0    1.334484320310655E+05
#  9.0  1.0    9.839000912153142E+05
#  9.0  3.5    1.173074963158710E+07
#  9.0  7.5    4.897833845586907E+08
#  9.0 15.0    1.080715538012005E+11
#  9.0 30.0    6.948254776893934E+13
#  9.0 60.0    6.299767361155796E+16
#  9.5 -3.0    5.642067020436533E+04
#  9.5 -1.0    4.168044535669152E+05
#  9.5  1.0    3.074986313749142E+06
#  9.5  3.5    3.686910477586340E+07
#  9.5  7.5    1.615856749616024E+09
#  9.5 15.0    4.273879330919564E+11
#  9.5 30.0    3.689532972232714E+14
#  9.5 60.0    4.668155109009914E+17
# 10.0 -3.0    1.806629241770091E+05
# 10.0 -1.0    1.334722123421517E+06
# 10.0  1.0    9.851381090333600E+06
# 10.0  3.5    1.186176377953597E+08
# 10.0  7.5    5.416646367586654E+09
# 10.0 15.0    1.701154132363905E+12
# 10.0 30.0    1.965505543248569E+15
# 10.0 60.0    3.467790683237043E+18
# 10.5 -3.0    5.924272114982210E+05
# 10.5 -1.0    4.376998997938984E+06
# 10.5  1.0    3.231634166275790E+07
# 10.5  3.5    3.903364896044762E+08
# 10.5  7.5    1.845016484905844E+10
# 10.5 15.0    6.814687278457835E+12
# 10.5 30.0    1.050272666569349E+16
# 10.5 60.0    2.582022264434903E+19

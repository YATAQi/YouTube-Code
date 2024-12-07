from manim import *

class V5(Scene):
    def construct(self):

        txt = MathTex(r"hello)")

class V5txt(Scene):
    def construct(self):

        txt = MathTex(r"\text{Polish Junior Mathematical Olympiad}").scale(1.6)
        txt2 = MathTex(r"\text{(2014)}").scale(1.6)

        self.play(Write(txt))
        self.wait(2)
        self.play(Unwrite(txt))
        self.play(Write(txt2))
        self.wait(2)
        self.play(Unwrite(txt2))

        txt3 = MathTex(r"1 \times 5").scale(2.4)
        txt4 = MathTex(r"1 \times 6").scale(2.4)

        self.play(Write(txt3))
        self.wait(2)
        self.play(Unwrite(txt3))
        self.play(Write(txt4))
        self.wait(2)
        self.play(Unwrite(txt4))

class V5txtB(Scene):
    def construct(self):

        txt0 = MathTex(r"\textbf{Problem: } \text{Cover the } 9 \times 9 \text{ square grid using only}")
        self.add(txt0)
        self.wait(3)
        self.remove(txt0)
        txt0b = MathTex(r"\text{tiles of size } 1 \times 5 \text{ and } 1 \times 6 \text{, or prove that it is}")
        self.add(txt0b)
        self.wait(3)
        self.remove(txt0b)
        txt0c = MathTex(r"\text{impossible to do so.}")
        self.add(txt0c)
        self.wait(3)
        self.remove(txt0c)


class V5tiles(Scene):
    def construct(self):

        s1 = Rectangle(height=7, width=7, grid_xstep=7/9, grid_ystep=7/9)
        s1.set_stroke(WHITE, width=8)
        
        s2 = Rectangle(height=7/9, width=35/9, grid_xstep=7/9)
        s2.set_fill(PURE_RED, opacity=1)
        s2.set_stroke(WHITE, width=8)

        s3 = Rectangle(height=7/9, width=14/3, grid_xstep=7/9)
        s3.set_fill(PURE_BLUE, opacity=1)
        s3.set_stroke(WHITE, width=8)
        s3.move_to(RIGHT*7/18)

        self.play(Create(s1), run_time=2)
        self.wait(5)
        self.play(Uncreate(s1))
        
        self.add(s2)
        self.wait(5)
        self.play(Transform(s2,s3))
        self.wait(5)
        self.remove(s2)
        self.wait(1)

        s2 = Rectangle(height=7/9, width=35/9, grid_xstep=7/9)
        s2.set_fill(PURE_RED, opacity=1)
        s2.set_stroke(WHITE, width=8)

        self.add(s3)
        self.wait(5)
        self.play(Transform(s3,s2))
        self.wait(5)
        self.remove(s3)

        s1b = Rectangle(height=7, width=7, grid_xstep=7/9, grid_ystep=7/9)
        s1b.set_fill(GREEN, opacity=1)
        s1b.set_stroke(WHITE, width=8)

        self.add(s1b)
        self.wait(2)
        self.remove(s1b)

class V59x9(Scene):
    def construct(self):

        l = Line([-4,0,0],[4,0,0])
        l2 = Line([-3.96,0,0],[-3.96,0.5,0])
        l3 = Line([3.96,0,0],[3.96,0.5,0])
        l.stroke_width=8
        l2.stroke_width=8
        l3.stroke_width=8

        self.play(GrowFromCenter(l))
        self.play(Create(l2), Create(l3), run_time=0.8)
        self.wait(3)
        self.play(ShrinkToCenter(l), Uncreate(l2), Uncreate(l3))

        nine = MathTex(r"9").scale(2.4)
        self.play(Write(nine))
        self.wait(2)
        self.play(Unwrite(nine))

        EO = MathTex(r"81 \text{ squares}").scale(2.4)
        self.play(Write(EO))
        self.wait(2)
        self.play(Unwrite(EO))

        eqn0 = MathTex(r"5x + 6y = 81").scale(2.4)
        eqn1 = MathTex(r"5(3) + 6(11) = 81").scale(2.4)
        self.play(Write(eqn0))
        self.wait(7)
        self.play(Transform(eqn0,eqn1))
        self.wait(3)
        self.play(Unwrite(eqn0))
        
        eqn0 = MathTex(r"5x + 6y = 81").scale(2.4)
        eqn2 = MathTex(r"5(9) + 6(6) = 81").scale(2.4)
        self.play(Write(eqn0))
        self.wait(7)
        self.play(Transform(eqn0,eqn2))
        self.wait(3)
        self.play(Unwrite(eqn0))

        eqn0 = MathTex(r"5x + 6y = 81").scale(2.4)
        eqn3 = MathTex(r"5(15) + 6(1) = 81").scale(2.4)
        self.play(Write(eqn0))
        self.wait(7)
        self.play(Transform(eqn0,eqn3))
        self.wait(3)
        self.play(Unwrite(eqn0))

class V5eqns(Scene):
    def construct(self):

        eqn1 = MathTex(r"5(3) + 6(11) = 81").scale(2.4)
        eqn1b = MathTex(r"3 + 11 = 14").scale(2.4)
        self.play(Write(eqn1))
        self.wait(3)
        self.play(Transform(eqn1,eqn1b))
        self.wait(3)
        self.play(Unwrite(eqn1))

        eqn2 = MathTex(r"5(9) + 6(6) = 81").scale(2.4)
        eqn2b = MathTex(r"9 + 6 = 15").scale(2.4)
        self.play(Write(eqn2))
        self.wait(3)
        self.play(Transform(eqn2,eqn2b))
        self.wait(3)
        self.play(Unwrite(eqn2))

        eqn3= MathTex(r"5(15) + 6(1) = 81").scale(2.4)
        eqn3b = MathTex(r"15 + 1 = 16").scale(2.4)
        self.play(Write(eqn3))
        self.wait(3)
        self.play(Transform(eqn3,eqn3b))
        self.wait(3)
        self.play(Unwrite(eqn3))

        eqn0 = MathTex(r"\text{Minimum number of tiles needed} = 14").scale(1.6)
        self.play(Write(eqn0))
        self.wait(3)
        self.play(Unwrite(eqn0))

        l = Line([-5,0,0],[5,0,0])
        l2 = Line([-4.96,0,0],[-4.96,0.5,0])
        l3 = Line([4.96,0,0],[4.96,0.5,0])
        l.stroke_width=8
        l2.stroke_width=8
        l3.stroke_width=8

        self.play(GrowFromCenter(l))
        self.play(Create(l2), Create(l3), run_time=0.8)
        self.wait(3)
        self.play(ShrinkToCenter(l), Uncreate(l2), Uncreate(l3))

        thrt = MathTex(r"13").scale(2.4)
        thrt2 = MathTex(r"13 \times 6 = 78").scale(2.4)
        self.play(Write(thrt))
        self.wait(3)
        self.play(Transform(thrt,thrt2))
        self.wait(3)
        self.play(Unwrite(thrt))

class V5atleast7(Scene):
    def construct(self):

        eqn0 = MathTex(r"\text{Number of horizontal tiles} \geq 7").scale(1.6)
        self.play(Write(eqn0))
        self.wait(3)
        self.play(Unwrite(eqn0))

        eqn1 = MathTex(r"\text{Number of vertical tiles} \geq 7").scale(1.6)
        self.play(Write(eqn1))
        self.wait(3)
        self.play(Unwrite(eqn1))

        eqn2 = MathTex(r"\text{OR}").scale(1.6)
        self.play(Write(eqn2))
        self.wait(3)
        self.play(Unwrite(eqn2))

class V5eachrow(Scene):
    def construct(self):

        txt1 = MathTex(r"\text{Maximum number of horizontal tiles per row} = 1").scale(1.2)
        txt2 = MathTex(r"\text{Maximum number of vertical tiles per column} = 1").scale(1.2)

        self.play(Write(txt1))
        self.wait(3)
        self.play(Unwrite(txt1))
        self.play(Write(txt2))
        self.wait(3)
        self.play(Unwrite(txt2))

class V5tiles2(Scene):
    def construct(self):
        
        sr1 = Rectangle(height=7/9, width=35/9, grid_xstep=7/9)
        sr1.set_fill(PURE_RED, opacity=1)
        sr1.set_stroke(WHITE, width=8)

        sb1 = Rectangle(height=7/9, width=14/3, grid_xstep=7/9)
        sb1.set_fill(PURE_BLUE, opacity=1)
        sb1.set_stroke(WHITE, width=8)
        sb1.move_to(RIGHT*7/18)

        sg = Rectangle(height=7/9, width=7/9)
        sg.set_fill(GREEN, opacity=1)
        sg.set_stroke(WHITE, width=8)
        
        self.add(sg)
        self.wait(5)
        self.play(Transform(sg,sr1))
        self.wait(5)
        self.remove(sg)
        self.wait(1)

        sg = Rectangle(height=7/9, width=7/9)
        sg.set_fill(GREEN, opacity=1)
        sg.set_stroke(WHITE, width=8)
        #s0.move_to(RIGHT*7/18)

        self.add(sg)
        self.wait(5)
        self.play(Transform(sg,sb1))
        self.wait(5)
        self.remove(sg)


        sr2 = Rectangle(height=7/9, width=35/9, grid_xstep=7/9)
        sr2.set_fill(PURE_RED, opacity=1)
        sr2.set_stroke(WHITE, width=8)
        sr2.move_to(RIGHT*7/9)


        sb2 = Rectangle(height=7/9, width=14/3, grid_xstep=7/9)
        sb2.set_fill(PURE_BLUE, opacity=1)
        sb2.set_stroke(WHITE, width=8)
        sb2.move_to(LEFT*7/6)

        sg = Rectangle(height=7/9, width=7/9)
        sg.set_fill(GREEN, opacity=1)
        sg.set_stroke(WHITE, width=8)
        
        self.add(sg)
        self.wait(5)
        self.play(Transform(sg,sr2))
        self.wait(5)
        self.remove(sg)
        self.wait(1)

        sg = Rectangle(height=7/9, width=7/9)
        sg.set_fill(GREEN, opacity=1)
        sg.set_stroke(WHITE, width=8)
        #s0.move_to(RIGHT*7/18)

        self.add(sg)
        self.wait(5)
        self.play(Transform(sg,sb2))
        self.wait(5)
        self.remove(sg)

class V5contrad(Scene):
    def construct(self):

        eqn0 = MathTex(r"\text{If we assume No. } \geq 7,").scale(1.6)
        eqn1 = MathTex(r"\text{then No. } = 9.").scale(1.6)
        eqn2 = MathTex(r"\text{As a result, No. } \leq 4.").scale(1.6)
        
        self.play(Write(eqn0))
        self.wait(3)
        self.play(Unwrite(eqn0))

        self.play(Write(eqn1))
        self.wait(3)
        self.play(Unwrite(eqn1))

        self.play(Write(eqn2))
        self.wait(3)
        self.play(Unwrite(eqn2))

        eqn3 = MathTex(r"\text{The gird can fit}").scale(1.6)
        self.play(Write(eqn3))
        self.wait(3)
        self.play(Unwrite(eqn3))

        eqn3b = MathTex(r"9+4").scale(1.6)
        eqn3c = MathTex(r"13 \text{tiles (max)}.").scale(1.6)
        self.play(Write(eqn3b))
        self.wait(3)
        self.play(Transform(eqn3b,eqn3c))
        self.wait(3)
        self.play(Unwrite(eqn3b))


        eqn4 = MathTex(r"\text{The grid requires}").scale(1.6)
        self.play(Write(eqn4))
        self.wait(3)
        self.play(Unwrite(eqn4))

        eqn4b = MathTex(r"14 \text{tiles (min).}}").scale(1.6)
        self.play(Write(eqn4b))
        self.wait(3)
        self.play(Unwrite(eqn4b))

class V5contradTWO(Scene):
    def construct(self):

        eqn3 = MathTex(r"\text{The gird can fit}").scale(1.6)
        self.play(Write(eqn3))
        self.wait(3)
        self.play(Unwrite(eqn3))

        eqn3b = MathTex(r"9+4").scale(1.6)
        eqn3c = MathTex(r"13").scale(1.6)
        self.play(Write(eqn3b))
        self.wait(3)
        self.play(Transform(eqn3b,eqn3c))
        self.wait(3)
        self.play(Unwrite(eqn3b))
        eqn3d = MathTex(r"\text{ tiles (max)}.").scale(1.6)
        self.play(Write(eqn3d))
        self.wait(3)
        self.play(Unwrite(eqn3d))

class V5lasttiles(Scene):
    def construct(self):

        txt3 = MathTex(r"1 \times 4").scale(2.4)
        txt4 = MathTex(r"1 \times 6").scale(2.4)

        self.play(Write(txt3))
        self.wait(2)
        self.play(Unwrite(txt3))
        self.play(Write(txt4))
        self.wait(2)
        self.play(Unwrite(txt4))

        sy = Rectangle(height=7/9, width=28/9, grid_xstep=7/9)
        sy.set_fill(YELLOW_C, opacity=1)
        sy.set_stroke(WHITE, width=8)

        self.add(sy)
        self.wait(10)

class V5eqnsNEW(Scene):
    def construct(self):

        eqn1 = MathTex(r"3 + 11 = 14").scale(2.4)
        self.play(Write(eqn1))
        self.wait(3)
        self.play(Unwrite(eqn1))

        eqn2 = MathTex(r"9 + 6 = 15").scale(2.4)
        self.play(Write(eqn2))
        self.wait(3)
        self.play(Unwrite(eqn2))

        eqn3 = MathTex(r"15 + 1 = 16").scale(2.4)
        self.play(Write(eqn3))
        self.wait(3)
        self.play(Unwrite(eqn3))
        
        eqn1 = MathTex(r"5(3) + 6(11) = 81").scale(2.4)
        self.play(Write(eqn1))
        self.wait(3)
        self.play(Unwrite(eqn1))

        eqn2 = MathTex(r"5(9) + 6(6) = 81").scale(2.4)
        self.play(Write(eqn2))
        self.wait(3)
        self.play(Unwrite(eqn2))

        eqn3= MathTex(r"5(15) + 6(1) = 81").scale(2.4)
        self.play(Write(eqn3))
        self.wait(3)
        self.play(Unwrite(eqn3))
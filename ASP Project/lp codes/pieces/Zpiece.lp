matrix(orient1,0,0,0,0,0;
	   orient1,1,0,0,0,0;
	   orient1,2,1,1,0,0;
	   orient1,3,0,1,1,0).
	 
matrix(orient2,0,0,0,0,0;
	   orient2,1,0,1,0,0;
	   orient2,2,1,1,0,0;
	   orient2,3,1,0,0,0).	 
	   
sframe(orient1,F) :- 
	
	frame(F,0,Xf11,Xf12,Xf13,Xf14),
	frame(F,1,Xf21,Xf22,Xf23,Xf24), 
	frame(F,2,Xf31,Xf32,Xf33,Xf34), 
	frame(F,3,Xf41,Xf42,Xf43,Xf44),
	
	matrix(orient1,0,Xm11,Xm12,Xm13,Xm14),
	matrix(orient1,1,Xm21,Xm22,Xm3,Xm24),
	matrix(orient1,2,Xm31,Xm32,Xm33,Xm34),
	matrix(orient1,3,Xm41,Xm42,Xm43,Xm44),
	
	Xf31 != Xm31, Xf32 != Xm32, Xf42 != Xm42, Xf43 != Xm43.

sframe(orient2,F) :- 

	frame(F,0,Xf11,Xf12,Xf13,Xf14),
	frame(F,1,Xf21,Xf22,Xf23,Xf24),
	frame(F,2,Xf31,Xf32,Xf33,Xf34),
	frame(F,3,Xf41,Xf42,Xf43,Xf44),
	
	matrix(orient2,0,Xm11,Xm12,Xm13,Xm14),
	matrix(orient2,1,Xm21,Xm22,Xm3,Xm24),
	matrix(orient2,2,Xm31,Xm32,Xm33,Xm34),
	matrix(orient2,3,Xm41,Xm42,Xm43,Xm44),
	Xf41 != Xm41, Xf31 != Xm31, Xf32 != Xm32, Xf22 != Xm22.
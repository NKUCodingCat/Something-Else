/*
 * File: CheckerboardKarel.java
 * ----------------------------
 * When you finish writing it, the CheckerboardKarel class should draw
 * a checkerboard using beepers, as described in Assignment 1.  You
 * should make sure that your program works for all of the sample
 * worlds supplied in the starter folder.
 */

import stanford.karel.*;

public class CheckerboardKarel extends SuperKarel {

	public void Up()
	{
		while (!facingNorth())
		{
			turnLeft();
		}
		move();
	}
	public void Down()
	{
		while (!facingSouth())
		{
			turnLeft();
		}
		move();
	}
	public void Lft()
	{
		while (!facingWest())
		{
			turnLeft();
		}
		move();
	}
	public void Rt()
	{
		while (!facingEast())
		{
			turnLeft();
		}
		move();
	}

	public void run()
	{
		/* == w
		Up();Up();Up();
		putBeeper();
		Down();Rt();
		putBeeper();
		Down();Rt();
		putBeeper();
		Up();Rt();
		putBeeper();
		Up();Rt();
		putBeeper();
		Down();Rt();
		putBeeper();
		Down();Rt();
		putBeeper();
		Up();Rt();
		putBeeper();
		Up();Rt();
		putBeeper();
		*/
		//== S ==
		/*
		Up();
		putBeeper();
		Down();Rt();
		putBeeper();
		Rt();
		putBeeper();
		Up();Rt();
		putBeeper();
		Up();
		putBeeper();
		Up();Lft();
		putBeeper();
		Lft();
		putBeeper();
		Up();Lft();
		putBeeper();
		Up();
		putBeeper();
		Up();Rt();
		putBeeper();
		Rt();
		putBeeper();
		Down();Rt();
		putBeeper();
		*/
		//==== C ===
		Rt();Rt();Rt();Rt();Rt();Rt();Rt();Rt();Up();
		putBeeper();
		Down();Lft();
		putBeeper();
		Lft();
		putBeeper();
		Lft();
		putBeeper();
		Lft();
		putBeeper();
		Lft();
		putBeeper();
		Lft();Up();
		putBeeper();
		Up();
		putBeeper();
		Up();
		putBeeper();
		Up();
		putBeeper();
		Up();
		putBeeper();
		Rt();Up();
		putBeeper();
		Rt();
		putBeeper();
		Rt();
		putBeeper();
		Rt();
		putBeeper();
		Rt();
		putBeeper();
		Rt();Down();
		putBeeper();
		
		
		
		
		//======status===========
		while (!facingWest())
		{
			turnLeft();
		}
		while(frontIsClear()){move();}
		while (!facingSouth())
		{
			turnLeft();
		}
		while(frontIsClear()){move();}
		while (!facingEast())
		{
			turnLeft();
		}
		//=======================
		
	}

}

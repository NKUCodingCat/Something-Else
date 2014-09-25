/*
 * File: StoneMasonKarel.java
 * --------------------------
 * The StoneMasonKarel subclass as it appears here does nothing.
 * When you finish writing it, it should solve the "repair the quad"
 * problem from Assignment 1.  In addition to editing the program,
 * you should be sure to edit this comment so that it no longer
 * indicates that the program does nothing.
 */

import stanford.karel.*;

public class StoneMasonKarel extends SuperKarel {
	
	
	
	
	public void run()
	{
		turnLeft();
		while (true)
		{
			
			if (frontIsClear())
			{
				move();
			}
			else
			{
				break;
			}

		}
		ppp();
		while (true)
		{
			
			move();
			if (!leftIsClear()){ppp();}
			if(!frontIsClear()){break;}
		}
		
		if (!facingWest())
		{
			while (true)
			{
				turnLeft();
				if (facingWest())
				{break;}
			}
		}
		while(frontIsClear()){move();}
		if (!facingSouth())
		{
			while (true)
			{
				turnLeft();
				if (facingSouth())
				{break;}
			}
		}
		while(frontIsClear()){move();}
		
		if (!facingEast())
		{
			while (true)
			{
				turnLeft();
				if (facingEast())
				{break;}
			}
		}
		
	}
	
	private void ppp()
	{
		//校正方向
		if (!facingEast())
		{
			while (true)
			{
				turnLeft();
				if (facingEast())
				{break;}
			}
		}
		turnLeft();turnLeft();turnLeft();
		while(true)
		{
			if (frontIsClear())
			{move();}
			else
			{break;}
		}
		turnLeft();turnLeft();
		
		while (true)
		{
			if (!beepersPresent())
			{putBeeper();}
			if (frontIsClear())
			{
				
				move();
			}
			else
			{
				break;
			}
		}
		
		turnLeft();turnLeft();turnLeft();
		//校正
		return;
	}

}

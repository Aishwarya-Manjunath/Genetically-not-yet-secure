import java.util.*;
import java.lang.Long.*;
import java.math.BigInteger;
class Crack_Java_Random{  
	private static long multiplier = 0x5DEECE66DL;
	private static long addend = 0xBL;
	private static long mask = (1L << 48) - 1;
        public static void main(String args[]){  
		Random random = new Random();
		BigInteger largeValue;
		long v1 = random.nextInt();
		long v2 = random.nextInt();
		System.out.println("v1:"+v1);
		System.out.println("v2:"+v2);
		System.out.println("mask:"+mask);
		for (int i = 0; i < 65536; i++) {
		    long act_v1 = v1 * 65536 + i;
		    long x = ((act_v1 * multiplier + addend) & mask) >>> 16;
		    if(v2<0)
		    {
			largeValue = new BigInteger(String.format("%64s", Long.toBinaryString(x)).replace(' ', '1'),2);
			x = largeValue.longValue();
		    }
		    if (x==v2) 
		    {
			System.out.println("Seed found: " + act_v1);
			System.out.println("From Random:"+"	"+"My guess:");
			long v3 = random.nextInt();
			long act_v2 = ((act_v1 * multiplier + addend) & mask);
			long next_v3 = ((act_v2 * multiplier + addend) & mask)>>>16;
			if(v3<0)
			{
			    largeValue = new BigInteger(String.format("%64s", Long.toBinaryString(next_v3)).replace(' ', '1'),2);
			    next_v3 = largeValue.longValue();
			}
			System.out.println(v3+"	"+next_v3);
			long v4 = random.nextInt();
			long act_v3 = ((act_v2 * multiplier + addend) & mask);
			long next_v4 = ((act_v3 * multiplier + addend) & mask)>>>16;
			if(v4<0)
			{
			    largeValue = new BigInteger(String.format("%64s", Long.toBinaryString(next_v4)).replace(' ', '1'),2);
			    next_v4 = largeValue.longValue();
			}
			System.out.println(v4+"	"+next_v4);
			long v5 = random.nextInt();
			long act_v4 = ((act_v3 * multiplier + addend) & mask);	
			long next_v5 = ((act_v4 * multiplier + addend) & mask)>>>16;
			if(v5<0)
			{
			    largeValue = new BigInteger(String.format("%64s", Long.toBinaryString(next_v5)).replace(' ', '1'),2);
			    next_v5 = largeValue.longValue();
	 
			}
			System.out.println(v5+"	"+next_v5);
			break;
		    }
		} 
		
        }  
}  



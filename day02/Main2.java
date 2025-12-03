import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main2 {
    public static void main(String[] args) {
        try {
            String input = readInput("day02/input.txt");
            solve1(input);
            solve2(input);
        } catch (IOException e) {
            System.err.println("Error reading input file: " + e.getMessage());
        }
    }

    public static String readInput(String fileName) throws IOException {
        StringBuilder content = new StringBuilder();

        try (BufferedReader reader = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }
        }

        return content.toString().trim(); // Remove trailing newline
    }

    public static void solve1(String input) {
        // terrible brute force solution

        String[] entries = input.split(",");
        long amount = 0L;


        for (String entry : entries) {
            String[] numbers = entry.split("-");
            String num1 = numbers[0];
            String num2 = numbers[1];

            if (num1.length() == num2.length() && num1.length() % 2 != 0) continue;

            long val1 = Long.parseLong(num1);
            long val2 = Long.parseLong(num2);

            for (long i = val1; i <= val2; i++) {
                String number = i + "";
                if (number.length() % 2 != 0) continue;

                if (number.substring(0, number.length()/2).equals(number.substring(number.length()/2))) {
                    amount += i;
                }
            }

        }

        System.out.println(amount);
    }

    public static void solve2(String input) {
        // terrible brute force solution

        String[] entries = input.split(",");
        BigInteger amount = BigInteger.valueOf(0L);


        for (String entry : entries) {
            String[] numbers = entry.split("-");
            String num1 = numbers[0];
            String num2 = numbers[1];

            BigInteger val1 = new BigInteger(num1);
            BigInteger val2 = new BigInteger(num2);

            for (BigInteger i = val1; i.compareTo(val2) <= 0; i = i.add(BigInteger.ONE)) {
                String number = i.toString();
                if (checkSequence(number)) {
                    amount = amount.add(i);
                }
            }

        }

        System.out.println(amount);
    }

    static boolean checkSequence(String string) {
        int n = string.length();
        if (n < 2) return false;
        List<Integer> divisors = getDivisors(n);

        for (Integer divisor : divisors) {  // check all splits of substrings.
            boolean sequence = true;

            for (int l = 0; l + divisor < n; l+=divisor) {
                int mid = l+divisor;
                int end = l+divisor*2;

                if (!string.substring(l, mid).equals(string.substring(mid, end))) {
                    sequence = false;
                }
            }

            if (sequence) return true;
        }


        return false;
    }

    static List<Integer> getDivisors(int n) {
        List<Integer> divisors = new ArrayList<>();

        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                divisors.add(i);

                if (i != n / i && n / i != n) {   // faster method to only iterate until Math.sqrt(n)

                    divisors.add(n / i);
                }
            }
        }

        return divisors;
    }
}



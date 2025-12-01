import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Collectors;

public class Main {
    public static void main(String[] args) {
        try {
            String input = readInput("day01/input.txt");
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
        String[] lines = input.split("\\n");
        String regex = "(\\w)(\\d+)";
        Pattern pattern = Pattern.compile(regex);
        int dial = 50;
        long res = 0;

        for (String s : lines) {
            Matcher matcher = pattern.matcher(s);

            if (matcher.matches()) {
                String letter = matcher.group(1);
                String digit = matcher.group(2);
                int value = Integer.parseInt(digit);

                if (letter.equals("R")) {
                    dial += value;
                    dial %= 100;
                } else {
                    dial -= value;
                    dial %= 100;
                }
            }
            if (dial == 0) {
                res++;
            }
        }

        System.out.println(res);
    }

    public static void solve2(String input) {
        String[] lines = input.split("\\n");
        String regex = "(\\w)(\\d+)";
        Pattern pattern = Pattern.compile(regex);
        int dial = 50;
        long res = 0;
        boolean prev_was_zero = false;

        for (String s : lines) {
            Matcher matcher = pattern.matcher(s);

            if (matcher.matches()) {
                String letter = matcher.group(1);
                String digit = matcher.group(2);
                int value = Integer.parseInt(digit);

                res +=  value/100;
                value %= 100;
                if (letter.equals("R")) {
                    dial += value;
                    if (dial >= 100) {
                        if (!prev_was_zero) {
                            res++;
                        }
                        dial -= 100;
                    }
                } else {
                    dial -= value;
                    if (dial <= 0) {
                        if (!prev_was_zero){
                            res++;
                        }
                        dial += 100;
                    }
                }
                dial %= 100;
                prev_was_zero = dial == 0;
            }
        }

        System.out.println(res);
    }
}



package com.example.hello;
import java.util.HashMap;

public class Solution {
    public static boolean isUnique(String string) {
        HashMap<Character, Character> map = new HashMap<Character, Character>();

        for (int i = 0; i < string.length(); i++) {
            char key = string.charAt(i);
            if (map.containsKey(key)) {
                return false;
            }

            map.put(key, key);
        }
        return true;
    }

    public static void main(String[] args) {
        String testCases[] = {"abcd", "a", "abccd"};

        for (String s : testCases) {
            boolean result = isUnique(s);
            String message = String.format("Testing %s: %b", s, result);
            System.out.println(message);
        }
    }
}

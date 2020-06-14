public String reverseWords(String s) {
		if (s == null) return "";
        String[] str = s.split("\\s+");
        StringBuilder b = new StringBuilder();
        for (int i = str.length - 1; i >= 0; i--) {
            b.append(str[i]);
            if (i != 0)
                b.append(" ");
        }
        return b.toString().trim();
    }

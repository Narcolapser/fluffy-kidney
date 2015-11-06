package littlefootlandmines.playground.dummy;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * Helper class for providing sample content for user interfaces created by
 * Android template wizards.
 * <p/>
 * TODO: Replace all uses of this class before publishing your app.
 */
public class Foo {

    /**
     * An array of sample (dummy) items.
     */
    public static List<Bar> ITEMS = new ArrayList<Bar>();

    /**
     * A map of sample (dummy) items, by ID.
     */
    public static Map<String, Bar> ITEM_MAP = new HashMap<String, Bar>();

    private static final int COUNT = 5;

    static {
        // Add some sample items.
//        for (int i = 1; i <= COUNT; i++) {
//            addItem(createDummyItem(i));
//        }
    }

    public static void addItem(Bar item) {
        ITEMS.add(item);
        ITEM_MAP.put(item.id, item);
    }

    private static Bar createDummyItem(int position) {
        return new Bar(String.valueOf(position), "Item " + position, makeDetails(position));
    }

    private static String makeDetails(int position) {
        StringBuilder builder = new StringBuilder();
        builder.append("Details about Item: ").append(position);
        for (int i = 0; i < position; i++) {
            builder.append("\nMore details information here.");
        }
        return builder.toString();
    }

    /**
     * A dummy item representing a piece of content.
     */
    public static class Bar {
        public String id;
        public String content;
        public String details;
        public String title;

        public Bar(String id, String title, String details) {
            this.title = title;
            this.id = id;
            this.content = "derp";
            this.details = details;
        }

        public Bar(String id, String content)
        {
            this.title = "yup";
            this.content = "content";
            this.details = content;
            this.id = id;
        }

        @Override
        public String toString() {
            return title;
        }
    }
}

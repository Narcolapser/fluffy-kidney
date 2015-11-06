
/**
 * Created by toben on 10/22/15.
 */
package littlefootlandmines.playground;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * The Recipe class
 */
public class RecipeType {

    /**
     * An array of sample (Recipe) items.
     */
    public static List<RecipeItem> ITEMS = new ArrayList<RecipeItem>();

    /**
     * A map of sample (Recipe) items, by ID.
     */
    public static Map<String, RecipeItem> ITEM_MAP = new HashMap<String, RecipeItem>();

    private static final int COUNT = 25;

    static {
        // Add some sample items.
        for (int i = 1; i <= COUNT; i++) {
            addItem(createRecipeItem(i));
        }
    }

    public static void addItem(RecipeItem item) {
        ITEMS.add(item);
        ITEM_MAP.put(item.id, item);
    }

    private static RecipeItem createRecipeItem(int position) {
        return new RecipeItem(String.valueOf(position), "Item " + position, makeDetails(position));
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
     * A Recipe item representing a piece of content.
     */
    public static class RecipeItem {
        public String id;
        public String content;
        public String details;

        public RecipeItem(int val)
        {

        }

        public RecipeItem(String id, String content, String details) {
            this.id = id;
            this.content = content;
            this.details = details;
        }

        @Override
        public String toString() {
            return content;
        }
    }
}

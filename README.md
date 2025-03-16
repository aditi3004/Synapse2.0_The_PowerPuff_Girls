# **Synapse 2.0: The PowerPuff Girls - Allergen Detection and Dietary Assistant**

## **Overview**
Synapse 2.0, also known as **The PowerPuff Girls**, is an advanced dietary assistant that helps individuals identify potential allergens in food items, manage dietary restrictions, and suggest suitable meal alternatives. This system leverages cutting-edge AI technologies, including **EfficientNet B0** for food image classification and **Gemini Vertex AI 2.0** for personalized allergy prediction and recommendation.

## **Core Features**
1. **EfficientNet B0 for Allergen Detection:**
   - EfficientNet B0 is a lightweight yet powerful Convolutional Neural Network (CNN) that excels at image classification tasks. In Synapse 2.0, it is used to:
     - Detect allergens in food images by identifying ingredient components.
     - Recognize packaged food items and extract nutritional information.
     - Identify potential cross-contamination risks by analyzing multiple food components in a single image.
   
2. **Gemini Vertex AI 2.0 for Allergy Prediction & Recommendations:**
   - **Gemini** enhances the assistant's ability to understand user preferences, analyze ingredients, and suggest allergy-friendly alternatives.
   - It provides:
     - **Conversational support** for users seeking dietary advice.
     - **OCR capabilities** for analyzing nutritional labels and restaurant menus.
     - **Personalized meal recommendations** based on user allergies, health goals, and nutritional balance.

3. **Streamlit UI:**
   - The system features an intuitive, interactive **Streamlit UI** that allows users to upload food images, input text descriptions, and even give voice commands to interact with the assistant in real-time.

## **System Architecture & Workflow**

1. **User Inputs:**
   - Users can interact with the system by providing various forms of input, including:
     - **Food images** (captured with a camera or uploaded directly).
     - **Text descriptions** (e.g., food ingredients or meals).
     - **Voice commands** (for hands-free interaction).

2. **EfficientNet B0 Processing:**
   - The **EfficientNet B0** model processes the uploaded food image and classifies it into a specific food category.
   - It then detects potential allergens in the image by identifying key ingredients, cross-referencing with known allergen data.

3. **Gemini Analysis:**
   - After classifying the food and detecting potential allergens, **Gemini** cross-references the ingredients with the user's allergy profile.
   - It then analyzes the detected allergens and provides suggestions for safe alternatives, along with additional dietary advice based on health goals.

4. **Recommendation Generation:**
   - The assistant generates **personalized meal plans** and **real-time dining suggestions** that cater to the user's dietary restrictions and preferences.
   - Recommendations include alternative ingredients (e.g., almond milk instead of regular milk), and restaurant options with allergen-free menus.

5. **Interactive Support:**
   - Users can interact with the assistant to clarify any doubts regarding food ingredients, cooking tips, and nutritional information. The assistant can also answer general queries related to allergens and healthy eating habits.

## **Datasets Used**
1. **Food Ingredients CSV:**
   - Contains nutritional information and allergen data for various food items.
   - Used to cross-reference food ingredients with potential allergens.

2. **Food Image Dataset:**
   - Provides labeled food images that are used for training the EfficientNet B0 model.
   - This dataset helps improve the accuracy of food classification and allergen detection.

## **Model Performance**
- The system runs on **Vertex AI 2.0 Flash 1**, ensuring fast, real-time predictions for allergen detection and dietary recommendations.

## **Technologies Used**
- **EfficientNet B0:** Image classification model for allergen detection.
- **Gemini Vertex AI 2.0:** AI model for allergy prediction, meal recommendations, and conversational support.
- **Streamlit:** For building an interactive user interface.
- **OCR Capabilities:** For reading nutritional labels and restaurant menus.

## **Installation and Setup**

### **1. Clone the Repository**
```bash
git clone https://github.com/your-repository/synapse2.0
cd synapse2.0
```

### **2. Install Dependencies**
Install required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### **3. Run the Application**
Run the application using Streamlit:

```bash
streamlit run app.py
```

The application will open in your browser, allowing you to upload food images, interact with the chatbot, and get allergy predictions and dietary recommendations.

## **Future Scope**
- **Barcode Scanning:** Integrate a barcode scanning feature for packaged food to automatically extract nutritional information and allergens.
- **Integration with Delivery Apps:** Sync with apps like **Swiggy**, **Zomato**, and grocery apps like **Blinkit** or **Zepto** for real-time allergen-free food recommendations based on restaurant menus and grocery inventories.
- **Expanded Database:** The system can be trained with more data to recognize a wider variety of food items and allergens.

## **Contributors**
- [Your Name or Team Name]
- GitHub: [Link to your repository]

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This README provides a structured approach for presenting your project, its features, system architecture, and setup instructions. Feel free to replace placeholders with actual information where needed.

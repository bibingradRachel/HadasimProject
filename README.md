# פרויקט הדסים

התוכנית מקבלת כקלט קובץ טקסט וקובץ טקסט ריק שבו היא כותבת דו"ח נתונים סטטים עליו.

הנתונים הסטטים אותם אנו מחלצים:
1. כמות השורות בקובץ - ע"י קריאה פשוטה של הקובץ באופן שמחלק אותו לשורות לתוך מערך lines
2. כמות המילים בקובץ -עבור כול שורה נהפוך אותה למערך שמכיל את כול המילים נבדוק את אורכו ונצבור את הסכום עבור כול השורות
3. כמות המילים הייחודיות - ייצרתי אחסון שיכיל את כול המילים ועבור כול מילה כמה פעמים היא נמצאת וכך כול המילים שמופיעות פעם אחת הם ייחודיות
4. אורך המשפט המקסימלי ואורך המשפט הממוצע - באופן פשוט השוותי אורכים ועשיתי ממוצע
5. רצף המילים הארוך ביותר שלא מכיל את התו קיי - שמרתי את המילים כמחרוזת עד שהגעתי למילה מכילה קיי ואז השוותי את מה שנוצר עם המחרוזת הכי ארוכה עד כה
6. המספר הגדול ביותר  - המרתי את המילים למספר והשוותי
7.  אילו שמות צבעים וכמה פעמים מופיע כול אחד - בדומה למילים שמרתי את כול הצבעים וכמות הפעמים שכול אחד מופיע ובדקתי אם מילה היא אכן צבע באמצעות פונקציה

לצורך יעילות עשיתי את כול מה שצריך חישוב ובדיקה בתוך לולאה אחת על כול השורות ועל כול המילים בטקסט

לאחר מכן הכנסתי את כול הנתונים לקובץ הריק 

דוגמא לקלט זה חלק מהקובץ טקסט שנתנו לנו
והפלט שלו יהיה בתוך קובץ טקסט:

![צילום מסך 2021-11-10 174135](https://user-images.githubusercontent.com/86181853/141144396-246d2125-2568-4ca3-94d4-e5f9519e62df.png)

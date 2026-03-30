### Rename your photographs based on content

You can use Gemini CLI to automate file management tasks that require visual
analysis. In this example, Gemini CLI renames images based on their actual
subject matter.

Scenario: You have a folder containing the following files:

```bash
photos/photo1.png
photos/photo2.png
photos/photo3.png
```

Give Gemini the following prompt:

```cli
Rename the photos in my "photos" directory based on their contents.
```

Result: Gemini asks for permission to rename your files.

Select **Allow once** and your files are renamed:

```bash
photos/yellow_flowers.png
photos/antique_dresser.png
photos/green_android_robot.png
```
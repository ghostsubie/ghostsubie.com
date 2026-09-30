# Publishing a Field Notes post (no coding needed)

Everything runs through GitHub. When you save a post, the live site rebuilds
itself in about a minute.

## Write a new post

1. Go to **github.dev/ghostsubie/ghostsubie.com** (sign in with your GitHub
   account if asked). This opens the website's files in a full editor,
   right in the browser.
2. In the left file list, open the `src/content/field-notes/` folder.
3. Right-click the folder → **New File**. Name it like
   `my-trip-to-big-bend.md` (lowercase, dashes instead of spaces).
4. Paste this at the very top, then write below it:

```markdown
---
title: "Your Post Title"
description: "One or two sentences — this shows on the card."
pubDate: 2026-10-05
category: "Trip Reports"
featured: false
---

Your writing goes here. Markdown works: **bold**, *italic*,
[links](https://example.com), and ![photo captions](image-url).
```

5. Press **Ctrl+S** (or Cmd+S on Mac), then click the **Source Control**
   icon (left sidebar, the branching icon) → type a message like
   "new post: big bend" → **Commit & Push**. Done — the site redeploys
   automatically.

## Edit an existing post

Same as above, but open the post's file instead of creating one, edit,
then Commit & Push.

## Add photos

Put the image file in the `public/images/` folder (drag it in), then
reference it in your post as `![caption](/images/your-photo.jpg)`.

## Categories

Use one of: `Rig Builds`, `Trip Reports`, `Preparedness`, `Camp Systems`.
The category shows on the card and filters the Field Notes page.

## Tips

- `featured: true` puts the post in the big spotlight slot (only one at
  a time — set the old one back to `false`).
- `pubDate` should be the publish date in `YYYY-MM-DD` format.
- If the site ever looks wrong after a push, text Ghosty — nothing is
  lost, every version is saved.

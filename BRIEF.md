# Daily Instagram poster brief

Every morning, make one poster for each brand below and show both to the owner for approval. Post only after they reply "ok".

## Brand 1: The Top Tickets (@thetoptickets)
- Business: online tickets for attractions and museums, similar to GetYourGuide or Viator.
- Instagram account id (Windsor.ai `instagram` connector): `17841434441137123`
- Website: thetoptickets.com
- WhatsApp: +33 7 51 13 64 73
- Email: contact@thetoptickets.com
- Logo: `templates/assets/toptickets-logo.png` (coral "T")
- Approved style: `templates/toptickets-template.html`, which is the posted Musée d'Orsay poster. It has a white header with the big logo and "THE TOP TICKETS", a navy scene with an SVG illustration, the attraction name, 2 benefit badges, a coral "BOOK NOW" button and a coral contact strip at the bottom.
- Known products (confirmed by owner): Musée d'Orsay Entry Ticket (instant confirmation, free cancellation), Musée de l'Orangerie tickets.
- Prices: the site shows prices in euros, but they are not known here. Do not put a price unless the owner gives it.

## Brand 2: Z Ocean Tours (@z.ocean_tours)
- Business: complete Europe holiday packages (Asia planned later).
- Instagram account id: `17841452250476808`
- Website: www.z-oceantours.com
- WhatsApp: +33 7 51 13 64 73
- Email: info@zoceantours.com
- Logo: `templates/assets/zocean-logo.jpg`
- Approved style: `templates/zocean-template.html`, which is the posted Paris + Switzerland poster. The owner liked it because it shows a specific package, duration and an inclusions list. It has a white logo header, a hero illustration with a big package title and a days/nights ribbon, a white "WHAT'S INCLUDED" card with 8 emoji-icon inclusions, a "Perfect for..." line, an orange "GET YOUR QUOTE ON WHATSAPP" button and a blue contact strip.
- The owner said a plain "Europe holiday" poster was boring. Always feature a specific multi-country package with inclusions.

## Rules
- Size 1080x1350 JPEG. Render the HTML with Playwright using /usr/bin/google-chrome, then look at the result and fix overlaps before showing it.
- Hosting: commit the JPEG to this repo (`toptickets/` or `zocean/` folder, file name with the date), push to main, and use `https://raw.githubusercontent.com/alizaidiparis/toptickets-posters/main/<path>` as the image_url.
- Never repeat a topic listed in `posts-log.md` until every option has been used.
- Inclusions, durations and attractions that the owner has not confirmed must be flagged in the preview message as "please verify", so customers are never promised something that is not sold.
- No real photos (photo sites are blocked); use SVG illustrations and emoji.
- Captions are in English, with emojis, contact details, "link in bio" and about 12 hashtags.
- Talk to the owner in Hinglish.

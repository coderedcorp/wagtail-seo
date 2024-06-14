Editing SEO Metadata
====================

Turning Features On or Off
--------------------------

The recommended way to turn features on or off is using the Wagtail Site
Settings. From the Wagtail Admin select **Settings > SEO**. From here each
type of metadata can be turned on or off.

.. note::

    In order for Twitter cards to work correctly, a twitter account must be
    specified. This is the "@username" of the site owner's Twitter account.
    Most likely this would be a brand account.


Specifying Metadata per Page
----------------------------

While editing the page, special SEO metadata can be specified under the
**Promote** tab.

.. note::

    Website developers may provide fallbacks for any of the values below if they
    are blank. See :doc:`/customizing/customize-meta`.

Search & Social Media Previews
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **SEO title** --- If specified, this title will show up in the browser tab,
  in search engine results, and on social media previews exactly as-is. If
  empty, the page's normal title will be used, appended with the Site name (from
  **Settings > Sites > Site name**) as so: "Page Title - Site Name"

* **Search description** --- This will show up in search engine results and
  social media previews.

* **Canonical URL** --- The preferred URL for duplicate or similar pages.

* **Preview image** --- This corresponds to the Open Graph image and will
  show up in social media previews (Facebook, LinkedIn, Twitter, and many other
  sites supporting the Open Graph standard).

Search Engine "Rich Snippets"
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Structured Data, referred to by Google as "rich snippets", is special metadata
which defines information about the content of the page, and the organization
producing the content. The following Structured Data should be provided
on your site's settings. Each site has its own settings to provide this information.
To provide this info for multiple locations, such as branches, stores, regional
offices, etc. --- they should all have their own site configured.
As an alternative, `seo_struct_org_` accessors can be overridden in models
inheriting from `SeoMixin`.

* **Organization type** --- Should be provided to identify the type of business.

* **Organization name** --- The name as it will show up in search results, maps,
  business listings, etc. If blank, the site name from **Settings > Sites** is
  used instead.

* **Organization logo** --- The logo that will show up in search results,
  business listings, news/article publications, etc.

* **Photo of Organization** --- A photo of the physical facility or location
  that will show up in search results, maps, business listings, etc.

* **Telephone number** --- Phone number, including country code (+1 for USA),
  that will show up in search results and business listings.

* **Address** --- Various address fields for the physical facility or location.
  This tells search engines how to display your website on a map or local
  business listing.

* **Geographic latitude & longitude** --- Similar to the address, this is used
  to pinpoint the exact location on a map. Should correspond to the entrance
  of the facility if possible.

* **Hours of operation** --- Days and hours your organization is open for
  business. To indicate late night hours, such as "Saturday 11pm--2am", make
  two days instead: "Saturday 23:00--23:59" and "Sunday 00:00--02:00".

  These hours should be updated regularly as your locations adjust their
  schedules. For example, if one branch has temporary limited hours due to
  COVID-19, the hours *should* be updated to reflect the new schedule, then
  re-updated again in the future when hours go back to normal.

* **Actions** --- Actions have somewhat limited support by Google, but can be
  used specifically for making reservations or online orders.

  * **Target**

* **Additional Organization Markup** --- Add custom JSON-LD here. Must be valid
  properties of https://schema.org/Organization, or your Organization type
  specified above. For example:

  .. code-block:: json

    {
      "legalName": "Ye National Cheese Emporium",
      "slogan": "Purveyor of fine cheese to the gentry (and the poverty-stricken too)."
    }

  While it may be tempting to try and provides hundreds of different data points
  falling within the Schema.org spec, in reality Google and other search engines
  only use a limited subset, the primary of which are already included by
  Wagtail SEO using the fields above.

  See Google's documentation on rich snippets for more context on how this data
  is used: https://developers.google.com/search/docs/data-types/local-business


Additional "Rich Snippet" Content
---------------------------------

Articles
~~~~~~~~

Wagtail SEO also provides Structured Data markup (a.k.a. "rich snippets") for
article type pages using a combination of the information above and the page's
included data (date published, author, etc.). No additional action is required
to enable article markup.

Others
~~~~~~

Google officially supports a few dozen types of specific structured data,
including recipes, events, books, etc. If your website deals in these types of
data, read how to extend Wagtail SEO's structured data in:
:doc:`/customizing/customize-meta`.


Preview Your Page on Search & Social
------------------------------------

After editing metadata and publishing a page, you can validate and preview
the metadata by using online tools. See :doc:`/test-meta`.

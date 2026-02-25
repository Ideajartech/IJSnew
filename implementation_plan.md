# Implementation Plan: Update "Work With Us" & "Latest Blog" Sections

## Objective
Update the "Work With Us" and "Latest Blog" sections across all case study pages to ensure consistency, fix typos, and align with the brand's latest messaging.

## scope
This update applies to the following 13 case study files:
1. `radian-move-b2b-growth.html`
2. `scalix-community-growth.html`
3. `aprisio-brand-strategy-mvg.html`
4. `teamcounsel-marketing-growth.html`
5. `nected-linkedin-growth.html`
6. `nokio-linkedin-growth.html`
7. `fieldpromax-seo-strategy.html`
8. `nurrish-community-growth.html`
9. `menoveda-marketing-growth.html`
10. `rushbykira-brand-growth.html`
11. `gen3-growth-marketing.html`
12. `airbound-deeptech-growth.html`
13. `farmtocups-brand-strategy.html`

## Proposed Changes

### 1. Work With Us Section
**Goal:** Standardize the Call to Action (CTA) and agency-wide statistics.

**Proposed Content Structure:**
- **Headline:** "Ready to see your growth?" (or updated copy if provided)
- **CTA Button:** "Talk to an expert" linking to `https://cal.com/mythri-ideajarstudio/strategy-call`
- **Floating Stats:**
  - **60M+** Organic Impressions
  - **3.7K+** Pipeline Influenced

**HTML Template (to be applied):**
```html
<div class="work-with-us section">
   <div class="container">
      <div class="row">
         <div class="col-md-8">
            <div class="sisf-sis-section-title section-title animated fadeInLeft mb-0">
               <h2 class="sisf-m-title sisf-m-title--scroll"><span class="sisf-e-decorated">Ready to drive business revenue?</span></h2>
               <p>Own your category through our signature marketing frameworks.</p>
               <div class="sisf-m-button mt-4">
                  <a href="https://tally.so/r/jaZ6gR" target="_blank" class="btn-default sisf-hover-reveal">Reserve Your Spot</a>
               </div>
               
            </div>
         </div>
         <div class="col-md-4">
            <div class="float">
               <div class="sisf-rotate-block">
                  <div class="counter-box animated rotateInDownRight mb-3">
                     <div class="counter-item border-0">
                        <div class="counter-title">
                           <h2><span class="counter text-black">60</span><span class="text-black">M+</span></h2>
                        </div>
                        <div class="counter-content">
                           <h3 class="text-black">organic impressions</h3>
                        </div>
                     </div>
                  </div>
                  <div class="counter-box animated rotateInDownRight">
                     <div class="counter-item border-0">
                        <div class="counter-title">
                           <h2><span class="counter text-black">3.7</span><span class="text-black">K+</span></h2>
                        </div>
                        <div class="counter-content">
                           <h3 class="text-black">pipeline influenced</h3>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
         </div>
      </div>
   </div>
</div>
```

### 2. Latest Blog Section
**Goal:** Fix the "Letest" typo and standardise the display.

**Proposed Content:**
- **Section Title:** "Latest Insights & Trends" (Removing redundant "Letest Blog" subtitle)
- **Content:** (Requires user input: Should this show specific recent blogs, or be removed if no dynamic blog exists? Assuming standard placeholder fix for now).
- **Fixes:**
  - Change "Letest Blog" to "Latest Blog" or remove.
  - Remove "AdminDigon" metadata if irrelevant.
  - Update placeholder dates if needed.

**HTML Template (to be applied):**
```html
   <div class="our-letest-blog section position-relative">
      <div class="container">
         <div class="row">
            <div class="col-12">
               <!-- Section Title Start -->
               <div class="sisf-sis-section-title text-center section-title wow zoomIn">
                  <h2 class="sisf-m-title sisf-m-title--scroll"><span class="sisf-e-decorated"> Other growth stories
                  </h2>
               </div>
               <!-- Section Title End -->
            </div>
         </div>
         <div class="row">
            <div class="col-lg-4 col-md-6">
               <div class="letest-blog-item sisf-blogs">
                  <div class="sisf-e-inner p-4">
                     <div class="sisf-e-media-holder">
                        <div class="sisf-e-media">
                           <div class="sisf-e-media-image media-image">
                              <a href="airbound-deeptech-growth.html">
                                 <img src="images/airbound-deeptech-growth-cover2.png" class="w-100" alt="Digon">
                              </a>
                           </div>
                        </div>
                     </div>
                     <div class="sisf-e-content p-0">
                        <div class="sisf-e-info sisf-info--top d-flex mt-4">
                           <div class="info-date me-3">
                              <a>Aerospace (Deeptech)
                              </a>
                           </div>

                        </div>
                        <div class="sisf-e-text">
                           <div class="sisf-e-title-wraper border-0 mb-0 pb-0">
                              <h5 class="sisf-e-title entry-title  blog-title">
                                 <a>
                                    145K+ reach & 19.06% CTR across content campaigns
                                 </a>
                              </h5>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
            <div class="col-lg-4 col-md-6">
               <div class="letest-blog-item sisf-blogs">
                  <div class="sisf-e-inner p-4">
                     <div class="sisf-e-media-holder">
                        <div class="sisf-e-media">
                           <div class="sisf-e-media-image media-image">
                              <a href="aprisio-brand-strategy-mvg.html">
                                 <img src="images/aprisio-brand-strategy-mvg-cover2.png" class="w-100"
                                    alt="0 to 50.4 K+ reach & PMF in 4 months">
                              </a>
                           </div>
                        </div>
                     </div>
                     <div class="sisf-e-content p-0">
                        <div class="sisf-e-info sisf-info--top d-flex mt-4">
                           <div class="info-date me-3">
                              <a>Lifestyle & Wellness</a>
                           </div>
                        </div>
                        <div class="sisf-e-text">
                           <div class="sisf-e-title-wraper border-0 mb-0 pb-0">
                              <h5 class="sisf-e-title entry-title blog-title">
                                 <a class="sisf-e-title-link blog-title-link" href="aprisio-brand-strategy-mvg.html">
                                    0 to 50.4 K+ reach & PMF in 4 months
                                 </a>
                              </h5>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>
            <div class="col-lg-4 col-md-6">
               <div class="letest-blog-item sisf-blogs">
                  <div class="sisf-e-inner p-4">
                     <div class="sisf-e-media-holder">
                        <div class="sisf-e-media">
                           <div class="sisf-e-media-image media-image">
                              <a href="rifa-ai-marketing-growth.html">
                                 <img src="images/rifa-ai-marketing-growth-cover2.png" class="w-100"
                                    alt="75K views + 30% rise in demo requests">
                              </a>
                           </div>
                        </div>
                     </div>
                     <div class="sisf-e-content p-0">
                        <div class="sisf-e-info sisf-info--top d-flex mt-4">
                           <div class="info-date me-3">
                              <a>Voice AI</a>
                           </div>
                        </div>
                        <div class="sisf-e-text">
                           <div class="sisf-e-title-wraper border-0 mb-0 pb-0">
                              <h5 class="sisf-e-title entry-title blog-title">
                                 <a class="sisf-e-title-link blog-title-link" href="rifa-ai-marketing-growth.html">
                                    75K views + 30% rise in demo requests
                                 </a>
                              </h5>
                           </div>
                        </div>
                     </div>
                  </div>
               </div>
            </div>

         </div>
      </div>
   </div>
```

## Next Steps
1. [x] Confirm the exact text/stats for the "Work With Us" section.
2. [x] Confirm if the blog section should remain static with these placeholders or if there are real blog posts to feature.
3. [x] Execute the changes across all 13 files.

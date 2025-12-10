# region Corporate
from .corporate import (
    SlidersBlock as CorporateSlidersBlock,
    AboutBlock as CorporateAboutBlock,
    ServicesWIconBlock as CorporateServicesWIconBlock,
    FeaturePairsBlock as CorporateFeaturePairsBlock,
    PortfolioBlock as CorporatePortfolioBlock,
    InformationBlock as CorporateInformationBlock,
    ParallaxFeatureBlock as CorporateParallaxFeatureBlock,
    ServicesGalleryBlock as CorporateServicesGalleryBlock,
    ParallaxBlock as CorporateParallaxBlock,
    ServicesWFeaturesBlock as CorporateServicesWFeaturesBlock,
)
# endregion Corporate

# region One Page
from .one_page import (
    AccordionBlock as OnePageAccordionBlock,
)

# endregion One Page

# region Start Up
from .start_up import (
    InformationBlock as StartUpInformationBlock,
)

# endregion Start Up

__all__ = [
    # region Corporate
    "CorporateSlidersBlock",
    "CorporateAboutBlock",
    "CorporateServicesWIconBlock",
    "CorporateFeaturePairsBlock",
    "CorporatePortfolioBlock",
    "CorporateInformationBlock",
    "CorporateParallaxFeatureBlock",
    "CorporateServicesGalleryBlock",
    "CorporateParallaxBlock",
    "CorporateServicesWFeaturesBlock",
    # endregion Corporate
    # region One Page
    "OnePageAccordionBlock",
    # endregion One Page
    # region Start Up
    "StartUpInformationBlock",
    # endregion Start Up
]

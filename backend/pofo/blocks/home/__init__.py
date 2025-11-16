# region Classic
from .classic import (
    # region Corporate
    CorporateSlidersBlock as ClassicCorporateSlidersBlock,
    CorporateAboutBlock as ClassicCorporateAboutBlock,
    CorporateServicesWIconBlock as ClassicCorporateServicesWIconBlock,
    CorporateFeaturePairsBlock as ClassicCorporateFeaturePairsBlock,
    CorporatePortfolioBlock as ClassicCorporatePortfolioBlock,
    CorporateInformationBlock as ClassicCorporateInformationBlock,
    CorporateParallaxFeatureBlock as ClassicCorporateParallaxFeatureBlock,
    CorporateServicesGalleryBlock as ClassicCorporateServicesGalleryBlock,
    CorporateParallaxBlock as ClassicCorporateParallaxBlock,
    CorporateServicesWFeaturesBlock as ClassicCorporateServicesWFeaturesBlock,
    # endregion Corporate
    # region One Page
    OnePageAccordionBlock as ClassicOnePageAccordionBlock,
    # endregion One Page
    # region Start Up
    StartUpInformationBlock as ClassicStartUpInformationBlock,
    # endregion Start Up
)
# endregion Classic

# region Creative
from .creative import (
    # region Small Business
    SmallBusinessServicesBlock as CreativeSmallBusinessServicesBlock,
    SmallBusinessClientsBlock as CreativeSmallBusinessClientsBlock,
    # endregion Small Business
)

# endregion Creative


__all__ = [
    # region Classic
    # region Corporate
    "ClassicCorporateSlidersBlock",
    "ClassicCorporateAboutBlock",
    "ClassicCorporateServicesWIconBlock",
    "ClassicCorporateFeaturePairsBlock",
    "ClassicCorporatePortfolioBlock",
    "ClassicCorporateInformationBlock",
    "ClassicCorporateParallaxFeatureBlock",
    "ClassicCorporateServicesGalleryBlock",
    "ClassicCorporateParallaxBlock",
    "ClassicCorporateServicesWFeaturesBlock",
    # endregion Corporate
    # region One Page
    "ClassicOnePageAccordionBlock",
    # endregion One Page
    # region Start Up
    "ClassicStartUpInformationBlock",
    # endregion Start Up
    # endregion Classic
    # region Creative
    # region Small Business
    "CreativeSmallBusinessServicesBlock",
    "CreativeSmallBusinessClientsBlock",
    # endregion Small Business
    # endregion Creative
]

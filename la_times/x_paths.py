class LATimesXPaths:
    """
    Defines XPaths used for interacting with the LA Times website.
    """

    class Search:
        """
        XPaths related to search functionality.
        """
        BUTTON = "//button[@data-element='search-button']"
        INPUT = "//input[@data-element='search-form-input']"
        SUBMIT = "//button[@data-element='search-submit-button']"
        NO_RESULTS = """//div[contains(text(),'There are not any results that match "{phrase}".')]"""
        RESULTS_FOR_TEXT = "//h1[text()='Search results for']"
        RESULTS = '//ul[@class="search-results-module-results-menu"]//li'

    class Category:
        """
        XPaths related to category selection.
        """
        TOPICS_SECTION = "//div[@class='search-filter']//p[contains(text(), 'Topics')]/parent::*"
        SEE_ALL_TOPICS = "//span[@class='see-all-text']"
        TOPIC = "//span[text()='{name}']"

    class Sort:
        """
        XPaths related to sorting.
        """
        SELECT_INPUT = "//select[@class='select-input']"

    class NewsArticle:
        """
        XPaths related to news articles.
        """
        TITLE = ".//h3//a[@class='link']"
        DATE = ".//p[@class='promo-timestamp']"
        DESCRIPTION = ".//p[@class='promo-description']"
        PROF_PIC = ".//img"

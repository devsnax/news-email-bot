def formatText(text):
    html_items = ""
    for headline, summary in text:
        html_items += f"""
                        <div style="margin-top: 20px; border-bottom: 1px solid #ccc; padding-bottom: 10px;">
                            <h2 style="margin: 0; font-size: 20px; font-weight: bold;">{headline.text}</h2>
                                <p style="font-size: 15px;">{summary.text}</p>\n
                        </div>
                    """

    html = f"""
                <html>
                    <body style="font-family: Arial, sans-serif;">
                        <h1>BBC Daily World News</h1>\n
                            <p>Daily news summaries scraped using Python</p>\n
                            {html_items}
                        <p style="margin-top: 40px;">Scraped daily, built by Snax.</p>
                    </body>
                </html>
            """
    
    return html
<?xml version="1.0"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:output method="xml"/>
    <xsl:template match="/">
        <items>
            <xsl:for-each select="//div[@class='item']">
                <item>
                    <name>
                        <xsl:value-of select="table[@class='receipt-row-1']//span[starts-with(@class, 'value receipt-value-')]"/>
                    </name>
                    <price>
                        <xsl:value-of select="table[@class='receipt-row-2']//td[@class='receipt-col2']//span"/>
                    </price>
                </item>
            </xsl:for-each>
        </items>
    </xsl:template>
</xsl:stylesheet>

const puppeteer = require('puppeteer');
const path = require('path');

async function generatePdfs() {
  const browser = await puppeteer.launch({ headless: 'new' });
  
  // Spanish Version
  const pageEs = await browser.newPage();
  await pageEs.goto('file://' + path.resolve('cv-impresion.html'), { waitUntil: 'networkidle0' });
  await pageEs.pdf({
    path: 'assets/CV_Fabian_Flores.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '0', right: '0', bottom: '0', left: '0' }
  });
  console.log('Generated assets/CV_Fabian_Flores.pdf');

  // English Version
  const pageEn = await browser.newPage();
  await pageEn.goto('file://' + path.resolve('cv-impresion-en.html'), { waitUntil: 'networkidle0' });
  await pageEn.pdf({
    path: 'assets/CV_Fabian_Flores_EN.pdf',
    format: 'A4',
    printBackground: true,
    margin: { top: '0', right: '0', bottom: '0', left: '0' }
  });
  console.log('Generated assets/CV_Fabian_Flores_EN.pdf');

  await browser.close();
}

generatePdfs().catch(console.error);

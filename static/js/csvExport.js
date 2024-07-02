class csvExport {
  constructor(table, header = true) {
    this.table = table;
    this.rows = Array.from(table.querySelectorAll("tr"));
    if (!header && this.rows[0].querySelectorAll("th").length) {
      this.rows.shift();
    }
  }

  exportCsv() {
    const lines = [];
    const ncols = this._longestRow();
    for (const row of this.rows) {
      let line = "";
      let colCount = 0;
      for (let i = 0; i < ncols; i++) {
        const cell = row.children[i];
        if (cell && cell.style.display !== "none") {
          if (colCount > 0) {
            line += ",";
          }
          line += csvExport.safeData(cell);
          colCount++;
        }
      }
      lines.push(line);
    }
    return lines.join("\n");
  }

  _longestRow() {
    let maxCols = 0;
    for (const row of this.rows) {
      const rowCols = row.querySelectorAll("th, td").length;
      if (rowCols > maxCols) {
        maxCols = rowCols;
      }
    }
    return maxCols;
  }

  static safeData(td) {
    let data = td.textContent;
    data = data.trim();
    data = data.replace(/"/g, `""`);
    data = /[",\n"]/.test(data) ? `"${data}"` : data;
    return data;
  }
}

const btnExport = document.querySelector("#btnExport");
const tableElement = document.querySelector(".table");

btnExport.addEventListener("click", () => {
  const obj = new csvExport(tableElement);
  const csvData = obj.exportCsv();
  const blob = new Blob([csvData], { type: "text/csv" });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  const pageTitle = document.title;
  a.download = `${pageTitle}.csv`;
  a.click();

  setTimeout(() => {
    URL.revokeObjectURL(url);
  }, 500);
});

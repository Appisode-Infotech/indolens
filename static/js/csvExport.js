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
    // Iterate through one less column by using `ncols - 1`
    for (let i = 0; i < ncols - 1; i++) {
      if (row.children[i] !== undefined) {
        line += csvExport.safeData(row.children[i]);
      }
      line += i !== ncols - 2 ? "," : "";
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
  // Trim leading and trailing spaces
  data = data.trim();
  data = data.replace(/"/g, `""`);
  data = /[",\n"]/.test(data) ? `"${data}"` : data;
  return data;
}

}

const btnExport = document.querySelector("#btnExport");
const tableElement = document.querySelector(".table"); // Use the class selector here

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

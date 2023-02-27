import React from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import AuthMaitenanceTable from "../tables/auth_maitenance_table.jsx";
import AuthRepairTable from "../tables/auth_repair_table.jsx";
import AuthCarTable from "../tables/auth_car_table.jsx";
import "./tabs.css";

const AuthPanel = () => {
  return (
    <div>
      <h1>
        Информация о комплектации и технических характеристиках Вашей техники
      </h1>
      <Tabs>
        <TabList>
          <Tab>Машины</Tab>
          <Tab>ТО</Tab>
          <Tab>Рекламации</Tab>
        </TabList>
        <TabPanel>
          <AuthCarTable />
        </TabPanel>
        <TabPanel>
          <AuthMaitenanceTable />
        </TabPanel>
        <TabPanel>
          <AuthRepairTable />
        </TabPanel>
      </Tabs>
    </div>
  );
};
export default AuthPanel;
